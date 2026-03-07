fav_fruits={"apple", "banana", "cherry"}
print("banana" in fav_fruits)
print("grape" in fav_fruits)
fav_fruits.add("grape")
print(fav_fruits)
fav_fruits.remove("banana")
print(fav_fruits)
fav_fruits=tuple(fav_fruits)
print(fav_fruits[0])
