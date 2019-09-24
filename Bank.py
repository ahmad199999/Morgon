
user = "AhmadMirzad"
userName = (input("write in your username:"))
if user != userName:
    exit()

pin = 1234
userPin = int(input("write in your password:"))
if pin != userPin:
    exit()    

menu = 0

saldo = 20000
while menu != 3:
    print("Ditt saldo är:", saldo)
    menu = int(input("skriv ditt val:[1,2,3] "))
    if menu == 1:
        saldo = saldo + float(input("hur mycket vill du sätta in:"))

    elif menu == 2:
        print("Utagg")
        saldo = saldo - int(input("hur mycket vill du ta ut:"))
        
    else:
        exit()
    

    

        

