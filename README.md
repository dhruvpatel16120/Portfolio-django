# Portfolio-django

A sleek, responsive Django-powered personal portfolio website showcasing projects, built with an emphasis on full-stack capabilities and SEO performance.

[Live Demo](https://django-portfolio-live.vercel.app/)

---

##  Table of Contents

- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Project Structure](#project-structure)  
- [Setup & Installation](#setup--installation)  
- [Deployment](#deployment)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Features

- **Dynamic Content** — Manage projects and updates via the Django admin panel.  
- **Mobile-Responsive UI** — Built with modern HTML, CSS, and JavaScript for a smooth user experience across devices.  
- **Full-stack SEO Optimized** — Clean code structure for improved performance and search engine friendliness.  
- **Easy Deployment** — Configured for rapid deployment (e.g., with Vercel).

---

## Technologies Used

- **Backend Framework**: Django (Python)  
- **Frontend**: HTML, CSS, JavaScript, bootstrap 4
- **Deployment**: Vercel (with `vercel.json`)  
- **Auxiliary**: Shell scripting (e.g., `build.sh`)  
- **Dependency Management**: `requirements.txt`  

---

## Project Structure

```

Portfolio-django/
├── templates/          # HTML templates for UI
├── static/             # Static assets (CSS, JS, images)
├── Home/               # Your Django app for homepage functionality
├── Contact\_And\_Feedback/  # App for handling contact/feedback
├── DPO/                # Another Django app (name TBD)
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
├── build.sh            # Build automation script
├── vercel.json         # Vercel deployment config
├── .env                # Environment variables (not committed)
└── db.sqlite3          # Local development database

``` 
---

## Setup & Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/dhruvpatel16120/Portfolio-django.git
   cd Portfolio-django
   ```

2. **Set up a virtual environment**

   ```bash
   python3 -m venv venv       # or: python -m venv venv
   source venv/bin/activate   # Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   * keep your database , gmail credentails in ".env" file

5. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   * Open `http://127.0.0.1:8000` in your browser.

---

## Deployment

This project is configured to deploy easily to platforms like **Vercel**, with predefined settings in `vercel.json` and automation via `build.sh`.
Ensure your environment variables are configured in your deployment settings for smooth operation.

---

## Contributing

Contributions—bug reports, enhancements, or tweaks—are welcome! Just follow these steps:

1. Fork this repo
2. Create a feature branch (`git checkout -b feature/name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to your branch (`git push origin feature/name`)
5. Open a pull request describing your changes

---

## License

[MIT License](LICENSE) or specify your preferred license.

---

## Contact

**Dhruv Patel**

* GitHub: [@dhruvpatel16120](https://github.com/dhruvpatel16120)
* Portfolio: [dhruvpatelofficial.vercel.app](https://dhruvpatelofficial.vercel.app)
* LinkedIn: [@dhruvpatel16120](https://www.linkedin.com/in/dhruvpatel16120/) 

---

> “Empowering full-stack development through clean, responsive design and seamless deployment.”

---
