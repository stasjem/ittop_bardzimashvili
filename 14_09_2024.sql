--14.09
-- 1. Выбрать все записи заказов в которых наименование страны отгрузки начинается с 'U'

-- 2. Выбрать записи заказов (включить колонки идентификатора заказа, идентификатора заказчика, веса и страны отгузки), которые должны быть отгружены в страны имя которых начинается с 'N', отсортировать по весу (по убыванию) и вывести только первые 10 записей.

-- 3. Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен

-- 4. Подсчитать кол-во заказчиков регион которых известен

-- 5. Подсчитать кол-во поставщиков в каждой из стран и отсортировать результаты группировки по убыванию кол-ва

-- 6. Подсчитать суммарный вес заказов (в которых известен регион) по странам, затем отфильтровать по суммарному весу (вывести только те записи где суммарный вес больше 2750) и отсортировать по убыванию суммарного веса.

-- 7. Выбрать все уникальные страны заказчиков и поставщиков и отсортировать страны по возрастанию

-- 8. Выбрать такие страны в которых "зарегистированы" одновременно и заказчики и поставщики и работники.

-- 9. Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики, но при этом в них не "зарегистрированы" работники.



--1 
-- SELECT * 
-- FROM orders 
-- WHERE ship_country LIKE 'U%';

--2
-- SELECT order_id, customer_id, weight, ship_country 
-- FROM orders 
-- WHERE ship_country LIKE 'N%' 
-- ORDER BY weight DESC 
-- LIMIT 10;

--3
-- SELECT first_name, last_name, phone, region 
-- FROM employees 
-- WHERE region IS NULL;

--4
-- SELECT COUNT(*) AS known_region_customers 
-- FROM customers 
-- WHERE region IS NOT NULL;

--5
-- SELECT country, COUNT(*) AS supplier_count 
-- FROM suppliers 
-- GROUP BY country 
-- ORDER BY supplier_count DESC;

--6
-- SELECT ship_country, SUM(weight) AS total_weight 
-- FROM orders 
-- WHERE region IS NOT NULL 
-- GROUP BY ship_country 
-- HAVING total_weight > 2750 
-- ORDER BY total_weight DESC;

--7
-- SELECT DISTINCT country 
-- FROM customers 
-- UNION 
-- SELECT DISTINCT country 
-- FROM suppliers 
-- ORDER BY country ASC;


--8
-- SELECT country 
-- FROM customers 
-- WHERE country IN (SELECT country FROM suppliers) 
-- AND country IN (SELECT country FROM employees);

--9
-- SELECT country 
-- FROM customers 
-- WHERE country IN (SELECT country FROM suppliers) 
-- AND country NOT IN (SELECT country FROM employees);
