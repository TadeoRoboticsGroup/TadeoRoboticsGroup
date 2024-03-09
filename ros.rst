.. _ros_documentation:

=============================================
Documentación de ROS1 y ROS2
=============================================

Introducción
------------

Este documento proporciona una introducción completa a ROS1 (Robot Operating System) y ROS2, incluyendo sus conceptos básicos, diferencias clave, cómo utilizarlos en proyectos de robótica, las bibliotecas y dependencias asociadas, y ejemplos de uso tanto en Python como en C++.

ROS1: Introducción
-------------------

ROS1 es un sistema de middleware de código abierto utilizado para desarrollar software para robots. Proporciona una infraestructura para la comunicación entre diferentes componentes de un sistema robótico, como sensores, actuadores y algoritmos de procesamiento. Algunos de los conceptos clave de ROS1 incluyen:

- Nodos: Procesos independientes que realizan tareas específicas y se comunican entre sí a través de mensajes.
- Tópicos: Canales de comunicación unidireccionales a través de los cuales los nodos intercambian mensajes.
- Servicios: Funciones que pueden ser llamadas remotamente por otros nodos para realizar tareas específicas.
- Bolsas: Archivos de registro que contienen datos de mensajes publicados en tópicos durante la ejecución de un sistema ROS.

ROS2: Introducción
-------------------

ROS2 es la versión más reciente de ROS, diseñada para abordar las limitaciones y desafíos encontrados en ROS1. Introduce mejoras en términos de escalabilidad, seguridad y soporte multiplataforma. Algunas de las características clave de ROS2 son:

- Soporte para múltiples arquitecturas de comunicación, incluyendo DDS (Data Distribution Service).
- Mejoras en la seguridad, como el soporte para cifrado de mensajes.
- Mayor modularidad y flexibilidad en comparación con ROS1.

Diferencias entre ROS1 y ROS2
------------------------------

Aunque ROS1 y ROS2 comparten conceptos fundamentales, también tienen diferencias significativas en términos de arquitectura y funcionalidades. Algunas de las diferencias más destacadas son:

- Arquitectura de comunicación: ROS1 utiliza un sistema de comunicación basado en TCPROS/UDPROS, mientras que ROS2 es compatible con diferentes arquitecturas de comunicación, incluyendo DDS.
- Soporte multiplataforma: ROS2 está diseñado para ser compatible con una amplia gama de plataformas, incluyendo Windows, macOS y sistemas embebidos.
- Seguridad: ROS2 incorpora características de seguridad mejoradas, como el cifrado de mensajes, que no están presentes en ROS1.

Uso de ROS1 y ROS2
--------------------

Para comenzar a utilizar ROS1 o ROS2 en tus proyectos de robótica, sigue estos pasos básicos:

1. Instala ROS1 o ROS2 en tu sistema operativo. Puedes encontrar instrucciones detalladas en la documentación oficial de ROS (https://wiki.ros.org/ROS/Installation).
2. Crea un espacio de trabajo de ROS utilizando `catkin_make` para ROS1 o `colcon` para ROS2.
3. Escribe nodos ROS en Python o C++ utilizando las bibliotecas proporcionadas por ROS (`rospy` para ROS1 y `rclcpp` para ROS2).
4. Comunica tus nodos utilizando tópicos, servicios o acciones, según sea necesario para tu aplicación específica.
5. Ejecuta y prueba tus nodos en un entorno simulado o en hardware real.

Bibliotecas y Dependencias
---------------------------

Tanto ROS1 como ROS2 proporcionan un conjunto de bibliotecas y herramientas que facilitan el desarrollo de software para robots. Algunas de las bibliotecas y dependencias comunes incluyen:

- `roscpp` (ROS1): Biblioteca de C++ para el desarrollo de nodos ROS en ROS1.
- `rospy` (ROS1): Biblioteca de Python para el desarrollo de nodos ROS en ROS1.
- `rclcpp` (ROS2): Biblioteca de C++ para el desarrollo de nodos ROS en ROS2.
- `rclpy` (ROS2): Biblioteca de Python para el desarrollo de nodos ROS en ROS2.
- Otras dependencias comunes incluyen herramientas de simulación como Gazebo y bibliotecas de percepción como OpenCV.

Por qué usar ROS
----------------

ROS proporciona una plataforma robusta y flexible para el desarrollo de software para robots. Algunas de las razones para utilizar ROS en tus proyectos incluyen:

- Comunidad activa: ROS cuenta con una gran comunidad de usuarios y desarrolladores que contribuyen con paquetes, tutoriales y soporte.
- Modularidad: ROS facilita la creación de sistemas robóticos modulares y reutilizables mediante el uso de nodos independientes.
- Herramientas integradas: ROS proporciona una amplia gama de herramientas integradas para la simulación, visualización y depuración de sistemas robóticos.
- Soporte multiplataforma: Tanto ROS1 como ROS2 son compatibles con una variedad de sistemas operativos y arquitecturas de hardware, lo que permite el desarrollo de aplicaciones para una amplia gama de plataformas.


ROS1 y ROS2 son herramientas poderosas para el desarrollo de software para robots, cada una con sus propias características y ventajas. Al comprender los conceptos básicos, las diferencias clave y cómo utilizar estas plataformas, estarás bien preparado para construir aplicaciones robóticas sofisticadas y escalables.



Ejercicios Prácticos
---------------------

A continuación se presentan algunos ejercicios prácticos para ayudarte a familiarizarte con ROS1 y ROS2:

1. **Publicación y suscripción de mensajes en Python:**
   - Crea un nodo que publique mensajes de tipo `std_msgs/String` en un tópico personalizado.
   - Crea otro nodo que se suscriba al tópico y muestre los mensajes recibidos en la consola.

2. **Llamadas a servicios en C++:**
   - Crea un servicio que devuelva la suma de dos números enteros.
   - Implementa un nodo cliente que llame al servicio y muestre el resultado en la consola.

continúa aprendiendo aquí

.. toctree::
   :titlesonly:
   :maxdepth: 
   :hidden:

   ros/exercises