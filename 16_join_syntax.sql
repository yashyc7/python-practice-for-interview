

select a.name , b.customer_id , b.order_name , b.amount
FROM TABLE_A AS a
INNER_JOIN TABLE_B AS b
ON a.customer_id = b.customer_id


select a.name , b.customer_id , b.order_name , b.amount
FROM TABLE_A AS a
LEFT_JOIN TABLE_B AS b
ON a.customer_id = b.customer_id



select a.name , b.customer_id , b.order_name , b.amount
FROM TABLE_A AS a
RIGHT_JOIN TABLE_B AS b
ON a.customer_id = b.customer_id




select a.name , b.customer_id , b.order_name , b.amount
FROM TABLE_A AS a
FULL_JOIN TABLE_B AS b
ON a.customer_id = b.customer_id