import os


class Index:
    def __init__(self,dirPath):
        self.dirPath=dirPath
        self._index={}
        self.allFileNames=[]
        self.findFiles()
        self._createIndex()
      

    def findFiles(self):
        for filename in os.listdir(self.dirPath):
            if filename.endswith(".txt"):
               self.allFileNames.append(filename)
        
        
    def _createIndex(self):
        for filename in self.allFileNames:
            filepath=self.dirPath+"/"+filename
            with open(filepath,'r') as f:
                s=f.read()
                mots=s.split()
                for mot in mots:
                    mot=mot.lower()
                    if mot not in self._index:
                        self._index[mot]=[filepath]
                    else:
                        if filepath not in self._index[mot]:
                            self._index[mot].append(filepath)
            
    def getIndex(self):
        return self._index

    def __str__(self):
        return "the index is {}".format(self._index)

