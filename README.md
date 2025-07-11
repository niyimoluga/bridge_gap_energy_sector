# Gender Gap in the Energy Sector – Visual Analytics Dashboard

This project explores gender disparities in the energy sector using an interactive data dashboard. It was developed for the course **Computational Visual Analytics**, based on OECD/IEA LinkEED data.

## 📁 Project Structure

gender-gap-dash/
│
├── app.py # Main Dash application
├── utils.py # Helper function to load and merge data
├── data/
│ ├── Employment.csv
│ ├── Innovation.csv
│ ├── Senior Management.csv
│ └── Entrepreneurship.csv
├── assets/ # (optional) For CSS styling or logo
├── README.md # This file
└── requirements.txt # Python dependencies

## 🚀 How to Run the App

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

## 🚀 How to Run the App

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
python app.py
Open in Browser
Visit http://127.0.0.1:8050/ in your browser.

💡 Features
✅ Overview Tab with KPI summaries for wage gap, senior roles, inventors, and founders

✅ Line and bar charts for employment trends

✅ Senior management breakdown by role and over time

✅ Innovation sector breakdown with female inventors

✅ Treemap view for gender-diverse founders by startup sector

✅ Explorer tab for custom comparisons

✅ Advanced Insights with country-level comparisons

📊 Data Source
OECD/IEA LinkEED matched employer–employee data

Countries: Austria, France, Germany, Portugal, Spain

Topics: Employment, Innovation, Senior Management, Entrepreneurship

👥 Target Users
Policy makers

Journalists

Energy sector HR managers

Researchers