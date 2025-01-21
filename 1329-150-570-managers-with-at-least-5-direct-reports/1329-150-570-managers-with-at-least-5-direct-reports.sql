# Write your MySQL query statement below
select t1.name
from employee as t1
left join employee as t2
on t1.id = t2.managerid
group by t1.id, t1.name
having count(t2.id) >= 5

-- SELECT t1.name
-- FROM employee AS t1
-- LEFT JOIN employee AS t2
-- ON t1.id = t2.managerId
-- GROUP BY t1.id, t1.name
-- HAVING COUNT(t2.id) >= 5;