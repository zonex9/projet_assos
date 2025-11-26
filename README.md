# Projet Associations

Projet de gestion de matériel réalisé avec Python, React.js et JavaScript, incluant le déploiement avec Docker.

## Contexte

Ce projet est réalisé en partenariat avec IT LINK et une association à Lyon, dans un but non lucratif.

L'objectif est de créer une application web permettant aux utilisateurs d'emprunter du matériel et de suivre leurs commandes directement depuis leur compte, le tout est 100% ligne.


## Commandes FLASK principales pour le démarrage de projet

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
flask db init
```
```
flask db migrate -m "db init"
```
```
flask db upgrade
```
```
flask run
```

## Commandes Reat principales pour le démarrage de projet React

### Créer d'un nouveau projet React

```
npx create-react-app frontend

```
### Installation package X

```
npm install nom_du_package

```
### Installer tous les packages du package.json

```
npm install

```
### démarrer le projet
```
npm start
```
