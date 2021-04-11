"""

Objectif :
    tester l'ajout d'image avec le paquet imageTk
    tester l'action de changer du texte au clic

Depuis le terminal : 
    pip install Image-Kit

En cliquant sur un bouton :
    on affiche un robot tiré au hasard dans tableau de dico

NB : Code non optimisé en l'état


"""


from tkinter import * 
from PIL import ImageTk, Image
import random

robots = [
    {
        "nom": "Achille",
        "numero": "268910",
        "fonction": "Interprète"
    },
    {
        "nom": "Hercule",
        "numero": "445623",
        "fonction": "Mécanicien"
    },
    {
        "nom": "Barbara",
        "numero": "123490",
        "fonction": "Agent de police"
    },
    {
        "nom": "Hermione",
        "numero": "459981",
        "fonction": "Infirmière"
    },
    {
        "nom": "Léonard",
        "numero": "345078",
        "fonction": "Transporteur"
    },
    {
        "nom": "Ulysse",
        "numero": "569976",
        "fonction": "Cuisinier"
    },
    {
        "nom": "Hector",
        "numero": "12122",
        "fonction": "Maçon"
    }
]


#
# Fonction reponse e déclencche lors du clic sur le bouton GO!

def reponse():
    # random robot
    r = random.randint(0, len(robots)-1)
    robot = robots[r]
    # texte robot
    robot_texte.config(text=robot['nom']+": "+ robot['fonction'])
    
    # image robot dans canvas
    imageFile = Image.open("./images/"+ robot['numero'] +".png")
    photoImage = ImageTk.PhotoImage(imageFile)
    canvas.delete("all")
    canvas.create_image((0, 0), image=photoImage, anchor='nw')
    canvas.pack()
    root.mainloop()



#
# creation de l'interface graphique
#
root = Tk()
#
# paramétrage de la fenetre principale
#
root.title = "Mon application"
root.geometry("800x600")
root.config(background='dodgerblue')

#
# canvas
#

canvas = Canvas(root, bg='dodgerblue')


#
# ajouter un titre
#
un_titre = Label(
                text="Quel Robot est demandé ?", 
                font=("sans-serif, 30"), 
                bg="dodgerblue", fg="white"
                ).pack()

#
# ajouter un bouton
#
bouton = Button(
                text="GO !", 
                bg="white", 
                font=("sans-serif, 20"), 
                fg="dodgerblue", 
                command=reponse
            ).pack(pady=10)




#
# un texte pour le robot
#
robot_texte = Label( 
        text="",
        font=("sans-serif, 20"), 
        bg="dodgerblue", fg="white"
    )
robot_texte.pack(pady=30)



# Affiche
root.mainloop()





