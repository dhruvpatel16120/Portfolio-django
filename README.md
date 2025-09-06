# Portfolio-django ✨

A sleek, responsive **Django-powered** personal portfolio website showcasing projects, built with an emphasis on **full-stack capabilities** and **SEO performance**.

[🌐 Live Demo](https://django-portfolio-live.vercel.app/)

---

## 📸 Preview

Here’s a quick look at the portfolio in action:  

| Desktop 💻 | Mobile 📱 |
|------------|-----------|
| ![Desktop Preview](https://via.placeholder.com/600x350?text=Portfolio+Desktop) | ![Mobile Preview](https://via.placeholder.com/250x500?text=Portfolio+Mobile) |

---

## 📑 Table of Contents

- [✨ Features](#-features)  
- [🛠️ Technologies Used](#️-technologies-used)  
- [📂 Project Structure](#-project-structure)  
- [⚡ Setup & Installation](#-setup--installation)  
- [🚀 Deployment](#-deployment)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  
- [📬 Contact](#-contact)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ⚡ **Dynamic Content** | Manage projects & updates via the Django admin panel. |
| 📱 **Mobile-Responsive UI** | Smooth user experience across all devices. |
| 🔍 **SEO Optimized** | Clean code structure for improved performance & search engine friendliness. |
| 🚀 **Easy Deployment** | Pre-configured for Vercel and other platforms. |

---

## 🛠️ Technologies Used

- **Backend Framework**: Django (Python) 🐍  
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 4 🎨  
- **Deployment**: Vercel (`vercel.json`) ☁️  
- **Automation**: Shell scripting (`build.sh`) ⚙️  
- **Dependency Management**: `requirements.txt` 📦  

---

## 📂 Project Structure

```

Portfolio-django/
├── templates/             # HTML templates for UI
├── static/                # Static assets (CSS, JS, images)
├── Home/                  # Homepage app
├── Contact_And_Feedback/  # Contact & feedback form app
├── DPO/                   # Main project folder
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
├── build.sh               # Build automation script
├── vercel.json            # Vercel deployment config
├── .env                   # Environment variables (not committed)
└── db.sqlite3             # Local development database

```

---

## ⚡ Setup & Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/dhruvpatel16120/Portfolio-django.git
   cd Portfolio-django
   ```

2. **Set up a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Store DB credentials & Gmail creds in `.env`.

5. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the server**

   ```bash
   python manage.py runserver
   ```

   Open → `http://127.0.0.1:8000` 🌐

---

## 🚀 Deployment

* Ready for **Vercel** out of the box (`vercel.json`, `build.sh`)
* Make sure environment variables are set in your hosting platform.

---

## 🤝 Contributing

Contributions are welcome 💡!

1. Fork this repo 🍴
2. Create a feature branch (`git checkout -b feature/awesome`)
3. Commit changes (`git commit -m "Added awesome feature ✨"`)
4. Push & open a PR 🚀

---

## 📜 License

This project is licensed under the **[MIT License](LICENSE)** 📄.

---

## 📬 Contact

👤 **Dhruv Patel**

* 🔗 GitHub: [@dhruvpatel16120](https://github.com/dhruvpatel16120)
* 🌐 Portfolio: [dhruvpatelofficial.vercel.app](https://dhruvpatelofficial.vercel.app)
* 💼 LinkedIn: [@dhruvpatel16120](https://www.linkedin.com/in/dhruvpatel16120/)

---

> “Empowering full-stack development through clean, responsive design and seamless deployment.” 🚀

---
