--21.09
-- 1. Вывести продукты количество которых в продаже меньше самого малого среднего количества продуктов в деталях заказов (группировка по product_id). Результирующая таблица должна иметь колонки product_name и units_in_stock.

-- 2. Напишите запрос, который выводит общую сумму фрахтов заказов для компаний-заказчиков для заказов, стоимость фрахта которых больше или равна средней величине стоимости фрахта всех заказов, а также дата отгрузки заказа должна находится во второй половине июля 1996 года. Результирующая таблица должна иметь колонки customer_id и freight_sum, строки которой должны быть отсортированы по сумме фрахтов заказов.

-- 3. Напишите запрос, который выводит 3 заказа с наибольшей стоимостью, которые были созданы после 1 сентября 1997 года включительно и были доставлены в страны Южной Америки. Общая стоимость рассчитывается как сумма стоимости деталей заказа с учетом дисконта. Результирующая таблица должна иметь колонки customer_id, ship_country и order_price, строки которой должны быть отсортированы по стоимости заказа в обратном порядке.

-- 4. Вывести все товары (уникальные названия продуктов), которых заказано ровно 10 единиц (конечно же, это можно решить и без подзапроса).


--1
-- WITH AvgProductQuantity AS (SELECT 
--         ProductID, 
--         AVG(Quantity) AS AvgQuantity
--     FROM order_details
--     GROUP BY ProductID),
-- MinAvgQuantity AS (SELECT MIN(AvgQuantity) AS MinAvg
--     FROM AvgProductQuantit)
-- SELECT p.ProductName, p.UnitsInStock
-- FROM products p
-- WHERE p.UnitsInStock < (SELECT MinAvg FROM MinAvgQuantity);

-- ---2

-- SELECT  o.CustomerID,  SUM(o.Freight) AS FreightSum
-- FROM orders o
-- WHERE  o.Freight >= (SELECT AVG(Freight) FROM orders) AND o.ShippedDate BETWEEN '1996-07-16' AND '1996-07-31'
-- GROUP BY  o.CustomerID
-- ORDER BY FreightSum;


--3
-- SELECT o.CustomerID, o.ShipCountry, SUM(od.UnitPrice * od.Quantity * (1 - od.Discount)) AS OrderPrice
-- FROM orders o
-- JOIN order_details od ON o.OrderID = od.OrderID
-- WHERE o.OrderDate >= '1997-09-01'
--     AND o.ShipCountry IN ('Argentina', 'Brazil', 'Venezuela', 'Mexico', 'Colombia', 'Chile', 'Peru')
-- GROUP BY  o.CustomerID, o.ShipCountry
-- ORDER BY OrderPrice DESC
-- LIMIT 3;


--4
-- SELECT DISTINCT p.ProductName
-- FROM products p
-- JOIN order_details od ON p.ProductID = od.ProductID
-- WHERE od.Quantity = 10;
