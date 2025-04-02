# RealAnalytics: Flask + PostgreSQL Analytics Dashboard

**RealAnalytics** is a full-stack Flask web application that tracks and visualizes article engagement using PostgreSQL. This project is designed for learning, resume enhancement, and demonstrating backend + data visualization capabilities.

---

## 🚀 Features

- 📊 **Interactive Dashboard** with Chart.js visualizations
- ⏱️ **Time Tracking** for each article view (auto-sent on idle or page exit)
- 🖱️ **Click Tracking** via AJAX requests
- 🌐 **Browser & OS Distribution** using `user-agents`
- 📦 **Dockerized** for easy deployment
- 🌍 **Live Deployment** on https://realanalytics.onrender.com/
- 📝 Clean project structure with Blueprints, SQLAlchemy models, and templates

---

## 📌 Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, Bootstrap, Chart.js, jQuery
- **Database**: PostgreSQL (hosted on Render)
- **Deployment**: Docker + Render.com

---

## 📊 What Is Tracked?

For each article:

- **Click count**
- **Total time spent** (in minutes)
- **Browser breakdown** (e.g., Chrome, Safari, Firefox)
- **Operating system breakdown** (e.g., Windows, Android, iOS)

---

## 🧠 How It Works

1. Landing page shows a list of articles
2. Each article click sends an **AJAX POST** request to `/update-analytics`
3. **User-Agent headers** are parsed to record browser and OS
4. A **time tracking script** tracks how long the user stays on the page
5. That time is sent to backend
6. Data is stored in a PostgreSQL database using SQLAlchemy models
7. Dashboard renders charts for:
   - Overall click distribution
   - Time spent distribution
   - Browser and OS breakdown for each article

---

## 🌐 Live Demo 

🔗 https://realanalytics.onrender.com/

![Demo](project.gif)
---

## 🧪 Future Usecases (My Plans)

- Auth system to track unique users
- Geo-location analytics
- Admin panel for article management
- Dark mode dashboard

---

## 👨‍💻 Created by

**Aashish** — [GitHub](https://github.com/KewlAashish)

Feel free to fork this project, contribute, or use it as a base for your own analytics platform!

