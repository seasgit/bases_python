import random
animaux = ['chien','chat','cheval','poule','tortue','canard','vache','mouton']
def getAnimal(data):
    r = random.randint(0, len(data)-1)
    return data[r]

print(getAnimal(animaux))
        