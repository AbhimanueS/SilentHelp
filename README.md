🆘 SILENTHELP – Anonymous Help Request Portal

A Flask-based anonymous web platform that empowers individuals to report sensitive issues — such as mental health struggles, bullying, or abuse — without fear of judgment or exposure. Designed for schools, colleges, NGOs, or any institution promoting psychological well-being and safe reporting.

🚀 Features

✅ Anonymous help request submission  
✅ Categories: Mental Health, Bullying, Domestic Abuse, Other  
✅ Optional email field for follow-up (never required)  
✅ Clean Bootstrap UI with emergency "Exit Quickly" button  
✅ Admin dashboard to view all requests (no login required yet)  
✅ Local SQLite database for lightweight, secure storage

📦 Technologies Used

🐍 Python  
🌐 Flask  
🎨 HTML, CSS, Bootstrap  
🗃 SQLite  
📥 Jinja2 Templating

📁 Project Structure

silenthelp/  
├── app.py                 # Flask backend logic  
├── requirements.txt       # Python dependencies  
├── README.md              # Project documentation  
├── templates/  
│   ├── index.html         # Anonymous form page  
│   └── dashboard.html     # Admin dashboard  
├── static/  
│   ├── css/style.css      # Custom styles  
│   └── js/script.js       # Alert on submit  
└── data.db (auto-created) # Local SQLite database

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/yourusername/silenthelp.git  
cd silenthelp

2. Create and Activate a Virtual Environment

python -m venv venv

Windows:  
venv\Scripts\activate  

Linux/macOS:  
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Flask App

python app.py

5. Access in Browser

Anonymous Help Form: http://127.0.0.1:5000  
Admin Dashboard: http://127.0.0.1:5000/dashboard

🌍 Social Impact

SILENTHELP addresses a critical societal need — the lack of anonymous reporting systems for people facing psychological pressure, abuse, or harassment. This platform helps:

• Encourage safe reporting without fear of retaliation  
• Give voice to the unheard and unseen  
• Provide a channel for institutions to monitor mental health or abuse cases  
• Create a compassionate support system in educational or community environments  

🧠 Future Improvements

• Admin login and moderation features  
• Captcha verification to prevent spam/fake submissions  
• Email notification system to alert support teams  
• Data export (CSV/PDF) for reports  
• Deployment on Render or Railway for online hosting  
• AI-based text analysis for categorizing urgency

