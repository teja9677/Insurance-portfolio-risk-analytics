select (count(*)*10000) as claim_liability
from policy_sales p
left join claims_data c on c.customer_id=p.customer_id
where claim_date IS NULL