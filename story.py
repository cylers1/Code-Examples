Blue = 1
Red = 2
Yellow = 3
Purple = 4

color = input("Color: ")
result = color.split()

if result[0] == "Pick":
    if result[1] == "1":
        print("Blue was taken")
    elif result[1] == "2":
        print("Red was taken")
    elif result[1] == "3":
        print("Yellow was taken")
    elif result[1] == "4":
        print("Purple was taken")
    else:
        print("no pebble was taken")
else:
    print("I broke")
