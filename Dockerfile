# Usar una imagen base de Python
FROM python:3.9-slim

# Instalar dependencias del sistema necesarias para Pillow y otras librerías
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7 \
    libtiff-dev \  # Reemplazar libtiff5 por libtiff-dev
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Añadir wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Establecer el directorio de trabajo
WORKDIR /app

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

# Comando para ejecutar Gunicorn usando wait-for-it
CMD ["/wait-for-it.sh", "db:5432", "--", "gunicorn", "webempresa.wsgi:application", "--bind", "0.0.0.0:8000"]
