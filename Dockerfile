# Dockerfile
FROM python:3.12-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos y las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Ejecuta collectstatic para preparar los archivos estáticos
RUN python manage.py collectstatic --noinput

# Ejecuta las migraciones
RUN python manage.py migrate

# Inicia Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]