'''
Created on Nov 9, 2018

@author: ana_m
'''
from Entities import Client,Film,Inchirieri

class ClientiRepo():
     
    def __init__(self):
        self.__clientStore={}
    
    def store(self,Client):
        """
        Salveaza client
        """
        if Client in self.__clientStore.values():
            raise ValueError()
        self.__clientStore[len(self.__clientStore)+1] = Client

    def getAll(self):
        """
        Returneaza lista de clienti.
        """
        return list(self.__clientStore.values())
    
    def __eq__(self,other):
        return self.__nume==other.__nume and self.__prenume==other.__prenume
    
    def find(self,nume,prenume):
        """
        Cauta un client dupa nume.
        """
        ok=False
        if self.__clientStore!={}:
            for cl in self.__clientStore.values():
                if cl.getNume()==nume and cl.getPrenume()==prenume:
                    ok=True
                    return cl
        if ok==False:
            print("Clientul nu exista in lista")
    
    def modifica(self,numeVechi,prenumeVechi,nume,prenume,CNP):
        """
        Parametri : numeVechi - un sir de caractere ce semnifica numele de familie al clientului cautat
                    prenumeVechi - un sir de caractere de semnifica prenumele clientului cautat
                    nume- un sir de caractere in care vrem sa schimbam numele
                    prenume- un sir de caractere in care vrem sa schimbam prenumele
                    CNP- un sir de caractere format din numere in care vrem sa modificam CNP-ul
        Modifica datele memorate in lista ale unui client 
        """
        ok=0
        for cl in self.__clientStore.values():
            if cl.getNume()==numeVechi and cl.getPrenume()==prenumeVechi:
                client=cl
                ok=1
                break
        if ok==1:
            client.set_nume(nume)
            client.set_prenume(prenume)
            client.set_CNP(CNP)
            return client

    def sterge (self,nume,prenume):
        """
        Parametri: nume- numele clientului cautat
                   prenume - prenumele clientului cautat
        Sterge clientul cu numele si renumele dat din repository
        """
        ok=0
        for cl in self.__clientStore.values():
            if cl.getNume()==nume and cl.getPrenume()==prenume:
                client=cl
                del self.__clientStore[client.getId()]
                return client
                ok=1
                break
        if ok==1:
            print("Clientul cautat nu exista in lista ") 

def testStoreClient():
    client1=Client(1,"Titulescu","Miguel","2990901920390")
    rep=ClientiRepo()
    rep.store(client1)
    assert len(rep.getAll())==1
    client2=Client(2,"Asmarandei","Ana-Maria","2990902199921")
    rep.store(client2)
    assert len(rep.getAll())==2
    client3=rep.find("Asmarandei","Ana-Maria")
    assert client2==client3
    client4=rep.modifica("Asmarandei","Ana-Maria","Asmarandei","Ana","29993982378")
    assert client4==Client(2,"Asmarandei","Ana","29993982378")
    rep.sterge("Asmarandei","Ana")
    assert len(rep.getAll())==1
    
testStoreClient()
    
class FilmeRepo():
    def __init__(self):
        self.__filmeStore={}
    
    def store(self,Film):
        """
        Stocheaza filmele.
        """
        if Film in self.__filmeStore.values():
            raise ValueError("Film exista deja.")
        self.__filmeStore[Film.getId()] = Film
        
    def __eq__(self,other):
        return self.__titlu==other.__titlu

    def getAll(self):
        """
        Returneaza lista de filme.
        """
        return list(self.__filmeStore.values())
    
    def find(self,titlu):
        """
        Cauta filmul dupa titlu
        """
        ok=False
        if self.__filmeStore!={}:
            for Film in self.__filmeStore.values():
                if Film.getTitlu()==titlu:
                    ok=True
                    return Film
        if ok==False:
            print("Filmul nu exista in lista.")
    
    def modifica (self,titluVechi,titlu,descriere,gen):
        """
        Parametri : titluVechi - titlul dupa care se cauta filmul
                    titlu - titlul cu care vrem sa inlocuim titlul vechi
                    descriere - descrierea cu care vrem sa inlocuim descrierea veche
                    gen- genul cu care vrem sa inlocuim genul vechi
        Modifica clientul dat ca parametru 
        """
        ok=0
        for fl in self.__filmeStore.values():
            if fl.getTitlu()==titluVechi:
                film=fl
                ok=1
                break
        if ok==1:
            film.setTitlu(titlu)
            film.setDescriere(descriere)
            film.setGen(gen)
            return film
    
    def sterge(self,titlu):
        """
        Parametri titlu - titlul dupa care se cauta filmul
        Sterge filmul cu titlul dat in parametri
        """
        ok=0
        for fl in self.__filmeStore.values():
            if fl.getTitlu()==titlu:
                film=fl
                del self.__filmeStore[film.getId()]
                return film
                ok=1
                break
        if ok==0:
            raise ValueError("Filmul nu exista in lista. ")
    
def testStoreFilm():
    film1=Film(1,"Sabrina","Interzis sub 16 ani","Horror,SF")
    rep=FilmeRepo()
    rep.store(film1)
    assert len(rep.getAll())==1
    film2=Film(2,"West World","Interzis sub 18 ani","Drama")
    rep.store(film2)
    assert len(rep.getAll())==2
    film3=rep.find("Sabrina")
    assert film3==film1
    rep.sterge("Sabrina")
    assert len(rep.getAll())==1
    film4=rep.modifica("West World","Elena","aywdga","wauegy")
    film5=Film(3,"Elena","aywdga","wauegy")
    assert film4==film5
    
testStoreFilm()

class InchirieriRepo():
    
    def __init__(self):
        self.__inchirieriStore={}
        self.__repFilm = FilmeRepo()
        self.__repClient = ClientiRepo
        
    def store(self,Inchiriere):
        """
        Salveaza inchirierea
        """
        for inchiriere in self.__inchirieriStore.values():
            if inchiriere.getTitlu()==Inchiriere.getTitlu() and inchiriere.getAdus==False:
                raise ValueError("Filmul este inchiriat.")
        self.__inchirieriStore[len(self.getAll())] = Inchiriere
        
    def returnareFilm(self,numeClient,prenumeClient,titluFilm):
        """
        Schimba valoarea campului adus daca clientul returneaza filmul
        """
        for inchiriere in self.__inchirieriStore.values():
            if inchiriere.getNume()==numeClient and inchiriere.getPrenume()==prenumeClient and inchiriere.getTitlu()==titluFilm:
                inchiriere.setAdus(True)
            
    def getAll(self):
        """
        Returneaza lista de inchirieri
        """
        return list(self.__inchirieriStore.values())
    
    
    
def testStoreInchirieri():
    repFilm=FilmeRepo()
    repClient=ClientiRepo()
    film=Film(1,"Sabrina","Interzis sub 16 ani","Horror,SF")
    client=Client(1,"Titulescu","Miguel","2990901920390")
    repFilm.store(film)
    film.setId(1)
    client.setId(2)
    rep = InchirieriRepo()
    inchiriere = Inchirieri(film.getId(), client.getId(), film.getTitlu(), client.getNume(), client.getPrenume(), False)
    rep.store(inchiriere)
    assert len(rep.getAll()) == 1        
    rep.returnareFilm("Titulescu","Miguel","Sabrina")
    assert inchiriere.getAdus()==True
    inchiriere1 = Inchirieri(2,3,"Sabrina","Asmarandei","Ana-Maria",False)
    rep.store(inchiriere1)
    inchiriere2 = Inchirieri(3,3,"Friends","Asmarandei","Ana-Maria",False)
    rep.store(inchiriere2)
            
testStoreInchirieri()
