
select sum(premium) as tenure_premiums,
sum(claim_amount) as total_claim,
policy_tenure,
round(sum(claim_amount)::numeric/sum(premium),4)
as loss_ratio
from policy_sales p
left join claims_data c on c.customer_id=p.customer_id
group by policy_tenure
