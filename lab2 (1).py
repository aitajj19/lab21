
# Online Python - IDE, Editor, Compiler, Interpreter

def ədədi_orta_hesabla(A):
    toplam=0
    n=len(A)
    
    for ədəd in A:
        toplam+=ədəd
        
    ortalama=toplam/n
    return ortalama
    
massiv=[1,2,3,4,5]

ədədi_orta=ədədi_orta_hesabla(massiv)
print("Massivin ədədi ortası:",ədədi_orta)