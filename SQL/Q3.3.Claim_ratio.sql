select policy_tenure,sum(claim_amount) as total_claim,sum(premium)as total_premium,
round(sum(claim_amount)/sum(premium),4) as claim_ratio
from policy_sales
left join claims_data on claims_data.customer_id=policy_sales. customer_id
group by policy_tenure
