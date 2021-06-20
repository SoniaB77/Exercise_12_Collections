cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
#cheese += 'Oke' - this isn't how you should add item to the end of a list.

cheese.append("Oke")
print(cheese)

cheese.extend(["Red Leicester", "Smoked Bavarian"])
print(cheese)


