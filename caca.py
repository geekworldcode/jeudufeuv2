#module
from tkinter import *
import pygame
from pygame import mixer
from tkinter import messagebox
import time
import animation

pygame.init()

#variables
partie = 0
nom_joueur2 = ""
journal = 5
carton = 10
bois = 10
nmb_chara = 0

# toute les defs
def quitter():
    exit()

def jouer():
    pygame.mixer.music.stop()
    global partie
    partie = 1
    window.destroy()

def quitter2():
    window2.destroy()

def briquet():
    pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\briquet.mp3")
    pygame.mixer.music.play(loops=0)
    mixer.music.set_volume(100)
    try:
        canv.delete("bois")
    except:
        ff = 10
    try:
        canv.delete("carton")
    except:
        ff = 10


def objet1():
    global journal
    if journal == 0:
        pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\journal.mp3")
        mixer.music.set_volume(10)
        canv.delete("journal")
    else:
        pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\journal.mp3")
        pygame.mixer.music.play(loops=1)
        mixer.music.set_volume(5)
        canv.delete("journal")
    if journal == 0:
        canv.create_text(700, 580, text="Vide", font=("noticia", 25), tag="journal", fill="red")
        pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\erreur.mp3")
        pygame.mixer.music.play(loops=1)
        mixer.music.set_volume(5)
    elif journal == 1:
        canv.create_text(650, 580, text="Il reste " + str(journal) + " journal", font=("noticia", 25), tag="journal")
        journal = journal - 1
    else:
        canv.create_text(650, 580, text="Il reste " + str(journal) + " journaux", font=("noticia", 25), tag="journal")
        journal = journal - 1

    try:
        canv.delete("bois")
    except:
        ff = 10
    try:
        canv.delete("carton")
    except:
        ff = 10

def objet2():
    global carton
    pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\carton.mp3")
    pygame.mixer.music.play(loops=1)
    mixer.music.set_volume(1)
    canv.delete("carton")
    if carton == 0:
        canv.create_text(700, 580, text="Vide", font=("noticia", 25), tag="carton", fill="red")
        pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\erreur.mp3")
        pygame.mixer.music.play(loops=1)
        mixer.music.set_volume(5)
    elif carton == 1:
        canv.create_text(650, 580, text="Il reste " + str(carton) + " carton", font=("noticia", 25), tag="carton")
        carton = carton - 1
    else:
        canv.create_text(650, 580, text="Il reste " + str(carton) + " cartons", font=("noticia", 25), tag="carton")
        carton = carton - 1

    try:
        canv.delete("bois")
    except:
        ff = 10
    try:
        canv.delete("journal")
    except:
        ff = 10

def objet3():
    global bois
    pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\beep.mp3")
    pygame.mixer.music.play(loops=1)
    mixer.music.set_volume(5)

    canv.delete("bois")
    if bois == 0:
        canv.create_text(700, 580, text="Vide", font=("noticia", 25), tag="bois", fill="red")
        pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\erreur.mp3")
        pygame.mixer.music.play(loops=1)
        mixer.music.set_volume(5)

    else:
        canv.create_text(650, 580, text="Il reste " + str(bois) + " bois", font=("noticia", 25), tag="bois")
        bois = bois - 1

    try:
        canv.delete("journal")
    except:
        ff = 10
    try:
        canv.delete("carton")
    except:
        ff = 10

def bg():
    prout = 1

def name():
    global nom_joueur2
    nom_joueur2 = entry.get()
    if nom_joueur2 == "":
        messagebox.showwarning("Jeu du feu", "Veuillez entrer un nom d'utilisateur")
    else:
        nom_joueur.destroy()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.maxhealth = 100
        self.image = pygame.image.load('Feu/Sprite1.png')
        self.rect = self.image.get_rect()


# parametre fenetre acceuil
window = Tk()
window.title("Jeu du Feu")
window.geometry("800x600")
window.maxsize(800, 600)
window.minsize(800, 600)

#image fond
canv = Canvas(window, width=800, height=600, bg='white')
canv.grid(row=0, column=0)
window.iconbitmap("D:\\pythonProject\\jeudufeu\\Images\\pixil-frame-0-_1_ (1).ico")
img = PhotoImage(file="D:\\pythonProject\\jeudufeu\\Images\\feu.png")
canv.create_image(0, 0, anchor=NW, image=img)
canv.create_text(400, 70, text="Jeu Du Feu", font=("Firestarter", 60), fill="#f99b31", tag="zizi")
#suprimer du texte, ajouter , tag="nom du tag")
#canv.delete("zizi")

#bouton, label...
bouton_jouer = Button(text="Jouer", font=("Firestarter", 30), command=jouer, width=7, bg="orange")
bouton_jouer.place(x=320, y=150)
bouton_quitter = Button(text="quitter", font=("Firestarter", 30), command=quitter, width=7, bg="orange")
bouton_quitter.place(x=320, y=400)
bouton_score = Button(text="score", font=("Firestarter", 30), width=7, bg="orange")
bouton_score.place(x=320, y=270)


#son
pygame.mixer.init()
pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\sondefeu.mp3")
pygame.mixer.music.play(loops=100)
pygame.mixer.music.set_volume(100)

window.mainloop()


if partie == 1:
    #fenetre nom joueuer
    nom_joueur = Tk()
    nom_joueur.iconbitmap("D:\\pythonProject\\jeudufeu\\Images\\pixil-frame-0-_1_ (1).ico")
    nom_joueur.geometry("300x100")
    nom_joueur.maxsize(300, 100)
    nom_joueur.minsize(300, 100)
    entrer = Button(nom_joueur, text="Entrer", bg='grey', fg='black', command=name, font=("Noticia", 30), width=20)
    entrer.place(x=0, y=30)
    nom_joueur.title("Nom utilisateur")
    entry = Entry(font=("Firestarter", 20))
    entry.pack()
    nom_joueur.protocol("WM_DELETE_WINDOW", bg)
    nom_joueur.mainloop()

    #deuxième fenetre
    window2 = Tk()
    window2.title("Jeu du Feu")
    window2.geometry("800x600")
    window2.maxsize(800, 600)
    window2.minsize(800, 600)

    # image fond
    canv = Canvas(window2, width=800, height=600, bg='white')
    canv.grid(row=0, column=0)
    window2.iconbitmap("D:\\pythonProject\\jeudufeu\\Images\\pixil-frame-0-_1_ (1).ico")
    img = PhotoImage(file="D:\\pythonProject\\jeudufeu\\Images\\Foret.png")
    canv.create_image(0, 0, anchor=NW, image=img)

    #texte avec canvas
    canv.create_text(400, 70, text="Score :", font=("Noticia", 25))
    canv.create_text(400, 20, text="Joueur : "+nom_joueur2, font=("Noticia", 25))
    canv.create_text(710,30, text="Inventaire", font=("Noticia", 25))

    #bouton, label....
    bouton_quitter2 = Button(window2, text="quitter", font=("Noticia", 15), command=quitter, bg="grey")
    bouton_quitter2.place(x=0, y=568)
    briquet = Button(window2, text="Briquet", bg='grey', fg='black',command=briquet, font=("Noticia", 15), width=7)
    briquet.place(x=681, y=75)

    objet = Button(window2, text="journal", bg='grey', fg='black', command=objet1, font=("Noticia", 15), width=7)
    objet.place(x=681, y=125)

    objet2 = Button(window2, text="carton", bg='grey', fg='black', command=objet2, font=("Noticia", 15), width=7)
    objet2.place(x=681, y=175)

    objet3 = Button(window2, text="bois", bg='grey', fg='black', command=objet3, font=("Noticia", 15), width=7)
    objet3.place(x=681, y=225)

    #image = PhotoImage(file="C:\\Users\\33610\\Documents\\pythonProject\\jeudufeu\\Images\\feu.png")
    #canv.create_image(140,20, image=image)

    pygame.mixer.init()
    pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\sondefeu.mp3")
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(100)
    window2.mainloop()
