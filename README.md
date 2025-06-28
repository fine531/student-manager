# 🎓 Student Management System (Super Easy Guide!)

Welcome! This is a simple web app to help you keep track of students. You can add students, see all students, search for them, and even see a log of what happened. It uses Django (a Python web tool) and Firebase (a cloud database). You don't need to know any coding to use it—just follow these steps!

---

## 🟢 What Does This Project Do?
- Lets you **add new students** (name, email, age, course)
- Shows a **list of all students**
- Lets you **search/filter** students instantly
- **Prevents duplicate emails**
- Shows **success and error popups** (toasts)
- Keeps an **activity log** of who was added

---

## 🟣 What Do You Need?
1. **A computer** (Windows, Mac, or Linux)
2. **Python 3.7 or newer** (ask an adult if you're not sure)
3. **Internet connection**
4. **A Firebase account** (free, just need a Google account)

---

## 🟠 How to Set Up (Step by Step)

### 1. Download the Project
- Get all the files in a folder on your computer (ask your teacher or download from GitHub).

### 2. Install Python (if you don't have it)
- Go to [python.org](https://www.python.org/downloads/) and download Python 3.7 or newer.
- Install it (ask an adult if you need help).

### 3. Open a Terminal or Command Prompt
- On Windows: Search for "cmd" or "Command Prompt" and open it.
- On Mac: Open "Terminal" from Applications > Utilities.
- On Linux: Open your terminal app.
- Use `cd` to go to your project folder. Example:
  ```
  cd "C:/Users/yourname/Desktop/Phani 's Pro"
  ```

### 4. Install the Needed Tools
- Type this and press Enter:
  ```
  python -m pip install -r requirements.txt
  ```

### 5. Set Up Firebase
- Go to [Firebase Console](https://console.firebase.google.com/)
- Click "Add project" and follow the steps (pick any name)
- Click "Firestore Database" on the left, then "Create database" (choose test mode)
- Go to "Project settings" (gear icon), then "Service accounts"
- Click "Generate new private key" and download the JSON file
- Rename it to `student-manager-key.json` and put it in your project folder (where `manage.py` is)

---

## 🟡 How to Run the App
1. In your terminal, type:
   ```
   python manage.py runserver
   ```
2. Open your web browser and go to:
   ```
   http://127.0.0.1:8000/
   ```
3. You'll see the Student Manager homepage!

---

## 🟤 How to Use Each Feature

### ➕ Add a Student
- Click "Add Student" in the menu
- Fill in the form (name, email, age, course)
- Click "Add Student"
- If the email is already used, you'll see a warning popup
- If it works, you'll see a green success popup

### 📋 See All Students
- Click "View Students" in the menu
- You'll see a table of all students
- Use the search box to filter by name, email, or course (it works instantly as you type!)

### 🗑️ Delete a Student
- Click the red trash can next to a student to delete them
- Confirm when asked

### 📝 See Activity Logs
- Go to `/students/logs/` or add `/logs/` after `/students/` in the address bar
- You'll see a list of the last 20 actions (like "Added student: John Doe")

---

## 🟦 Troubleshooting (If Something Doesn't Work)
- **Can't run the server?**
  - Make sure you installed Python and the requirements
  - Check you are in the right folder
- **Firebase error?**
  - Make sure your `student-manager-key.json` is in the project folder
  - Make sure you enabled Firestore in Firebase
- **Page not loading?**
  - Check the terminal for errors
  - Try restarting the server (`CTRL+C` to stop, then run again)
- **Still stuck?**
  - Ask a teacher, parent, or post your question on [Stack Overflow](https://stackoverflow.com/)

---

## 🟩 Where to Get Help
- Ask your teacher or a parent
- Google your error message
- Try [Stack Overflow](https://stackoverflow.com/)
- Or just try again—mistakes are how you learn!

---

   ## Live Demo

   [Student Management System on Render](https://student-manager-1-subo.onrender.com/students/)
---

**Happy Learning! 🚀** 
