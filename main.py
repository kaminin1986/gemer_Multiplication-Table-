import random
import eel
eel.init("web")
eel.start("main.html", size= (400, 600))

shet=0
otric=0
for x in range (1,10):
    a=random.randint(2,9)
    b=random.randint(2,9)
    #print(a,b)
    f=a*b
    #print (f)
    print (a,"x",b)
    i=int(input("ввидете ответ "))
    
       # except ValueError:
        #    print("значение не integer")
         #   return code()

    if f==i:
        shet=shet+1
        print('Поздравляю!!! Это правильный  ответ')
    else:
        otric=otric+1
        print('Попробуй еще поучить таблицу')

print('Из прорешонных 10 выражений, правильных: ' , shet , ', не правльных ответов: ' , otric )