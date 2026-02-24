# k8s-cloud-app-base

Proyecto base para aprender y practicar la integración de Docker con Kubernetes.

## Contenido

- `dockerfile` – Construye la imagen del contenedor de la aplicación.
- `deployment.yaml` – Despliega la app en Kubernetes con un Deployment.
- `service.yaml` – Expone la app mediante un Service de tipo ClusterIP.
- `configmap.yaml` – Configuración de variables de entorno para la app.
- `app.py` – Aplicación simple en Python.
- `requirements.txt` – Dependencias de Python.
- `logs.txt` – Logs de pruebas locales.

## Uso

1. Construir la imagen Docker:

docker build -t cloud-app:v2 .

2. Desplegar en Kubernetes (Minikube o cluster real):

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml

3. Verificar los pods:
kubectl get pods

4. Exponer el servicio y obtener la URL:
   minikube service cloud-app-service --url

Objetivo del proyecto

Repasar conceptos básicos de Docker y Kubernetes.

Tener una base rápida para prácticas en entornos Cloud (AWS / GCP) antes de trabajar en producción.

Preparación para desplegar aplicaciones containerizadas de manera sencilla y reproducible.
