FROM python:3.11-slim

WORKDIR /app

# dependencias del sistema (psycopg2 necesita esto)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements
COPY requirements.txt .

# instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# copiar código
COPY main.py .
COPY database.py .

# exponer puerto
EXPOSE 8000

# ejecutar app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
