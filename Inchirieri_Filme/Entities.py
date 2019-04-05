'''
Created on Nov 9, 2018

@author: ana_m
'''
class Client:
    def __init__(self,id,nume,prenume,CNP):
        self.__nume=nume
        self.__prenume=prenume
        self.__CNP=CNP
        self.__id=id

    def set_nume(self, value):
        """
        Seteaza numele.
        """
        self.__nume = value

    def set_prenume(self,value):
        """
        Seteaza prenumele.
        """
        self.__prenume=value
        
    def set_CNP(self,value):
        """
        Seteaza CNP-ul.
        """
        self.__CNP=value
           
    def __str__(self):
        return str(self.__id)+" "+self.__nume+" "+self.__prenume+" "+str(self.__CNP)
    
    def __repr__(self):
        return str(self)
        
    def setId(self,value):
        """
        Seteaza valoarea id-ului.
        """
        self.__id=value
    
    def getId(self):
        """
        Returneaza valoarea id-ului
        """
        return self.__id
    
    def getNume(self):
        """
        Returneaza numele.
        """
        return self.__nume
    
    def getPrenume(self):
        """
        Returneaza prenumele.
        """
        return self.__prenume
    
    def getCNP(self):
        """
        Returneaza CNP-ul.
        """
        return self.__CNP
    
    def __eq__(self,other):
        return self.__nume==other.__nume and self.__prenume==other.__prenume
    

def testCreazaClient():
    client=Client(1,"Titulescu","Miguel","2990901920390")
    assert client.getId()==1
    assert client.getNume()=="Titulescu"   
    assert client.getPrenume()=="Miguel"
    assert client.getCNP()=="2990901920390"
    
testCreazaClient()     

def testEqual():
    cl1=Client(1,"Asmarandei","Ana",299018291)
    cl2=Client(1,"Asmarandei","Ana",210937832)
    assert cl1==cl2
    
testEqual()

class Film:
    def __init__(self,id,titlu,descriere,gen):
        self.__id=id
        self.__titlu=titlu
        self.__descriere=descriere
        self.__gen=gen
        
    def __eq__(self,other):
        return self.__titlu==other.__titlu 
    
    def setTitlu(self, value):
        """
        Seteaza titlul
        """
        self.__titlu = value
        
    
    def setDescriere(self, value):
        """
        Seteaza descrierea
        """
        self.__descriere = value


    def setGen(self, value):
        """
        Seteaza genul.
        """
        self.__gen = value

     
    def setId(self,value):
        """
        Seteaza valoarea id-ului
        """
        self.__id=value
        
    def __str__(self):
        return str(self.__id)+" "+self.__titlu+" "+self.__descriere+" "+self.__gen
            
    def __repr__(self):
        return str(self)
            
    def getId(self):
        """
        Returneaza valoarea id-ului.
        """
        return self.__id
    
    
    def getTitlu(self):
        """
        Returneaza titlul.
        """
        return self.__titlu
    
    def getDescriere(self):
        """
        Returneaza descrierea.
        """
        return self.__descriere
    
    def getGen(self):
        """
        Returneaza genul.
        """
        return self.__gen
    
def testCreazaFilme():
    film=Film(1,"Sabrina","Interzis sub 16 ani","Horror,SF")
    assert film.getId()==1
    film.setId(1)
    assert film.getId()==1
    assert film.getTitlu()=="Sabrina"
    assert film.getDescriere()=="Interzis sub 16 ani"
    assert film.getGen()=="Horror,SF"
    
testCreazaFilme()

class Inchirieri():
    def __init__(self,idFilm,idClient,titluFilm,numeClient,prenumeClient,adus):
        self.__idFilm = idFilm
        self.__idClient = idClient
        self.__titluFilm = titluFilm
        self.__numeClient = numeClient
        self.__prenumeClient = prenumeClient
        self.__adus = adus
        
    def __str__(self):
        return str(self.__idFilm)+" "+str(self.__idClient)+" "+ self.__titluFilm+" "+self.__numeClient+" "+self.__prenumeClient
    
    def __repr__(self):
        return str(self)
    
    def getIdClient(self):
        """
        Returneaza id-ul clientului
        """
        return self.__idClient
    
    def getIdFilm(self):
        """
        Returneaza id-ul filmului
        """
        return self.__idFilm
    
    def getTitlu(self):
        """
        Returneza titlul filmului
        """
        return self.__titluFilm
    
    def getNume(self):
        """
        Returneaza numele clientului
        """
        return self.__numeClient
    
    def getPrenume(self):
        """
        Returneaza prenumele clientului
        """
        return self.__prenumeClient
    
    def setAdus(self,value):
        """
        Seteaza valoarea campului adus
        """
        self.__adus = value

    def getAdus(self):
        """
        Returneaza adus
        """
        return self.__adus 

def testCreazaInchiriere():
    film=Film(1,"Sabrina","Interzis sub 16 ani","Horror,SF")
    client=Client(1,"Titulescu","Miguel","2990901920390")
    film.setId(1)
    client.setId(2)
    inchiriere=Inchirieri(film.getId(),client.getId(),film.getTitlu(),client.getNume(),client.getPrenume(),False)
    assert inchiriere.getTitlu()=="Sabrina"
    assert inchiriere.getNume()=="Titulescu"
    assert inchiriere.getPrenume()=="Miguel"
    assert inchiriere.getIdClient()==2
    assert inchiriere.getIdFilm()==1
    assert inchiriere.getAdus() == False
    inchiriere.setAdus(True)
    assert inchiriere.getAdus() == True

    
testCreazaInchiriere()        

class NrInchirieriClienti():
    def __init__(self,idClient,numeClient,prenumeClient):
        self.__idClient = idClient
        self.__numeClient = numeClient
        self.__prenumeClient = prenumeClient
        self.__numarDeInchirieri = 1
        
    def inchiriereNoua(self):
        """
        Adauga 1 la numarDeInchirieri 
        """
        self.__numarDeInchirieri+=1
        
    def __str__(self):
        return str(
            self.__idClient)+" "+str(self.__numeClient)+" "+str(self.__prenumeClient)+" "+str(self.__numarDeInchirieri)
    
    def __repr__(self):
        return str(self)
    
    def getNumarDeInchirieri(self):
        """
        Returneaza numarDeInchirieri
        """
        return self.__numarDeInchirieri
    
    def getNume(self):
        return self.__numeClient
    
    def getPrenume(self):
        return self.__prenumeClient
    
def testNrInchirieriClienti():
    in1 = NrInchirieriClienti(1,"Asmarandei","Ana-Maria")
    in2 = NrInchirieriClienti(2,"Iloaia","Andreea")
    assert in1.getNumarDeInchirieri() == 1
    in2.inchiriereNoua()
    assert in2.getNumarDeInchirieri() == 2
    assert in1.getPrenume()=="Ana-Maria"
    assert in2.getNume()=="Iloaia"
    
testNrInchirieriClienti()    
        
class NrInchirieriFilme():
    def __init__(self, idFilm, titluFilm):
        self.__idFilm = idFilm
        self.__titluFilm = titluFilm
        self.__numarInchirieri = 1
        
    def inchiriereNoua(self):
        """
        Adauga 1 la numarInchirieri 
        """
        self.__numarInchirieri+=1
        
    def __str__(self): 
        return str(self.__idFilm)+" "+str(self.__titluFilm)+" "+str(self.__numarInchirieri)
    
    def __repr__(self):
        return str(self)
    
    def getNumarInchirieri(self):
        """
        Returneaza numarInchirieri
        """
        return self.__numarInchirieri

def testNrInchirieriFilme():
    in1 = NrInchirieriFilme(1,"Sabrina")
    in2 = NrInchirieriFilme(2,"Friends")
    assert in1.getNumarInchirieri() == 1
    in2.inchiriereNoua()
    assert in2.getNumarInchirieri() == 2
    
testNrInchirieriFilme()