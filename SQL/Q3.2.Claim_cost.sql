select extract(month from claim_date),sum(claim_amount) as monthly_claim
from claims_data 
where extract(year from claim_date) =2025
group by extract(month from claim_date)


select extract(month from claim_date),sum(claim_amount) as monthly_claim
from claims_data 
where extract(year from claim_date) =2026
group by extract(month from claim_date)


