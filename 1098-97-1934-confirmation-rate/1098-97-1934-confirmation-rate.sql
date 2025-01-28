# Write your MySQL query statement below
-- select user_id, round((ifnull(c_a, 0) / total), 2) as confirmation_rate
-- from
-- (select s.user_id, c.action, count(c.action) as total,
-- -- case when action = "timeout" then count(action) end as t_a,
-- case when action = "confirmed" then count(action) end as c_a
-- from Signups as s
-- left join Confirmations as c
-- on s.user_id = c.user_id
-- group by s.user_id) as T

select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;