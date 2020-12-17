# -*-coding:Latin-1-*
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *

email_regex = re.compile(r"[\w\.-]+@[\w\.-]+")
phone_num_regex = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
url_regex_https = re.compile(r"https?://www\.?\w+\.\w+")
url_regex = re.compile(r"http?://www\.?\w+\.\w+")

#recuperation et affichage des mails
def extraireMail():
    entry2.delete('1.0',END)
    textes = str(entry1.get('1.0',END))
    resultats = email_regex.findall(textes)
    num_resultat = len(resultats)
    result = '\nNous avons trouvé {} mails :{}'.format(num_resultat,resultats)
    entry2.insert(END,result)

#recuperation et affichage des numeros de telephone
def extraireNumero():
    entry2.delete('1.0',END)
    textes = str(entry1.get('1.0',END))
    resultats = phone_num_regex.findall(textes)
    num_resultat = len(resultats)
    result = '\nNous avons trouvé {} numeros de telephone :{}'.format(num_resultat,resultats)
    entry2.insert(END,result)

#recuperation et affichage des URL
def extraireUrl():
    entry2.delete('1.0',END)
    textes = str(entry1.get('1.0',END))
    resultats = url_regex_https.findall(textes)
    num_resultat = len(resultats)
    result = '\nNous avons trouvé {} de lien https :{}'.format(num_resultat,resultats)
    entry2.insert(END,result)

#Initialisation de la fenetre principal
fenetre = Tk()

fenetre.title('Fandr\'s app')
fenetre.minsize(950,555)
fenetre.maxsize(950,555)
fenetre.iconbitmap('icon.ico')
fenetre.config(background='#ffffff')
imageEveloppe = PhotoImage(file='email.png').zoom(5).subsample(20)

#titre
frameTitre = Frame(fenetre,bg='#a99bff',relief=SUNKEN,bd=0,highlightthickness=0)
titre = Label(frameTitre,text='Extracteur Mail,Numero,Url',bg='#ffffff',bd=0,font=("Arial Black",15))
titre.pack(expand=YES)
frameTitre.pack(expand=YES)

# Canva image de fond
canvaEnveloppe = Canvas(fenetre,width=950,height=550,bg='#ffffff',bd=0,highlightthickness=0)
canvaEnveloppe.pack(expand=YES,fill='both')
canvaEnveloppe.create_image(410,110,image=imageEveloppe,anchor='nw')

label = Label(canvaEnveloppe)
labelc = canvaEnveloppe.create_text(20,5,anchor='nw',text="Entrez le texte dans cette case:",font=('Eras Demi ITC',10))

#Input et out put scrolled text
entry1 = ScrolledText(fenetre,width=45,height=30)
entry2 = ScrolledText(fenetre,width=45,height=30)

boutonMail = Button(text='Extraire mail',font=('Arial Black',8),command=extraireMail)
boutonNumero = Button(text='Extraire numero',font=('Arial Black',8),command=extraireNumero)
boutonUrl = Button(text='Extraire URL',font=('Arial Black',8),command=extraireUrl)

entry1Canva = canvaEnveloppe.create_window(10,20,anchor='nw',window=entry1)
entry2Canva = canvaEnveloppe.create_window(550,20,anchor='nw',window=entry2)

boutonM = canvaEnveloppe.create_window(425,247,anchor='nw',window=boutonMail)
boutonN = canvaEnveloppe.create_window(415,290,anchor='nw',window=boutonNumero)
boutonU = canvaEnveloppe.create_window(425,330,anchor='nw',window=boutonUrl)

copyRight = Label(fenetre,text="©CopyRight RAVELOHARISON Fandresena")
copyrightLabel = canvaEnveloppe.create_text(720,508,anchor='nw',text="©CopyRight RAVELOHARISON Fandresena")


fenetre.mainloop()