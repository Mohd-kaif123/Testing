# agar python-project file sonar-scaner me run na ho tab
1) file exploser > C:\Users\manso\Downloads\sonar-scanner-cli-8.0.1.6346-linux-x64\sonar-scanner-8.0.1.6346-linux-x64\bin

2) Update sonar-project.properties:-

sonar.projectKey=python-project
sonar.projectName=python-project
sonar.projectVersion=1.0

sonar.sources=app
sonar.tests=tests

sonar.python.coverage.reportPaths=coverage.xml
sonar.sourceEncoding=UTF-8

sonar.host.url=http://localhost:9000
sonar.token=sqa_0f717fc3bb7d12a11f6165XXXXX

3) Step 1: PythonProject folder mein jao:- 
cd /mnt/d/Testing/sonarQube_with_jenkins/PythonProject

Step 2: Sahi path se scanner run karo:-
/mnt/c/Users/manso/Downloads/sonar-scanner-cli-8.0.1.6346-linux-x64/sonar-scanner-8.0.1.6346-linux-x64/bin/sonar-scanner

4) EXECUTION SUCCESS