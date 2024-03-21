import os
import tkinter.messagebox
#biblioteca Tkinter
from tkinter import*

#biblioteca pillow
from PIL import Image,ImageTk

#pygame

import pygame
from pygame import mixer



Dark_Turquoise = "#7093DB"
Medium_Slate_Blue = "#7F00FF"
thistle ="#D8BFD8"
steelblue= "#236B8E"
cinza = "#708090"
branco = "#feffff"
preto = "#2e2d2c"
khaki = "#F0E68C"
lawngreen ="#7CFC00"
deepskyblue ="#00BFFF"
lightSteelBlue="#B0C4DE"
#criando janela com tkinter
janela = Tk()
janela.title("Hashfy")
janela.geometry('300x500')
janela.configure(background=Dark_Turquoise)
janela.resizable(width=False,height=False)


#divisoes(frames)
div_esquerda = Frame(janela,width=120,height=120,bg=steelblue)
div_esquerda.grid(row=0,column=0,pady=1,padx=1,sticky=None)

div_direita = Frame(janela,width=180,height=300,bg=branco)
div_direita.grid(row=0,column=1,pady=0,padx=1,sticky=None)

div_baixo = Frame(janela,width=300,height=300,bg=lightSteelBlue)
div_baixo.grid(row=1,column=0,columnspan=3,pady=1,padx=0,sticky=None)

div_inferior = Frame(janela,width=300,height=100,bg=khaki)
div_baixo.grid(row=3,column=0,pady=2,padx=1,sticky=None)

#configurando o div_esquerda
listen = Image.open('music.png')
listen = listen.resize((130,130))
listen = ImageTk.PhotoImage(listen)
esquerda_logo = Label(div_esquerda,height=130,image=listen,compound=LEFT,padx=0,anchor='center')
esquerda_logo.place(x=0,y=0)

def playMusic():
    tocando = listbox.get(ACTIVE)
    baixo_logo['text'] = tocando
    mixer.music.load(tocando)
    mixer.music.set_volume(0.5)
    mixer.music.play()


mixer.init()


def volume_down():
    volume_atual = pygame.mixer.music.get_volume()
    volume_atual-= 0.125
    pygame.mixer.music.set_volume(volume_atual)

def volume_up():
    volume_atual = pygame.mixer.music.get_volume()
    volume_atual +=0.125
    pygame.mixer.music.set_volume(volume_atual)

def stopMusic():
    tocando=listbox.get(ACTIVE)
    mixer.music.pause()


def resumeMusic():
    tocando = baixo_logo['text']
    mixer.music.unpause()

def proxMusic():
    tocando = baixo_logo['text']
    pos = musicas.index(tocando)

    if pos == len(musicas)-1:
        tkinter.messagebox.showwarning(title='Aviso',message='Não há músicas após essa')
    else:
        pos += 1
        tocando = musicas[pos]
        mixer.music.load(tocando)
        mixer.music.play()

        listbox.delete(0,END)

        mostrar()

        listbox.select_set(pos)
        listbox.config(selectmode=SINGLE)
        baixo_logo['text'] = tocando




def anteriorMusic():
    if baixo_logo['text'] == 'Player Pausado':
        tkinter.messagebox.showwarning(title='Aviso',message='Despause o player primero')
    else:
        tocando = baixo_logo['text']
        pos = musicas.index(tocando)
        pos-=1
        tocando = musicas[pos]
        mixer.music.load(tocando)
        mixer.music.play()

        listbox.delete(0,END)
        mostrar()
        listbox.select_set(pos)
        listbox.config(selectmode=SINGLE)
        baixo_logo['text'] = tocando




#configurando o div_direira
listbox = Listbox(div_direita,width=22,height=10,selectmode=SINGLE,font=('arial 10 bold'),bg=Dark_Turquoise,fg=preto)
listbox.grid(row=0,column=0)
scButton = Scrollbar(div_direita)
scButton.grid(row=0,column=1,sticky=NSEW)
listbox.config(yscrollcommand=scButton.set)
scButton.config(command=listbox.yview)






#configurando o div_baixo
baixo_logo = Label(div_baixo,text="Escolha uma música",width=50,justify=LEFT,anchor='nw',font=('ivy 10'),bg=branco,fg=preto)
baixo_logo.place(x=0,y=1)


#botão anterior


anterior = Image.open('back.png')
anterior = anterior.resize((60,60))
anterior = ImageTk.PhotoImage(anterior)

buttom_anterior = Button(div_baixo,command=anteriorMusic,image=anterior,width=60,height=60,font=('ivy 10'),relief=RAISED,overrelief=RIDGE,bg=branco)
buttom_anterior.place(x=-5,y=70)


#botão pause
pause1 = Image.open('pause.png')
pause1 = pause1.resize((60,60))
pause1 = ImageTk.PhotoImage(pause1)

buttom_pause = Button(div_baixo,command=stopMusic,image=pause1,width=60,height=60,relief=RAISED,overrelief=RIDGE,bg=branco,fg=preto)
buttom_pause.place(x=80,y=170)


#botão despause

resume = Image.open('unpause2.png')
resume = resume.resize((60,60))
resume = ImageTk.PhotoImage(resume)

buttom_play = Button(div_baixo,image=resume,command=resumeMusic,width=60,height=60,relief=RAISED,overrelief=RIDGE,bg=branco,fg=preto)
buttom_play.place(x=160,y=170)

#botão play

play = Image.open('resume.png')
play = play.resize((60,60))
play = ImageTk.PhotoImage(play)

buttom_play = Button(div_baixo,image=play,command=playMusic,width=80,height=80,relief=RAISED,overrelief=RIDGE,bg=branco,fg=preto)
buttom_play.place(x=110,y=50)


#botão forward
avanco = Image.open('avanço.png')
avanco= avanco.resize((60,60))
avanco = ImageTk.PhotoImage(avanco)

buttom_avanco = Button(div_baixo,command=proxMusic,image=avanco,width=60,height=60,relief=RAISED,overrelief=RIDGE,bg=branco,fg=preto)
buttom_avanco.place(x=237,y=70)

#botão volume UP
up = Image.open('volumeUp.png')
up = up.resize((40,40))
up = ImageTk.PhotoImage(up)

buttom_Up = Button(div_baixo,command=volume_up,image=up,width=40,height=40,relief=RAISED,overrelief=RIDGE,bg=branco,fg=preto)
buttom_Up.place(x=240,y=240)


#botão volume down
down =Image.open('volumeDown.png')
down = down.resize((40,40))
down = ImageTk.PhotoImage(down)

buttom_down = Button(div_baixo,command=volume_down,image=down,width=40,height=40,relief=RAISED,overrelief=RIDGE,bg=branco,fg=preto)
buttom_down.place(x=10,y=240)



#lidando com a musica

os.chdir(r'C:\Users\Miguel\PycharmProjects\pythonMusicPlayer\Music')
musicas = os.listdir()

def mostrar():
    for elem in musicas:
        listbox.insert(END,elem)

mostrar()
janela.mainloop()
