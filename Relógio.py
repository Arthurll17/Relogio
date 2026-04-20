import tkinter as tk
from time import strftime

#Atualização
def atualizar_relogio():
    hora = strftime("%H: %M: %S")
    rotulo.config(text=hora)
    rotulo.after(1000, atualizar_relogio)  # Atualiza a cada 1 segundo
#Janela
janela = tk.Tk()
janela.title ("Relógio")
janela.geometry("250x150")  #Tamanho da janela

rotulo = tk.Label(janela, font=("Arial", 40), bg= "gray", fg= "blue" \
"")
rotulo.pack(expand= True)

atualizar_relogio()

#Agir como pop-up
janela.attributes("-topmost", True)

janela.mainloop()