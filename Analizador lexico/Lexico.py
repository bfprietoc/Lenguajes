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
    
        return fil,col,i,x,b
    else:
        return fil,col+1,i,x,b

def err_letras(fil,col,i,x,b):
    if i>len(x)-1:
        b = 0
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
    elif x[i] == " ":
        b=0
        col+=1
        return fil,col,i,x,b
    else:
        return fil,col,i,x,b


def reserv(fil,col,i,x):

    if x[i:i+3]=="or ":
        i+=2
        col+=3
        return fil,col,i,x


    if x[i:i+4]=="and ":
        i+=3
        col+=4
        return fil,col,i,x
    if x[i:i+5]=="suma ":
        i+=4
        col+=5
        return fil,col,i,x
    if x[i:i+8]=="archivo ":
        i+=7
        col+=8
        return fil,col,i,x
    if x[i:i+5]=="caso ":
        i+=4
        col+=5
        return fil,col,i,x    
    if x[i:i+6]=="const ":
        i+=5
        col+=6
        return fil,col,i,x
    if x[i:i+11]=="constantes ":
        i+=10
        col+=11
        return fil,col,i,x
    if x[i:i+6]=="desde ":
        i+=5
        col+=6
        return fil,col,i,x
    if x[i:i+5]=="eval ":
        i+=4
        col+=5
        return fil,col,i,x    
    if x[i:i+4]=="fin ":
        i+=3
        col+=4
        return fil,col,i,x
    if x[i:i+6]=="hasta ":
        i+=5
        col+=6
        return fil,col,i,x
    if x[i:i+7]=="matrix ":
        i+=6
        col+=7
        return fil,col,i,x
    if x[i:i+9]=="mientras ":
        i+=8
        col+=9
        return fil,col,i,x    
    if x[i:i+4]=="not ":
        i+=3
        col+=4
        return fil,col,i,x
    if x[i:i+7]=="inicio ":
        i+=6
        col+=7
        return fil,col,i,x
    if x[i:i+4]=="lib ":
        i+=3
        col+=4
        return fil,col,i,x
    if x[i:i+7]=="libext ":
        i+=6
        col+7
        return fil,col,i,x    
    
    if x[i:i+5]=="paso ":
        i+=4
        col+=5
        return fil,col,i,x
    if x[i:i+10]=="subrutina ":
        i+=9
        col+=10
        return fil,col,i,x
    if x[i:i+9]=="programa ":
        i+=8
        col+=9
        return fil,col,i,x    
    if x[i:i+4]=="ref ":
        i+=3
        col+=4
        return fil,col,i,x
    if x[i:i+9]=="registro ":
        i+=8
        col+=9
        return fil,col,i,x
    if x[i:i+8]=="repetir ":
        i+=7
        col+=8
        return fil,col,i,x
    if x[i:i+9]=="retorna ":
        i+=8
        col+=9
        return fil,col,i,x    
    if x[i:i+3]=="si ":
        i+=2
        col+=3
        return fil,col,i,x
    if x[i:i+5]=="sino ":
        i+=4
        col+=5
        return fil,col,i,x
    if x[i:i+6]=="tipos ":
        i+=5
        col+=6
        return fil,col,i,x
    if x[i:i+4]=="var ":
        i+=3
        col+=4
        return fil,col,i,x    
    if x[i:i+10]=="variables ":
        i+=9
        col+=10
        return fil,col,i,x
    if x[i:i+7]=="vector ":
        i+=6
        col+=7
        return fil,col,i,x
    if x[i:i+9]=="imprimir ":
        i+=8
        col+=9
        return fil,col,i,x
    if x[i:i+9]=="numerico ":
        i+=8
        col+=9
        return fil,col,i,x    
    if x[i:i+5]=="leer ":
        i+=4
        col+=5
        return fil,col,i,x
    else :
        
x=input()   
a=len(x)
col=1  #ubica en que columna est·
fil=1  #ubica en que fila est·
i=0   #contador de cada parte del arreglo

while i<a:

    if x[i]==" ":
        col=col+1
        p = col
    '''
    if x[i]=="\n":
        fil=fil+1
        col=1
    '''

    if x[i]=="0" or x[i]=="1" or x[i]=="2" or x[i]=="3" or x[i]=="4" or x[i]=="5" or x[i]=="6" or x[i]=="7" or x[i]=="8" or x[i]=="9":
        p=col
        k=fil
        b=1
        (fil,col,i,x,b)=tk_numeros(fil,col,i,x,b)
        if b==1:
            print("\ntk_num",",",k,",",p,",",x[p-1:i+1])
            '''
            if i==a:
                break
            else:
                if x[i-1]=="\n":
                    col=1
                    fil=fil+1
            '''               
        if b==0:
            print ("Error lexico",",",k,",",p )
            break
    if (ord(x[i]))>=97 and (ord(x[i]))<=122:
        p=col
        k=fil
        (fil,col,i,x)=reserv(fil,col,i,x)
        print(x[p-1:i],",",k,",",p)

       

                
    i+=1





        

    #se salta todos los comentarios si los hay
   
    
    
    
    
    