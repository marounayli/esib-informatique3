import argparse

# python argparseEntiers.py -h
# python argparseEntiers.py 4 3

parser = argparse.ArgumentParser()
parser.add_argument("a", help="premier entier", type=int)

parser.add_argument("b",help="deuxieme entier",type=int)

args = parser.parse_args()

print(args.a+args.b)

