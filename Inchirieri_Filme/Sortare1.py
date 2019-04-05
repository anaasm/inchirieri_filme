from random import randint


def cmp(x,y,reverse):     
        if x == y:
            return 0
        if reverse == False:
            if x < y:
                return -1
            else:
                return 1
        else:
            if x < y:
                return 1
            else:
                return -1        
    
def bingoSort(l,key,reverse):
        """
        Sorteaza lista l ascendent
        Returneaza l
        """
        i = 0
        while i < len(l):   
            min_idx = i 
            for j in range(i+1, len(l)): 
                if cmp(key(l[min_idx]),key(l[j]),reverse) > 0: 
                    min_idx = j
            l[i],l[min_idx] = l[min_idx],l[i] 
            for k in range(min_idx+1,len(l)):
                if cmp(key(l[min_idx]),key(l[k]),reverse) == 0:
                    l[i], l[min_idx] = l[min_idx], l[i] 
                    i+=1
            i+=1
        return l
    

    
def merge(arr,L,R,key,reverse):
        """
        Parametri : arr,L,R -liste
        Inteclaseaza listele in ordine crescatoare L si R si le pune in arr
        Returneaza lista arr
        """
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if cmp(key(L[i]),key(R[j]),reverse) < 0: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
        return arr
    
def mergeSort(arr,key,reverse):
    """
    Sorteaza lista arr descrescator sau crescator
    """
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]   
        R = arr[mid:] 
        mergeSort(L,key,reverse) 
        mergeSort(R,key,reverse)
        merge(arr,L,R,key,reverse) 
    return arr

def my_sorted1(lst,*,key = None,reverse = False):
    if key == None:
        key = lambda x:x
    lst = mergeSort(lst,key,reverse)
    return lst

def my_sorted2(lst,key,reverse):
    if key == None:
        key = lambda x:x
    lst = bingoSort(lst,key,reverse)
    return lst


def test():
    assert my_sorted1([]) == []
    assert my_sorted1([7,2]) == [2,7]
    assert my_sorted1([12, 11, 13, 5, 6, 7],key = None,reverse=False) == [5,6,7,11,12,13]
    assert my_sorted1([9,8,7,6,5,4,3,2,1],key = None,reverse = True) == [9,8,7,6,5,4,3,2,1]
    assert my_sorted2([12, 11, 13, 5, 6, 7],key = None,reverse = False) == [5,6,7,11,12,13]
    assert my_sorted2([9,8,7,6,5,4,3,2,1],key = None,reverse = True) == [9,8,7,6,5,4,3,2,1]
    
test()

def testeMari():
    lst = []
    for i in range(20):
        n = randint(500,1000)
        for j in range(n):
            lst.append(randint(1,1000))
        assert sorted(lst) == my_sorted1(lst)
    for i in range(20):
        n = randint(500,1000)
        for j in range(n):
            lst.append(randint(1,1000))
        assert sorted(lst,reverse = True) == my_sorted1(lst,reverse = True)
    for i in range(20):
        n = randint(500,1000)
        for j in range(n):
            lst.append(randint(1,1000))
        assert sorted(lst,key = lambda x:-x ,reverse = False ) == my_sorted1(lst,key = lambda x:-x,reverse = False )
    for i in range(20):
        n = randint(500,1000)
        for j in range(n):
            lst.append(randint(1,1000))
        assert sorted(lst,key = lambda x:-x) == my_sorted1(lst,key = lambda x:-x)
        
        
        
testeMari()