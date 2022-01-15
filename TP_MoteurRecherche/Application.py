import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Index import *

class Application:
    def __init__(self,root):
        self.varKeyword=StringVar()
        self.root=root
        self.frameSearch=ttk.Frame(root,padding=(50,50))
        self.frameSearch.grid(row=0,column=0,sticky=(N,E,W,S))
        self.frameResult=ttk.Labelframe(root,padding=(10,10),text="Resultats :")
        self.frameResult.grid(row=1,column=0,sticky=(N,E,W,S))
        self.labelKeyword=ttk.Label(self.frameSearch,text="Mot-cle")
        self.entryKeyword=ttk.Entry(self.frameSearch, width=20,textvariable=self.varKeyword)
        self.buttonSearch=ttk.Button(self.frameSearch,text="Rechercher", command=self.searchKeyword)
        self.labelKeyword.grid(row=0,column=0)
        self.entryKeyword.grid(row=0,column=1)
        self.buttonSearch.grid(row=0,column=2)
    
    def searchKeyword(self):
        for widget in self.frameResult.winfo_children():
           widget.destroy()
        try:
          #on suppose qu'il existe dans le dossier courant un dossier nomme X
          path=os.getcwd()
          path=path+"/X"
          index1=Index(path) #on fait la recherche des mot-cle dans les fichiers texte du dossier X
          index=index1.getIndex()
          print(index)
          if index:
             mot_cle=self.varKeyword.get().lower()
             if mot_cle in index:
                for filepath in index[mot_cle]:
                  ttk.Label(self.frameResult,text="- "+filepath.replace(path+"/","")).grid(sticky=W)
             else:
                 ttk.Label(self.frameResult,text="Introuvable",foreground='red').grid()
          else:
            messagebox.showerror("Erreur","Absence de fichiers texte dans le repertoire")
        except OSError:
            print("Repertoire introuvable")
root=Tk()
root.title("Moteur de recherche")
Application(root)
root.mainloop()
