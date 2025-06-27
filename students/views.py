"""
Django Views for Student Management System
This file contains views for listing, adding, and managing students.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import StudentForm
from firebase_config import db, MOCK_STUDENTS, FIREBASE_AVAILABLE
import logging
import uuid
from firebase_admin import firestore

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage for development when Firebase is not available
mock_students_data = MOCK_STUDENTS.copy()

def index(request):
    """
    View to display all students from Firestore or mock data.
    Reads all student documents and renders them in a table.
    """
    try:
        if db is None or not FIREBASE_AVAILABLE:
            # Use mock data when Firebase is not available
            students = mock_students_data
            logger.info(f"Using mock data: {len(students)} students")
            
            return render(request, 'students/index.html', {
                'students': students,
                'total_students': len(students),
                'mock_mode': True
            })
        
        # Get all students from Firestore
        students_ref = db.collection('students')
        docs = students_ref.stream()
        
        students = []
        for doc in docs:
            student_data = doc.to_dict()
            student_data['id'] = doc.id  # Add document ID for reference
            students.append(student_data)
        
        logger.info(f"Retrieved {len(students)} students from Firestore")
        
        return render(request, 'students/index.html', {
            'students': students,
            'total_students': len(students),
            'mock_mode': False
        })
    
    except Exception as e:
        logger.error(f"Error retrieving students: {e}")
        messages.error(request, f"Error retrieving students: {str(e)}")
        return render(request, 'students/index.html', {'students': []})

def add_student(request):
    """
    View to handle adding a new student.
    Shows the form on GET request and processes form data on POST request.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                # Get cleaned form data
                student_data = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'age': form.cleaned_data['age'],
                    'course': form.cleaned_data['course']
                }
                # Duplicate prevention (Firestore only)
                if db is not None and FIREBASE_AVAILABLE:
                    students_ref = db.collection('students')
                    query = students_ref.where('email', '==', student_data['email']).limit(1).stream()
                    if any(query):
                        messages.warning(request, '⚠️ Student with this email already exists.')
                        return render(request, 'students/add_student.html', {'form': form})
                else:
                    # For mock mode, check in-memory
                    if any(s['email'].lower() == student_data['email'].lower() for s in mock_students_data):
                        messages.warning(request, '⚠️ Student with this email already exists.')
                        return render(request, 'students/add_student.html', {'form': form})
                # Add student
                if db is None or not FIREBASE_AVAILABLE:
                    student_data['id'] = f"mock-{uuid.uuid4().hex[:8]}"
                    mock_students_data.append(student_data)
                    messages.success(request, '✅ Student added successfully! (Mock Mode)')
                else:
                    students_ref = db.collection('students')
                    doc_ref = students_ref.add(student_data)
                    messages.success(request, '✅ Student added successfully!')
                    # Log activity
                    try:
                        # Use getattr for compatibility
                        server_timestamp = getattr(firestore, 'SERVER_TIMESTAMP', 'SERVER_TIMESTAMP')
                        db.collection('activity_logs').add({
                            'action': f"Added student: {student_data['name']}",
                            'timestamp': server_timestamp
                        })
                    except Exception as log_err:
                        logger.error(f"Error logging activity: {log_err}")
                return redirect('students:success')
            except Exception as e:
                logger.error(f"Error adding student: {e}")
                messages.error(request, f"Error adding student: {str(e)}")
                return render(request, 'students/add_student.html', {'form': form})
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'students/add_student.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def success(request):
    """
    View to display success message after adding a student.
    Simple confirmation page.
    """
    return render(request, 'students/success.html')

def delete_student(request, student_id):
    """
    View to delete a student from Firestore or mock data.
    Handles DELETE requests for removing students.
    """
    if request.method == 'POST':
        try:
            if db is None or not FIREBASE_AVAILABLE:
                # Delete from mock data
                global mock_students_data
                mock_students_data = [s for s in mock_students_data if s['id'] != student_id]
                logger.info(f"Student with ID {student_id} deleted from mock data")
                messages.success(request, "Student deleted successfully! (Mock Mode)")
            else:
                # Delete student from Firestore
                students_ref = db.collection('students')
                students_ref.document(student_id).delete()
                logger.info(f"Student with ID {student_id} deleted successfully")
                messages.success(request, "Student deleted successfully!")
            
        except Exception as e:
            logger.error(f"Error deleting student: {e}")
            messages.error(request, f"Error deleting student: {str(e)}")
    
    return redirect('students:index')

def logs(request):
    """
    View to display the last 20 activity logs from Firestore.
    """
    logs = []
    try:
        if db is not None and FIREBASE_AVAILABLE:
            # Use getattr for compatibility
            query_desc = getattr(getattr(firestore, 'Query', object), 'DESCENDING', 'DESCENDING')
            logs_ref = db.collection('activity_logs').order_by('timestamp', direction=query_desc).limit(20)
            docs = logs_ref.stream()
            for doc in docs:
                log = doc.to_dict()
                log['id'] = doc.id
                logs.append(log)
        else:
            # Mock logs for development
            logs = [
                {'action': 'Added student: John Doe', 'timestamp': None},
                {'action': 'Added student: Jane Smith', 'timestamp': None},
            ]
    except Exception as e:
        logger.error(f"Error retrieving logs: {e}")
    return render(request, 'students/logs.html', {'logs': logs})
