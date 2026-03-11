import pandas as pd
import numpy as np


policy_df = pd.read_csv("policy_sales.csv")


policy_df["Policy_Purchase_Date"] = pd.to_datetime(policy_df["Policy_Purchase_Date"])
policy_df["Policy_Start_Date"] = pd.to_datetime(policy_df["Policy_Start_Date"])


policy_df["purchase_day"] = policy_df["Policy_Purchase_Date"].dt.day




# Eligible vehicles (7,14,21,28)
eligible_2025 = policy_df[
    policy_df["purchase_day"].isin([7,14,21,28])
].copy()

# 30% claim probability
claims_2025 = eligible_2025.sample(frac=0.30, random_state=42)

claims_2025["Claim_Date"] = claims_2025["Policy_Start_Date"]
claims_2025["Claim_Amount"] = 10000
claims_2025["Claim_Type"] = 1



# Only 4 year tenure policies
eligible_2026 = policy_df[
    policy_df["Policy_Tenure"] == 4
].copy()

# 10% claim probability
claims_2026 = eligible_2026.sample(frac=0.10, random_state=42)

# Randomly distribute claims across 59 days
start_date = pd.to_datetime("2026-01-01")
claims_2026["Claim_Date"] = start_date + pd.to_timedelta(
    np.random.randint(0,59,len(claims_2026)), unit="D"
)

claims_2026["Claim_Amount"] = 10000
claims_2026["Claim_Type"] = 2




claims_df = pd.concat([claims_2025, claims_2026])

claims_df = claims_df[[
    "Customer_ID",
    "Vehicle_ID",
    "Claim_Amount",
    "Claim_Date",
    "Claim_Type"
]]


claims_df.insert(0, "Claim_ID", range(1, len(claims_df)+1))

claims_df.to_csv("claims_data.csv", index=False)

print("Claims dataset created successfully")
print("Total claims:", len(claims_df))