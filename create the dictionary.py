x={}
n1=int(input("enter the number from where range start"))
n2=int(input("enter the number end of range"))
for i in range(n1,n2+1):
    x[chr(i)]=i
print("dictionary=",x)    
