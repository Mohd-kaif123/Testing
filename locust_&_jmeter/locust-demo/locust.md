##### Locust with Jenkins - Step by Step Explanation ####

Yeh guide Locust (load testing tool) ko Jenkins (CI/CD automation tool) ke saath use karne ke baare mein hai. Chalo ekdum simple aur step-by-step samajhte hain:

# 🔵 Pehle Samjho - Yeh Kya Hai?
-> Locust = Ek tool jo website/API par load testing karta hai (matlab fake users banata
    hai aur check karta hai server kitna load handle kar sakta hai)
-> Jenkins = Ek tool jo automatically tasks run karta hai (jaise code build karna, tests chalana)

### 📌 Part 1: Locust Install Karna ###

# Step 1 — System Update Karo
sudo apt update
->Yeh command system ke packages ko update karta hai. Sab kuch latest version mein hoga.

# Step 2 — Python Virtual Environment Install Karo
sudo apt install python3-venv python3-full -y
-> python3-venv = Virtual environment banane ka tool
-> Virtual environment kyu? Taaki Locust ka installation system ke baaki Python
    packages se alag rahe — koi conflict nahi hoga

# Step 3 — Virtual Environment Banao
python3 -m venv venv
-> Ek folder ban jayega jiska naam venv hoga — ismein tumhara isolated Python environment hoga

# Step 4 — Virtual Environment Activate Karo
source venv/bin/activate
-> Ab terminal mein (venv) dikhega — matlab tum ab us environment ke andar ho

# Step 5 — Locust Install Karo
pip install locust
-> Yeh Locust ko virtual environment mein install kar dega

### 📌 Part 2: Jenkins Setup Karna ###

# Step 6 — Jenkins Start Karo
sudo systemctl start jenkins
-> Jenkins ek background service hai, yeh command se start hoti hai

# Step 7 — Browser Mein Jenkins Kholo
localhost:8080
-> Jenkins ka dashboard yahan dikhega

# Step 8 — Naya Pipeline Banao
-> Jenkins mein jaao aur "New Item" click karo → Pipeline select karo → naam do (jaise locust_pipeline)

# Step 9 — Pipeline Script Likho
Yeh script Jenkins ko batati hai ki kya karna hai automatically:

groovy
pipeline {
    agent any
    stages {

        stage('setup python environment') {  // Stage 1: Environment banao
            steps {
                sh '''
                    python3 -m venv venv        // Virtual env banao
                    . venv/bin/activate         // Activate karo
                    pip install --upgrade pip   // pip update karo
                    pip install locust          // Locust install karo
                '''
            }
        }

        stage('Run Locust Tests') {           // Stage 2: Test chalao
            steps {
                sh '''
                    . venv/bin/activate        // Env activate karo
                    locust -f locustfile.py    // Locust test chalao
                '''
            }
        }

    }
}
2 Stages hain:

Stage 1 → Environment ready karo
Stage 2 → Locust test chalao

### 📌 Part 3: locustfile.py Banana ###

# Step 10 — Jenkins Workspace Mein Jao
cd /var/lib/jenkins/workspace/
ls
-> Yahan Jenkins apne projects rakhta hai

# Step 11 — Agar Project Folder Nahi Dikh Raha
-> Ek baar Jenkins mein Build chalao — build fail hogi, koi baat nahi! Fail hone ke
baad folder ban jayega. Phir dobara ls karo, folder dikh jayega.

# Step 12 — Project Folder Mein Jao
cd locust_pipeline    # apna project naam likhna yahan

# Step 13 — locustfile.py Banao
sudo nano locustfile.py
-> Yeh file mein tum likhoge ki kaun se URL test karne hain, kitne users banane hain etc.

Nano editor mein:

Ctrl + S → Save
Ctrl + O → Write (save to file)
Ctrl + X → Exit

# Step 14 — Jenkins Mein Build Chalao
-> Jenkins dashboard par jao → apna pipeline kholo → "Build Now" click karo

# Step 15 — Browser Mein Result Dekho
-> Locust apna web UI kholta hai, browser mein jao:

localhost:8089
Yahan dikhega kitne users test kar rahe hain, response time kya hai, errors kitni hain etc.

#######################################################################################

🟢 Pura Flow Ek Baar Mein Samjho
Tum → Jenkins mein Build Click karo
         ↓
Jenkins → Python Virtual Env banata hai
         ↓
Jenkins → Locust install karta hai
         ↓
Jenkins → locustfile.py se test chalata hai
         ↓
Tum → Browser mein localhost:8089 pe result dekhte ho



⚠️ Important Notes
        Baat	                                        Explanation
- Build pehli baar fail hogi	                - Yeh normal hai, ghabrao mat
- venv activate karna zaroori hai	            - Bina activate kiye locust command nahi milegi
- locustfile.py sahi jagah hona chahiye	        - Jenkins workspace folder mein hona chahiye
- Jenkins aur Locust dono alag kaam karte hain  - Jenkins automation karta hai, Locust actual testing



