# Application de Chat avec Traduction en Temps Réel

Cette application permet aux utilisateurs de communiquer en temps réel avec traduction automatique des messages.

## Fonctionnalités

- Chat en temps réel
- Traduction automatique des messages
- Support de plusieurs langues
- Interface utilisateur intuitive

## Prérequis

- Docker et Docker Compose
- ou Python 3.8+

## Installation

### Avec Docker (recommandé)

1. Clonez le dépôt :
```bash
git clone <votre-repo>
cd translation_chat_app
```

2. Construisez et lancez avec Docker Compose :
```bash
docker-compose up --build
```

3. Accédez à l'application sur `http://localhost:8080`

### Sans Docker

1. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix
# ou
.\venv\Scripts\activate  # Sur Windows
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Copiez le fichier d'environnement :
```bash
cp .env.example .env
```

4. Lancez l'application :
```bash
python app.py
```

## Déploiement

L'application est prête à être déployée sur diverses plateformes :

### Heroku

1. Créez une nouvelle application sur Heroku
2. Connectez votre dépôt GitHub
3. Déployez la branche principale

### Railway

1. Créez un nouveau projet
2. Importez depuis GitHub
3. Railway détectera automatiquement le Dockerfile

### DigitalOcean App Platform

1. Créez une nouvelle application
2. Sélectionnez votre dépôt
3. Configurez les variables d'environnement

## Variables d'Environnement

Copiez `.env.example` vers `.env` et ajustez les valeurs :

- `FLASK_ENV`: 'development' ou 'production'
- `PORT`: Port du serveur (par défaut: 8080)
- `SECRET_KEY`: Clé secrète pour Flask
- `USE_SSL`: 'true' ou 'false' (en développement uniquement)

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.
