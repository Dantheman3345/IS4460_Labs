x=-2
y=3 * (abs(2*x)+4)
print(y)

print(f"a: {20>9}")
print(f"b: {5==6}")
print(f"c: {1==0}")
print(f"d: {1==1}")

print("one is equal to 2:",int(1==2))
print("one is equal to 1:",int(1==1))

myname = "brian"
myage = 37
print(f"a:{73}")
print(f"b:{'Hello'}")
print(f'c:{False}')
print(f'd:{myname}')
print(f"e:{myage}")

print((1-2+3),(3-2+1))
print((1*2+3),(3*2+1))

print(f"is 'matt'=='matthew'?{'matt'=='matthew'}")
print(f"is 'guy'=='Guy'?{'guy'=='Guy'}")

my_name ='matt'
print("assignment: ",my_name)
print("equality: ",my_name =='matt')

print("comparison:","aa" < "b")
print("comparison:", 5<6)

a=2
b=3
print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a<b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a>= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

bank_balance = 50
if bank_balance < 100:
    money = 1000
    bank_balance += money

bank_balance = 50
if bank_balance > 100:
    money = 1000
    bank_balance += money
else:
    print("balance is less than ore equal to 100")


bank_balance = 600
savings = 100
if bank_balance < 100:
    money = 10
    bank_balance += money
elif bank_balance > 200:
    savings += 100
    bank_balance -= 1000
elif bank_balance == 1000000000:
    print("you rich")
else:
    savings += 50
    bank_balance -= 50

print(bank_balance)
print(savings)



fuel = 100
print("Fill tank now" if fuel <=1 else "There's enough fuel")

fuel = 1
print("Fill tank now" if fuel<= 1 else "there's enough fuel")

fuel = 0
print("Fill tank now" if fuel<= 1 else "there's enough fuel")


fuel = 9
while fuel > 1:
    # keep driving
    print("There's plenty of fuel lol")
    fuel -= 1


books = ['harry potter', 'lord of the rings', 'matts autobiography']
count = 0
for books in books:
    print(f'book:{books}')
    count+=1
print(count)

for i in range (5):
    print(f'i:{i}')

funny_num=0
for count in range(13):
    print(f"{count} times 12 is {count * 12}")
    if count ==7:
        break
for count in range(30):
    if count == 7:
        funny_num+=1
        continue
    print(f'{count} times 12 is {count *12}')
