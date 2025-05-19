# Projet Associations

 
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
