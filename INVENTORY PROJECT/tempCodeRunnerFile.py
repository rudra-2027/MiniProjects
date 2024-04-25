menu={
    "Apples":50,
    "Banana":50,
    "Maggie":50,
    "Cold Drink":80
    
}
print(menu)
print("Item \t               Amount")
for i in menu:
    print(i,":  ",end="  ")
    print(menu[i])
