![Screenshot (260)](https://github.com/user-attachments/assets/88d0e164-a5ba-4033-8d81-2db03613fea0)
![Screenshot (259)](https://github.com/user-attachments/assets/9aa7e8ae-d97b-4e69-992a-b92e53b215f5)


# 🧠 Kidney Disease Prediction Web App

A Django-based web application that predicts the risk of kidney disease using a machine learning model. Built with `SQLite3` as the backend database and integrates a pre-trained `.joblib` model for real-time predictions.

---

## 🚀 Features

- User-friendly form to enter medical data.
- Predicts kidney disease using a trained machine learning model.
- Displays prediction results instantly.
- Clean UI with Bootstrap (optional).
- Powered by Django and SQLite.

---

## 🗂️ Project Structure
KidneyDiseaseProject/
├── myproject/ # Django project folder
│ ├── settings.py
│ └── ...
├── kidneyapp/ # Django app folder
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ ├── templates/
│ └── ...
├── model/ # Folder with ML model
│ └── kidney_model.joblib
├── db.sqlite3 # (development only, ignore for production)
├── manage.py
├── requirements.txt
└── README.md
commands to run Project:
cd myproject
python manage.py runserver
