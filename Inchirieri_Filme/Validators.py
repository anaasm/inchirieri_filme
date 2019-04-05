'''
Created on Nov 15, 2018

@author: ana_m
'''
from Entities import Client,Film,Inchirieri
from Repo import ClientiRepo,FilmeRepo,InchirieriRepo
from FileRepo import ClientiFileRepo

class ValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        """
        Retuneaza erorile
        """
        return self.errors
    
class Validator():
    def validateClient(self,cl):
        """
        Salveaza erorile si ridica exceptii in caz ca ele exista
        """
        errors = []
        if (cl.getId() == ""):
            errors.append("Id cannot be empty")
        if (cl.getNume()==""):
            errors.append("Surname cannot be empty")
        if(cl.getPrenume()==""):
            errors.append("Name cannot be empty")
        if(cl.getCNP()==""):
            errors.append("CNP cannot be empty")
        if len(errors)>0:
            raise ValidatorException(errors)
    
    def validateFilm(self,fl):
        """
        Salveaza erorile si ridica exceptii in caz ca ele exista
        """
        errors=[]
        if fl.getId()=="":
            errors.append("Id cannot be empty.")
        if fl.getTitlu()=="":
            errors.append("Title cannot be empty.")
        if fl.getDescriere()=="":
            errors.append("Description cannot be empty.")
        if fl.getGen()=="":
            errors.append("Gen cannot be empty.")
        if len(errors)>0:
            raise ValidatorException(errors)
        
    def validateInchiriere(self,inchiriere):
        """
        Salveaza erorile si ridica exceptii in caz ca ele exista
        """
        errors=[]
        if inchiriere.getIdFilm()=="":
            errors.append("Film id cannot be empty")
        if inchiriere.getIdClient()=="":
            errors.append("Client id cannot be empty")
        if inchiriere.getTitlu()=="":
            errors.append("Title cannot be empty")
        if inchiriere.getNume()=="":
            errors.append("Surname cannot be empty")
        if inchiriere.getPrenume()=="":
            errors.append("Name cannot be empty")
        if len(errors)>0:
            raise ValidatorException(errors)
        
    def validateRepoFilm(self,fl,a):
        """
        Salveaza erorile si ridica exceptii in caz ca ele exista
        """
        errors = []
        for el in a:
            if el.getTitlu()==fl.getTitlu() or el.getId()==fl.getId():
                errors.append("Film existent in lista")
        if len(errors)>0:
            raise ValidatorException(errors)
        
    def validateRepoClienti(self,cl,a):
        """
        Salveaza erorile si ridica exceptii in caz ca ele exista
        """
        errors = []
        for el in a:
            if el.getNume()==cl.getNume() and el.getPrenume()==cl.getPrenume() or el.getId()==cl.getId():
                errors.append("Client existent in lista")
        if len(errors)>0:
            raise ValidatorException(errors)
      
def testClientValidator():
    validator = Validator()
    
    cl = Client("","","","")
    try:
        validator.validateClient(cl)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==4
        
    cl=Client(1,"Asmarandei","","")
    try:
        validator.validateClient(cl)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==2
    
    cl=Client(1,"Asmarandei","Ana","")
    try:
        validator.validateClient(cl)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors())==1
        
    cl=Client(1,"Asmarandei","Ana",2990128798)
    try:
        validator.validateClient(cl)
        assert True
    except ValidatorException as ex:
        assert False

testClientValidator()

def testFilmValidator():
    validator = Validator()
    fl=Film(1,"","","")
    try:    
        validator.validateFilm(fl)
        assert False
    except ValidatorException as ex:
        assert len(ex.errors)==3

testFilmValidator()

def testRepoClientiValidator():
    validator = Validator()
    repo = ClientiRepo()
    cl = Client(1,"Asmarandei", "Ana", "2990127392163")
    repo.store(cl)  
    cl2 = Client(2,"Asmarandei","Ana","8131282742412")
    try:
        validator.validateRepoClienti(cl2,repo.getAll())
    except ValidatorException as ex:
        assert len(ex.errors)==1
    try:
        repo.store(cl2)
    except ValueError :
        assert True
        
testRepoClientiValidator()
