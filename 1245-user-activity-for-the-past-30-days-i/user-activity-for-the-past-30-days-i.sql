select activity_date as day, count(distinct user_id) AS active_users
from Activity
where activity_date between "2019-06-28" and "2019-07-28" 
GROUP BY activity_date;