# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código de tu aplicación al contenedor
COPY . /app

# Instala las dependencias utilizando pip
RUN pip install -r requirements.txt

# Ejecuta cualquier script de inicialización necesario

RUN python scripts/migrate_csv_to_sqlite.py

# Expón el puerto en el que corre tu aplicación
EXPOSE 8000

# Comando por defecto para ejecutar tu aplicación con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]