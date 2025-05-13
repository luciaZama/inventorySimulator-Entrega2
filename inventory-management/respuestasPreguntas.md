### Vue no detecta cambios dentro de los objetos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?
En Vue, los cambios dentro de los objetos anidados no son detectados automáticamente debido a las limitaciones de reactividad con Object.assign() o modificaciones directas. Para observar un cambio en una propiedad anidada, se puede utilizar $watch con una opción deep: true o utilizar Vue.set / reactive / ref


### watch() permite escuchar cambios en propiedades específicas dentro de reactive(), explica como funciona.
- reactive(): Convierte un objeto o un array en un objeto reactivo. Esto significa que cualquier cambio en las propiedades del objeto se detectará automáticamente.
- watch(): Es una función que te permite observar un valor reactivo o una expresión computada. Puedes especificar qué propiedad específica del objeto deseas observar y hacer que Vue ejecute una función cada vez que esa propiedad cambie. En la práctica se puede ver como dependiendo de la disponibilidad y la cantidad de stock, el color de cada 'tarjeta' cambia.


### ¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?
En esta práctica se ha creado un array de productos con una cantidad de stock y una disponibilidad. Mediante un watch(), se revisa que la disponibilidad será true si el stock es mayor a 0 o false si es menor. Si no hay stock, se pinta de rojo la 'tarjeta' referente a ese producto.

Otra manera de hacerlo es crear un watch() para revisar si algún valor de algún producto ha sido cambiado, y si es así, el callback lo ejecutaría. 
