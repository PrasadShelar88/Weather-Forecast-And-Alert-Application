# Weather Forecast & Alert Application
**Weather Forecast & Alert Application** that fetches weather data, analyzes forecast conditions, generates risk alerts, and displays weather insights through a clean dashboard.This project is built using **Python, FastAPI, Open-Meteo API, SQLite, React, Vite, and Recharts**. It is designed as a student-friendly and GitHub-ready project for roles related to **Python Development, API Integration, Automation, Data Analysis, and Web App Development**.---## 📌 Project OverviewWeather conditions affect daily life, travel, farming, logistics, outdoor events, and business operations. Manually checking weather updates for multiple cities can be time-consuming.The **Weather Forecast & Alert Application** solves this problem by automatically fetching weather data, processing forecasts, checking alert conditions, and displaying useful weather information in a dashboard.The system can generate alerts for conditions such as rain, high temperature, strong wind, high humidity, and UV risk.---## 🎯 Project ObjectiveThe main objective of this project is to build a weather monitoring system that can:- Fetch current and forecast weather data- Display city-wise weather information- Analyze temperature, humidity, rain, wind, and UV index- Generate weather alerts based on threshold values- Show forecast trends using charts- Provide a clean dashboard for users- Store or simulate weather data for testing- Generate reports for GitHub/project documentation---## 🧩 Problem StatementUsers, farmers, travelers, event planners, and logistics teams often need quick weather insights and alerts. Checking weather manually may cause delays or missed warnings.This project automates weather tracking and alert generation using public weather data and rule-based alert logic.---## 🚀 Features- City-wise weather forecast- Current weather details- Hourly forecast data- Daily forecast data- Rain alert generation- High temperature alert- High wind alert- Humidity alert- UV risk alert- Weather trend charts- Forecast dashboard- SQLite-based local storage- Open-Meteo API integration- No API key required- FastAPI backend- React frontend dashboard- Error handling for invalid requests- GitHub-ready project structure---## 🛠️ Tech Stack### Backend- Python- FastAPI- Uvicorn- HTTPX / Requests- SQLite- Pandas- Pydantic- Datetime- JSON### Frontend- React- Vite- JavaScript- HTML- CSS- Axios- Recharts### API / Data Source- Open-Meteo API- Sample weather simulation data### Concepts Used- API integration- JSON parsing- Weather data processing- Forecast analysis- Alert condition checking- Rule-based alert engine- Data visualization- Dashboard development---## 🔄 Project Workflow```textCity Selection      ↓Weather API Request      ↓JSON Response Parsing      ↓Weather Data Processing      ↓Forecast Analysis      ↓Alert Rule Checking      ↓Weather Dashboard Display      ↓Report / Output Generation

📁 Project Structure
Weather-Forecast-Alert-Application/│├── backend/│   ├── api/│   │   └── app.py│   ││   ├── src/│   │   ├── weather_client.py│   │   ├── alert_engine.py│   │   ├── database.py│   │   ├── report_generator.py│   │   └── sample_data.py│   ││   ├── data/│   │   └── sample_weather.json│   ││   ├── db/│   │   └── weather.db│   ││   ├── outputs/│   │   └── weather_report.csv│   ││   ├── requirements.txt│   ├── .env.example│   └── README.md│├── frontend/│   ├── src/│   │   ├── App.jsx│   │   ├── main.jsx│   │   ├── api.js│   │   └── styles.css│   ││   ├── public/│   ├── package.json│   └── README.md│├── images/├── reports/├── docs/├── README.md└── .gitignore

📂 Folder Explanation
Folder / FileDescriptionbackend/Contains FastAPI backend and weather logicbackend/api/Contains backend API entry pointbackend/src/Contains weather fetching, alert, database, and report modulesbackend/data/Stores sample weather databackend/db/Stores SQLite databasebackend/outputs/Stores generated reportsfrontend/Contains React dashboardimages/Stores GitHub screenshotsreports/Stores exported reportsdocs/Stores additional documentation.env.exampleShows environment variable format.gitignorePrevents unnecessary/private files from upload

⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/your-username/Weather-Forecast-Alert-Application.gitcd Weather-Forecast-Alert-Application

▶️ Backend Setup
1. Go to Backend Folder
cd backend
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
For Windows:
venv\Scripts\activate
For macOS/Linux:
source venv/bin/activate
4. Install Backend Dependencies
pip install -r requirements.txt
5. Run Backend Server
uvicorn api.app:app --reload
Backend will run at:
http://127.0.0.1:8000
Swagger API documentation:
http://127.0.0.1:8000/docs

💻 Frontend Setup
1. Go to Frontend Folder
cd frontend
2. Install Frontend Dependencies
npm install
3. Run Frontend
npm run dev
Frontend will run at:
http://localhost:5173

📌 API Endpoints
MethodEndpointDescriptionGET/Backend status checkGET/healthAPI health checkGET/locationsGet available city/location listGET/weather/currentGet current weatherGET/forecast/hourlyGet hourly forecastGET/forecast/dailyGet daily forecastGET/alertsGet generated weather alertsPOST/refreshRefresh weather dataGET/reportGet generated weather report

🧪 Sample Cities
PuneMumbaiDelhiBengaluruHyderabadChennaiNagpurNashikChhatrapati Sambhajinagar

🧪 Sample Output
City: PuneTemperature: 31°CHumidity: 54%Wind Speed: 12 km/hRain Probability: 20%UV Index: 6Alert Status:No critical weather alert detected.

⚠️ Sample Alert Output
City: MumbaiAlert Type: Rain AlertSeverity: WarningMessage: Rain is likely in the next 12 hours. Carry an umbrella and plan travel carefully.
City: NagpurAlert Type: Heat AlertSeverity: CriticalMessage: High temperature expected. Stay hydrated and avoid outdoor activity during peak afternoon hours.

✅ Alert Logic
The application checks weather conditions using predefined rules.
ConditionAlertRain probability above thresholdRain AlertTemperature above thresholdHeat AlertWind speed above thresholdWind AlertHumidity above thresholdHumidity AlertUV index above thresholdUV Alert
Example thresholds:
Rain Probability >= 60%Temperature >= 40°CWind Speed >= 50 km/hHumidity >= 80%UV Index >= 8

📊 Visualizations
The frontend dashboard can display:


Current temperature card


Humidity card


Wind speed card


Rain probability card


Hourly temperature chart


Daily forecast chart


Rain probability chart


Alert badges


Example screenshot links:
![Dashboard](images/dashboard.png)![Hourly Forecast](images/hourly-forecast.png)![Daily Forecast](images/daily-forecast.png)![Weather Alerts](images/weather-alerts.png)

📄 Generated Reports
The project can generate reports inside:
backend/outputs/
Example report files:
weather_report.csvweather_summary.txt
Report contains:


City name


Date and time


Temperature


Humidity


Wind speed


Rain probability


UV index


Alert type


Alert severity


Alert message



🖼️ Recommended Screenshots for GitHub
Add these screenshots inside the images/ folder:


Project folder structure


Backend running terminal


FastAPI Swagger UI


Frontend dashboard


City search/dropdown


Current weather output


Hourly forecast chart


Daily forecast chart


Alert message output


Generated CSV report


GitHub repository preview



🔐 API Key and Security Notes
This project can use Open-Meteo API, which does not require an API key.
If you use another provider such as OpenWeatherMap or WeatherAPI, do not upload your API key to GitHub.
Use .env for real keys:
WEATHER_API_KEY=your_api_key_here
Use .env.example for GitHub:
WEATHER_API_KEY=your_api_key_here
Add .env to .gitignore.

✅ Example .gitignore
.envvenv/__pycache__/*.pycnode_modules/dist/build/.db*.sqlite3.DS_Store

🌍 Real-World Use Cases
This application can be useful for:


Travelers checking weather before trips


Farmers planning irrigation


Logistics teams planning routes


Event planners monitoring rain risk


Schools checking heat advisories


Outdoor workers checking weather alerts


Daily users checking city forecasts


Businesses planning weather-sensitive operations



📈 Industry Relevance
Weather applications are widely used in:


Logistics


Agriculture


Travel


Public safety


Event management


Renewable energy


Smart city applications


Fleet management


This project demonstrates skills in:


Python API integration


Backend development


JSON data processing


Data visualization


Rule-based alert systems


Frontend dashboard development


Report generation


Full-stack project development



🧠 Learning Outcomes
By completing this project, I learned:


How weather APIs work


How to fetch data from public APIs


How to parse JSON responses


How to process forecast data


How to generate alerts using conditions


How to build APIs using FastAPI


How to store weather data locally


How to connect React frontend with Python backend


How to visualize weather data using charts


How to prepare a GitHub-ready full-stack project



🚀 Future Enhancements


Add live location support


Add map view using Leaflet


Add AQI alerts


Add email weather alerts


Add SMS/WhatsApp notifications


Add multi-city comparison


Add weather history tracking


Add user login system


Add dark/light mode


Add mobile responsive PWA support


Add Docker deployment


Add cloud hosting



📌 GitHub Commit Plan
Day 1
Initial project setup with backend and frontend folders
Day 2
Added weather API integration and sample city data
Day 3
Implemented JSON parsing and forecast processing
Day 4
Added alert engine for rain, heat, wind, humidity, and UV
Day 5
Created weather dashboard with charts and alert badges
Day 6
Added report generation, documentation, and screenshots

❓ Interview Questions and Answers
1. Explain your project.
This project is a Weather Forecast & Alert Application that fetches current and forecast weather data for selected cities, processes the data, checks weather risk conditions, and generates alerts for rain, heat, wind, humidity, and UV index. It also displays weather insights using a dashboard.
2. What problem does this project solve?
It helps users get weather updates and alerts automatically without manually checking weather websites. It is useful for travelers, farmers, logistics teams, event planners, and daily users.
3. What technologies did you use?
I used Python, FastAPI, HTTPX or Requests, SQLite, Pandas, React, Vite, Axios, and Recharts.
4. How does the application fetch weather data?
The backend sends an API request to a weather provider such as Open-Meteo. The response is received in JSON format and then processed by the application.
5. What is JSON and why is it used?
JSON stands for JavaScript Object Notation. It is used by APIs to send structured data in a lightweight format.
6. How does the alert system work?
The alert system compares weather values with predefined thresholds. If rain probability, temperature, wind speed, humidity, or UV index crosses the threshold, the system generates an alert.
7. How did you handle API errors?
I handled API errors using try-except blocks, HTTP status checks, fallback sample data, and proper error messages.
8. What output does your project generate?
The project generates current weather details, hourly and daily forecasts, alert messages, charts, and optional CSV reports.
9. How can this project be improved?
It can be improved by adding AQI data, live location, maps, notifications, SMS alerts, email alerts, and cloud deployment.
10. How would you explain this project to a non-technical person?
I created an application that checks weather conditions for a city and automatically warns the user if there is rain, high temperature, strong wind, or any important weather condition.

👨‍💻 Author
Prasad Shelar
B.Tech Computer Science Student

⭐ Support
If you found this project useful, please give it a star on GitHub.
