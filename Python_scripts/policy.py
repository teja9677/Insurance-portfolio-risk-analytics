import pandas as pd
import numpy as np

# Number of customers
n = 1000000

# Create customer IDs
customer_id = np.arange(1, n+1)
vehicle_id = np.arange(1, n+1)

# Purchase dates evenly across 2024
purchase_dates = pd.date_range(start="2024-01-01", end="2024-12-31")
purchase_dates = np.tile(purchase_dates, int(np.ceil(n/len(purchase_dates))))[:n]

# Tenure distribution
tenure_choices = [1,2,3,4]
tenure_prob = [0.2,0.3,0.4,0.1]

policy_tenure = np.random.choice(tenure_choices, size=n, p=tenure_prob)


vehicle_value = 100000


premium = policy_tenure * 100


policy_start = pd.to_datetime(purchase_dates) + pd.Timedelta(days=365)


policy_end = policy_start + pd.to_timedelta(policy_tenure*365, unit="D")

policy_df = pd.DataFrame({
    "Customer_ID": customer_id,
    "Vehicle_ID": vehicle_id,
    "Vehicle_Value": vehicle_value,
    "Premium": premium,
    "Policy_Purchase_Date": purchase_dates,
    "Policy_Start_Date": policy_start,
    "Policy_End_Date": policy_end,
    "Policy_Tenure": policy_tenure
})

policy_df.to_csv("policy_sales.csv", index=False)

print("Policy dataset created")
