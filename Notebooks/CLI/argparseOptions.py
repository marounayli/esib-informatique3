import argparse 

# python argparseOptions.py Michel Dupont
# python argparseOptions.py -s Hola Michel Dupont
# python argparseOptions.py -s Hola -p Mr Michel Dupont
# python argparseOptions.py -s Hola -p Mr Michel

desc = "Inspection des parametres et options de la ligne de commande"
parser = argparse.ArgumentParser(description = desc)
parser.add_argument('-s','--salutation',help = 'la salutation a utiliser',required=True)
parser.add_argument('-p','--prefix',help = 'le prefix a utiliser',required = False)
parser.add_argument("prenom")
parser.add_argument("nom")

args = parser.parse_args()

salutation = "Hello"
prefix = "Mr./Ms."

if args.salutation:
    salutation = args.salutation
if args.prefix:
    prefix = args.prefix
    
print(f"{salutation}  {prefix} {args.prenom} {args.nom}")
