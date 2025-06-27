# 🌍 Gender Gap Visual Analytics Dashboard

This project explores **gender disparities in the energy sector** across multiple countries and dimensions — including **employment, leadership, innovation, and entrepreneurship** — using interactive dashboards built with **Python Dash**.

---

## 🎯 Project Title

**"Bridging the Gender Gap in the Energy Sector: A Multidimensional Exploration"**

---

## 📊 About the Project

The dashboard visualizes and analyzes gender-based inequalities across four key datasets, allowing users (e.g., policymakers, researchers) to:

- Track **gender wage gaps**
- Monitor **women’s leadership representation**
- Assess **female participation in innovation**
- Analyze **diversity among startup founders**

---

## 📁 Datasets Used

Data Source: [OECD / IEA LinkEED project]

| Dataset            | Focus Area            | Key Columns                                       |
|--------------------|------------------------|---------------------------------------------------|
| `Employment.csv`   | Wage gaps, education    | Country, Year, Gender, Sector, Wage Gap, etc.     |
| `Senior_Management.csv` | Women in leadership | Country, Role, % Women in Senior Roles            |
| `Innovation.csv`   | Patents & inventorship | Country, Year, Tech Type, % Female Inventors      |
| `Entrepreneurship.csv` | Startups & founders  | Country, Founder Gender, Capital Raised           |

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Dash by Plotly**
- **Plotly Express** – Charts and maps
- **Pandas** – Data cleaning & aggregation
- *(Optional)* GeoPandas, Scikit-learn – for advanced features

---

## 🧭 Dashboard Features

### Tabs Overview:
1. **Overview** – KPI Cards for wage gap, inventors, senior roles, and startup diversity
2. **Employment** – Line and bar charts on wage gaps
3. **Senior Management** – Leadership trends by role
4. **Innovation & Patents** – Female inventorship by tech sector
5. **Entrepreneurship** – Gender-diverse founder analysis
6. **Explorer** – Interactive filter for all indicators
7. **Advanced Insights** – Summary comparison charts by country

---

## 🚀 Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gender-gap-dash.git
cd gender-gap-dash
