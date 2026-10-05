# College Assignment and Practical Submission Tracker

A Python-based desktop application designed to simplify the management of college assignments, practicals, projects, deadlines, submissions, and grading. The system provides separate dashboards for students and teachers to make the academic submission process more organized and efficient.

## Features

## Student

* Student registration and login
* View assigned assignments and practicals
* Track submission deadlines
* Upload assignment/practical files
* View submission status
* View marks and feedback
* Dashboard for tracking academic work

### teacher

* Teacher registration and login
* Create and manage assignments
* Set deadlines and maximum marks
* View student submissions
* Download submitted files
* Grade submissions
* Provide feedback
* Track assignment and practical submissions

### Smart Features

* Submission tracking
* Deadline monitoring
* Risk prediction for pending submissions
* Assignment similarity/plagiarism checking
* PDF/file attachment support

## Technologies Used

* **Python**
* **Tkinter** – Graphical User Interface
* **SQLite** – Database management
* **PDF/File Handling**
* **Similarity Checking**
* **Machine Learning/AI concepts** for smart features

## Project Structure

```text
College-Assignment-and-Practical-Submission-Tracker/
│
├── database/
│   ├── db.py
│   └── smartclass.db
│
├── pages/
│   ├── login.py
│   ├── student_dashboard.py
│   ├── teacher_dashboard.py
│   └── ...
│
├── main.py
├── requirements.txt
├── README.md
└── ...
```

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/College-Assignment-and-Practical-Submission-Tracker.git
```

### 2. Navigate to the project directory

```bash
cd College-Assignment-and-Practical-Submission-Tracker
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

##  Database

The application uses **SQLite** to store and manage:

* User accounts
* Student and teacher information
* Assignments
* Deadlines
* Submission records
* Marks
* Feedback

The database is initialized automatically when the application starts.

##  Objective

The main objective of this project is to provide a centralized platform for managing college assignments and practical submissions. It reduces manual tracking, helps students stay aware of deadlines, and allows teachers to efficiently manage submissions and grading.

##  Future Enhancements

* Email/notification reminders
* Cloud-based file storage
* Advanced plagiarism detection
* Performance analytics
* Mobile/web version
* AI-powered academic insights

##  Project

**College Assignment and Practical Submission Tracker**

Developed as an academic software project using Python, Tkinter, and SQLite.
