# Tests python depuis le terminal
```yaml
# lancer Python
 python
```
## Test opération arithmétiques
```python
 a = 1
  a +=1
## division
 5/2
 5//2 # tronquée
```
## sortie terminal
```python
 mot = "hello"
 print(mot)
```
## variables et typage
```python
# attribuer une valeur
 n = 3.5
# fonction vérifie le type
 type(n)
<class 'float'>
# effacer une variable
 del n
# type string
 texte = "hello"
 type(texte)
# <class 'str'>
```
## tableaux
```python
 lettres = ['A','B','C','D']
## afficher pour l'utilisateur
 print(lettres[0])
## afficher pour le dev
 lettres[0]
## voir aussi : https://www.w3schools.com/python/python_arrays.asp
```
## string concatenate
```python
 mot = "Chien"
 a= 1
 a+mot
## Oups!
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
## pour que ça marche
 str(a)+mot
'1Chien'
```
## Booleans
```python

 s = true ## NOK
 s =  True ## OK
```
## conditions
```python
res = input('combien ?')
combien ?3

if res == 1:
...     print(res +' = un')
... else:
...     print(res +' = autre')
... 
3 = autre
```
## Terminal : exécuter un fichier .py
- Copier depuis l'explorateur l'adresse du fichier
- exp: `C:\__MyAPPS\python`
- Tapez dans le terminal : 
    - cd `C:\__MyAPPS\python`
    - puis `python lefichier.py`
#
# Python depuis Visual studio code
- créer des fichiers avec l'extension `.py`
- Installer l'extension `python`

