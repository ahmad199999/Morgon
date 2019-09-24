
print("Welcome dear user")
identity = input("Enter your name please?[Ahmad, Max, Jan, Kiki]")


season = input("Vilken årstid är det?[höst, sommar, vår, vinter]")
if season == "höst":
    print("Du behöver jacka")
elif season == "sommar":
    print("Du behöver cykel idag")
elif season == "vår":
    print("Du behöver blommor")
elif season == "vinter":
    print("Du behöver varma kläder")
else:
    print("Please be careful about the quistions!")
#Condition = 1
#while Condition < 10:
    #print("condition")
    #Condition += 1

print("you have to enter the time")
time = input("What time is it[20:21, 21:20, 33:22]")
if time == "21:20":
    print("Let's get to the gym")
elif time == "20:21":
    print("let's have a cap of tea")
elif time == "33:22":
    print("Don't do any stupid things")
else:
    print("go and get some sleep")

