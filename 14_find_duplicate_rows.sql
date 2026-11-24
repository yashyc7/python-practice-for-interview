"""
Find the emails that appear more than once in the users table.

Sample table:

id	email
1	a@x.com
2	b@x.com
3	a@x.com
4	c@x.com
5	b@x.com

Expected output:

email	cnt
a@x.com	2
b@x.com	2
Code
"""

select email , count(*) as cnt 
from users 
group by email 
having count(*)>1