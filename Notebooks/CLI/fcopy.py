import sys

if len(sys.argv) !=3:
    print("Usage : {0} fichier1 fichier2".format(sys.argv[0]))
else:
    fichier1=sys.argv[1]
    fichier2=sys.argv[2]
    with open(fichier1,'r') as f1:
        s=f1.read()
    with open(fichier2,'w') as f2:
         f2.write(s)
                  
          
