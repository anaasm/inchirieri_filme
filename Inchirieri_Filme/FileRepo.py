'''
Created on Dec 3, 2018

@author: ana_m
'''
from Repo import ClientiRepo,FilmeRepo,InchirieriRepo
from Entities import Client,Inchirieri,Film

class ClientiFileRepo():
    """
    Responsabil cu incarcarea studentilor dintr-un/intr-un fisier text
    Include diferite versiuni de :
          citire din fisier
          accesarea atributelor de baza (campuri, metode)
    """
    def __init__(self,fileName):
        self.__fName = fileName
        
    def createClientFromLine(self,line):
        """
        Proceseaza o linie din fisier si creaza un client 
        Returneaza un client
        """
        fields = line.split(";")
        cl = Client(fields[0],fields[1],fields[2],fields[3])
        return cl
    
    def __appendToFile(self,cl,fileName):
        """
        Adauga o noua linie in fisier ce reprezinta un nou client 
        """
        f = open(fileName,"a")
        line = str(cl.getId())+";"+str(cl.getNume())+";"+str(cl.getPrenume())+";"+str(cl.getCNP())
        f.write("\n")
        f.write(line)
        f.close()
        
    
    def store(self,cl):
        """
        Parametri : cl - client
        Scrie in fisier noul client
        Ridica ValueError cand clientul exista deja in fisier
        """
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue 
                else:
                    cl1 = self.createClientFromLine(line)
                if cl1 == cl:
                    raise ValueError()
        f.close()
        self.__appendToFile(cl,self.__fName)
    
    def getAll(self):
        """
        Returneaza o lista ce contine toti clietii din fisier
        """
        all = []
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    cl = self.createClientFromLine(line)
                    all.append(cl)
        return all
    
    def find(self,nume,prenume):
        """
        Cauta un client dupa nume si prenume
        Retureaza cientul gasit
        """
        found = False
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    cl = self.createClientFromLine(line)
                    if cl.getNume() == nume and cl.getPrenume() == prenume:
                        found = True
                        return cl 
        f.close()
        if found == False:
            print("Clientul cautat nu exista")
            
    def transfer(self,fName1,fName2):
        """
        Transfera datele din fName2 in fName1
        """
        f1 = open(fName1,"w")
        with open(fName2,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    cl = self.createClientFromLine(line)
                    line = str(cl.getId())+";"+str(cl.getNume())+";"+str(cl.getPrenume())+";"+str(cl.getCNP())
                    f1.write(line)
        f1.close
        f.close
    
    def sterge(self,nume,prenume):
        """
        Cauta un client dupa nume si prenume si il sterge
        """
        ftemp = open("Temporar","w")
        ftemp.close()
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    cl = self.createClientFromLine(line)
                    if cl.getNume() == nume and cl.getPrenume() == prenume:
                        continue
                    else:
                        self.__appendToFile(cl,"Temporar")
        self.transfer(self.__fName, "Temporar")
     
    def modifica(self,nume,prenume,numeNou,prenumeNou,CNPnou):
        """
        Cauta un client dupa nume si prenume si il modifica
        """
        ftemp = open("Temporar","w")
        ftemp.close()
        ftemp = open("Temporar","a")
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    cl = self.createClientFromLine(line)
                    if cl.getNume() == nume and cl.getPrenume() == prenume:
                        cl.set_nume(numeNou)
                        cl.set_prenume(prenumeNou)
                        cl.set_CNP(CNPnou)
                    self.__appendToFile(cl, "Temporar")
        self.transfer(self.__fName,"Temporar")
                    
             
def clearFileContent(fileName):
    """
      Clear the content of the file
      Post: the given file exist and is empty
    """
    f = open(fileName, "w")
    f.close()
     
def testRepoClienti():
    fName = "Test"
    clearFileContent(fName)
    repo = ClientiFileRepo(fName)
    assert len(repo.getAll())==0
    repo.store(Client(1,"Asmarandei","Ana","299878759374"))
    repo.store(Client(2,"Iloaia","Andreea","9826491624"))
    assert len(repo.getAll())==2
    assert repo.find("Asmarandei","Ana") == Client(1,"Asmarandei","Ana","299878759374")
    repo.sterge("Asmarandei","Ana")
    assert len(repo.getAll())==1
    repo.modifica("Iloaia", "Andreea", "Iloai", "Andre", "2891269283273")
    assert repo.find("Iloai", "Andre") == Client(2,"Iloai","Andre","2998765432")
    
testRepoClienti()
    

class FilmeFileRepo():
    def __init__(self,fName):
        self.__fName = fName
        
    def createFilmFromLine(self,line):
        """
        Proceseaza o linie din fisier si creaza un film
        Returneaza un film
        """
        fields = line.split(";")
        fl = Film(fields[0],fields[1],fields[2],fields[3])
        return fl
    
    def __appendToFile(self,fl,fName):
        """
        Adauga o noua linie in fisier ce reprezinta un nou film
        """
        f = open(fName,"a")
        line = str(fl.getId())+";"+str(fl.getTitlu())+";"+str(fl.getDescriere())+";"+str(fl.getGen())
        f.write("\n")
        f.write(line)
        f.close()
        
    def store(self,fl):
        """
        Parametri : fl - film
        Scrie in fisier noul film
        """
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    fl1 = self.createFilmFromLine(line)
                    if fl1.getTitlu() == fl.getTitlu():
                        raise ValueError() 
        f.close()               
        self.__appendToFile(fl,self.__fName)
        
    def __loadFromFile(self):
        """
        Incarca clienti din fisier
        Proceseaza linie cu linie
        """
        f = open(self.__fName) 
        for line in f:
            if line.strip()=="":
                continue
            fl  = self.createFilmFromLine(line)
            #importa metoda de baza din ClientiRepo
            FilmeRepo.store(self, fl)
        f.close
        
    def getAll(self):
        """
        Returneaza lista de filme.
        """
        all = []
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    fl = self.createFilmFromLine(line)
                    all.append(fl)
        return all
    
    def find(self,titlu):
        """
        Gaseste un film dupa titlu
        Returneaza filmul gasit
        """
        found = False
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    fl = self.createFilmFromLine(line)
                    if fl.getTitlu()==titlu:
                        found = True
                        return fl
        f.close()
        if found == False:
            print("Filmul nu exista in lista")
            
    def transfer(self,fName1,fName2):
        """
        Transfera datele din fName2 in fName1
        """
        f1 = open(fName1,"w")
        with open(fName2,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    fl = self.createFilmFromLine(line)
                    line = str(fl.getId())+";"+str(fl.getTitlu())+";"+str(fl.getDescriere())+";"+str(fl.getGen())
                    f1.write(line)
        f1.close
        f.close
        
    def sterge(self,titlu):
        """
        Cauta un film dupa titlu si il sterge daca exita in lista
        """
        ftemp = open("Temporar","w")
        ftemp.close()
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    fl = self.createFilmFromLine(line)
                    if fl.getTitlu()==titlu:
                        continue
                    else:
                        self.__appendToFile(fl, "Temporar")
        self.transfer(self.__fName, "Temporar")           
        
    def modifica(self,titlu,titluNou,descriereNoua,genNou):
        """
        Cauta un film dupa titlu si in modifica     
        """
        ftemp = open("Temporar","w")
        ftemp.close()
        with open(self.__fName,"r") as f:
            for line in f :
                if line == "\n":
                    continue
                else:
                    fl = self.createFilmFromLine(line)
                    if fl.getTitlu() == titlu:
                        fl.setTitlu(titluNou)
                        fl.setDescriere(descriereNoua)
                        fl.setGen(genNou)
                    self.__appendToFile(fl, "Temporar")
        self.transfer(self.__fName, "Temporar")
                    
        
def testFilmeRepo():
    fName = "test.txt"
    clearFileContent(fName)
    repo = FilmeFileRepo(fName)
    assert len(repo.getAll())==0
    repo.store(Film(1,"Sabrina","Horror","SF"))
    assert len(repo.getAll())==1
    repo.store(Film(2,"West World","Interzis","Drama"))
    assert repo.find("Sabrina") == Film(1,"Sabrina","Horror","SF")
    assert len(repo.getAll())==2
    repo.sterge("Sabrina")
    assert len(repo.getAll())==1
    repo.modifica("West World","Friend","About friends","Comedy")
    assert repo.find("Friend") == Film(2,"Friend","About friends","Comedy")
    
testFilmeRepo()
    
class InchirieriFileRepo():
    def __init__(self,fName):
        self.__fName = fName
        
    def createInchiriereFromLine(self,line):
        """
        Proceseaza o linie din fisier si creaza o inchiriere
        Returneaza o inchiriere
        """
        fields = line.split(";")
        inc = Inchirieri(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5])
        return inc
    
    def store(self,inc):
        """
        Parametri : inc - inchiriere
        Scrie in fisier noua inchiriere
        """
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    inchiriere = self.createInchiriereFromLine(line)
                    if inchiriere.getAdus()==False and inchiriere.getTitlu()==inc.getTitlu():
                        raise ValueError()
        f.close()
        self.__appendToFile(inc)
        
    
    def __appendToFile(self,inc):
        """
        Adauga o noua linie in fisier ce reprezinta un nou film
        """
        f = open(self.__fName,"a")
        line = str(inc.getIdFilm())+";"+str(inc.getIdClient())+";"+str(inc.getTitlu())+";"+str(inc.getNume())+";"+str(inc.getPrenume())+";"+str(inc.getAdus())
        f.write("\n")
        f.write(line)
        f.close()
        
    def getAll(self):
        """
        Returneaza lista tuturor inchirierilor
        """
        all = []
        with open(self.__fName,"r") as f:
            for line in f:
                if line == "\n":
                    continue
                else:
                    inc = self.createInchiriereFromLine(line)
                    all.append(inc)
        return all
        
def testInchirieriRepo():
    fName = "test.txt"
    clearFileContent(fName)
    repo = InchirieriFileRepo(fName)
    assert len(repo.getAll()) == 0
    repo.store(Inchirieri("1","1","Sabrina","Asmarandei","Ana",False))
    assert len(repo.getAll()) == 1
    repo.store(Inchirieri("2","1","West World","Iloaia","Andreea",False))
    assert len(repo.getAll()) == 2
    
testInchirieriRepo()