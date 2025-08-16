# Imagen base de Python
FROM python:3.11-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la app
COPY app.py .

# Exponer el puerto de Flask
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
