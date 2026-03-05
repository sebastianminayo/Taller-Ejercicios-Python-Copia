# Taller de Python - Manejo de Datos

## Dataset
Archivo: `data/personas.csv` con 300,000 registros.

Los campos `nombre_cifrado` y `apellido_cifrado` usan cifrado ROT13. El resto de columnas tienen datos sucios (espacios, caracteres especiales como @, %, #, etc.).

Para descifrar ROT13: `codecs.decode(texto, 'rot_13')`

---

## Ejercicios

1. ¿Cuántas filas tienen el campo `id` con caracteres no numéricos? → **`83648`**
2. ¿Cuántas veces aparece el nombre "Maria" en el dataset? → **`4160`**
3. ¿Cuántas veces aparece el nombre "Juan" en el dataset? → **`3986`**
4. ¿Cuál es el nombre más frecuente en el dataset y cuántas veces aparece? → **`Gonzalo - 4221`**
5. ¿Cuál es el apellido más frecuente en el dataset y cuántas veces aparece? → **`Reyes - 7490`**
6. ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar? → **`14969`** 
7. ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar? → **`15193`** 
8. ¿Cuántas ciudades únicas existen después de normalizar? → **`20`** 
9. ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar? → **`12083`** 
10. ¿Cuántos registros tienen la profesión "Programador" después de limpiar? → **`12062`** 
11. ¿Cuántas profesiones únicas existen después de normalizar? → **`25`** 
12. ¿Cuántos registros tienen el campo `email` con espacios adicionales? → **`45447`**
13. ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos? → **`85266`**
14. ¿Cuál es el salario promedio después de limpiar? → **`8005689.17`**
15. ¿Cuál es el salario máximo después de limpiar? → **`14999995`**
16. ¿Cuál es el salario mínimo después de limpiar? → **`1000032`**
17. ¿Cuántos registros tienen `activo` como verdadero? → **`149863`**
18. ¿Cuántos registros tienen `activo` como falso? → **`150137`**
19. ¿Cuántos registros tienen fecha con formato diferente a YYYY-MM-DD? → **`89823`**
20. ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive)? → **`53404`**
21. ¿Cuántas personas nacieron antes de 1960? → **`66577`**
22. ¿Cuántas personas tienen más de 50 años (al 2026-02-26)? → **`144846`**
23. ¿Cuántos registros tienen nombre "Carlos" y ciudad "Cali"? → **`187`**
24. ¿Cuántos registros tienen nombre "Ana" y son "Medico"? → **`172`**
25. ¿Cuántos registros tienen profesión "Abogado" y salario > 10,000,000? → **`4405`**
26. ¿Cuántos registros tienen ciudad "Barranquilla", activos y nacidos después de 1980? → **`3241`**
27. ¿Cuál es la ciudad con más "Ingenieros"? → **`Popayan`**
28. ¿Cuál es la profesión con el salario promedio más alto? → **`Biologo`**
29. ¿Cuántos registros tienen email con dominio "gmail.com"? → **`56462`**
30. ¿Cuántos registros tienen nombre "Jose" y apellido "Garcia"? → **`96`**

