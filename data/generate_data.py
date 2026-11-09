import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

n_records = 5000

# Generate timestamps over the last 30 days
start_date = pd.to_datetime("2026-10-01")
timestamps = [
    start_date
    + pd.Timedelta(
        days=np.random.randint(0, 30),
        hours=np.random.randint(0, 24),
        minutes=np.random.randint(0, 60),
    )
    for _ in range(n_records)
]

# Categorize event types and severities
event_types = [
    "Failed Login Attempt",
    "Brute Force Detected",
    "Unusual Outbound Traffic",
    "Malware Signature Blocked",
    "Privileged Escalation",
    "Phishing Link Clicked",
    "Unauthorized Port Scan",
]
event_weights = [0.45, 0.15, 0.10, 0.10, 0.05, 0.10, 0.05]

departments = [
    "Finance",
    "Engineering",
    "Executive Leadership",
    "Human Resources",
    "Sales & Marketing",
    "IT Infrastructure",
]
severities = ["Low", "Medium", "High", "Critical"]
severity_weights = [0.60, 0.25, 0.10, 0.05]

status_list = ["Resolved", "Investigating", "False Positive", "Escalated"]
status_weights = [0.70, 0.15, 0.10, 0.05]

# Build DataFrame
data = {
    "Event_ID": [f"SEC-{i:05d}" for i in range(1, n_records + 1)],
    "Timestamp": sorted(timestamps),
    "Department": np.random.choice(departments, n_records),
    "Event_Type": np.random.choice(
        event_types, n_records, p=event_weights
    ),
    "Severity": np.random.choice(
        severities, n_records, p=severity_weights
    ),
    "Source_IP": [
        f"{np.random.randint(10, 200)}.{np.random.randint(0, 255)}.{np.random.randint(0, 255)}.{np.random.randint(1, 255)}"
        for _ in range(n_records)
    ],
    "Status": np.random.choice(status_list, n_records, p=status_weights),
}

df = pd.DataFrame(data)

# Generate resolution times using the correct numpy random module method
df["Resolution_Time_Hours"] = np.round(
    np.random.exponential(scale=4, size=n_records), 2
)

# Adjust resolution time for items still under investigation
df.loc[df["Status"] == "Investigating", "Resolution_Time_Hours"] = np.nan

# Save to CSV
df.to_csv("enterprise_security_logs.csv", index=False)
print(
    f"Successfully generated {n_records} security event records and saved to 'enterprise_security_logs.csv'."
)