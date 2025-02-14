import tkinter as tk
import random

def move_no_button():
    """Mueve el botón 'No' a una posición aleatoria dentro de la ventana."""
    x = random.randint(50, 250)
    y = random.randint(50, 250)
    no_button.place(x=x, y=y)

def on_yes():
    """Muestra un mensaje cuando se presiona 'Sí'."""
    label.config(text="¡Sabía que dirías que sí! ❤️")
    yes_button.place_forget()
    no_button.place_forget()

# Crear la ventana principal
root = tk.Tk()
root.title("San Valentín 💖")
root.geometry("400x300")

# Crear un label con la pregunta
label = tk.Label(root, text="¿Quieres ser mi San Valentín?", font=("Arial", 14))
label.pack(pady=20)

# Botón "Sí"
yes_button = tk.Button(root, text="Sí", font=("Arial", 12), bg="lightgreen", command=on_yes)
yes_button.place(x=100, y=150)

# Botón "No" (se moverá)
no_button = tk.Button(root, text="No", font=("Arial", 12), bg="lightcoral", command=move_no_button)
no_button.place(x=200, y=150)

# Ejecutar la aplicación
root.mainloop()
