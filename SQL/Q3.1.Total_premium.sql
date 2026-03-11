select sum(premium) as Total_premium
from policy_sales
where extract(year from policy_purchase_date)=2024