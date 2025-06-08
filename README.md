# prueba-juliann
Prueba Julian: Citas Web Scraping
Este proyecto es parte de la Evidencia de Aprendizaje 3 de la materia Programación para Análisis de Datos en la IU Digital de Antioquia. Tiene como objetivo demostrar la aplicación de la automatización de procesos mediante GitHub Actions, realizando web scraping de citas motivacionales y desplegando los resultados en una página web usando GitHub Pages.

Introducción
Este repositorio contiene un proyecto desarrollado en Python que extrae información de citas motivacionales desde la web y las almacena en un archivo CSV. Además, se implementa un pipeline CI/CD con GitHub Actions que automatiza el proceso desde la instalación de dependencias hasta el despliegue del sitio web generado con HTML.

Instalación
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/JulianValenciaGomez/prueba-julian.git
cd prueba-julian
Crea y activa un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
./venv/Scripts/activate  # En Windows
Instala las dependencias del proyecto:

bash
Copiar
Editar
pip install -e .
Uso
Para ejecutar el scraper y generar el archivo HTML con los resultados:

bash
Copiar
Editar
python dataweb.py
El archivo generado index.html contiene una tabla con las citas extraídas de la web.

Automatización (GitHub Actions)
El proyecto incluye un flujo de trabajo de GitHub Actions definido en .github/workflows/accionables.yml, que:

Se ejecuta automáticamente al hacer push a la rama main.

Instala Python y dependencias.

Ejecuta el script dataweb.py para generar el archivo actualizado.

Realiza un commit automático con los cambios al repositorio.

Esto permite que los resultados del scraping siempre estén actualizados sin intervención manual.

Despliegue
La página web generada con las citas extraídas está desplegada en GitHub Pages:

https://julianvalenciagomez.github.io/prueba-julian/

Cada vez que se actualiza la rama main, el contenido del sitio también se actualiza automáticamente gracias al pipeline CI/CD.

Autor
Julian Esteban Valencia Gomez
Estudiante de la Universidad IU Digital de Antioquia
Materia: Programación para Análisis de Datos
Profesor: Andrés Felipe Callejas
Grupo: PREICA2501B020065









