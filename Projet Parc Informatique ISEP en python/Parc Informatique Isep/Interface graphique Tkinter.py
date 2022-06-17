from tkinter import *                            #commande d'importation du module d'interface Tkinter, le programme va aller chercher toutes les fonctions de la bibliothèque Tkinter
import ParcInformatiqueSQlite                    #importe l'autre fichier "ParcInformatiqueSQlite
window = Tk()                                    #creéation de la fenêtre
window.geometry("1100x850")                      #résolution de la fenêtre
window.minsize(1100, 850)                        #résolution minimum de la fenêtre
window.wm_title("Parc Informatique ISEP")        #nom de la fenêtre
window.iconbitmap("logo_isep.ico")               #change l'icone de la fenêtre par un ficher .ico qui est dans le dossier du programme

#TOUS LES CADRES
frameBouton = Frame(window)
frameListbox = Frame(window)
frameLabel = Frame(window)
frameTexte = Frame(window)
frameScroll= Frame(window)

def get_selected_row(event):
    try:
        global select_tup
        index=list1.curselection()[0]
        select_tup = list1.get(index)
        e1.delete(0,END)                            #supprime l'ancienne valeur et insère la nouvelle
        e1.insert(END, select_tup[1])
        e2.delete(0,END)
        e2.insert(END, select_tup[2])
        e3.delete(0,END)
        e3.insert(END, select_tup[3])
        e4.delete(0,END)
        e4.insert(END, select_tup[4])
        e5.delete(0, END)
        e5.insert(END, select_tup[5])
        e6.delete(0, END)
        e6.insert(END, select_tup[6])
        e7.delete(0, END)
        e7.insert(END, select_tup[7])
        e8.delete(0, END)
        e8.insert(END, select_tup[8])
        e9.delete(0, END)
        e9.insert(END, select_tup[9])
        e10.delete(0, END)
        e10.insert(END, select_tup[10])
        e11.delete(0, END)
        e11.insert(END, select_tup[11])
        e12.delete(0, END)
        e12.insert(END, select_tup[12])
        e13.delete(0, END)
        e13.insert(END, select_tup[13])
        e14.delete(0, END)
        e14.insert(END, select_tup[14])
        e15.delete(0, END)
        e15.insert(END, select_tup[15])
        e16.delete(0, END)
        e16.insert(END, select_tup[16])
        e17.delete(0, END)
        e17.insert(END, select_tup[17])
    except IndexError:
        pass

#définition de chaques fonctions correspondant à chaques boutons

def view_command():
    list1.delete(0, END)
    for row in ParcInformatiqueSQlite.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in ParcInformatiqueSQlite.search(poste_text.get(), salle_text.get(), os_text.get(), brand_text.get(), date_text.get(), cpu_text.get(), ram_text.get(), gpu_text.get(), screen_text.get(), hdd_text.get(), ssd_text.get(), wifi_text.get(), bluetooth_text.get(), usbports_text.get(), cdplayer_text.get(), solidworks_text.get(), proteus_text.get()):
        list1.insert(END, row)

def add_command():
    ParcInformatiqueSQlite.insert(poste_text.get(), salle_text.get(), os_text.get(), brand_text.get(), date_text.get(), cpu_text.get(), ram_text.get(), gpu_text.get(), screen_text.get(), hdd_text.get(), ssd_text.get(), wifi_text.get(), bluetooth_text.get(), usbports_text.get(), cdplayer_text.get(), solidworks_text.get(), proteus_text.get())
    list1.delete(0, END)
    list1.insert(END, (poste_text.get(), salle_text.get(), os_text.get(), brand_text.get(), date_text.get(), cpu_text.get(), ram_text.get(), gpu_text.get(), screen_text.get(), hdd_text.get(), ssd_text.get(), wifi_text.get(), bluetooth_text.get(), usbports_text.get(), cdplayer_text.get(), solidworks_text.get(), proteus_text.get()))

def delete_command():
    ParcInformatiqueSQlite.delete(select_tup[0])

def update_command():
    ParcInformatiqueSQlite.update(select_tup[0], poste_text.get(), salle_text.get(), os_text.get(), brand_text.get(), date_text.get(), cpu_text.get(), ram_text.get(), gpu_text.get(), screen_text.get(), hdd_text.get(), ssd_text.get(), wifi_text.get(), bluetooth_text.get(), usbports_text.get(), cdplayer_text.get(), solidworks_text.get(), proteus_text.get())

titre = Label(frameTexte, text="Parc Informatique", font=("Helvetica", 40))    #Widget "Label" ( qui permet d'afficher des lignes de texte ou un image ), le texte qu'on veut afficher, la police, et la taille
titre.grid()

#CHAQUES BOUTONS AVEC LEUR COMMANDE

x=0
b1 = Button(frameBouton, text= "Voir tout", width=12, command=view_command)     #Widget "Button" de tk ( qui créer un bouton), le cadre correspondant, le texte, la largeur, et la commande du bouton
b1.grid(row=1, column=x)                                                        #Positionnement du bouton grâce au gestionnaire .grid()
x+=1
b2 = Button(frameBouton, text= "Rechercher", width=12, command=search_command)
b2.grid(row=1, column=x)
x+=1
b3 = Button(frameBouton, text= "Ajouter", width=12, command=add_command)
b3.grid(row=1, column=x)
x+=1
b4 = Button(frameBouton, text= "Modifier", width=12, command=update_command)
b4.grid(row=1, column=x)
x+=1
b5 =Button(frameBouton, text= "Supprimer", width=12, command=delete_command)
b5.grid(row=1, column=x)
x+=1
b6 = Button(frameBouton, text= "Fermer", width=12, command=window.destroy)     #commande "window.destroy" qui ferme la fenêtre
b6.grid(row=1, column=x)
x+=1

#NOM DE CHAQUES CHAMPS DE SAISIE

l1 = Label(frameLabel, text="N° Poste")                                         #Widget "Label" ( qui permet d'afficher des lignes de texte ou un image ), le cadre correspondant, et le texte qu'on veut afficher
l1.grid(row=3,column=0)                                                         #Positionnement du texte grâce au gestionnaire .grid()

l2 = Label(frameLabel, text="N° Salle")
l2.grid(row=5,column=0)

l3 = Label(frameLabel, text="Système d'exploitation")
l3.grid(row=7,column=0)

l4 = Label(frameLabel, text="Marque")
l4.grid(row=9,column=0)

l5 = Label(frameLabel, text="Date d'achat")
l5.grid(row=11,column=0)

l6 = Label(frameLabel, text="Processeur")
l6.grid(row=13,column=0)

l7 = Label(frameLabel, text="RAM")
l7.grid(row=15,column=0)

l8 = Label(frameLabel, text="Carte graphique")
l8.grid(row=17,column=0)

l9 = Label(frameLabel, text="Taille ecran")
l9.grid(row=19,column=0)

l10 = Label(frameLabel, text="Stockage Disque Dur")
l10.grid(row=21,column=0)

l11 = Label(frameLabel, text="Stockage SSD")
l11.grid(row=23,column=0)

l12 = Label(frameLabel, text="Wi-Fi")
l12.grid(row=25,column=0)

l13 = Label(frameLabel, text="Bluetooth")
l13.grid(row=27,column=0)

l14 = Label(frameLabel, text="Nombre de ports USB")
l14.grid(row=29,column=0)

l15 = Label(frameLabel, text="Lecteur/Graveur CD")
l15.grid(row=31,column=0)

l16 = Label(frameLabel, text="Présence et/ou date d'expiration SolidWorks")
l16.grid(row=33,column=0)

l17 = Label(frameLabel, text="Présence et/ou date d'expiration Proteus")
l17.grid(row=35,column=0)

#CHAQUE CHAMPS DE SAISIE

poste_text = StringVar()                                  #lier le widget d'entrée à l'instance Stringvar et définir le texte d'entrée via cette variable
e1 = Entry(frameLabel, textvariable= poste_text)          #Widget "Entry" de tk, le cadre correspondant, et l'argument
e1.grid(row=4, column=0)                                  #Positionnement du champs de saisie grâce au gestionnaire .grid()

salle_text = StringVar()
e2 = Entry(frameLabel, textvariable= salle_text)
e2.grid(row=6, column=0)

os_text = StringVar()
e3 = Entry(frameLabel, textvariable= os_text)
e3.grid(row=8, column=0)

brand_text = StringVar()
e4 = Entry(frameLabel, textvariable= brand_text)
e4.grid(row=10, column=0)

date_text = StringVar()
e5 = Entry(frameLabel, textvariable= date_text)
e5.grid(row=12, column=0)

cpu_text = StringVar()
e6 = Entry(frameLabel, textvariable= cpu_text)
e6.grid(row=14, column=0)

ram_text = StringVar()
e7 = Entry(frameLabel, textvariable= ram_text)
e7.grid(row=16, column=0)

gpu_text = StringVar()
e8 = Entry(frameLabel, textvariable= gpu_text)
e8.grid(row=18, column=0)

screen_text = StringVar()
e9 = Entry(frameLabel, textvariable= screen_text)
e9.grid(row=20, column=0)

hdd_text = StringVar()
e10 = Entry(frameLabel, textvariable= hdd_text)
e10.grid(row=22, column=0)

ssd_text = StringVar()
e11 = Entry(frameLabel, textvariable= ssd_text)
e11.grid(row=24, column=0)

wifi_text = StringVar()
e12 = Entry(frameLabel, textvariable= wifi_text)
e12.grid(row=26, column=0)

bluetooth_text = StringVar()
e13 = Entry(frameLabel, textvariable= bluetooth_text)
e13.grid(row=28, column=0)

usbports_text = StringVar()
e14 = Entry(frameLabel, textvariable= usbports_text)
e14.grid(row=30, column=0)

cdplayer_text = StringVar()
e15 = Entry(frameLabel, textvariable= cdplayer_text)
e15.grid(row=32, column=0)

solidworks_text = StringVar()
e16 = Entry(frameLabel, textvariable= solidworks_text)
e16.grid(row=34, column=0)

proteus_text = StringVar()
e17 = Entry(frameLabel, textvariable= proteus_text)
e17.grid(row=36, column=0)

frameTexte.pack(side=TOP)                   #emplacement de chaque frame
frameBouton.pack(side=TOP)
frameListbox.pack(side=RIGHT)
frameLabel.pack(side=LEFT)
frameScroll.pack(side=RIGHT)
list1 = Listbox(frameListbox, height=44, width=140)          #widget "Listbox", le cadre, la hauteur, et la largeur
list1.bind("<<ListboxSelect>>", get_selected_row)            #permet d'afficher les informations quand on selectionne une des lignes
list1.pack()
sb1 = Scrollbar(frameScroll)                                 #widget "Scrollbar"
sb1.pack()
list1.configure(yscrollcommand=sb1.set)                      #liaison entre la liste et sa scrollbar
sb1.configure(command=list1.yview)


window.mainloop()