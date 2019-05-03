
#Tokens para numeros
def tk_numeros (fil,col,i,x,b):
    if i>len(x)-1:
        b = 1
        return fil,col,i,x,b
    if x[i]=="0" or x[i]=="1" or x[i]=="2" or x[i]=="3" or x[i]=="4" or x[i]=="5" or x[i]=="6" or x[i]=="7" or x[i]=="8" or x[i]=="9" or x[i]==".":
        i=i+1
        col=col+1
        b=1
        return tk_numeros(fil,col,i,x,b)    
    if ((ord(x[i]))>=65 and (ord(x[i]))<=90) or ((ord(x[i]))>=97 and (ord(x[i]))<=122):
        return err_letras(fil,col,i,x,b)

def err_letras(fil,col,i,x,b):
    if i>len(x)-1:
        #b = 1
        return fil,col,i,x,b
    elif ((ord(x[i]))>=65 and (ord(x[i]))<=90) or ((ord(x[i]))>=97 and (ord(x[i]))<=122):
        b=0
        i+=1
        col+=1
        return err_letras(fil,col,i,x,b)
    elif x[i]=="0" or x[i]=="1" or x[i]=="2" or x[i]=="3" or x[i]=="4" or x[i]=="5" or x[i]=="6" or x[i]=="7" or x[i]=="8" or x[i]=="9" or x[i]==".":
        b=0
        i+=1
        col+=1
        return err_letras(fil,col,i,x,b)
    elif x[i] == "*":
        b=0
        i+=1
        col+=1
        return fil,col,i,x,b
    else:
        return fil,col,i,x,b



    #if x[i]


#
#print (ord('A')-65)

x=input()
a=len(x)
i=0   #contador de cada parte del arreglo
col=1  #ubica en que columna está
fil=1  #ubica en que fila está



while i<a:
    
    if x[i]=="*":
        i+=1
        col+=1
    if x[i]=='\n':
        fil+=1
        i+=1
        col=1
    
    
    if x[i]=="0" or x[i]=="1" or x[i]=="2" or x[i]=="3" or x[i]=="4" or x[i]=="5" or x[i]=="6" or x[i]=="7" or x[i]=="8" or x[i]=="9":
        p=col
        k=fil
        b=1
        (fil,col,i,x,b)=tk_numeros(fil,col,i,x,b)
        if b==1:
            print("tk_num",",",k,",",p,",",x[p-1:i+1])
        if b==0:
            print ("Error lexico")    
    i+=1
  
            
    

