
import tkinter as tk 
from tkinter import messagebox

def verificar():
    resposta = entrada.get().strip().lower()
    if resposta in ["homem", "ser humano", "o homem","humano"]:
        messagebox.showinfo("Vitória!!!!"," Parabéns! VocÊ venceu a Esfinge !!!!")
    else:
        messagebox.showerror("Derrota"," Parabéns! VocÊ venceu a Esfinge !!!!")    
        
        
        
        
janela = tk.Tk()
janela.title("O Enigma da esfinge")
janela.geometry("500x300")
janela.config(bg="black")


titulo = tk.Label(janela, text=" O Grande Enigma da Esfinge", font=("Arial", 18, "bold"), fg="gold", bg="black")
titulo.pack(pady=10)

texto = """Qual é o animal que de manhã anda com quatro patas , ao meio-dia com duas , e á noite com três?"""
label_enigma = tk.Label(janela, text=texto,font=("Arial",12), fg="white", bg="black", wraplength=450)
label_enigma.pack(pady=20)

entrada = tk.Entry(janela, font=("Arial",14), width=30)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Responder", font=("Arial",14), bg="gold", command=verificar)
botao.pack(pady=10)


janela.mainloop()