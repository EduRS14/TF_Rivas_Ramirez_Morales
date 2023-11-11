**Universidad Peruana de Ciencias Aplicadas**

![Upc Logo](logoUPC.png)

**INFORME DEL TRABAJO PARCIAL (TP)**

CURSO DE COMPLEJIDAD ALGORÍTMICA - CC184

**Facultad de Ingeniería**

Carrera de Ciencias de la Computación

**SECCIÓN:**

WX73

**DOCENTE:**

Luis Martin Canaval Sanchez

**Grupo:**

3

**INTEGRANTES:**

Eduardo Jose Rivas Siesquen - u202216407

Rodrigo Alonso Ramírez Cesti - u202210690

Tarik Gustavo Morales Oliveros - u202210472

**09/2023**

**ÍNDICE**

1. Descripción del problema
1. Descripción del conjunto de datos (dataset)
1. Propuesta

Bibliografía



1. **Descripción del problema:**

En el mundo actual, hemos podido desarrollar diferentes medios por los cuales podemos lograr conexiones y relaciones entre todos nosotros, ya sea de forma presencial mediante el cara a cara, o por medio del uso de plataformas como redes sociales. En estas últimas, hemos creado la posibilidad de formar lazos entre dos usuarios, los cuales pueden ser direccionales (como seguir a una persona) o bidireccionales (cuando dos usuarios son amigos). En este último es en el que nos vamos a centrar, donde dos usuarios son amigos, y cada uno de estos tiene sus diferentes contactos independientemente.

Entre tantas personas que llegamos a conocer a diario o que hemos conocido previamente, siempre habrá el problema de no poder conocer directamente a cierta persona en específico, lo cual puede ser un grave problema si se necesita saber algo de este individuo, como un dato, información, etc. Por ejemplo, cuando buscas una oportunidad de trabajo pero no cuentas con alguien que directamente te la pueda ofrecer, pero, entre todos los contactos y amigos que tienes, puedes ir buscando personas entre estos, hasta poder dar con el objetivo al que apuntas llegar. De esta manera, podemos conectar dos personas por medio de una relación que no sea directa, pero que por medio de un camino formado por los diferentes contactos que pueden tener entre sí se puedan conectar de forma indirecta. Esta propuesta está basada en la idea de los seis grados de separación. Esta teoría sostiene que cualquier individuo en el planeta puede establecer una conexión con otro a través de una secuencia de conocidos que no exceda los 5 intermediarios. Esto implica que pueden conectarse de un contacto a otro, hasta llegar a 6 conexiones que unen a esta pareja de usuarios (Gonzales, 2015). 

Por lo que, a partir de este análisis, vamos a tratar la situación y necesidad de conocer y determinar un camino que relacione a dos personas desconocidas entre sí a través de sus contactos, usando el menor número de intermediarios y conexiones posibles.



1. **Descripción del conjunto de datos (dataset):**

Se usará como fundación la base de datos “Facebook Data” (Batra, 2018). Los nodos de la nueva base de datos tendrán las siguientes características (pseudocódigo):


|Clase VÉRTICE|
| :-: |
|entero user\_id                   //un identificador para otros usuarios|
|entero friend\_count          //cantidad de aristas que conectan con otros usuarios|
|array <entero> amigos    //un arreglo de los user\_id de otros usuarios|
|bool es\_ lista\_priv          //un booleano que determina si su lista de amigos es privada|

Las aristas del grafo no serán dirigidas, ya que asumimos que al ser dos usuarios ”amigos” implica que se aceptaron la solicitud de amistad recíprocamente. Asimismo, las aristas no tendrán peso alguno, ya que el “valor” de la amistad en una red social es la misma para todos los usuarios.

El número de nodos con el que se trabajará será de 1500.

Subgrafo de ejemplo:

![](grafo1_h2.png)

![](grafo2_h2.png)

(Las versiones anteriores del subgrafo se guardarán en la carpeta llamada “Versiones del Grafo” en el repositorio)



1. **Propuesta:**

Proponemos un programa con un algoritmo en el que buscamos que a través de los contactos, exista la posibilidad de llegar de una persona a otra solo con solo conocer los contactos de estos y los contactos que estos últimos a su vez tienen y así sucesivamente hasta encontrar un camino, es como una relación amigo de mi amigo, alguien que uno no conoce pero que su conocido si lo conoce. Por ejemplo, podemos determinar dos usuarios totalmente desconocidos entre sí, sin haber alguna relación directa entre estos dos, pero podemos ir viendo los contactos que hay entre estos y hallar una conexión indirecta entre ambos desconocidos, como un amigo de ambos en común. Esto lo conseguiremos aplicando la teoría de los “seis grados de separación”, donde intentamos probar que cualquier persona puede estar conectada con otra a través de no más de 6 enlaces. En resumidas cuentas, y tomando en cuenta la teoría que aplicamos para nuestra dataset, proponemos un programa que logre encontrar el menor número de enlaces para encontrar un camino entre una persona y otra mediante un algoritmo, en el que entre estas 2 personas no haya un camino directo.

Para lograrlo, vamos a utilizar una técnica de recorrido y búsqueda de grafos, más específicamente, una búsqueda en profundidad iterativa (IDS, por sus siglas en inglés). Aplicando este algoritmo, vamos a poder partir de un nodo A hasta un nodo B, buscando a través de sus conexiones con los demás nodos un camino hacia este y, si es necesario, ir ampliando el límite de profundidad de la búsqueda a medida que se recorran los diferentes caminos y no se haya encontrado aún el camino al objetivo.

Para el desarrollo de nuestra propuesta seguiremos una cierta metodología en específico. Sobre la comunicación que tendrá el equipo a nivel de decisiones, información y archivos de proyectos, se usarán chats de texto, específicamente Whatsapp, para las comunicaciones más directas, Google Drive y sus herramientas para la redacción de textos y presentaciones, mientras que la plataforma GitHub para la realización de proyectos más relacionados al código, además de ir guardando nuestros archivos y avances en esta plataforma, para que esté al alcance de todos nosotros y poder ir actualizando los datos de forma segura periódicamente gracias a los comandos de Git, y así ir mejorando el proyecto a medida que pase el tiempo. Por otro lado, a nivel de la investigación y trabajo, primero identificamos nuestros datos con un dataset, es decir un conjunto de datos, los cuales consideraremos posteriormente en nuestro algoritmo. Después, analizaremos como podemos aplicar teoría vinculada con nuestra propuesta como la de grafos y/o los “seis grados de separación” dentro de nuestro algoritmo, usando para ello el conjunto de datos que hemos identificado e ir actualizando nuestras ideas y propuestas.



**Bibliografía:**

Batra, S. (2018). *Facebook Data*. <https://www.kaggle.com/datasets/sheenabatra/facebook-data>  


Gonzales, B. (2015, 7 de septiembre). *Seis grados de separación*. <https://www.anabad.org/seis-grados-de-separacion/> 

