import customtkinter as ctk
from random import randint
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Configuração do tema e aparencia
ctk.set_appearance_mode("System") # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue") # Temas: "blue" (padrão), "green", "dark-blue"

# Inicializa a janela principal
root = ctk.CTk()
root.geometry("520x380")
root.title("Gerador de Senha")

# Tenta carregar a imagem do ícone
try:
    icon_path = resource_path("senha1.ico")
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)
except Exception as e:
    print(f"Erro ao carregar o ícone: {e}")

# Função para gerar uma nova senha aleatória
def rand():
    pw_length = my_entry.get()
    my_entry.delete(0, ctk.END)
    pw_length = int(pw_length) if pw_length else 0
    my_password = "".join([chr(randint(33, 125)) for _ in range(pw_length)])
    pw_entry.delete(0, ctk.END)
    pw_entry.insert(0, my_password)
    pw_entry.configure(fg="black")

# Função para copiar a senha gerada para a área de transferência
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Função para limpar os campos de entrada
def clear_entry():
    my_entry.delete(0, ctk.END)
    pw_entry.delete(0, ctk.END)

# Função para validar o comprimento máximo do input
def validate_length(input):
    if input.isdigit() and len(input) <= 2 and int(input) <= 32:
        return True
    elif input == "":
        return True
    else:
        return False

# Define a regra de validação para o Entry
validate_command = root.register(validate_length)

# Cria o Frame para input do comprimento da senha
my_frame = ctk.CTkFrame(root)
my_frame.pack(pady=20)

# Label para o input do comprimento da senha
ctk.CTkLabel(my_frame, text="Quantos caracteres (Máximo 32)?", font=("Helvetica", 16)).pack(pady=10)

# Entry para input do comprimento da senha
my_entry = ctk.CTkEntry(my_frame, font=("Helvetica", 24), validate="key", validatecommand=(validate_command, "%P"))
my_entry.pack(pady=20)

# Entry para exibir a senha gerada
pw_entry = ctk.CTkEntry(root, font=("Helvetica", 24), justify="center", width=500)
pw_entry.pack(pady=20)

# Carrega as imagens para os botões
try:
    create_image = ctk.CTkImage(light_image=Image.open(resource_path("create.png")), dark_image=Image.open(resource_path("create.png")), size=(20, 20))
    copy_image = ctk.CTkImage(light_image=Image.open(resource_path("copy.png")), dark_image=Image.open(resource_path("copy.png")), size=(20, 20))
    clean_image = ctk.CTkImage(light_image=Image.open(resource_path("clean.png")), dark_image=Image.open(resource_path("clean.png")), size=(20, 20))
except Exception as e:
    print(f"Não foi possível carregar uma ou mais imagens dos botões: {e}")
    create_image = copy_image = clean_image = None

# Botão para gerar senhas fortes (verde)
# Create a separate frame for the buttons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=20)

# Create the buttons inside the button frame
my_button = ctk.CTkButton(button_frame, text="Gerar senha forte", command=rand, image=create_image, fg_color="#4CAF50", hover_color="#45A049")
my_button.grid(row=0, column=0, padx=10)

clip_button = ctk.CTkButton(button_frame, text="Copiar", command=clipper, image=copy_image, compound="left", font=("Helvetica", 16), fg_color="#FFC300", hover_color="#FF5733")
clip_button.grid(row=0, column=1, padx=10)

clear_button = ctk.CTkButton(button_frame, text="Limpar", command=clear_entry, image=clean_image, compound="left", font=("Helvetica", 16), fg_color="#FF9800", hover_color="#F57C00")
clear_button.grid(row=0, column=2, padx=10)

# Inicia o loop principal da aplicação
root.mainloop()
