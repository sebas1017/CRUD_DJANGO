 
 ![alt text](https://github.com/sebas1017/CRUD_DJANGO/blob/master/DEMO.jpg?raw=true)



[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=sebas1017)](https://github.com/sebas1017/CRUD_DJANGO)

Tenemos una aplicacion CRUD realizada en el framework Django junto a python y utilizando una base de datos POSTGRESQL que corre en la nube 
en un cluster de heroku, la aplicacion corriendo en la nube se encuentra en heroku pero estan en distintos servidores (base de datos y la aplicacion)

si se desea replicar localmente el proyecto debe clonar el repositorio y una vez estando en la carpeta descargada crear un entorno virtual

python3 -m venv venv

luego debe activar el entorno virtual (en el caso de LINUX)

source venv/bin/activate


una vez activado el entorno virtual debe instalar las dependencias que se encuentran en el archivo requirements.txt con el comando
pip install -r requirements.txt


una vez instaladas las dependencias debe estar en la raiz del proyecto donde se encuentra el archivo manage.py y ejecutar el comando 
python manage.py runserver


una vez ejecutado podra observar la aplicacion corriendo en la direccion http://127.0.0.1:8000/

de acuerdo a los requerimientos planteados tenemos validacion de campos vacios , verificacion de que la hora final de atencion no sea mayor a la hora inicial de atencion
y validacion de formatos de fechas  , por lo que tambien puede observar la aplicacion corriendo en la nube en el siguiente url


https://geteco-app.herokuapp.com/

