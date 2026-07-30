# HARD PASSWORD #
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
password=''
print("welcome to password generator")
c=int(input("how many letters do you want to have in your password?\n"))
d=int(input("how many numbers do you want to have in your password?\n"))
e=int(input("how many symbols do you want to have in your password?\n"))
for i in range(c):
    char=random.choice(letters)
    password+=char
for i in range(d):
    num=random.choice(numbers)
    password+=num
for i in range(e):
    symbol=random.choice(symbols)
    password+=symbol
print(password)
pass_word=set(password)
print(pass_word)
_password=''
for i in pass_word:
    _password+=i
print(_password)