### Codigo para formalizar una gramatica la forma normal de chumsky

**Requisitos**

python >= 3.5

**Como Ejecutarlo**

python3 main.py

**Ejemplo de Ejecucion**

primero nos solicita las variables no terminales y terminales debemos digitarlas usando solamente "," para
separalas

![imagen de la primera parte]
(http://i.prntscr.com/aFE96vWwRnKfB7URMG-yBg.png)

digitamos la cantidad de regla por variable no terminal  y vamos digitando su respectiva regla
es importante digita la regla con la palabra tal como se escribio al principio

![imagen de la segunda parte]
(http://i.prntscr.com/9Hb0fcI0SkW4UOQmSANvjw.png)

luego digitamos la variable inicial , es importante escribir la variable tal como la hemos 
guardado en nuestras variables no terminales

![imagen segunda parte]
(http://i.prntscr.com/ObnpImekSkGrd7dGD_1UXw.png)

**Resultado**

al final el programa dara unas palabras generadas usando el siguiente formato
noterminal =>[[noterminal,noterminal],[noterminal]]
ejm
A=>BC es equivalente a A=>[[B,C]]