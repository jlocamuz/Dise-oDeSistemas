# la inyección de dependencia es un técnica de desarrollo que nos permite escribir código
# con un alto nivel de cohesión y un bajo nivel de dependencia.

# la cohesión no es más que una medida que nos permite conocer qué tanta relación existe
# para un bloque de código con sigo mismo (Llamase módulos, clases, métodos, funciones etc...).

# Por ejemplo, si definimos la siguiente clase, podemos decir que su nivel de cohesión es alta,
#  ya que todos los métodos tiene una relación bajo un mismo contexto

# Si por el contrarío, definimos el siguiente módulo (cada funcion x separado)podemos decir que su nivel de cohesión 
# es bajo, ya que las funciones no tienen una relación unas con otras.

Podemos definir el acoplamiento como la forma en que se relacionan componentes de nuestro código entre ellos
Lo ideal es que la función se deslinde del cómo obtener los datos, y solo se enfoque en el qué hacer, de esta forma nuestro código será mucho más flexible.

Con este refactor no solo reducimos el acoplamiento, si no que aplicamos el principio de responsabilidad única:

    Una clase debería tener solo una razón para cambiar
    Si una clase asume más de una responsabilidad, será más sensible al cambio.
    Si una clase asume más de una responsabilidad, las responsabilidades se acoplan.

Tenemos, principalmente, 3 tipos de inyección de dependencias.

Constructor injection.
Property injection.
Method injection.

Una muy buena analogía para comprender el tema de inyección de dependencias es ver a las dependencias cómo si de piezas de lego se tratasen. Pudiendo reemplazarla unas por otras dependiendo de nuestras necesidades