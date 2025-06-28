# 🎓 Student Management System (Django + Firebase)

Welcome to the **Student Management System** – a cloud-powered, Python Django web app integrated with Firebase Firestore for easy student tracking and management.

---

## 🚀 Live Demo

Try it here: [Student Management System on Render](https://student-manager-1-subo.onrender.com/students/)

Add, view, search, and manage students live!

---

## 🟢 Features

✅ **Add New Students** (name, email, age, course)
✅ **List and Search Students Instantly** (live filtering)
✅ **Duplicate Email Prevention**
✅ **Success and Error Toast Notifications**
✅ **Activity Logs of Added Students**
✅ **Clean Bootstrap Interface**
✅ **Cloud Data Management with Firebase Firestore**

---

## ⚙️ Tech Stack

* 🐍 Python 3.7+
* 🌐 Django
* ☁️ Firebase Firestore
* 🖌️ Bootstrap
* ⚡ Vanilla JavaScript
* 🖥️ HTML/CSS

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/student-manager.git
cd student-manager
```

### 2️⃣ Install Dependencies

Ensure you have Python 3.7+ installed:

```bash
python -m pip install -r requirements.txt
```

### 3️⃣ Set Up Firebase Firestore

1. Go to [Firebase Console](https://console.firebase.google.com/) and create a new project.
2. Navigate to **Firestore Database** and click **Create Database** (use test mode).
3. Go to **Project Settings > Service Accounts > Generate New Private Key**.
4. Download and rename the JSON key file to `student-manager-key.json`.
5. Place the file in your project root (same folder as `manage.py`).

### 4️⃣ Run the Application

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/` to view your Student Management System.

---

## 🗂️ Usage Guide

### ➕ Add a Student

* Click **Add Student** in the navigation bar.
* Fill in the form with name, email, age, and course.
* Submit the form.
* Get instant success/error toast notifications.

### 📋 View & Search Students

* Go to **View Students**.
* Use the search box for **instant filtering by name, email, or course**.

### 📝 Activity Logs

* Visit `/logs/` to view the last 20 activity logs showing student additions.

### 🗑️ Delete Students

* Use the delete icon next to a student to remove them (confirmation required).

---

## 🩺 Troubleshooting

✅ **Server Issues?**
Ensure Python and dependencies are installed correctly, and you are in the correct project directory.

✅ **Firebase Errors?**
Verify your JSON key is correctly placed, and Firestore is enabled.

✅ **Browser Not Loading?**
Check the terminal for errors, restart the server using `CTRL+C` and `python manage.py runserver`.

✅ **Still stuck?**
Ask on [Stack Overflow](https://stackoverflow.com/) or recheck each step calmly.

---

## 🛡️ License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

---

## 🙋‍♂️ About the Author

👨‍💻 **Phanindra Dharmavarapu**
Aspiring Python Developer building practical, cloud-powered projects for real-world use.
📫 [Connect on LinkedIn](www.linkedin.com/in/phanindra-dharmavarapu-183093250)
📧 [d.phanindra0076@gmail.com](mailto:d.phanindra0076@gmail.com)

---

**Happy Learning and Building! 🚀**
