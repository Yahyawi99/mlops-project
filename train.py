import random
import sys

print("--------------------------------------------------")
print("Training Model...")
print("Loading dataset")

# fake metric score
accuracy = round(random.uniform(0.70, 0.95), 2)
print(f"Model Accuracy: {accuracy}")

# performance threshold
threshold = 0.80
if accuracy >= threshold:
    print(f"Success: Performance ({accuracy}) exceeds threshold ({threshold}).")
    print("--------------------------------------------------")
    sys.exit(0)
else:
    print(f"Failure: Performance ({accuracy}) is below threshold ({threshold}).")
    print("--------------------------------------------------")
    sys.exit(1)