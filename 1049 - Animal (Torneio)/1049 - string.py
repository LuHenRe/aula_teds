palavra1 = input().strip().lower()
palavra2 = input().strip().lower()
palavra3 = input().strip().lower()

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            animal = "aguia"
        elif palavra3 == "onivoro":
            animal = "pomba"
    elif palavra2 == "mamifero":
        if palavra3 == "onivoro":
            animal = "homem"
        elif palavra3 == "herbivoro":
            animal = "vaca"
elif palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hematofago":
            animal = "pulga"
        elif palavra3 == "herbivoro":
            animal = "lagarta"
    elif palavra2 == "anelideo":
        if palavra3 == "hematofago":
            animal = "sanguessuga"
        elif palavra3 == "onivoro":
            animal = "minhoca"

print(animal)
