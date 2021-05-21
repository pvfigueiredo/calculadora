import tkinter as tk
import webbrowser
from tkinter import StringVar, font
from tkinter.constants import BOTH, GROOVE, LEFT, SE
from calculadora.calculadora import Calculadora
from constantes import Constantes


class CalculadoraView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.equacao = StringVar()
        self.equacao.set(0)
        self.var = ""
        self.clr_label = False
        self.pack()
        self.cria_btn_rows()
        self.butoes_numericos()
    
    def cria_btn_rows(self):
        self.label_row = tk.Frame(self)
        self.label_row.pack(expand=True, fill=BOTH)

        self.btn_row4 = tk.Frame(self)    
        self.btn_row4.pack(expand=True, fill=BOTH)

        self.btn_row3 = tk.Frame(self)
        self.btn_row3.pack(expand=True, fill=BOTH)       
        
        self.btn_row2 = tk.Frame(self)
        self.btn_row2.pack(expand=True, fill=BOTH)

        self.btn_row1 = tk.Frame(self)
        self.btn_row1.pack(expand=True, fill=BOTH)        

        self.btn_row0 = tk.Frame(self)
        self.btn_row0.pack(expand=True, fill=BOTH)

    def get_font(self):
        return ("Verdana", 18, "bold")
    
    def valida_digitos(self):
        if len(self.var) > 10:
            self.clr_label = True
            self.var = "Muito número!"
            self.equacao.set(self.var)

    def add_valor(self, valor: str):
        if self.clr_label and not valor in Constantes.OPERADORES() :
            self.clear_label()
        self.var += valor
        self.equacao.set(self.var)
        self.clr_label = False
        self.valida_digitos()

    def back_space(self):
        self.var = self.var[:-1]
        self.equacao.set(self.var)
        if self.var == "":
            self.equacao.set("0")    
    
    def clear_label(self):
        self.var = ""
        self.equacao.set("0")
        self.clr_label = False

    def calcula_resultado(self):
        if self.equacao.get() == Constantes.COD():
            webbrowser.open_new(url=Constantes.URL())
            self.clr_label = True
            return
        self.var = str(Calculadora.calcula(expressao=self.equacao.get()))
        self.equacao.set(self.var)
        self.clr_label = True
    
    def butoes_numericos(self):
        self.label = tk.Label(self.label_row, anchor=SE, font=("Verdana", 22), textvariable=self.equacao, height=2)
        self.label.pack(expand=True, fill=BOTH)

        self.button_pow = tk.Button(self.btn_row4, text="x^y", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("**"))
        self.button_pow.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_clear = tk.Button(self.btn_row4, text="CE", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.clear_label())
        self.button_clear.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_bckspace = tk.Button(self.btn_row4, text="BACK", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.back_space())
        self.button_bckspace.pack(side=LEFT, expand=True, fill=BOTH)
        
        self.button7 = tk.Button(self.btn_row3, text="7", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("7"))
        self.button7.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button8 = tk.Button(self.btn_row3, text="8", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("8"))
        self.button8.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button9 = tk.Button(self.btn_row3, text="9", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("9"))
        self.button9.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_div = tk.Button(self.btn_row3, text="÷", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("/"))
        self.button_div.pack(side=LEFT, expand=True, fill=BOTH)
        
        self.button4 = tk.Button(self.btn_row2, text="4", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("4"))
        self.button4.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button5 = tk.Button(self.btn_row2, text="5", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("5"))
        self.button5.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button6 = tk.Button(self.btn_row2, text="6", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("6"))
        self.button6.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_multi = tk.Button(self.btn_row2, text="X", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("*"))
        self.button_multi.pack(side=LEFT, expand=True, fill=BOTH)

        self.button1 = tk.Button(self.btn_row1, text="1", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("1"))
        self.button1.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button2 = tk.Button(self.btn_row1, text="2", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("2"))
        self.button2.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button3 = tk.Button(self.btn_row1, text="3", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("3"))
        self.button3.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_sub = tk.Button(self.btn_row1, text="-", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("-"))
        self.button_sub.pack(side=LEFT, expand=True, fill=BOTH)
    
        self.button0 = tk.Button(self.btn_row0, text="0", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("0"))
        self.button0.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_virg = tk.Button(self.btn_row0, text=",", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("."))
        self.button_virg.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_resultado = tk.Button(self.btn_row0, text="=", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.calcula_resultado())
        self.button_resultado.pack(side=LEFT, expand=True, fill=BOTH)

        self.button_soma = tk.Button(self.btn_row0, text="+", font=self.get_font(), relief=GROOVE, background="gray", width=3, command= lambda: self.add_valor("+"))
        self.button_soma.pack(side=LEFT, expand=True, fill=BOTH)

    def press(self, botao):
        self.expressao = self.expressao + str(botao)

if __name__ == "__main__":
   root = tk.Tk()
   root.title("Calculadora")
   root.geometry("240x320")
   root.resizable(height=False, width=False) 
   app = CalculadoraView(master=root)
   app.mainloop()