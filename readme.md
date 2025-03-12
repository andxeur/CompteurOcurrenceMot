Description
-----------

Ce projet vise à fournir des methodes pour analyser une phrase et compter les occurrences de chaque mot.

Fonctionnalités
---------------

*   `mot_plus_utiliser(phrase)`: affiche le mot le plus utilisé dans une phrase et son nombre d'occurrences.
*   `compt_mot_utiliser(phrase)`: affiche tous les mots et leur nombre d'occurrences dans une phrase.

Utilisation
------------

Pour utiliser ces fonctions, il suffit de les appeler en passant une phrase en argument :
```python
mot_plus_utiliser("Ceci est un exemple de phrase,bon exemple .")
compt_mot_utiliser("Ceci est un exemple de phrase,bon exemple.")
```

Fonctionnalités techniques
-------------------------

*   Les fonctions utilisent des expressions régulières pour supprimer les ponctuations et convertir les phrases en minuscules.

Exemples de sortie
-----------------

*   `mot_plus_utiliser("Le soleil brille, brille et illumine le ciel. brille.")` :
	+ le mot le plus utiliser est 'brille' --> utiliser 3 fois
*   `compt_mot_utiliser("Le soleil brille, brille et illumine le ciel. brille.")` :
	+ le mot 'le' est utiliser 2 fois
    + le mot 'soleil' est utiliser 1 fois
    + le mot 'brille' est utiliser 3 fois
    + le mot 'et' est utiliser 1 fois
    + le mot 'illumine' est utiliser 1 fois
    + le mot 'ciel' est utiliser 1 fois

Note
----

*   Ce code est sous licence : Assammond Andre (Andxeur)
