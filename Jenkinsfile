pipeline {
    agent any
    
    environment {
        GITHUB_USERNAME = "Yahyawi99" 
    }
    
    stages {
        stage('1. Install Heavy Dependencies') {
            steps {
                echo "Provisioning deep learning packages..."
                sh 'pip install --break-system-packages -r requirements.txt'
            }
        }
        
        stage('2. Execute ML Workloads (CI)') {
            when {
                expression { params.EVENT_TYPE == 'PULL_REQUEST' || params.EVENT_TYPE == 'RETRAIN_ON_NEW_DATA' }
            }
            steps {
                echo "Triggering Ray Torch distributed trainer..."
                
                sh '''
                python3 madewithml/train.py \
                    --experiment-name "madewithml-experiment" \
                    --dataset-loc "datasets/projects.csv" \
                    --train-loop-config '{"dropout_p": 0.5, "lr": 1e-4, "lr_factor": 0.8, "lr_patience": 3}' \
                    --num-workers 1 \
                    --num-epochs 1 \
                    --batch-size 128
                '''
            }
        }
    }
}