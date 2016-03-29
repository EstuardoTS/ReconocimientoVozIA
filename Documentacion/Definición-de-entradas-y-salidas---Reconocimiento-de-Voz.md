

 
 
 
 

### Facultad de Ingeniería
### Ingeniería en Informática y Sistemas

### Inteligencia Artificial
### Ing. Dhaby Xiloj
 
### Integrantes:
### Kevin Uriel Martinez Monterroso 1552809
### Mariano Estuardo Teleguario Sincal 1554809

 
**Datos que se usarán para el entrenamiento del proyecto Reconocimiento de voz**

El proyecto consiste en un agente inteligente, el agente será un software capaz de detectar y reconocer la voz de una persona.

Por lo tanto los datos deben ser las grabaciones de voz realizadas previamente y almacenadas en una base de datos, esta base de datos ayudará a la comparación de una voz de “entrada” con la que está almacenada en la base de datos.

En si podemos obtener 100 datos de entrada, las cuales son las grabaciones previas para la base de datos. Las entradas deben ser convertidas por medio de un codificador (software), por consiguiente debe pasar por una red neuronal y al finalizar el proceso deberá tener como resultado una salida, en este caso debe desplegar en pantalla que se ha reconocido la voz o desplegar de quien es la voz.

![](https://github.com/EstuardoTS/ReconocimientoVozIA/blob/master/Documentacion/imagenes%20documentacion/ModeloProceso.PNG)

**Figura 1. Representación del proceso de reconocimiento de voz.**

Los archivos sonoros, deben transformarse en un conjunto de datos o patrones que sean entendibles por parte de la red neuronal. Esta tarea de mapeo de datos es realizada por un bloque codificador de entrada.

**La captura de voz**

Se puede realizar con simulink de Matlab®, lo que se quiere es que el archivo no sea tan pesado para poder obtener una codificación menor o pequeña, por lo que se puede grabar entre 4 o 6 segundos tomando una resolución de 8 bits, lo que hace que los datos sean pequeños pero suficientes para poder analizar.

Los archivos sonoros deben estar en formato .wav por su versatilidad de manejo con el software Matlab®,  los archivos sonoros pueden ser las voces de varias personas para tener disponibilidad de información.

En la siguiente tabla se representa como debería quedar el formato de cada archivo sonoro.

**Tabla 1. Representación del formato de cada archivo sonoro**

|Descripción  |  Características  |
| ------------  |  ---------------  |
|Velocidad de transmisión          |  128 Kbps      |
|Tamaño de la muestra	           |  16 bits       |
|Tipo de canal	                   |  Monofónico   | 
|Velocidad de muestreo de sonido   |  11 Khz        |
|Formato de audio	           |  *.wav        |

**Procesamiento de los archivos de voz**

En este proceso debemos optimizar la señal de entrada, puesto que serán las entradas para la red neuronal estas entradas deberán ser entendidas por la red neuronal, lo primero que se debe realizar es acotar la señal de voz eliminando la parte inicial y final de la misma, estas partes sólo representan el ruido al grabar los archivos de voz, para posteriormente utilizar la transformada de Fourier o utilizar el método Wavelets, que tiene las mismas características que la transformada de Fourier.

**Figura 2. Acotamiento de la señal**

![](https://github.com/EstuardoTS/ReconocimientoVozIA/blob/master/Documentacion/imagenes%20documentacion/acotamiento.PNG)

Como se ve en la Figura 3, se toma la sub-señal a[n] correspondiente a las bajas frecuencias de la señal de voz donde se localiza la mayor cantidad de energía de la misma, despreciando a la sub-señal b[n] que corresponde a las altas frecuencias ya que es donde se encuentra la mayor cantidad de ruido de la señal (ruido ambiental). Obteniendo así una señal de voz compacta y filtrada con respecto a la original.

**Figura 3. Representación del procesamiento por Fourier o Wavelets**

![](https://github.com/EstuardoTS/ReconocimientoVozIA/blob/master/Documentacion/imagenes%20documentacion/Frecuencias.PNG) 

Lo anterior, son los primeros pasos para obtener la información que servirán como entradas para la red neuronal, lo más importante es el acotamiento y reducción de ruido en los archivos de voz, de esta forma se filtra la parte más importante que es la voz.

**Salidas Del Proyecto de reconocimiento de voz**

El uso del reconocimiento de voz tiene muchas aplicaciones en distintos campos, desde facilitar la accesibilidad a las personas para el uso de sistemas hasta el permitir o denegar acceso a ciertas características de un sistema, como en este caso.

Como salidas la red neuronal devolverá un conjunto de bits (1 y 0) como respuesta a las entradas para que de este modo se pueda comprobar la autenticidad de la persona que está generando las entradas de voz y darle acceso o comunicación al sistema o software.

**Figura 4. Representación del proceso de salidas y comunicación con el Software**

![](https://github.com/EstuardoTS/ReconocimientoVozIA/blob/master/Documentacion/imagenes%20documentacion/salidasycomunicacion.PNG)

Estos mismos conjuntos de datos de las salidas puede ser guardado en una base de datos para que de este modo a través del correcto entrenamiento de la RNA se puedan cotejar con los datos almacenados y clasificar a diferentes individuos, siendo un sistema cerrado.

**Sistema cerrado**

Un sistema cerrado da por supuesto que el locutor que se quiere identificar se encuentra ya almacenado en la base de datos. El locutor con más probabilidades a la salida del clasificador, que comparte más características con el locutor a buscar, será la salida resultante del sistema.

**Figura 5. Representación del reconocimiento de voz con varios locutores registrados.**

![](https://github.com/EstuardoTS/ReconocimientoVozIA/blob/master/Documentacion/imagenes%20documentacion/proceso.PNG)

**Ambientes en que se desenvolverá el agente inteligente**

**Accesible:** como se trata de un software o softbot, este agente va a tener acceso a todo el entorno o ambiente, en este caso solo es el audio o recepción de voz, esta voz es realizada por una persona. El único dispositivo con que contará el agente será un micrófono que le proporcionara toda la información posible.

**Determinista:** al realizar la tarea de reconocimiento de voz del locutor que esté utilizando el micrófono, el agente deberá decidir si dará acceso o no a dicho locutor, lo cual será definido por la entrada y procesamiento del estado anterior.

**No episódico:** el trabajo del agente no se dividirá en episodios, esto implica que será el mismo agente que esté realizando el trabajo de reconocimiento de voz por consiguiente no cambiará de agente, si el reconocimiento de voz se pausara, al reanudarse las acciones no cambiarían seguiría analizando un archivo de audio y dando como resultado un acceso o negado o concedido, lo que quiere decir que no ha reconocido o que sí ha reconocido la voz de una persona.

**Discreto:** Es discreto debido a que existen un conjunto de acciones diferentes y discernibles en las cuales el agente inteligente se desenvolverá, siendo estas el reconocimiento de voz, la validación y brindar el acceso al locutor, sin ninguna otra acción no definida o inesperada que pueda afectar su correcto funcionamiento.

**Estático:** si tomamos la definición de ambiente estático, entonces podemos decir que los datos que toma el agente van a ser aleatorios, esto quiere decir, no todos los archivos de audio tomados por el agente van a ser los mismos, unos archivos puede que pesen unos bits más o bits menos, el procesamiento de audio no dará el mismo resultado, por lo que podemos decir que los datos serán aleatorios siempre. Otra de las partes de la definición de ambiente estático es que no habrá otro agente que contradiga sus acciones.

**Es un Agente Basado en Utilidad:** El agente tiene un conjunto de metas ya establecidas (reconocimiento de voz y brindar acceso) de este modo se puede garantizar una conducta de alta calidad al realizar el trabajo por parte del agente inteligente.
