#### Jenkins + Locust + Flask — Pura Project Samjho ####

# 🧠 Pehle Samjho — Yeh Project Kya Hai?
Tumhara Flask API  →  Locust se Load Test  →  Jenkins se Automate

3 cheezein milke kaam karti hain:-
Flask = Ek chota sa website/API banata hai
Locust = Us API par fake users bhejta hai (load test)
Jenkins = Yeh sab automatically karta hai


📒 NOTES — Task by Task

✅ Task 1: Flask App Banana
-> Flask kya hai? — Python ka ek simple web framework. Matlab Python se website/API bana sakte ho.

app.py file banao:-

from flask import Flask

app = Flask(__name__)

@app.route("/")          # localhost:5000 par jaoge to yeh chalega
def home():
    return {
        "status": "success",
        "message": "Flask API Running"
    }

@app.route("/health")    # localhost:5000/health par jaoge to yeh chalega
def health():
    return {
        "status": "UP"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)   # Port 5000 par chalao

Test karo:
python app.py
Browser mein kholo:

http://localhost:5000 → {"status": "success", "message": "Flask API Running"}
http://localhost:5000/health → {"status": "UP"}


✅ Task 2: Locust File Banana
locustfile.py — Yeh batata hai ki Locust kya kare
pythonfrom locust import HttpUser, task, between

class ApiUser(HttpUser):        # Ek fake user ka blueprint

    wait_time = between(1, 2)   # Har request ke beech 1-2 second wait karo

    @task
    def home(self):
        self.client.get("/")        # "/" URL hit karo

    @task
    def health(self):
        self.client.get("/health")  # "/health" URL hit karo

Simple explanation:

ApiUser = Ek fake user hai
@task = Yeh user yeh kaam karega
wait_time = Har kaam ke beech thoda rukega


✅ Task 3: Requirements File
requirements.txt — Sare dependencies ek jagah
flask
locust

Install karo ek command se:-
pip install -r requirements.txt

✅ Task 4: Locust Manually Chalao (2 Terminal)
Terminal 1                    Terminal 2
-----------                   -----------
python app.py        →        locust -f locustfile.py
(Flask chalu karo)            (Locust chalu karo)
Browser mein jao: http://localhost:8089

Wahan fill karo:
Field           Value
Users           20
Ramp Up         5
Host            http://localhost:5000

✅ Task 5: Headless Locust (Bina Browser ke)
-> Jab Jenkins se chalana ho to browser nahi khulega, isliye headless mode:
locust \
-f locustfile.py \
--host=http://localhost:5000 \
--users 50 \
--spawn-rate 5 \
--run-time 30s \
--headless

Option                  Matlab
--users 50              50 fake users banao
--spawn-rate 5          Har second 5 user add karo
--run-time 30s          30 second tak test chalao
--headless              Bina UI ke chalao

✅ Task 6: Jenkins Freestyle Project
-> Jenkins mein Freestyle Project banao aur Execute Shell mein yeh likho:
python3 -m venv venv          # Virtual environment banao
. venv/bin/activate            # Activate karo
pip install -r requirements.txt  # Dependencies install karo

nohup python app.py > app.log 2>&1 &   # Flask background mein chalao
sleep 5                        # 5 second ruko (Flask start hone do)

locust \
-f locustfile.py \
--host=http://localhost:5000 \
--users 50 \
--spawn-rate 5 \
--run-time 30s \
--headless

-> nohup ... & ka matlab = Background mein chalao, terminal band hone par bhi chalta rahe


✅ Task 7: Jenkins Pipeline (Jenkinsfile)
Pipeline mein stages hoti hain — har stage alag kaam karti hai:
Stage 1: Checkout    →  GitHub se code lo
Stage 2: Setup       →  Python env + packages install
Stage 3: Flask Start →  API background mein chalao
Stage 4: Locust Test →  Load test chalao

Jenkinsfile:-

pipeline {
    agent any

    stages {

        stage('Checkout') {          // GitHub se code lo
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {      // Environment ready karo
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start Flask API') {   // Flask chalao (background mein)
            steps {
                sh '''
                . venv/bin/activate
                nohup python app.py > app.log 2>&1 &
                sleep 5
                '''
            }
        }

        stage('Run Locust Test') {   // Load test chalao
            steps {
                sh '''
                . venv/bin/activate
                locust \
                -f locustfile.py \
                --host=http://localhost:5000 \
                --users 50 \
                --spawn-rate 5 \
                --run-time 30s \
                --headless
                '''
            }
        }
    }

    post {                           // Test ke baad kya karna hai
        success { echo 'Performance Test Passed' }
        failure { echo 'Performance Test Failed' }
        always  { archiveArtifacts artifacts: '*.log' }  // Log file save karo
    }
}

✅ Bonus: HTML Report Generate Karo
bashlocust \
-f locustfile.py \
--host=http://localhost:5000 \
--users 50 \
--spawn-rate 5 \
--run-time 30s \
--headless \
--html report.html       # ← Yeh add karo bas

-> report.html file ban jayegi jisme poora test result dikhega

🔁 Pura Flow Ek Baar Mein
GitHub (code rakho)
       ↓
Jenkins (automatically trigger hota hai)
       ↓
Python Virtual Env banta hai
       ↓
Flask API start hoti hai (port 5000)
       ↓
Locust 50 fake users bhejta hai 30 sec tak
       ↓
Result/Log save hota hai
       ↓
Build → Pass ✅ ya Fail ❌

📁 Project Files Structure
project/
│
├── app.py              ← Flask API
├── locustfile.py       ← Locust test
├── requirements.txt    ← Dependencies
├── Jenkinsfile         ← Pipeline script
└── app.log             ← Flask logs (auto-generate)

Ab perform karna hai? Toh batao — kahan se shuru karein:

1. Flask app locally chalana hai pehle?
2. Seedha Jenkins pipeline setup karna hai?
3. GitHub se connect karna hai?
