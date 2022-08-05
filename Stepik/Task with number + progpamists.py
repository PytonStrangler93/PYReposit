number = input()
if 20 >= int(number) >= 5 or 120 >= int(number) >= 105 or 220 >= int(number) >= 205 or 320 >= int(number) >= 305 or 420 >= int(number) >= 405 or 520 >= int(number) >= 505 or 620 >= int(number) >= 605 or 720 >= int(number) >= 705 or 820 >= int(number) >= 805 or 920 >= int(number) >= 905:
    print(number + ' ' + 'программистов')
elif int(number) in range(1,1001,10):
    print(number + ' ' + 'программист')
elif int(number[-1]) == 0 or 9 >= int(number[-1]) >= 5:
    print(number + ' ' + 'программистов')
elif  4 >= int(number[-1]) >= 2:
    print(number + ' ' + 'программиста')
    
i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)


a=int(input())
if 2<=a%10<=4 and not 12<=a%100<=14:
  b='программиста' 
elif a%10 ==1 and a%100!=11:
  b='программист'
else:
  b='программистов'

print(str(a), b)

n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))