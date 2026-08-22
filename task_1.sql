SELECT c.login, COUNT(o.id)
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o
ON c.id = o."courierId" AND o."inDelivery" = true
GROUP BY c.login;