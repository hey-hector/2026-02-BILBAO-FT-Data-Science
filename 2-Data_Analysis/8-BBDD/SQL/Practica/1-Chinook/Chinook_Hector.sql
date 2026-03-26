--ex1: para sacar cómo se llama el país de Brasil en la BBDD, necesito sacar la columna "Country" dentro de "customers":
SELECT DISTINCT customers.country
FROM customers;
--Nos da en el resultado que se llama "Brazil", por lo que:
SELECT * 
FROM customers
WHERE country = "Brazil";

--ex2: para sacar cómo se llaman los agentes de ventas en la BBDD, necesito sacar la columna "Title" dentro de "employees":
SELECT DISTINCT employees.title
FROM employees;
--Nos da en el resultado que se llaman "Sales Support Agent", por lo que:
SELECT *
FROM employees
WHERE title = "Sales Support Agent";

--ex3: deducimos que las canciones de AC/DC en la BBDD está en la tabla "tracks". Probamos a sacar los valores de "Name":
SELECT DISTINCT tracks.name
FROM tracks;
--No es así, por lo que probamos con "composer":
SELECT DISTINCT tracks.composer
FROM tracks;
--Vemos que la respuesta se escribe "AC/DC", así que:
SELECT *
FROM tracks
WHERE composer = "AC/DC";

--ex 4: para sacar cómo se llaman los EEUU en la BBDD, necesito sacar la columna "Country" dentro de "customers":
SELECT DISTINCT customers.country
FROM customers;
--Nos da en el resultado que se llama "USA", por lo que ahora ponemos las condiciones de lo que queremos sacar:
--de la tabla "customers": "first name", "last name", "customerid" y "country":
SELECT firstname || " " || lastname AS Nombre_completo, --juntar "first name" y "last name" como nombre_completo (nombre asignado)
        customerid AS ID,
        country AS País
FROM customers
WHERE country <> "USA";

--ex5: sabemos que los agentes de ventas se llaman "Sales Support Agent":
--de ellos tenemos que sacar de la tabla "employees": 
--"first name" y "last name" como "Nombre_completo"
--"city", "state" y "country" como "Dirección
--"email"
SELECT firstname || " " ||lastname AS Nombre_completo,
        City || " " || State || " " || Country AS Dirección,
        email
FROM employees
WHERE title = "Sales Support Agent";

--ex6: buscamos dónde hay países en la tabla "invoices" y se llaman "BillingCountry". Queremos una lista con los países con facturas:
SELECT DISTINCT invoices.billingcountry
FROM invoices;

--ex7: Obtén una lista con los estados de USA no repetidos de donde son los clientes y cuántos clientes en cada uno, por lo que:
--Necesito los "states" de la tabla "customers" donde el "country" sea "USA"(sabemos que EEUU se llama así por el ex4)
--Hay que identificar los clientes que hay en estos estados y decir cuántos hay x estado:
SELECT customers.state, count(customerid) AS N_clientes 
--El comando "Count" cuenta los "customerid" diferentes que hay y los guardamos como N_clientes
FROM customers
WHERE country = "USA"
GROUP BY state; --"Group by" agrupa las filas que tienen los mismos valores en filas resumen. En este caso, los "customerid" de cada "state"

--ex8: ¿Cuántos artículos tiene la factura 37?
--Se entiende que hay que mirar el "invoiceid" de la tabla "invoice_items":
SELECT invoice_items.invoiceid
FROM invoice_items;
--Vemos que los "invoiceid" se repiten, por lo que pide cuántas veces se repite el valor 37:
SELECT invoice_items.invoiceid, count(invoiceid) AS N_articulos --contamos los "invoiceid" y guardamos como N_articulos
FROM invoice_items
WHERE invoiceid = 37;