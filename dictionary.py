Person={
    "name":"Merisa",
    "age":18,
    "gender":"Female",
    "address":{
        "City":"ktm",
        "country":"Nepal",
        "fav_movies":["3 idiots","nepali"]
    }
}
print(Person)
print("Name:", Person["name"])
Person["age"]=19
print(Person["age"])
print(Person.get("age"))
print(Person.get("address").get("City"))
print(Person.get("fav_movies"))
print(len(Person))


