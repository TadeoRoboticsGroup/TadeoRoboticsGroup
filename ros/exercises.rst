Ejercicios Prácticos en ROS2
=============================

A continuación se presentan dos ejercicios prácticos para ayudarte a familiarizarte con la creación de nodos en ROS2 para el envío y recepción de mensajes.

Envío de Mensajes en ROS2
--------------------------

Escribe un nodo en ROS2 que publique mensajes de tipo `std_msgs/String` en un tópico personalizado. Sigue estos pasos:

1. Crea un nuevo archivo Python, por ejemplo `publisher_node.py`.
2. Escribe el siguiente código en el archivo para definir el nodo de publicación:

   .. code:: python
      :linenos:

      # Importa las bibliotecas necesarias de ROS2
      import rclpy
      from rclpy.node import Node
      from std_msgs.msg import String

      class PublisherNode(Node):
          def __init__(self):
              super().__init__('publisher_node')  # Nombre del nodo
              self.publisher_ = self.create_publisher(String, 'topic', 10)  # Crea el publicador
              timer_period = 1  # Publica el mensaje cada segundo
              self.timer = self.create_timer(timer_period, self.publish_message)

          def publish_message(self):
              msg = String()  # Crea un mensaje de tipo String
              msg.data = 'Hola desde ROS2'  # Asigna el contenido del mensaje
              self.publisher_.publish(msg)  # Publica el mensaje

      def main(args=None):
          rclpy.init(args=args)
          publisher_node = PublisherNode()
          rclpy.spin(publisher_node)
          rclpy.shutdown()

      if __name__ == '__main__':
          main()

3. Ejecuta el nodo utilizando el siguiente comando en la terminal:

   .. code:: bash
      :linenos:

      $ python3 publisher_node.py

   Este nodo publicará mensajes en el tópico especificado.

Recepción de Mensajes en ROS2
------------------------------

Escribe un nodo en ROS2 que se suscriba a un tópico y muestre los mensajes recibidos en la consola. Sigue estos pasos:

1. Crea un nuevo archivo Python, por ejemplo `subscriber_node.py`.
2. Escribe el siguiente código en el archivo para definir el nodo de suscripción:

   .. code:: python

      # Importa las bibliotecas necesarias de ROS2
      import rclpy
      from rclpy.node import Node
      from std_msgs.msg import String

      class SubscriberNode(Node):
          def __init__(self):
              super().__init__('subscriber_node')  # Nombre del nodo
              self.subscription = self.create_subscription(
                  String, 'topic', self.listener_callback, 10)  # Se suscribe al tópico
              self.subscription  # Evita que la referencia se elimine prematuramente

          def listener_callback(self, msg):
              self.get_logger().info(f'Mensaje recibido: {msg.data}')  # Muestra el mensaje en la consola

      def main(args=None):
          rclpy.init(args=args)
          subscriber_node = SubscriberNode()
          rclpy.spin(subscriber_node)
          rclpy.shutdown()

      if __name__ == '__main__':
          main()

3. Ejecuta el nodo utilizando el siguiente comando en la terminal:

   .. code:: bash

      $ python3 subscriber_node.py

   Este nodo se suscribirá al tópico especificado y mostrará los mensajes recibidos en la consola.

¡Estos ejercicios te ayudarán a empezar con la creación de nodos en ROS2 para el envío y recepción de mensajes!
