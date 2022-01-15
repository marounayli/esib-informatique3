import argparse

# python argparseArg2.py John Smith
# python argparseArg2.py -h

parser = argparse.ArgumentParser() #Créer un objet "parser" de la classe ArgumentParser
parser.add_argument("prenom", help="Saisir le prénom d'une personne") #ajouter à cet objet un premier argument. Ici "prenom" est donné comme nom de l'argument
parser.add_argument("nom", help="Saisir le nom d'une personne") #ajouter à cet objet un deuxième argument. Ici "nom" est donné comme nom de l'argument
args = parser.parse_args() #récupérer tous les arguments ajoutés dans "args"

print(f"Bonjour {args.prenom} {args.nom}") #accéder aux argument "prenom" et "nom"#accéder aux argument "prenom" et "nom"
