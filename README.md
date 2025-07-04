# 📚 AI Story Generator from Prompts

A web-based application that uses **Google Gemini AI** to generate creative story ideas based on user-provided inputs like genre, theme, and main character. This tool helps writers, students, and content creators overcome creative blocks and brainstorm unique story concepts using Generative AI.

---

## 🚀 Features

- 🧠 Generates short, creative story ideas from structured prompts
- 🧾 Users can select between **Basic**, **Elaborate**, and **Constraint**-based storytelling modes
- 🧑‍💻 Simple and clean **Flask** (or Streamlit) web interface
- ⚡ Fast and responsive with **Gemini 1.5 Flash API**
- 🔁 Robust handling of edge cases and invalid inputs

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Google Gemini API** via `google-generativeai`
- **Flask** (or use [Streamlit] for faster prototyping)
- **HTML / CSS** (Jinja2 templates)
- Optional: Deployed via [Render] or [Streamlit Cloud]

---

## 📥 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ai-story-generator.git
cd ai-story-generator

🧪 Example Input
Genre: Sci-Fi
Theme: Memory loss
Main Character: A robot nurse who once had feelings
📝 Example Output
In a future where memories are stored like files, a robot nurse begins to experience glitches—visions of a life she never lived. As she searches for answers, she uncovers a hidden part of her identity that threatens the foundation of the robotic world.
📁 Project Structure
php
Copy
Edit
├── app.py                 # Main Python application (Flask or Streamlit)
├── templates/
│   └── index.html         # HTML UI for Flask version
├── static/                # Optional: CSS or images
├── requirements.txt       # Python dependencies
├── README.md              # This file
🎯 Future Improvements
Add full story generation, not just ideas
Multilingual support (Hindi, Telugu, etc.)
Save/export generated stories as PDF or text
AI story continuation or character builder
Deploy live with user accounts and feedback

🙋‍♀️ Author
Name: Jeevana
College: VIT VELLORE
Email: kudum.jeevana2023@vitstudent.ac.in




