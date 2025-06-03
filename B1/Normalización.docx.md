# 1. **Normalización**

* Eliminación d dependencias entre atributos q originen anomalías en actualización d datos, y proporcionar 1 estructura \+ regular para representación d tablas, constituyendo el soporte para diseño d BBDD relacionales pra obtener 1 modelo lógico d datos normalizado.

* 1\. Dependencia funcional

  * Un atributo Y se dice que depende funcionalmente de otro X si, y sólo si, **a cada valor de X le corresponde un único valor de Y**. 

* 2\. Dependencia funcional completa

  * Un atributo Y tiene dependencia funcional completa respecto de otro X, **si depende**  
**funcionalmente de él en su totalidad, es decir, no depende de ninguno de los posibles atributos que formen parte de X**.

* 3\. Dependencia transitiva

  * Un atributo depende transitivamente de otro si, y sólo si, **depende de él a través de otro atributo.**

## 1. **Formas normales**:  
* 1\. Primera forma normal (1FN)
  * Entidad está en 1FN **si no tiene grupos repetitivos, es decir, un atributo sólo puede tomar un único valor de un dominio simple** (ni arrays ni nada de eso).
* 2\. Segunda forma normal (2FN)
  * Entidad está en 2FN si está en 1FN y todos los atributos q **no forman parte de las claves candidatas tienen dependencia funcional completa respecto de éstas**, es decir, no hay dependencias funcionales d atributos no principales respecto d 1 parte de las claves.
* 3\. Tercera forma normal (3FN)
  * Entidad está en 3FN si está en 2FN y **todos sus atributos no principales dependen directamente de la clave primaria**, es decir, no hay dependencias funcionales transitivas de atributos no principales respecto de las claves.
* 4\. Forma Normal de Boyce-Codd
  * Entidad está en FNBC si está en 3FN y **no existen** **dependencias funcionales no triviales de los atributos que no sean un conjunto de la clave candidata**.
* 5\. Cuarta formal normal (4FN)
  * Entidad está en 4NF si está en 3FN o FNBC y no posee dependencias multivaluadas no triviales.
* 6\. Quinta formal normal (5FN)
  * Entidad está en 5FN si está en 4FN y no existen relaciones de dependencias de reunión (join) no triviales que no se generen desde las claves. **Cada relación de dependencia de reunión (join) se encuentra definida por claves candidatas**.

| FN | Condición |
| :---- | :---- |
| 1FN | **no tiene grupos repetitivos** |
| 2FN | todos los atributos q **no forman parte de las claves candidatas tienen dependencia funcional completa respecto de éstas** |
| 3FN | **todos sus atributos no principales dependen directamente de la clave primaria**, es decir, no hay dependencias funcionales transitivas de atributos no principales respecto de las claves |
| FNBC | **no existen** **dependencias funcionales no triviales de los atributos que no sean un conjunto de la clave candidata** |
| 4FN | no posee dependencias multivaluadas no triviales |
| 5FN | no existen relaciones de dependencias de reunión (join) no triviales que no se generen desde las claves |

