from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

cor1 = "#ffffff" #branco
cor2 = "#000000" #preto
cor3 = "#091d42" #azul marinho
cor4 = "#4f4e4e" #cinza


janela = Tk()
janela.title("")
janela.geometry('250x400')
janela.configure(bg= cor2)
janela.resizable(width = False, height = False)

style = ttk.Style(janela)
style.theme_use('clam')

#Frames
frameCima= Frame(janela, width = 300, height = 50, bg = cor1, relief = "flat")
frameCima.grid(row = 0, column = 0)
frameMeio= Frame(janela, width = 300, height = 90, bg = cor4, relief = "flat")
frameMeio.grid(row = 1, column = 0)
frameBaixo= Frame(janela, width = 300, height = 290, bg = cor3, relief = "flat")
frameBaixo.grid(row = 2, column = 0)

#Logo
app_ = Label(frameCima, text = "Orçamento", compound = LEFT, padx = 5, relief = FLAT,
            anchor = NW, font = ("Verdana 20"), bg = cor1, fg = cor3)
app_.place(x = 0, y=0)

#abrindo imagem
app_img = Image.open('emoji_internet.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image = app_img, compound = LEFT, padx = 5, relief = FLAT,
                anchor = NW, font = ("Verdana 20"), bg = cor1, fg = cor3)
app_logo.place(x = 160, y = 0)

# Funcao
def calcular(): 
    # obtendo renda mensal
    renda_mensal = float(entry1.get())
    
    obter50porcento = (50/100) * renda_mensal
    obter30porcento = (30/100) * renda_mensal
    obter20porcento = (20/100) * renda_mensal

    label_necessidades['text']=("R$: {:,.2f}".format(obter50porcento))
    label_gastos['text']=("R$: {:,.2f}".format(obter30porcento))
    label_lazer['text']=("R$: {:,.2f} ".format(obter20porcento))


#frame meio
app_ = Label(frameMeio, text = "Insira sua renda mensal", relief = FLAT, anchor=NW,
            font= ("Ivy 10"), bg= cor1, fg = cor3)
app_.place(x=10, y=15)

app_linha1 = Label(frameCima, width = 300, relief = FLAT, anchor=NW, font= ("Ivy 1"),
                    bg= cor2, fg = cor1)
app_linha1.place(x=0,y=47)

entry1 = Entry(frameMeio, width = 10, font  = ('Ivy 10'), justify = CENTER, 
               relief = SOLID)
entry1.place(x = 10, y = 40)

btn_calcular = Button(frameMeio, text = "calcular".upper(), overrelief = RIDGE,
                command=calcular,anchor=NW, font= ("Ivy 7"), bg= cor1, fg = cor3)
btn_calcular.place(x=100, y=40)

#Frame baixo
app_ = Label(frameBaixo, text = "Seus números de 50% 30% e 20%", relief = FLAT,
            width=35, anchor=NW, font= ("Verdana 10"), bg= cor1, fg = cor3)
app_.place(x=0, y=0)

#necessidades
total_necessidades = Label(frameBaixo, text = "Necessidades:", relief = FLAT,
            width=35, anchor=NW, font= ("Verdana 10"), bg= cor3, fg = cor1)
total_necessidades.place(x=10, y=40)

label_necessidades= Label(frameBaixo, relief=FLAT, width=22, anchor= NW, font = ('Verdana 12'),bg =cor1,fg=cor2)
label_necessidades.place(x=10, y=75)

#gastos
total_gastos = Label(frameBaixo, text = "Gastos:", relief = FLAT,
            width=35, anchor=NW, font= ("Verdana 10"), bg= cor3, fg = cor1)
total_gastos.place(x=10, y=115)

label_gastos= Label(frameBaixo, relief=FLAT, width=22, anchor= NW, font = ('Verdana 12'),bg =cor1,fg=cor2)
label_gastos.place(x=10, y=145)

#lazer
total_lazer = Label(frameBaixo, text = "Lazer:", relief = FLAT,
            width=35, anchor=NW, font= ("Verdana 10"), bg= cor3, fg = cor1)
total_lazer.place(x=10, y=185)

label_lazer= Label(frameBaixo, relief=FLAT, width=22, anchor= NW, font = ('Verdana 12'),bg =cor1,fg=cor2)
label_lazer.place(x=10, y=215)



janela.mainloop()