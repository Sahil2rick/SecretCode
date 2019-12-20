import random
print('SECRET CODE')
while True:
     a=random.randint(0,9)
     b=random.randint(0,9)
     c=random.randint(0,9)
     d=random.randint(0,9)
     e=random.randint(0,9)
     f=random.randint(0,9)
     h=random.randint(0,9)
     i=random.randint(0,9)
     
     
     if a!=b and a!=c and a!=d and a!=e and a!=f and a!=h and a!=i and b!=c and b!=d and b!=a and b!=e and b!=f and b!=h and b!=i and c!=a and c!=b and c!=d and c!=e and c!=f and c!=h and c!=i and d!=a and d!=b and d!=c and d!=e and d!=f and d!=h and d!=i and e!=a and e!=b and e!=c and e!=d and e!=f and e!=h and e!=i and f!=a and f!=b and f!=c and f!=e and f!=d and f!=h and f!=i and h!=a and h!=b and h!=c and h!=e and h!=f and h!=d and h!=i and i!=a and i!=b and i!=c and i!=e and i!=f and i!=h and i!=d:
      break 
print('lets start the game')
a=str(a)
b=str(b)
c=str(c)
d=str(d)
e=str(e)
f=str(f)
h=str(h)
i=str(i)
code=a+b+c+d+e+f+h+i
n=6
for i in range(n):
    g=input('enter a 8 digit code')
    try:
      if g[0]==a:
            print('**')
      elif g[0]==b or g[0]==c or g[0]==d or g[0]==e or g[0]==f or g[0]==h or g[0]==i :
            print('*')
      if g[1]==b:
            print('**')
      elif g[1]==a or g[1]==c or g[1]==d or g[1]==e or g[1]==f or g[1]==h or g[1]==i:
            print('*')
      if g[2]==c:
            print('**')
      elif g[2]==a or g[2]==b or g[2]==d or g[2]==e or g[2]==f or g[2]==h or g[2]==i:
            print('*')
      if g[3]==d:
            print('**')
      elif g[3]==a or g[3]==b or g[3]==c or g[3]==e or g[3]==f or g[3]==h or g[3]==i:
            print('*')
      if g[4]==e:
            print('**')
      elif g[4]==a or g[4]==b or g[4]==c or g[4]==d or g[4]==f or g[4]==h or g[4]==i:
            print('*')
      if g[5]==f:
            print('**')
      elif g[5]==a or g[5]==b or g[5]==c or g[5]==e or g[5]==i or g[5]==h or g[5]==d :
            print('*')
      if g[6]==h:
            print('**')
      elif g[6]==a or g[6]==b or g[6]==c or g[6]==d or g[6]==f or g[6]==e or g[6]==i:
            print('*')
      if g[7]==i:
            print('**')
      elif g[7]==a or g[7]==b or g[7]==c or g[7]==e or g[7]==f or g[7]==h or g[7]==d :
            print('*')      
            
      if g==code:
        print('congratulation')
        print('You Win !!!!!')
        break
    except:
         pass
if g!=code:
 print('YOU LOSE')
 print('The code is',code) 
      
     
            
    
    
