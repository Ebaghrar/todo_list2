# Utiliser une image de base contenant Python et MySQL 5.6.35
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu actuel du répertoire vers le répertoire de travail
COPY . /app

# Installer les dépendances nécessaires
RUN pip install -r requirements.txt

# Installer MySQL 5.6.35
RUN apt-get update && apt-get install -y mysql-server-5.6

# Configurer la base de données MySQL
RUN service mysql start && mysql -e "CREATE DATABASE todolist;"

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]
