import argparse

# python volumePyramide.py -c 9 -ha 20 

desc = "Calcul du volume d'une pyramide"
parser = argparse.ArgumentParser(description = desc)

parser.add_argument("--cote","-c",help="cote de la base",type=float,required=True)
parser.add_argument("--hauteur","-ha",help="Hauteur de la pyramide",type=float,required=True)

args = parser.parse_args()

aire=args.cote**2
volume=aire*args.hauteur/3
print(f" Le volume de la pyramide vaut {volume}")

