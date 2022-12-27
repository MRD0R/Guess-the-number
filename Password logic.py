import random 

def generate_password(a,b):
    c = ''
    for i in range(a):
        c += random.choice(b)
    return c
d = '0123456789'
l = 'abcdefghijklmnopqrstuvwxyz'
u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
p = '!#$%&*+-=?@^_'
chars = ''

cntPw = int(input('Specify the number of passwords to generate:'))
lenPw = int(input('Specify the length of one password:'))
digOn = input('Whether to include numbers 0123456789? (yes/no)')
ABCOn = input('Whether to include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (yes/no)')
abcOn = input('Whether to include lowercase letters abcdefghijklmnopqrstuvwxyz? (yes/no)')
chOn = input('Should the characters !#$%&*+-=?@^_ be included? (yes/no)')
excOn = input('Should il1Lo0O ambiguous characters be excluded? (yes/no)')

chars = chars + d*(digOn == 'yes') + u*(ABCOn == 'yes') + l*(abcOn == 'yes') + p*(chOn == 'yes')

for i in range(cntPw):
    if excOn == 'yes':
        for c in 'il1Lo0O':
            chars.replace(c,'')

for _ in range(cntPw):
    print(generate_password(lenPw,chars))   