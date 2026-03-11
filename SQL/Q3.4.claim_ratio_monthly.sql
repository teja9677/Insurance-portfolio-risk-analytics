select sum(premium)as total_premium,
sum(claim_amount) as total_claim, 
extract(month from policy_purchase_date) as policy_month,
round( sum(claim_amount)::NUMERIC/sum(premium),4) as claim_ratio
from policy_sales p
left join claims_data c on c.customer_id =p.customer_id
where extract(year from policy_purchase_date)=2024
group by policy_month
