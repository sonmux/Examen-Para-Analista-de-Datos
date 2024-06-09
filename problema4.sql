/*
1. Obtener una lista de todos los clientes con sus respectivas cuentas, mostrando las columnas
nombre , direccion , telefono , id_cuenta y saldo . Ordenar los resultados por el nombre del
cliente.
*/
SELECT c.nombre, c.direccion, c.telefono, cu.id_cuenta, cu.saldo
FROM clientes c
INNER JOIN cuentas cu ON c.id_cliente = cu.id_cliente
ORDER BY c.nombre;

/*
2. Calcular el saldo total en el banco sumando los saldos de todas las cuentas.
*/
SELECT SUM(saldo) AS saldo_total
FROM cuentas;

/*
3. Encontrar los 5 clientes con los saldos más altos en sus cuentas, mostrando las columnas
nombre, id_cuenta y saldo. Ordenar los resultados por el saldo de mayor a menor.
*/
SELECT c.nombre, cu.id_cuenta, cu.saldo
FROM clientes c
INNER JOIN cuentas cu ON c.id_cliente = cu.id_cliente
ORDER BY cu.saldo DESC
LIMIT 5;

/*
4. Obtener una lista de todos los cheques emitidos en el último mes, mostrando las columnas
id_cheque , nombre (del cliente que emitió el cheque), monto , fecha_emision y beneficiario .
Ordenar los resultados por la fecha de emisión de más reciente a más antigua.
*/
SELECT ch.id_cheque, c.nombre, ch.monto, ch.fecha_emision, ch.beneficiario
FROM cheques ch
INNER JOIN cuentas cu ON ch.id_cuenta = cu.id_cuenta
INNER JOIN clientes c ON cu.id_cliente = c.id_cliente
WHERE ch.fecha_emision >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
ORDER BY ch.fecha_emision DESC;

/*
5. Encontrar el monto total de cheques emitidos por cada cliente en el último mes, mostrando
las columnas nombre y monto_total_cheques . Ordenar los resultados por el monto total de
cheques de mayor a menor.
*/
SELECT c.nombre, SUM(ch.monto) AS monto_total_cheques
FROM cheques ch
INNER JOIN cuentas cu ON ch.id_cuenta = cu.id_cuenta
INNER JOIN clientes c ON cu.id_cliente = c.id_cliente
WHERE ch.fecha_emision >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
GROUP BY c.nombre
ORDER BY monto_total_cheques DESC;

/*
6. Calcular el monto total de préstamos otorgados en el último año.
*/
SELECT SUM(monto) AS monto_total_prestamos
FROM prestamos
WHERE fecha_otorgamiento >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

/*
7. Encontrar los 10 clientes con los mayores montos de préstamos otorgados en el primer
cuatrimestre del año.
*/
SELECT c.nombre, SUM(pr.monto) AS monto_total_prestamos
FROM clientes c
INNER JOIN prestamos pr ON c.id_cliente = pr.id_cliente
WHERE MONTH(pr.fecha_otorgamiento) <= 4
GROUP BY c.nombre
ORDER BY monto_total_prestamos DESC
LIMIT 10;
