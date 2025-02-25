# HealingEdu1-project
```markdown
Healing Edu is an integrated web application designed to provide educational resources on healing and wellness. The project combines the power of **Django** for backend web development and **Streamlit** for creating an interactive chatbot interface.

---

## 📂 Project Structure
```bash
├── app/              # Django application with views, models, and forms
├── data/             # Data files used by the project
├── project/          # Django project configurations and settings
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates for the Django frontend
├── chatbot.py        # Streamlit application for the chatbot interface
├── manage.py         # Django management script
├── requirements.txt  # List of Python dependencies
└── .gitignore        # Files and directories to be ignored by Git
```

---

## 🚀 Features
- **Interactive Chatbot:** Built using Streamlit for providing instant support and information.
- **User-Friendly Website:** Created with Django to display educational content on healing practices.
- **Seamless Integration:** Both the chatbot and website work together to offer a unified experience.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/SumayyaAli11/HealingEdu1-project.git 
cd healing-edu
```

### 2. Create and activate a virtual environment
```bash
# On macOS/Linux:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\\Scripts\\activate
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the Django project
```bash
python manage.py migrate        # Apply database migrations
python manage.py runserver      # Run the Django development server
```

### 5. Run the Streamlit chatbot
```bash
streamlit run chatbot.py
```

---

## 🖥️ Usage
- Visit the Django website: http://localhost:8000 for healing resources.
- Access the Streamlit chatbot via the URL provided after running the above Streamlit command.

---

## 📑 Requirements
```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt
```

---

## 🤝 Contributing
Contributions are welcome! 
- Fork the repository
- Create a new branch: `git checkout -b feature/your-feature`
- Commit your changes: `git commit -m "Add your message"`
- Push to the branch: `git push origin feature/your-feature`
- Open a Pull Request

---

## 📄 License
This project is licensed under the **MIT License**. See the `LICENSE` file for more information.

---

## 🙌 Acknowledgements
Thanks to the open-source community for providing the tools and frameworks that made this project possible.

---

## 💡 Contact
For questions or support, feel free to reach out via sumayyaali.work@gmail.com.
```
