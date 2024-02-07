import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Thomas
apellido: Esses
---
Ejercicio: entrada_salida_08
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, calcular y mostrar el resto de la división entre ambos números, utilizando el Dialog Alert. 
Ej: "El resto de dividir 7 por 2 es: 1" 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        operador_a = int(self.txt_operador_a.get())
        operador_b = int(self.txt_operador_b.get())
        
        Resultado = operador_a % operador_b
        mensaje = f"El resto de dividir {operador_a} por {operador_b} es:{Resultado}"
        alert("Resultado", mensaje)
           
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()