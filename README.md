# Projet Associations

Projet de gestion des matériels réalisé avec Python/React.JS

## Contexte

Ce projet est réalisé en partenariat avec IT LINK et une association à Lyon, dans un but non lucratif.

L'objectif est de créer une application web permettant aux utilisateurs d'emprunter du matériel et de suivre leurs commandes directement depuis leur compte, le tout est 100% ligne.


## Commandes principales pour le démarrage de projet

```
pip install -r .\requirements.txt
```
```
$env:FLASK_ENV = "development"
```
```
$env:FLASK_APP = "run.py"
```
```
python -m flask db init
```
```
python -m flask db migrate -m "db init"
```
```
python -m flask db upgrade
```
```
python -m flask run
```
