palavra1 = input().strip().lower()
palavra2 = input().strip().lower()
palavra3 = input().strip().lower()

animais = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero": {
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado": {
        "inseto": {
            "hematofago": "pulga",
            "herbivoro" : "lagarta"
        },
        "anelideo": {
            "hematofago" : "sanguesuga",
            "onivoro" : "minhoca"
        }
    }
}

animal = animais[palavra1][palavra2][palavra3]
print(animal)
