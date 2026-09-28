**Parte A**

**1**. De los tres ordenamientos básicos la que hace menor trabajo de todas es insertion Sort; puesto que cada elemento se compara una vez con su vecino y no se moveria. Aparte, su complejidad es de O(n), de manera que en este caso solo haria n-1 comparaciones y 0 intercambios.

**2**. En este caso para el QuickSort un conjunto de datos que lo haga comportarse pesimo sería un conjunto de datos ya ordenado; tomemos como ejemplo una lista n=[1,2,3,4,5,6, 7,8], si elije el 1 como pivote todos los otros elementos del conjunto n van a ser mayores que el por lo tanto se dividiria de una manera desproporcionada haciendo uno vacio a la izquierda y uno con n-1 elementos es decir seria ([2,3,4,5,6,7,8 ]) y asi seguirá, es decir que elevaria su complejidad a O(n^2).

**3**. La mejor manera seria ordenarla y luego realizar las busquedas puesto que para la busqueda secuencial tendriamos que en el peor de los casos el elemento que estemos buscando en esas busquedas se encuentre en el elemento 10000 o en el 9999 realizando una cantidad muy alta de comparaciones. En cambio, si utilizamos un ordenamiento de complejidad O(nlogn) enves de uno básico y luego aplicamos binaria se reduciria significativamente la cantidad de comparaciones que realizariamos en esas 100 busquedas. 
