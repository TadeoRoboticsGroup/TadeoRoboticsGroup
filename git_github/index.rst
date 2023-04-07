.. _git_github:

Introducción a Git
###############

Git es un sistema de control de versiones distribuido que permite a los usuarios llevar un registro de los cambios en un archivo o conjunto de archivos. Los usuarios pueden rastrear el historial de cambios, revertir a versiones anteriores, colaborar con otros usuarios y mantener un registro completo de todos los cambios realizados en el código.

Configuración inicial
*********************
    Antes de comenzar a usar Git, es necesario realizar una configuración inicial. Primero, debes descargar e instalar Git en tu ordenador. Luego, deberás configurar tus credenciales de Git usando el siguiente comando:

        .. code-block:: bash
            git config --global user.name "Tu nombre"
            git config --global user.email "Tu correo electrónico"

    Esto te permitirá identificarte correctamente al momento de hacer cambios en un repositorio.

Creación de un repositorio
**************************
    Para comenzar a utilizar Git, primero necesitas crear un repositorio. Para hacerlo, debes navegar a la carpeta donde deseas crear el repositorio y ejecutar el siguiente comando:

        .. code-block:: bash
            git init

    Esto creará un nuevo repositorio vacío en la carpeta seleccionada.

Añadiendo archivos al repositorio
*********************************
    Una vez que tienes un repositorio, puedes comenzar a agregar archivos. Para hacerlo, coloca los archivos en la carpeta del repositorio y ejecuta el siguiente comando:

        .. code-block:: bash
            git add archivo
    Este comando agregará los archivos al área de preparación de Git, lo que significa que Git comenzará a realizar un seguimiento de los cambios realizados en los archivos.

Confirmar los cambios
*********************
    Una vez que has agregado archivos al área de preparación, es necesario confirmar los cambios usando el siguiente comando:

        .. code-block:: bash
            git commit -m "Mensaje de confirmación"
    Este comando confirmará los cambios realizados en los archivos y agregará una descripción en el mensaje de confirmación.

Visualizando el estado del repositorio
**************************************
    Para visualizar el estado actual del repositorio y los cambios que se han realizado, usa el siguiente comando:

        .. code-block:: bash
            git status
    Este comando te mostrará los archivos que han sido modificados, los archivos que están en el área de preparación y los archivos que han sido confirmados.

Trabajando con ramas
********************
    Las ramas son una parte importante de Git, ya que permiten a los usuarios trabajar en diferentes versiones de un mismo proyecto al mismo tiempo. Para crear una nueva rama, usa el siguiente comando:

        .. code-block:: bash
            git branch nueva-rama
    Este comando creará una nueva rama con el nombre "nueva-rama". Para cambiar a esta nueva rama, usa el siguiente comando:

        .. code-block:: bash
            git checkout nueva-rama
    Para ver una lista de todas las ramas existentes en el repositorio, usa el siguiente comando:

        .. code-block:: bash
            git branch
    Para fusionar dos ramas, primero debes cambiar a la rama en la que deseas fusionar las otras ramas. Luego, usa el siguiente comando:

        .. code-block:: bash
            git merge otra-rama
    Este comando fusionará la rama "otra-rama" con la rama actual.

    Para eliminar una rama, usa el siguiente comando:

        .. code-block:: bash
            git branch -d rama-a-eliminar


Publicando cambios
******************
    Para publicar los cambios realizados en un repositorio, es necesario subirlos a un servidor remoto. Para hacerlo, primero debes agregar el servidor remoto usando el siguiente comando:

        .. code-block:: bash
            git remote add origin <URL del servidor>
    Luego, sube los cambios usando el siguiente comando:

        .. code-block:: bash
            git push origin <nombre de la rama>
    Este comando subirá los cambios realizados en la rama especificada al servidor remoto.

Trabajando con repositorios remotos
***********************************
    Para descargar un repositorio remoto a tu ordenador, usa el siguiente comando:

        .. code-block:: bash
            git clone <URL del repositorio>

    Este comando descargará el repositorio remoto en tu ordenador y creará una copia local del mismo.

    Para obtener cambios realizados en el repositorio remoto, usa el siguiente comando:

        .. code-block:: bash
            git pull
    Este comando descargará los cambios realizados en el repositorio remoto y los fusionará con tu rama actual.

Conclusión
**********
    Git es una herramienta poderosa y esencial para cualquier desarrollador. Con su capacidad de rastrear y controlar el historial de cambios, Git permite a los desarrolladores trabajar de manera más eficiente y colaborativa en proyectos. Aunque los comandos básicos de Git son sencillos, hay muchos otros comandos y técnicas avanzadas que pueden ser útiles para un flujo de trabajo más avanzado. Esperamos que esta introducción a Git te haya proporcionado una base sólida para comenzar a trabajar con Git y que te animes a explorar más allá de los comandos básicos.
