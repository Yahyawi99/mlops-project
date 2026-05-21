## STEP 1: Launch Jenkins via Docker

docker run -d -p 8080:8080 -p 50000:50000 --name mlops-jenkins -u root jenkins/jenkins:lts

## step 2: Install Python Inside the Jenkins

docker exec -it mlops-jenkins bash
apt-get update
apt-get install -y python3 python3-pip
exit

## Step 3: Unlock the Jenkins Web Interface

bash docker logs mlops-jenkins

## Step 4: Create Mock Machine Learning Scripts

train.py
