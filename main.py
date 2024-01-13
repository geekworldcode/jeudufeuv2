import pygame
from pygame.locals import *
from tkinter import *
import time

def quitter():
    exit()

def jouer():
    window.destroy()
    pygame.mixer.init()
    pygame.mixer.music.load("D:\\pythonProject\\jeudufeu\\Sons\\sondefeu.mp3")
    pygame.mixer.music.play(loops=100)
    pygame.mixer.music.set_volume(100)
    nom_utilisateur = "Test"
    pygame.init()
    run = True
    score = 0
    screen = pygame.display.set_mode((800, 600))
    bg = pygame.image.load("Foret.png")
    bg_2 = pygame.transform.scale(bg, (800, 600))
    pygame.display.set_caption("Jeu du feu")
    img_buche = pygame.image.load("buche.png")
    img_journaux = pygame.image.load("journaux.png")
    img_bois_feu = pygame.image.load("pine-firewood-for-sale-stettler-camrose-drumheller.png")
    img_bois_feu_recadre = pygame.transform.scale(img_bois_feu, (300, 200))
    img_bois_feu_rect = img_bois_feu_recadre.get_rect(topleft=(170, 400))
    img_batton = pygame.image.load("batton.png")
    font = pygame.font.Font("FIRESTARTER.TTF", 42)
    img_batton = pygame.image.load("batton.png")
    font2 = pygame.font.Font("FIRESTARTER.TTF", 40)
    text2 = font2.render(nom_utilisateur + " Score", 1, (255, 200, 0))
    font_inventaire = pygame.font.Font("Toddler Writing.ttf", 30)
    texte_inventaire = font_inventaire.render("Inventaire", 1, (0, 0, 0))
    taillexbois = 320
    tailleybois = 320

    image_sprite = [pygame.image.load("Sprite1.png"),
                    pygame.image.load("Sprite2.png"),
                    pygame.image.load("Sprite3.png")]
    clock = pygame.time.Clock()
    value = 0

    buche_presse = False
    journaux_presse = False
    batton_presse = False
    ley = 190
    lex = 150

    while run:
        clock.tick(500)
        if value >= len(image_sprite):
            value = 0
        image = image_sprite[value]
        image_resized = pygame.transform.scale(image, (taillexbois, tailleybois))
        screen.blit(image_resized, (lex, ley))
        text = font.render(nom_utilisateur + " Score:" + str(score), 1, (0, 0, 0))
        pygame.display.update()
        screen.fill((0, 0, 0))
        value += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if buche_presse == True:
                    buche_presse = False
                elif journaux_presse == True:
                    journaux_presse = False
                elif batton_presse == True:
                    batton_presse = False
                if img_buche_rect.collidepoint(event.pos):
                    buche_presse = True
                if img_journaux_rect.collidepoint(event.pos):
                    journaux_presse = True
                if img_batton_rect.collidepoint(event.pos):
                    batton_presse = True

            if event.type == MOUSEBUTTONUP:
                if buche_presse and img_bois_feu_rect.collidepoint(event.pos):
                    tailleybois += 20
                    taillexbois += 20
                    ley -= 20  # Ajustement de la position en x et y
                    lex -= 10
                    score += 100
                if batton_presse and img_bois_feu_rect.collidepoint(event.pos):
                    tailleybois += 10
                    taillexbois += 10
                    ley -= 10  # Ajustement de la position en x et y
                    lex -= 5
                    score += 75
                if journaux_presse and img_bois_feu_rect.collidepoint(event.pos):
                    tailleybois += 5
                    taillexbois += 5
                    ley -= 5  # Ajustement de la position en x et y
                    lex -= 2.5
                    score += 50

                buche_presse = False
                journaux_presse = False
                batton_presse = False

        screen.fill((0, 0, 0))
        screen.blit(bg_2, (0, 0))
        x, y = pygame.mouse.get_pos()
        img_buche_rect = screen.blit(img_buche, (680, 150))
        img_journaux_rect = screen.blit(img_journaux, (680, 250))
        img_batton_rect = screen.blit(img_batton, (680, 350))
        screen.blit(img_bois_feu_recadre, (170, 400))
        screen.blit(text, (265, 5))
        screen.blit(text2, (270, 0))
        screen.blit(texte_inventaire, (670, 70))

        if buche_presse == True:
            screen.blit(img_buche, (x - 50, y - 20))  # permet a l'objet de suivre la souris
        if journaux_presse == True:
            screen.blit(img_journaux, (x - 50, y - 20))  # permet a l'objet de suivre la souris
        if batton_presse == True:
            screen.blit(img_batton, (x - 50, y - 20))

        pygame.display.flip()

    pygame.quit()

# parametre fenetre acceuil
window = Tk()
window.title("Jeu du Feu")
window.geometry("800x600")
window.maxsize(800, 600)
window.minsize(800, 600)

# image fond
canv = Canvas(window, width=800, height=600, bg='white')
canv.grid(row=0, column=0)
window.iconbitmap("D:\\pythonProject\\jeudufeu\\Images\\pixil-frame-0-_1_ (1).ico")
img = PhotoImage(file="D:\\pythonProject\\jeudufeu\\Images\\feu.png")
canv.create_image(0, 0, anchor=NW, image=img)
canv.create_text(400, 70, text="Jeu Du Feu", font=("Firestarter", 60), fill="#f99b31", tag="zizi")
# suprimer du texte, ajouter , tag="nom du tag")
# canv.delete("zizi")

# bouton, label...
bouton_jouer = Button(text="Jouer", font=("Firestarter", 30), command=jouer, width=7, bg="orange")
bouton_jouer.place(x=320, y=150)
bouton_quitter = Button(text="quitter", font=("Firestarter", 30), command=quitter, width=7, bg="orange")
bouton_quitter.place(x=320, y=400)
bouton_score = Button(text="score", font=("Firestarter", 30), width=7, bg="orange")
bouton_score.place(x=320, y=270)

window.mainloop()
