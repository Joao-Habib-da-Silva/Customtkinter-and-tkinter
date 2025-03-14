import customtkinter as custom
janela = custom.CTk()
def but():
   print("Agua")
botao = custom.CTkButton(janela, text="Botao", command=but, fg_color="red", hover_color="blue")
botao.pack()
janela.mainloop()
