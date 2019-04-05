'''
Created on Nov 16, 2018

@author: ana_m
'''
from Entities import Client,Film,Inchirieri,NrInchirieriClienti,NrInchirieriFilme
from Validators import Validator,ValidatorException
from Repo import ClientiRepo,FilmeRepo, InchirieriRepo
from Sortare1 import my_sorted1
import random

class ServiceClient():
    def __init__(self,repClient,val):
        """
        Initiaza service-ul
        rep- repository - stocheaza clientii
        val - validator - valideaza clientii
        """
        self.__repClient = repClient
        self.__val = val
        
    def createClient(self,id,nume,prenume,CNP):
        """
        Stocheaza clientul
        nume, prenume , CNP - siruri de caractere
        returneaza clientul
        raise RepositoryExeption - daca clientul exista deja
        raise ValidationException - daca datele date sunt invalide
        """
        #creaza obiectul student
        cl=Client(id,nume,prenume,CNP)
        #valideaza datele introduse de utilizator
        self.__val.validateClient(cl)
        self.__val.validateRepoClienti(cl,self.getAllClient())
        #stocheaza student folosind repository
        self.__repClient.store(cl)
        return cl
    
    def getAllClient(self):
        """
        Returneaza lista de clienti din repository
        """
        return self.__repClient.getAll()
    
    def findNume(self,nume,prenume):
        """
        Parametri: nume - numele dupa care se cauta clientul
                   prenumele - prenumele dupa care se cauta clientul
        Afiseaza clientul cautat
        """
        cl=self.__repClient.find(nume,prenume)
        return cl
    
    def stergeNume(self,nume,prenume):
        """
        Parametri: nume - numele dupa care se cauta clientul
                   prenumele - prenumele dupa care se cauta clientul
        Sterge clientul cautat dupa nume
        """
        cl=self.__repClient.sterge(nume,prenume)
        return cl
        
    def modificaClient(self,numeVechi,prenumeVechi,nume,prenume,CNP):
        """
        Parametri : numeVechi - numele vechi al clientului
                    prenumeVechi - prenumele vechi al clientului
                    nume - numele nou al clientului
                    prenumele - prenumele nou al clientului
                    CNP - Cnp-ul noi al clientului
        Modifica clientul cautat dupa nume
        """
        cl = self.__repClient.modifica(numeVechi,prenumeVechi,nume,prenume,CNP)
        return cl
    
    def randomClient(self,n):
        """
        Functia primeste ca parametru n - un numar ce semnifica numarul de clienti ce trebuie generat
        Functia creaza aleatoriu numele,prenumele si CNP-ul pentru n clienti si ii stocheaza in repository 
        """
        letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cons="bcdfghjklmnpqrstvwxyz"
        voc="aeiou"
        numbers="1234567890"
        for i in range(int(n)):
            id = len(self.__repClient.getAll())
            x=random.randint(4,50)
            nume=""
            for j in range(x):
                if j==0:
                    l= random.choice(letters)
                elif j%2==1:
                    l= random.choice(cons)
                elif j%2==0:
                    l= random.choice(voc) 
                nume+=l
            prenume=""
            for j in range(x):
                if j==0:
                    l= random.choice(letters)
                elif j%2==0:
                    l= random.choice(cons)
                elif j%2==1:
                    l= random.choice(voc)
                prenume+=l
            CNP=""
            for j in range(13):
                l= random.choice(numbers)
                CNP+=l
            self.createClient(id,nume,prenume,CNP)
                      
    
def testServiceClient():
    repClient = ClientiRepo()
    val = Validator()
    srv = ServiceClient(repClient,val)
    cl1 = srv.createClient(1,"Asmarandei","Ana-Maria",29901292736)
    srv.createClient(2,"Iloaia","Andreea",2991092893756)
    srv.createClient(3,"Joanta","Tudor",2919837263723)
    srv.createClient(4,"Ceparu","Stefan",21992836644)
    assert len(srv.getAllClient()) == 4
    assert srv.findNume("Asmarandei","Ana-Maria") == cl1
    cl2=srv.stergeNume("Asmarandei","Ana-Maria")
    assert cl2 == cl1
    cl3 = srv.modificaClient("Ceparu","Stefan","Cep","Ste",2999019273273)
    cl4= Client(4,"Cep","Ste",2999019273273)
    assert cl3 == cl4
    
testServiceClient()

class ServiceFilme():
    def __init__(self,repFilm,val):
        self.__repFilm = repFilm
        self.__val = val
    
    def createFilm(self,id,titlu,descriere,gen):
        """
        Stocheaza filmul
        nume, prenume , CNP - siruri de caractere
        returneaza clientul
        raise RepositoryExeption - daca clientul exista deja
        raise ValidationException - daca datele date sunt invalide
        """
        #creaza obiectul student
        fl=Film(id,titlu,descriere,gen)
        #valideaza datele introduse de utilizator
        self.__val.validateFilm(fl)
        self.__val.validateRepoFilm(fl,self.getAllFilm())
        #stocheaza student folosind repository
        self.__repFilm.store(fl)
        return fl
    
    def getAllFilm(self):
        """
        Returneaza lista de filme din repository
        """
        return self.__repFilm.getAll()
    
    def findTitlu(self,titlu):
        """
        Parametri : titlu - titlul dupa care este cautat filmul
        Afiseaza clientul cautat
        """
        fl=self.__repFilm.find(titlu)
        return fl
    
    def stergeTitlu(self,titlu):
        """
        Parametri: titlu - titlul dupa care se cauta filmul
        Sterge filmul cu titlul dat in parametri
        """ 
        fl=self.__repFilm.sterge(titlu)
        return fl
    
    def modificaFilm(self,titluVechi,titlu,descriere,gen):
        fl = self.__repFilm.modifica(titluVechi,titlu,descriere,gen)
        return fl

def testServiceFilme():
    repFilm = FilmeRepo()
    val = Validator()
    srv = ServiceFilme(repFilm,val)
    srv.createFilm(1,"Sabrina","Interzis sub 16 ani","Horror,SF")
    fl2 = srv.createFilm(2,"West World","Interzis sub 18 ani","Drama,SF")
    srv.createFilm(3,"Friends","About Friends","Comedie")
    assert len(srv.getAllFilm()) == 3
    assert srv.findTitlu("West World") == fl2
    fl3 = srv.stergeTitlu("West World")
    assert fl2 == fl3
    assert len(srv.getAllFilm()) == 2
    fl4 = srv.modificaFilm("Friends","Doctors","jieuh","Comedie")
    fl5 = Film(4,"Doctors","jieuh","Comedie")
    assert fl4 == fl5

testServiceFilme()

def testRandomClient():
    repClient = ClientiRepo()
    val = Validator()
    srv=ServiceClient(repClient,val)
    srv.randomClient(3)
    assert len(srv.getAllClient()) == 3
    srv.randomClient(4)
    assert len(srv.getAllClient()) == 7
    srv.randomClient(10)
    assert len(srv.getAllClient()) == 17
    
testRandomClient()

class ServiceInchirieri():
    def __init__(self,repFilm,repClient,repInchirieri,val):
        self.__repFilm = repFilm
        self.__repClient = repClient
        self.__repInchirieri = repInchirieri
        self.__val = val
    
    def createInchiriere(self,idFilm,idClient,titluFilm,numeClient,prenumeClient,adus):
        """
        Creaza obiectul inchirirere si il salveaza in repInchiriere
        """
        # creaza obiectul inchiriere
        inchiriere=Inchirieri(idFilm,idClient,titluFilm,numeClient,prenumeClient,adus)
        # valideaza datele introduse de utilizator
        self.__val.validateInchiriere(inchiriere)
        #salveaza in lista inchirierea
        self.__repInchirieri.store(inchiriere)
        return inchiriere
    
    def getAllInchirieri(self):
        """
        Returneaza lista de inchirieri
        """
        return self.__repInchirieri.getAll()
    
    def returnareFilm(self,numeClient,prenumeClient,titluFilm):
        self.__repInchirieri.returnareFilm(numeClient,prenumeClient,titluFilm)
    
    def sortAfterName(self):
        """
        Sorteaza lista de inchirieri dupa numele clientilor
        Retuneaza lista sortata
        """
        a = self.__repInchirieri.getAll()
        a = my_sorted1(a , key = lambda Inchirieri : Inchirieri.getNume(), reverse = False)
        return a
    
    def sortAfterNrInchirieri(self):
        """
        Sorteaza lista ce contine numele, prenumele clientului si numarul de inchirieri dupa numarul de filme inchiriate.
        Returneaza lista sortata
        """
        
        dtos =self.__repInchirieri.getAll()
        nrFilme = {}
        
        for inchiriere in dtos:
            if inchiriere.getIdClient() in nrFilme:
                nrFilme[inchiriere.getIdClient()].inchiriereNoua()
            else:
                nrFilme[inchiriere.getIdClient()] = NrInchirieriClienti(inchiriere.getIdClient()
                                        ,inchiriere.getNume(),inchiriere.getPrenume())
        nrFilme = list(nrFilme.values())
        nrFilmesorted = my_sorted1(nrFilme , key = lambda NrInchirieriClienti : NrInchirieriClienti.getNumarDeInchirieri() ,
                                reverse = True)
        return nrFilmesorted
    
    def celeMaiInchiriateFilme(self):
        """
        Creaza lista celor mai inchiriate filme , si o sorteaza descrescator. 
        Returneaza lista primelor 3 cele mai inchiriate filme
        """
        dtos = self.__repInchirieri.getAll()
        nrFilme = {}
        
        for inchiriere in dtos:
            if inchiriere.getIdFilm() in nrFilme:
                nrFilme[inchiriere.getIdFilm()].inchiriereNoua()
            else:
                nrFilme[inchiriere.getIdFilm()] = NrInchirieriFilme(inchiriere.getIdFilm(),inchiriere.getTitlu())
        nrFilme = list(nrFilme.values())
        nrFilmeSorted = my_sorted1(nrFilme , key = lambda NrInchirieriFilme : NrInchirieriFilme.getNumarInchirieri(),
                               reverse = True)
        b = []
        if len(nrFilme)>3:
            for el in range(3):
                b.append(nrFilmeSorted(el))
        else:
            b=nrFilmeSorted
        return b 
    
    def topClienti(self):
        """
        Preia lista ce contine numele , prenumele si numarul de inchirieri sortata descrescator si retine primii 30%
        Returneaza lista ce contine primii 30% din clienti
        """
        a = self.sortAfterNrInchirieri()  
        b=[]
        c = int(len(a)*(3/10))
        for el in range(c):
            b.append(a[el])
        return b 
     
    def ClientiOrdDescCuInchirieriMaiMariCa3(self):
        """
        Preia lista ce contine numele ,prenumele si numarul de inchirieri sortara descrescator dupa numarul de inchirieri
        Elimina clientii a ce au mai putin de 3 inchirieri
        Returneaza lista cu proprietatile    
        """
        a =  self.sortAfterNrInchirieri()  
        b=[]
        for el in a:
            if int(el.getNumarDeInchirieri())>3:
                b.append(el)
        return b
        
def testServiceInchirieri():
    repClient = ClientiRepo()
    val = Validator()
    repFilm = FilmeRepo()
    repInchiriere = InchirieriRepo()
    srv = ServiceInchirieri(repFilm,repClient,repInchiriere,val)
    repInchiriere = InchirieriRepo()
    srv.createInchiriere(1,3,"Sabrina","Joanta","Tudor",False)
    srv.createInchiriere(1, 1,"Sabrina", "Asmarandei","Ana-Maria", False)
    assert len(srv.getAllInchirieri()) == 2        
    srv.returnareFilm("Asmarandei","Ana-Maria","Sabrina")
    srv.createInchiriere(3,1,"Friends","Asmarandei","Ana-Maria",False)
    srv.createInchiriere(3,2,"Friends","Iloaia","Andreea",False)
    srv.createInchiriere(3,4,"Friends","Ceparu","Stefan",False)
    
testServiceInchirieri()

def testClientiOrdDescCuInchirieriMaiMariCa3():
    repClient = ClientiRepo()
    val = Validator()
    repFilm = FilmeRepo()
    repInchiriere = InchirieriRepo()
    srv = ServiceInchirieri(repFilm,repClient,repInchiriere,val)
    srv.createInchiriere(1,3,"Sabrina","Joanta","Tudor",False)
    srv.createInchiriere(1, 1,"Sabrina", "Asmarandei","Ana-Maria", False)
    srv.createInchiriere(3,1,"Friends","Asmarandei","Ana-Maria",False)
    srv.createInchiriere(3,2,"Friends","Iloaia","Andreea",False)
    srv.createInchiriere(3,4,"Friends","Ceparu","Stefan",False)
    srv.createInchiriere(2,1,"West World","Asmaranadei","Ana-Maria",False)
    srv.createInchiriere(4,1,"hwafilewhf","Asmarandei","Ana-Maria",False)
    assert len(srv.ClientiOrdDescCuInchirieriMaiMariCa3()) == 1
    srv.createInchiriere(1,2,"Sabrina","Iloaia","Andreea",False)
    srv.createInchiriere(2,2,"West World","Iloaia","Andreea",False)
    srv.createInchiriere(4,2,"Fytdytd","Iloaia","Andreea",False)
    assert len(srv.ClientiOrdDescCuInchirieriMaiMariCa3()) == 2
    
testClientiOrdDescCuInchirieriMaiMariCa3()