# Write your MySQL query statement below
select name
from Customer
where referee_id != 2 or referee_id  is Null;

-- '''
-- Approach 2:
-- Using nvl function.
-- '''
-- -- select name
-- -- from Customer
-- -- where nvl(referee_id,0) != 2