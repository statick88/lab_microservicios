# Laboratorio Microservicios

## Descripción

Este laboratorio tiene como objetivo la integración de varios microservicios mediante Docker Compose y la implementación de un orquestador de contenedores.

## Requisitos

- Docker
- Docker Compose

## Instrucciones

1. Clonar el repositorio

```bash
git clone https://github.com/statick88/lab_microservicios.git
```

2. Ingresar al directorio del repositorio

```bash
cd lab_microservicios
```

3. Crear la red de Docker

```bash
docker network create lab_microservicios
```

4. Construir las imágenes de Docker

```bash
docker-compose build
```

5. Iniciar los contenedores

```bash
docker-compose up -d
```

6. Verificar que los contenedores estén en ejecución

```bash
docker-compose ps
```

7. Acceder a la URL del orquestador de contenedores

```
http://localhost:8080
```

8. Detener los contenedores

```bash
docker-compose down
```

9. Eliminar la red de Docker

```bash
docker network rm lab_microservicios
```
