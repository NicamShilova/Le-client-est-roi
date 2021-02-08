# Le client est roi




## Votre client pour qui vous avez développé la base de données dans le brief "Les pays en chiffre" souhaite faire évoluer sa base de données en NoSQL


### Pré-requis

Python

Anaconda

Flask

request

render_template

jsonify

MongoClient
app

date

json

csv

random

logging


### Installation

Installer Anaconda

Installer vscode

Dans Anaconda, creer un environnement

S'inscrire sur https://account.mongodb.com/

Sur ce compte, ajouter un cluster, et ajouter une base de données "pays"

Et ajouter l'adresse IP de son poste de travail



### Exécution

Dans vscode, charger la classe pays.py

Démarrer un shell

Executer la ligne de commande : & & C:/Users/Simplon/anaconda3/envs/mongodb/python.exe "c:/Users/Simplon/Documents/briefs/Python/Le client est roi/pays.py"

Démarrer un navigateur internet

Dans la barre de navigation, saisir les adresses suivantes :
 - Afficher les informations d'un pays sélectionné  : http://127.0.0.1:5000/api/countryselection/ajouter_le_nom_dy_pays
 - Ajouter un pays  : http://127.0.0.1:5000/api/addcountry/ajouter_le_nom_dy_pays
 - Classer les pays par densité selon des critères  : http://127.0.0.1:5000/api/countrydensityselection/