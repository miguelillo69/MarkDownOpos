# WCAG 2.1/WCAG 2.2

## Principios y pautas de WCAG 2.2

### Principios 
  - En el nivel más alto se sitúan los cuatro principios que proporcionan los fundamentos de la accesibilidad web: perceptible, operable, comprensible y robusto.

### Pautas
  - Por debajo de los principios están las pautas. Las doce pautas proporcionan los objetivos básicos que los autores deben lograr con el fin de crear un contenido más accesible para los usuarios con distintas discapacidad. Estas pautas no son verificables, pero proporcionan el marco y los objetivos generales que ayudan a los autores a comprender los criterios de conformidad y a implementar mejor las técnicas.

### Principio 1: 
* **Perceptible**: la información y los componentes de la interfaz de usuario deben ser mostrados a los usuarios en formas que ellos puedan entender.
  * Pauta 1.1: Texto alternativo: Proporciona texto alternativo para el contenido que no sea textual, así podrá ser transformado en otros formatos que la gente necesite, como caracteres grandes, lenguaje braille (braile no es correcto), lenguaje oral, símbolos o lenguaje más simple.
  * Pauta 1.2: Contenido multimedia dependiente del tiempo: Proporcione alternativas sincronizadas para contenidos multimedia sincronizados dependientes del tiempo.
  * Pauta 1.3: Adaptable: Crear contenido que pueda ser presentado de diferentes formas sin perder ni información ni estructura.
  * Pauta 1.4: Distinguible: Facilitar a los usuarios ver y escuchar el contenido incluyendo la distinción entre lo más y menos importante.
### Principio 2: 
* **Operable**: Los componentes de la interfaz de usuario y la navegación debe ser manejable.
  * Pauta 2.1: Teclado accesible: Poder controlar todas las funciones desde el teclado.
  * Pauta 2.2 Tiempo suficiente: Proporciona tiempo suficiente a los usuarios para leer y utilizar el contenido.
  * Pauta 2.3: Ataques epilépticos: No diseñar contenido que pueda causar ataques epilépticos.
  * Pauta 2.4: Navegación: Proporciona formas para ayudar a los usuarios a navegar, a buscar contenido y a determinar donde están estos.
  * (Nuevo) Pauta 2.5: Modalidades de entrada: Facilitar a los usuarios operar la funcionalidad a través de varios métodos de entrada además del teclado.
### Principio 3:
* **Comprensible**. La información y las operaciones de usuarios deben ser comprensibles.
  * Pauta 3.1: Legible. Hacer contenido de texto legible y comprensible.
  * Pauta 3.2 Previsible: Hacer la apariencia y la forma de utilizar las páginas web previsibles.
  * Pauta 3.3 Asistencia a la entrada de datos: los usuarios de ayuda evitarán y corregirán errores.
### Principio 4:
* **Robustez**: el contenido deber ser suficientemente robusto para que pueda ser bien interpretado por una gran variedad de agentes de usuario, incluyendo tecnologías de asistencia.
  * Pauta 4.1 Compatible: Maximiza la compatibilidad con los agentes de usuario actuales y futuros, incluyendo tecnologías de asistencia.

## Niveles de adecuación de WCAG 2.2
* Las pautas se componen de criterios de cumplimiento (success criteria). Cada criterio de cumplimiento tiene un nivel de adecuación o conformidad (A, AA o AAA) que indica su impacto en la accesibilidad.

* **Nivel de conformidad**: Uno de los siguientes niveles de conformidad se satisface por completo.
  * **Nivel A**: Para lograr conformidad con el Nivel A (el mínimo), la página web satisface todos los Criterios de Conformidad del Nivel A, o proporciona una versión alternativa conforme.
  * **Nivel AA**: Para lograr conformidad con el Nivel AA, la página web satisface todos los Criterios de Conformidad de los Niveles A y AA, o proporciona una versión alternativa conforme al Nivel AA.
  * **Nivel AAA**: Para lograr conformidad con el Nivel AAA, la página web satisface todos los Criterios de Conformidad de los Niveles A, AA y AAA, o proporciona una versión alternativa conforme al Nivel AAA.
* **Páginas completas**: 
* La conformidad (y los niveles de conformidad) se aplican a las páginas web completas, y no pueden ser alcanzadas si se excluye una parte de la página.
* **Procesos completos**: 
* Cuando una página web es parte de una serie de páginas web que presentan un proceso (es decir, una secuencia de pasos que es necesario completar para realizar una actividad), todas las páginas en ese proceso deben ser conformes con el nivel especificado o uno superior. (No es posible lograr conformidad con un nivel en particular si una de las páginas del proceso no cumple con ese nivel o uno superior).
* **Uso exclusivo de tecnologías de modo compatible con la accesibilidad**: 
* Sólo se puede depender de las tecnologías usadas de forma compatible con la accesibilidad para satisfacer los criterios de conformidad. Toda información o funcionalidad que se proporcione de una forma que no sea compatible con la accesibilidad debe estar disponible de una forma que sí sea compatible con la accesibilidad.
* **Sin interferencia**: 
* Si las tecnologías se usan de una forma que no es compatible con la accesibilidad, o están usadas de una forma que no cumple los requisitos de conformidad, no deben impedir a los usuarios acceder al contenido del resto de la página. Además, es necesario que la página web en su conjunto siga cumpliendo con los requisitos de conformidad en las siguientes circunstancias:
  * 1\. cuando cualquier tecnología de la que no se depende está activada en una aplicación de usuario,
  * 2\. cuando cualquier tecnología de la que no se depende está desactivada en una aplicación de usuario, y
  * 3\. cuando cualquier tecnología de la que no se depende no es soportada por una aplicación de usuario
* Además, los siguientes criterios de conformidad se aplican a todo el contenido de la página, incluyendo el contenido del que, de todos modos, no se depende para alcanzar la conformidad, ya que su incumplimiento puede interferir con el uso de la página:
  * 1.4.2 - Control del audio,
  * 2.1.2 - Sin trampas para el foco del teclado,
  * 2.3.1 - Umbral de tres destellos o menos, y
  * 2.2.2 - Poner en pausa, detener, ocultar.