import customtkinter as custom
janela = custom.CTk()
custom.set_appearance_mode("sistem")
botao = custom.CTkButton(janela, text="Modo dark pressionado", fg_color="grey", hover_color="white", command="dark")
botao.pack()
botaolight = custom.CTkButton(janela, text="Modo Light pressionado", fg_color="yellow", hover_color="blue", command="light")
botaolight.pack()
def light():
    custom.set_appearance_mode("light")
def dark():
    custom.set_appearance_mode("dark")
janela.mainloop() 