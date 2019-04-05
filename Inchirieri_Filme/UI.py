'''
Created on Nov 12, 2018

@author: ana_m
'''
from Repo import FilmeRepo,ClientiRepo , InchirieriRepo
from Entities import Client,Film
from Service import ServiceClient,ServiceFilme,ServiceInchirieri
from Validators import Validator, ValidatorException
from FileRepo import FilmeFileRepo,ClientiFileRepo,InchirieriFileRepo

class Console:
    def __init__(self,srvc,srvf,srvi):
        self.__srvc = srvc
        self.__srvf = srvf
        self.__srvi = srvi

    def start(self):
        print("Apasati tasta 1 pentru a adauga un element. ")
        print("Apasati tasta 2 pentru a sterge un element. ")
        print("Apasati tasta 3 pentru a modifica un element. ")
        print("Apasati tasta 4 pentru a afisa lista de clienti, filme sau inchirieri. ")
        print("Apasati tasta 5 pentru cautari. ")
        print("Apasati tasta 6 pentru a sorta lista de inchirieri. ")
        print("Apasati tasta 7 pentru a afisa primele 3 cele mai inchiriate filme")
        print("Apasati tasta 8 pentru a afisa primii 30% clienti cu cele mai multe inchirieri")
        print("Apasati tasta 9 pentru a afisa lista clientilor ordonati dupa numarul de inchirieri si care au mai mult de 3 inchirieri")
        print("Apasati tasta x pentru a iesi din aplicatie.")
   
    def adaugaFilm(self):
        id = input("Scrieti id-ul filmului: ")
        titlu=input("Scrieti titlul filmului: ")
        descriere=input("Scrieti descrierea filmului: ")
        gen=input("Scrieti genul filmului: ")
        self.__srvf.createFilm(id,titlu,descriere,gen)
        

    def adaugaClient(self):
        id = input("Scrieti id-ul clientului: ")
        nume=input("Scrieti numele clientului: ")
        prenume=input("Scrieti prenumele clientului: ")
        CNP=input("Scrieti CNP-ul clientului: ")
        self.__srvc.createClient(id,nume,prenume,CNP)
        
    def adaugaInchiriere(self):
        idFilm = input("Scrieti id-ul filmului: ")
        idClient = input("Scrieti id-ul clientului: ")
        titluFilm = input("Scrieti titlul filmului: ")
        numeClient = input ("Scrieti numele clientului: ")
        prenumeClient = input("Scrieti prenumele clientului: ")
        self.__srvi.createInchiriere(idFilm,idClient,titluFilm,numeClient,prenumeClient,False)
        
    def stergeFilm(self,titlu):
        a = self.__srvi.getAllInchirieri()
        ok = 1
        for el in a :
            if el.getTitlu() == titlu:
                print("Filmul nu poate fi sters deorece este inchiriat")
                ok=0
                break
        if ok == 1:
            self.__srvf.stergeTitlu(titlu)
                       
    def stergeClient(self,nume,prenume):
        a = self.__srvi.getAllInchirieri()
        ok = 1
        for el in a :
            if el.getNume() == nume and el.getPrenume() == prenume:
                print("Clientul nu poate fi sters deorece are filme inchiriate")
                ok = 0
                break
        if ok ==1:
            self.__srvc.stergeNume(nume,prenume)
   
    def subMeniu_1(self):
        print("Apasati tasta f pentru a adauga un film in lista de filme")
        print("Apasati tasta c pentru a adauga un client in lista de clienti")
        print("Apasati tasta i pentru a adauga o inchiriere in lista de inchirieri")
        print("Apasati tasta m pentru intoarcerea la meniul principal")
        alegere=input()
        try:
            while alegere!='m':
                if alegere!='f' and alegere!='c' and alegere!='m' and alegere!='i':
                    raise ValueError
                if alegere=='f':
                    try:
                        self.adaugaFilm()
                    except ValidatorException as e:
                        print(e)   
                elif alegere=='c':
                    try:
                        self.adaugaClient()
                    except ValidatorException as e:
                        print(e)
                elif alegere == 'i':
                    self.adaugaInchiriere()
                print("Apasati tasta f pentru a adauga un film in lista de filme")
                print("Apasati tasta c pentru a adauga un client in lista de clienti")
                print("Apasati tasta i pentru a adauga o inchiriere in lista de inchirieri")
                print("Apasati tasta m pentru intoarcerea la meniul principal")
                alegere=input()
        except ValueError as ex:
            print("Optiunea introdusa nu exista. Incercati din nou.")
            self.subMeniu_1()
    
    def subMeniu_2(self):
        print("Apasati tasta f pentru a sterge un film")
        print("Apasati tasta c pentru a sterge un client")
        print("Apasati tasta m pentru intoarcerea la meniul principal")
        alegere=input()
        try:
            if alegere!='f' and alegere!='m' and alegere!='c':
                raise ValueError()
            if alegere=='f':
                titlu=input("Scrieti titlul filmului: ")
                self.stergeFilm(titlu)
            elif alegere=='c':
                nume=input("Scrieti numele clientului: ")
                prenume=input("Scrieti prenumele clientului: ")
                self.stergeClient(nume,prenume)
            if alegere != 'm':
                self.subMeniu_2()
        except ValueError as ex:
            print("Optiunea aleasa nu exista. Incercati din nou")
            self.subMeniu_2()
    
    def subMeniu_3(self):
        print("Apasati tasta f pentru a modifica un film")
        print("Apasati tasta c pentru a modifica un client")
        print("Apasati tasta m pentru a va intoarce la meniul principal")
        alegere = input()
        try:
            while alegere!='m':
                if alegere!='f' and alegere!='c' and alegere!='m':
                    raise ValueError
                if alegere == 'f':
                    titlu = input("Scrieti titlul filmului pe care vreti sa il modificati: ")
                    titluNou = input("Scrieti noul titlu al filmului: ")
                    descriere = input("Scrieti noua descriere a filmului: ")
                    gen = input("Scrieti noul gen al fimului:")
                    self.__srvf.modificaFilm(titlu,titluNou,descriere,gen)
                elif alegere == 'c':
                    nume = input("Scrieti numele clientului pe care vreti sa il modificati: ")
                    prenume = input("Scrieti prenumele clientului pe care vreti sa-l modificati: ")
                    numeNou = input("Scrieti noul nume al clientului: ")
                    prenumeNou = input("Scrieti noul prenume al clientului: ")
                    CNP = input("Scrieti noul CNP al clientului: ")
                    self.__srvc.modificaClient(nume,prenume,numeNou,prenumeNou,CNP)
                print("Apasati tasta f pentru a modifica un film")
                print("Apasati tasta c pentru a modifica un client")
                print("Apasati tasta m pentru a va intoarce la meniul principal")
                alegere = input()
        except ValueError as ex:
            print("Optiunea aleasa nu exista. Incercati din nou")
            self.subMeniu_3()
        
    def subMeniu_4(self):
        print("Apasati tasta f pentru a afisa lista de filme. ")
        print("Apasati tasta c pentru a afisa lista de clienti. ")
        print("Apasati tasta i pentru a afisa lista de inchirireri")
        print("Apasati tasta m pentru intoarcerea la meniul principal")
        alegere=input()
        try:
            while alegere!='m':
                if alegere!='f' and alegere!='c' and alegere!='m' and alegere!='i':
                    raise ValueError
                if alegere=='f':
                    a =self.__srvf.getAllFilm()
                    for el in a:
                        print(el)
                elif alegere=='c':
                    a = self.__srvc.getAllClient()
                    for el in a:
                        print(el)
                elif alegere == 'i':
                    a = self.__srvi.getAllInchirieri()
                    for el in a:
                        print(el)
                print("Apasati tasta f pentru a print lista de filme. ")
                print("Apasati tasta c pentru a afisa lista de clienti. ")
                print("Apasati tasta i pentru a afisa lista de inchirireri")
                print("Apasati tasta m pentru intoarcerea la meniul principal")   
                alegere=input()
        except ValueError as ex:
            print("Optiunea introdusa nu exista.Incercati din nou. ")
            self.subMeniu_4()

    def subMeniu_5(self):
        print("Apasati tasta f pentru a cauta un film dupa titlu. ")
        print("Apasati tasta c pentru a cauta un client dupa nume. ")
        print("Apasati tasta m pentru intoarcerea la meniul principal. ")
        alegere=input()
        try:
            while alegere!='m':
                if alegere!='f' and alegere!='c' and alegere!='m':
                    raise ValueError
                if alegere=='f':
                    titlu=input("Scrieti titlul filmului pe care vreti sa il cautati: ")
                    print(self.__srvf.findTitlu(titlu))
                elif alegere=='c':
                    nume=input("Scrieti numele clientului pe care vreti sa il cautati: ")
                    prenume=input("Scrieti prenumele clientului pe care vreti sa il cautati: ")
                    print(self.__srvc.findNume(nume,prenume))
                print("Apasati tasta f pentru a cauta un film dupa titlu. ")
                print("Apasati tasta c pentru a cauta un client dupa nume. ")
                print("Apasati tasta m pentru intoarcerea la meniul principal. ")
                alegere=input()  
        except ValueError as ex:
            print("Optiunea introdusa nu exista. Incercati din nou.")
            self.subMeniu_5()
        
    def subMeniu_6(self):
        print("Apasati tasta a pentru a sorta dupa numele clientului. ")
        print("Apasati tasta b pentru a sorta dupa numarul de inchirieri. ")
        print("Apasati tasta m pentru intoarcerea la meniul principal. ")
        alegere = input()
        try:
            while alegere!= 'm':
                if alegere!='a' and alegere!='b' and alegere!='m':
                    raise ValueError()
                if alegere == 'a':
                    a = self.__srvi.sortAfterName()
                    for el in a:
                        print(el)
                elif alegere == 'b':
                    a= self.__srvi.sortAfterNrInchirieri()
                    for el in a:
                        print(el)
                print("Apasati tasta a pentru a sorta dupa numele clientului. ")
                print("Apasati tasta b pentru a sorta dupa numarul de inchirieri. ")
                print("Apasati tasta m pentru intoarcerea la meniul principal. ")
                alegere = input()
        except ValueError as ex:
            print("Optiunea introdusa nu exista. Incercati din nou.")
            self.subMeniu_6()
    
    def subMeniu_7(self):
        a = self.__srvi.celeMaiInchiriateFilme()
        for el in a:
            print(el)
            
    def subMeniu_8(self):
        a = self.__srvi.topClienti()
        for el in a :
            print(el)
    
    def subMeniu_9(self):
        a = self.__srvi.ClientiOrdDescCuInchirieriMaiMariCa3()
        for el in a :
            print(el)
 
    def Meniu(self):
        self.start()
        alegere=input()
        optiuni=['1','2','3','4','5','6','7','8','9','x']  
        try:
                ok=0
                for a in optiuni:
                    if alegere==a:
                        ok=1
                if ok==0:
                    raise ValueError
                if alegere=='1':
                    self.subMeniu_1()
                elif alegere=='2':
                    self.subMeniu_2()
                elif alegere=='3':
                    self.subMeniu_3()
                elif alegere=='4':
                    self.subMeniu_4()
                elif alegere=='5':
                    self.subMeniu_5()
                elif alegere =='6':
                    self.subMeniu_6()
                elif alegere == '7':
                    self.subMeniu_7()
                elif alegere =='8':
                    self.subMeniu_8()
                elif alegere == '9':
                    self.subMeniu_9()
                if alegere=='x':
                    print("Bye bye!!!")
                else:
                    self.Meniu()
        except ValueError as ex:
            print(" ")
            print("Optiunea introdusa nu exista. Incercati din nou.",end='\n\n')
            self.Meniu()
     
           
def main():
    #repClient = ClientiRepo()
    #repFilme = FilmeRepo()
    #repInchiriere = InchirieriRepo()
    repClient = ClientiFileRepo("client.txt")
    repFilme = FilmeFileRepo("film.txt")
    repInchiriere = InchirieriFileRepo("inchiriere.txt")
    val = Validator()
    srvc = ServiceClient(repClient,val)
    srvf = ServiceFilme(repFilme,val)
    srvi = ServiceInchirieri(srvf,srvc,repInchiriere,val)
    #srvc.createClient("Asmarandei","Ana-Maria",29901292736)
    #srvc.createClient("Iloaia","Andreea",2991092893756)
    #srvc.createClient("Ceparu","Stefan",21992836644)
    #srvf.createFilm("Sabrina","Interzis sub 16 ani","Horror,SF")
    #srvf.createFilm("West World","Interzis sub 18 ani","Drama,SF")
    #srvf.createFilm("Friends","About Friends","Comedie")
    #srvi.createInchiriere(1, 1,"Sabrina", "Asmarandei","Ana-Maria", False)
    #srvi.returnareFilm("Asmarandei","Ana-Maria","Sabrina")
    #srvi.createInchiriere(3,1,"Friends","Asmarandei","Ana-Maria",False)
    #srvi.createInchiriere(3,2,"Friends","Iloaia","Andreea",False)
    #srvi.createInchiriere(3,4,"Friends","Ceparu","Stefan",False)
     
    console=Console(srvc,srvf,srvi)
    console.Meniu()
    
    
main()
