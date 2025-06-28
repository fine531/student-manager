"""
Firebase Configuration for Student Management System
This file initializes the Firebase connection using the service account key.
"""

import os
import json
# import firebase_admin
from firebase_admin import credentials, firestore

# Try to import Firebase dependencies
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    FIREBASE_AVAILABLE = True
except ImportError as e:
    print(f"Firebase Admin SDK not available: {e}")
    print("Running in development mode without Firebase.")
    FIREBASE_AVAILABLE = False

def initialize_firebase():
    """
    Initialize Firebase connection and return Firestore client.
    Returns the Firestore database client for use in views.
    """
    if not FIREBASE_AVAILABLE:
        print("Firebase Admin SDK not installed. Please install with: pip install firebase-admin==5.3.0")
        return None
    
    try:
        # Check if Firebase app is already initialized
        if not firebase_admin._apps:
            cred_json = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_JSON')
            if cred_json:
                cred = credentials.Certificate(json.loads(cred_json))
                firebase_admin.initialize_app(cred)
            else:
                # fallback for local dev
                cred = credentials.Certificate('student-manager-key.json')
                firebase_admin.initialize_app(cred)
            print("Firebase initialized successfully!")
        
        # Get Firestore client
        db = firestore.client()
        return db
    
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        print("Running in development mode with mock data.")
        return None

def get_firestore_client():
    """
    Get the Firestore client instance.
    Returns the Firestore database client.
    """
    return initialize_firebase()

# Initialize Firebase when module is imported
db = get_firestore_client()

# Mock data for development when Firebase is not available
MOCK_STUDENTS = [
    {
        'id': 'mock-1',
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'age': 20,
        'course': 'Computer Science'
    },
    {
        'id': 'mock-2', 
        'name': 'Jane Smith',
        'email': 'jane.smith@example.com',
        'age': 22,
        'course': 'Mathematics'
    },
    {
        'id': 'mock-3',
        'name': 'Mike Johnson',
        'email': 'mike.johnson@example.com',
        'age': 19,
        'course': 'Physics'
    }
] 