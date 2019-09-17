

vaken = "n" 

print("Du sover djupt som björnen i ide...") 

while vaken == "n": # Den loopar rount.      == är lika med.
    vaken = input("Vaknar du? [y/n] ")

print("Du masar dig upp och släppar dig in i duschen.")
print("Någon har lämnat en brödrost i din dusch")

duscha = input("flyttar du på brödrosten? [y/n] ")

if duscha == "n":
    exit("Du elckockas och ditt äventyr är slut")
       
elif duscha == "y":
    print("friskt vatten sköljer över dig och du börjar äntligen vakna.")
else:
    print("Does not compute")
#årstider
season = False
while season == False:
    season =input("vilken årstid är det?[vår, vinter, sommar, höst]")
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt och slask, fy tusen!")
        print("Du klär på dig vinterpälsen...")
    elif season == "sommar":
        print("Sommar!shorts och flip flops")
    else:
        season = False

