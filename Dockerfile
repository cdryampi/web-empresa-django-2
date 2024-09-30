# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Recoger archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer el puerto que usa Gunicorn
EXPOSE 8000

# Comando para ejecutar Gunicorn
CMD ["gunicorn", "tu_proyecto.wsgi:application", "--bind", "0.0.0.0:8000"]
