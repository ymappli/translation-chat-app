FROM python:3.8-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de l'application
COPY . .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Variables d'environnement
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=10000

# Exposition du port
EXPOSE 10000

# Commande de démarrage
CMD gunicorn --worker-class gevent --workers 1 --bind 0.0.0.0:$PORT app:app
