import re
from collections import Counter


def mot_plus_utiliser(phrase: str):
    # supprime toutes les ponctuations sauf les lettres, les chiffres, et espace
    phrase = re.sub(r'[^\w\s]', '', phrase).lower().split(" ")

    # renvoie un dictionnaire de chaque mot et son occurance comme valeur
    dico_compteur = Counter(phrase)
    mot_plus_utiliser = max(dico_compteur, key=dico_compteur.get)

    print(f"le mot le plus utiliser est '{mot_plus_utiliser}' --> utiliser {phrase.count(mot_plus_utiliser)} fois")


def compt_mot_utiliser(phrase: str):
    # supprime toutes les ponctuations sauf les lettres, les chiffres, et espace
    phrase = re.sub(r'[^\w\s]', '', phrase).lower().split(" ")

    # renvoie un dictionnaire de chaque mot et son occurance comme valeur
    dico_compteur = Counter(phrase)

    for cle, valeur in dico_compteur.items():
        print(f"le mot '{cle}' est utiliser {valeur} fois")


phrase = "Le soleil brille, brille et illumine le ciel. brille."

mot_plus_utiliser(phrase)
compt_mot_utiliser(phrase)


