"""
Django Forms for Student Management System
This file contains the StudentForm for adding new students.
"""

from django import forms

class StudentForm(forms.Form):
    """
    Django Form for adding a new student.
    Contains fields: name, email, age, and course.
    """
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter student name',
            'required': True
        }),
        label='Student Name'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter student email',
            'required': True
        }),
        label='Email Address'
    )
    
    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter student age',
            'required': True
        }),
        label='Age'
    )
    
    course = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter course name',
            'required': True
        }),
        label='Course'
    )
    
    def clean_age(self):
        """
        Custom validation for age field.
        Ensures age is a positive integer.
        """
        age = self.cleaned_data.get('age')
        if age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age
    
    def clean_email(self):
        """
        Custom validation for email field.
        Ensures email is properly formatted.
        """
        email = self.cleaned_data.get('email')
        if not email or '@' not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email.lower() 