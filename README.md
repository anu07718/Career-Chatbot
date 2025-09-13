# 🚀 AI Career Guidance Chatbot!

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent career guidance chatbot powered by Python Flask that analyzes user interests and provides personalized career recommendations with step-by-step roadmaps.

![WhatsApp Image 2025-08-03 at 23 15 26_b7dfea72](https://github.com/user-attachments/assets/2c3f9f0b-a897-493b-abbb-5037dbd87476)
![WhatsApp Image 2025-08-03 at 23 15 47_68666e01](https://github.com/user-attachments/assets/418dc895-3247-4308-9c47-6e3d3d329294)
![WhatsApp Image 2025-08-03 at 23 16 09_b9e93673](https://github.com/user-attachments/assets/26c3723e-a035-4187-9379-6528bb1e1363)


## ✨ Features

- 🎯 **Smart Career Matching** - AI-powered interest analysis
- 💼 **Detailed Career Info** - Skills, salary, growth prospects
- 🗺️ **Interactive Roadmaps** - Step-by-step career paths
- 🤖 **Real-time Chat** - Modern responsive interface

## 🚀 Quick Start

1. **Clone & Setup**
```bash
git clone https://github.com/yourusername/career-guidance-chatbot.git
cd career-guidance-chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install & Run**
```bash
pip install flask
python app.py
```

3. **Open Browser**
Navigate to `http://localhost:5000`

## 📁 Project Structure

```
career-guidance-chatbot/
├── app.py              # Flask backend with AI logic
├── templates/
│   └── index.html     # Frontend interface
├── requirements.txt   # Dependencies
└── README.md         # Documentation
```

## 💻 Usage Examples

```
User: "I love technology and programming"
Bot: "Great! Here are 3 career matches:
     • Software Developer ($70k-$150k+)
     • Data Scientist ($80k-$160k+) 
     • Cybersecurity Analyst ($75k-$140k+)"

User: "Show me roadmap for Software Developer"
Bot: [Displays 10-step detailed career roadmap]
```

## 🎯 Supported Careers

| Domain | Careers |
|--------|---------|
| 💻 **Technology** | Software Developer, Data Scientist, Cybersecurity |
| 🏥 **Healthcare** | Registered Nurse, Physical Therapist |
| 💼 **Business** | Business Analyst, Digital Marketing |
| 🎨 **Creative** | UX/UI Designer |
| 📚 **Education** | Elementary Teacher |

## 🛠️ Tech Stack

- **Backend**: Python Flask, Natural Language Processing
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Features**: RESTful API, Responsive Design, Real-time Chat

## 📡 API Endpoints

```bash
POST /chat           # Process user messages
GET /roadmap/<title> # Get career roadmap
GET /history         # Conversation history
```

## 🎨 Customization

Add new careers in `app.py`:
```python
'new_domain': {
    'keywords': ['keyword1', 'keyword2'],
    'careers': [{
        'title': 'Career Name',
        'description': 'Description...',
        'skills': ['Skill1', 'Skill2'],
        'salary_range': '$X - $Y',
        'roadmap': [...]
    }]
}
```

## 🚀 Deployment

**Heroku:**
```bash
# Create Procfile: web: python app.py
heroku create your-app-name
git push heroku main
```

**Docker:**
```bash
docker build -t career-chatbot .
docker run -p 5000:5000 career-chatbot
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Open Pull Request

## 📋 Requirements

```txt
Flask==2.3.3
Werkzeug==2.3.7
Jinja2==3.1.2
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Support

- 🐛 Issues: https://github.com/anu07718/Career-Chatbot
- 📧 Email: askotal077@gmail.com
- ⭐ Star this repo if helpful!

---
Made By Anushka ❤️
