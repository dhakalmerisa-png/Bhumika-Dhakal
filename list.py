fav_fruits=["apple", "banana", "cherry"]
print(fav_fruits[0])  
print(fav_fruits[2])  
fav_fruits[1]="grape"
print(fav_fruits)
fav_fruits.append("orange")
print(fav_fruits)
fav_fruits.insert(1,"kiwi")
print(fav_fruits)   
fav_fruits.remove("cherry")
print(fav_fruits)
fav_fruits.pop(2)
print(fav_fruits)
fav_fruits.sort()
print(fav_fruits)
fav_fruits.sort(reverse=True)
print(fav_fruits)
fav_fruits.sort(reverse=False)
print(fav_fruits)


numbers=[5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

fav_fruits=["apple", "banana", "cherry"]
print("banana" in fav_fruits)
print("grape" in fav_fruits)

fav_fruits=["apple", "banana", "cherry"]
print(fav_fruits)
fav_fruits2=["grape", "kiwi"]
print(fav_fruits2)
combined_fruits=fav_fruits+fav_fruits2
print(combined_fruits)
fav_fruits.append("fav_fruits2")
print(fav_fruits)

