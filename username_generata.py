import random
usernam = ('ahmad','aliyu','umar','abubakar','sadik','abba','najeeb','umar1,','usman','zainab','aishat','maryam')
password = ('nam90','paa1234','umii123','mmae')
while True:
    users = random.choice(usernam)
    if  usernam == 'nnome':
        print('invalid')
    passw = random.choice(password)
    for  users in passw:
        print(' is good')
    namess = (users + "" + passw )
    print(' is username :' + namess)
