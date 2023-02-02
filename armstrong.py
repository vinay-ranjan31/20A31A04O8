
n=15
s=0
t=n
while n>0:
     r= n%10
     s+=r*r 
     n=n//10
if s==t:
      print("armstrong number")
else:
     print("not armstrong ")
