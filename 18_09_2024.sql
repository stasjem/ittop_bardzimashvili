--18.09
-- 1. Найти заказчиков и обслуживающих их заказы сотрудников таких, что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.

-- 2. Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.

-- 3. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.

-- 4. Переписать предыдущий запрос, использовав симметричный вид джойна (подсказка: речь о LEFT и RIGHT).


--1
-- SELECT 
--     customers.CompanyName AS CustomerCompany,
--     CONCAT(employees.FirstName, ' ', employees.LastName) AS EmployeeFullName
-- FROM 
--     orders
-- JOIN 
--     customers ON orders.CustomerID = customers.CustomerID
-- JOIN 
--     employees ON orders.EmployeeID = employees.EmployeeID
-- JOIN 
--     shippers ON orders.ShipVia = shippers.ShipperID
-- WHERE 
--     customers.City = 'London'
--     AND employees.City = 'London'
--     AND shippers.CompanyName = 'Speedy Express';

--2
-- SELECT 
--     products.ProductName,
--     products.UnitsInStock,
--     suppliers.ContactName,
--     suppliers.Phone
-- FROM 
--     products
-- JOIN 
--     suppliers ON products.SupplierID = suppliers.SupplierID
-- JOIN 
--     categories ON products.CategoryID = categories.CategoryID
-- WHERE 
--     categories.CategoryName IN ('Beverages', 'Seafood')
--     AND products.UnitsInStock < 20
--     AND products.Discontinued = 0;

--3
-- SELECT 
--     customers.ContactName,
--     orders.OrderID
-- FROM 
--     customers
-- LEFT JOIN 
--     orders ON customers.CustomerID = orders.CustomerID
-- WHERE 
--     orders.OrderID IS NULL;
---4
-- SELECT 
--     customers.ContactName,
--     orders.OrderID
-- FROM 
--     customers
-- LEFT JOIN 
--     orders ON customers.CustomerID = orders.CustomerID
-- WHERE 
--     orders.OrderID IS NULL

-- UNION

-- SELECT 
--     customers.ContactName,
--     orders.OrderID
-- FROM 
--     orders
-- RIGHT JOIN 
--     customers ON customers.CustomerID = orders.CustomerID
-- WHERE 
--     orders.OrderID IS NULL;
