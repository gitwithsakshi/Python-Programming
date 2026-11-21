cutie = {
    "name":"Aayu" , "age":19, 
}

X = cutie.pop("age")
#del cutie["age"]   to delete a key
print(X)
print(cutie)

print(cutie.get("xyz",23232))