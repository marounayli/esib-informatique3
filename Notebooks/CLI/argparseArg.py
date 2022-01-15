import argparse

# python argparseArg.py Sami
# python argparseArg.py -h

parser = argparse.ArgumentParser() #Créer un objet "parser" de la classe ArgumentParser
parser.add_argument("prenom", help="Saisir le prénom d'une personne") #ajouter à cet objet un argument. Ici le nom "prenom" est donné comme nom de l'argument
args = parser.parse_args()

print("Bonjour {}".format(args.prenom))
