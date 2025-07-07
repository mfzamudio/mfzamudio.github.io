
USE bicycle_store;

### Average, min, max, total spend,cost of repairs, number of appointments by client (View)

CREATE VIEW bicycle_store.stattperclient AS
SELECT 
	cu.customerid,
    concat(cu.firstname, " ", cu.lastname) AS clientname,
    ROUND(AVG(ord.totalamount),0) AS AverageSpent,
    ROUND(MIN(ord.totalamount),0) AS MinSpentOrder,
    ROUND(MAX(ord.totalamount),0) AS MaxSpentOrder,
    ROUND(SUM(ord.totalamount),0) AS totalSpent,
    ROUND(SUM(rep.repaircost),0) AS totalCost,
    COUNT(app.customerid) AS NumAppointment
FROM customers AS cu
JOIN orders AS ord ON cu.customerid = ord.customerid
JOIN repairs AS rep ON cu.customerid = rep.customerid
JOIN appointments AS app ON cu.customerid = app.customerid
GROUP BY cu.customerid
ORDER BY cu.customerid;


### Windows function and CTE

WITH summary AS (
SELECT 
    AVG(ord.totalamount) OVER () AS AverageSpent,
    MIN(ord.totalamount) OVER () AS MinSpentOrder,
    MAX(ord.totalamount) OVER () AS MaxSpentOrder,
	SUM(ord.totalamount) OVER () AS totalSpent,
    SUM(rep.repaircost) OVER () AS totalCost,
    COUNT(app.customerid) OVER () AS NumAppointment
FROM customers AS cu
JOIN orders AS ord ON cu.customerid = ord.customerid
JOIN repairs AS rep ON cu.customerid = rep.customerid
JOIN appointments AS app ON cu.customerid = app.customerid)
SELECT *
FROM summary
LIMIT 1;

### Summary of number of purchases by customer

SELECT 
o.customerid,
odt.itemtype,
SUM(odt.quantity) AS Purchases
FROM orderdetails odt
JOIN orders o ON o.orderid=odt.orderdetailid
GROUP BY o.customerid, odt.itemtype
ORDER BY o.customerid;


##view consulting

SELECT *
FROM stattperclient;

SELECT *
FROM stattperclient
WHERE customerid = 5