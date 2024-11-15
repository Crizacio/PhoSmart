# PhoSmart

## Setup
Para el entorno de desarrollo, sigue los siguientes pasos para levantar:

> Para Windows basta usar el alias `py`.  
> Para Linux puede ser necesario usar `python3`.  
> Se utilizo el terminal para Windows PowerShell.  

 1. Clona el repositorio.  
    ```sh
    git clone https://github.com/Crizacio/PhoSmart.git
    ```
 2. Crea un entorno virtual de Python.  
    ```sh
    py -m venv .venv
    ```
 3. Activa el entorno virtual de Python.  
    ```sh
    .\.venv\Scripts\Activate.ps1
    ```
 4. Instala las librerias de Python requeridas.  
    ```sh
    pip install -r requirements.txt
    ```
 5. Realiza las migraciones.  
    ```sh
    py manage.py makemigrations
    py manage.py migrate
    ```
 6. Levanta el servidor.
    ```sh
    py manage.py runserver
    ```
