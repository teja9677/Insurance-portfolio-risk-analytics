select 
Round(sum((premium::numeric/(policy_tenure*365))
*LEAST(DATE'2026-02-28'-policy_start_date,policy_end_date-policy_start_date)),0) as earned_premium

from policy_sales
where policy_start_date<=DATE '2026-02-28'


