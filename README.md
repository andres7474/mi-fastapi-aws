FastAPI AWS Project (S3 + RDS + EC2 + Docker + ECR + Lambda)
Descripción del proyecto

Este proyecto implementa una API construida con FastAPI que permite:

Subida de imágenes a Amazon S3
Registro de metadata en Amazon RDS (PostgreSQL)
Consulta de imágenes mediante URLs prefirmadas
Despliegue en EC2 con Docker
Publicación de imagen en Amazon ECR
Creación de función Lambda basada en contenedor
Arquitectura
FastAPI (Backend API)
Amazon S3 (almacenamiento de imágenes)
Amazon RDS PostgreSQL (base de datos)
EC2 (hosting de aplicación)
Docker (contenedorización)
Amazon ECR (registro de imagen)
AWS Lambda (despliegue serverless desde contenedor)
Tecnologías utilizadas
Python 3.11
FastAPI
Boto3
Psycopg2
Uvicorn
Docker
AWS S3
AWS RDS PostgreSQL
AWS EC2
AWS ECR
AWS Lambda
Estructura del proyecto
mi-fastapi-aws/
│
├── main.py
├── database.py
├── requirements.txt
├── FastAPI.service
├── Dockerfile
├── README.md
Configuración de variables de entorno
DB_HOST=talleraws.c4p0giyyc1j9.us-east-1.rds.amazonaws.com
DB_NAME=talleraws
DB_USER=postgres
DB_PASSWORD=Cuota205070
AWS_REGION=us-east-1
S3_BUCKET=user-1014980791-ueia-so
Base de datos (RDS PostgreSQL)
Endpoint RDS
talleraws.c4p0giyyc1j9.us-east-1.rds.amazonaws.com
Base de datos
talleraws
Tabla utilizada
CREATE TABLE imagenes (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(100),
    s3_key TEXT,
    fecha TIMESTAMP DEFAULT NOW()
);
S3 Bucket

Bucket utilizado:

user-1014980791-ueia-so

Funciones:

Almacenamiento de imágenes PNG/JPG
Acceso mediante URLs prefirmadas
Endpoints API
Subir imagen
Body (form-data):

usuario: string
file: imagen PNG/JPG
Obtener imagen
GET /image?usuario=xxx&nombre_imagen=xxx
Respuesta:

URL prefirmada desde S3
Fecha de almacenamiento en RDS
Docker
Build imagen
docker build -t fastapi-s3-rds .
Ejecutar contenedor
docker run -p 8000:8000 \
-e DB_HOST=talleraws.c4p0giyyc1j9.us-east-1.rds.amazonaws.com \
-e DB_NAME=talleraws \
-e DB_USER=postgres \
-e DB_PASSWORD=Cuota205070 \
FastAPI AWS Project (S3 + RDS + EC2 + Docker + ECR + Lambda)
Descripción del proyecto

Este proyecto implementa una API construida con FastAPI que permite:

Subida de imágenes a Amazon S3
Registro de metadata en Amazon RDS (PostgreSQL)
Consulta de imágenes mediante URLs prefirmadas
Despliegue en EC2 con Docker
Publicación de imagen en Amazon ECR
Creación de función Lambda basada en contenedor
Arquitectura
FastAPI (Backend API)
Amazon S3 (almacenamiento de imágenes)
Amazon RDS PostgreSQL (base de datos)
EC2 (hosting de aplicación)
Docker (contenedorización)
Amazon ECR (registro de imagen)
AWS Lambda (despliegue serverless desde contenedor)
Tecnologías utilizadas
Python 3.11
FastAPI
Boto3
Psycopg2
Uvicorn
Docker
AWS S3
AWS RDS PostgreSQL
AWS EC2
AWS ECR
AWS Lambda
Estructura del proyecto
mi-fastapi-aws/
│
├── main.py
├── database.py
├── requirements.txt
├── FastAPI.service
├── Dockerfile
├── README.md
Configuración de variables de entorno
DB_HOST=talleraws.c4p0giyyc1j9.us-east-1.rds.amazonaws.com
DB_NAME=talleraws
DB_USER=postgres
DB_PASSWORD=Cuota205070
AWS_REGION=us-east-1
S3_BUCKET=user-1014980791-ueia-so
Base de datos (RDS PostgreSQL)
Endpoint RDS
talleraws.c4p0giyyc1j9.us-east-1.rds.amazonaws.com
Base de datos
talleraws
Tabla utilizada
CREATE TABLE imagenes (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(100),
    s3_key TEXT,
    fecha TIMESTAMP DEFAULT NOW()
);
S3 Bucket

Bucket utilizado:

user-1014980791-ueia-so

Funciones:

Almacenamiento de imágenes PNG/JPG
Acceso mediante URLs prefirmadas
Endpoints API
Subir imagen
Body (form-data):

usuario: string
file: imagen PNG/JPG
Obtener imagen
GET /image?usuario=xxx&nombre_imagen=xxx
Respuesta:

URL prefirmada desde S3
Fecha de almacenamiento en RDS
Docker
Build imagen
docker build -t fastapi-s3-rds .
Ejecutar contenedor
docker run -p 8000:8000 \
-e DB_HOST=talleraws.c4p0giyyc1j9.us-east-1.rds.amazonaws.com \
-e DB_NAME=talleraws \
-e DB_USER=postgres \
-e DB_PASSWORD=Cuota205070 \
-e AWS_REGION=us-east-1 \
-e S3_BUCKET=user-1014980791-ueia-so \
fastapi-s3-rds
Amazon ECR

Imagen subida a:

557690624990.dkr.ecr.us-east-1.amazonaws.com/fastapi-s3-rds:latest
AWS Lambda
Función creada desde imagen en ECR
Tipo: Container Image
URL pública habilitada (Function URL)
Imagen utilizada: ECR FastAPI container
EC2 Deployment

La aplicación está desplegada en EC2 con Docker.

Puerto: 8000
Acceso público vía Security Group
Uvicorn ejecutando FastAPI
URL de acceso
http://<EC2-PUBLIC-IP>:8000/docs
