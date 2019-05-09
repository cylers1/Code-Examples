Blue = 0
Red = 0
Yellow = 0
Green = 0
Gold = 1
Health = 100
Experience = 0

if Gold == 1:
    print("The chest opens")
    Health += 50
    Experience += 100
    

elif Blue == 1:
    print("DEATH Appears")
    Health -= 100

elif Red == 1:
    print("The chest burns you")
    Health -= 50

elif Yellow == 1:
    print("A monster appears behind you")

elif Green == 1:
    print("A giant boulder falls from the ceiling and rolls toward you")


else:
    print("You need a key to open this")

print("Health:", Health)
print("Experience:", Experience)

if Health <= 0:
    print("GAME OVER")
else:
    print("")
