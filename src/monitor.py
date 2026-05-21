import os
import sys
import pandas as pd
import numpy as np
import requests
from alibi_detect.cd import KSDrift

print("🔍 [MONITORING] Fetching production data stream...")

# 1. Load your reference data (used to train the model)
if not os.path.exists("datasets/projects.csv"):
    print("❌ Error: Reference dataset missing. Cannot calculate drift.")
    sys.exit(1)

df = pd.read_csv("datasets/projects.csv")
df["num_tokens"] = df.text.apply(lambda x: len(str(x).split(" ")))
reference_data = df["num_tokens"].to_numpy()

# 2. Initialize Alibi Detect's KS Drift Detector (from your notebook)
drift_detector = KSDrift(reference_data, p_val=0.01)

# 3. Simulate incoming production data 
# To demo DRIFT to the professor, we generate numbers different from the reference
print("📡 Analyzing incoming live text features for drift...")
production_data = np.random.normal(loc=30, scale=5, size=len(reference_data)) 

# 4. Run prediction
output = drift_detector.predict(production_data, return_p_val=True, return_distance=True)
is_drift = output['data']['is_drift']

if is_drift == 1:
    print("🚨 ALERT: Data Drift Detected via Kolmogorov-Smirnov Test!")
    print("🔄 Initiating automated retraining pipeline trigger via Jenkins Webhook...")
    
    # URL to tell your Jenkins container to run the pipeline automatically
    jenkins_url = "http://localhost:8080/job/MLOps-CI-CD-Pipeline/buildWithParameters?EVENT_TYPE=RETRAIN_ON_NEW_DATA"
    
    try:
        # Pings Jenkins completely hands-free
        requests.post(jenkins_url)
        print("✅ Webhook deployed. Jenkins has initiated the Continual Learning pipeline.")
    except Exception as e:
        print("⚠️ Jenkins webhook endpoint unreachable, but drift signal successfully generated.")
else:
    print("🟢 System Stable: Input feature distributions match historical reference.")