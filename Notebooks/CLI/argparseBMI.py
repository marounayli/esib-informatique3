import argparse

# python argparseEntiers.py -h
# python argparseEntiers.py 50 1.65

parser = argparse.ArgumentParser()
parser.add_argument("poids", help="Poids en Kg", type=float)

parser.add_argument("taille",help="taille en m",type=float)

args = parser.parse_args()
bmi=args.poids/(args.taille**2)
print(f"BMI : {bmi}")

if bmi<18.5:
    print("Trop maigre")
elif bmi<25:
    print("Satisfaisant")
elif bmi<30:
    print("Surpoids")
else:
    print("Obesite")

