from tkinter import*
from math import sqrt, pow
import random 

tela = Tk ()

final1 = StringVar ()
final2 = StringVar ()
final3 = StringVar ()

__autor__ = "Jeremy Djerry"


class calcula ():
      
      def Um (self):
            self.entry.insert(50, "1")
      
      def Dois (self):
            self.entry.insert(50, "2")
      
      def Tres (self):
            self.entry.insert(50, "3")
      
      def Quatro (self):
            self.entry.insert(50, "4")

      def Cinco (self):
            self.entry.insert(50, "5")
      
      def Seis (self):
            self.entry.insert(50, "6")

     
      def Sete (self):
            self.entry.insert(50, "7")

      
      def Oito (self):
            self.entry.insert(50, "8")

      
      def Nove (self):
            self.entry.insert(50, "9")

     
      def Zero (self):
            self.entry.insert(50, "0")


      def Ponto (self):
            self.entry.insert(50, ".")
      
      def Adicao (self):
            self.entry.insert(50, "+")
      
      def Raiz (self):
            """
            Função que insere o
            valor '√' na entry.
            
            """
            try:
                  self.vazio = str(self.entry.get ())
                  self.raiz = (float(self.entry.get())**(0.5))
                  self.label9.configure (text = (self.raiz))
            except:
                  self.label9.configure (text = "Operação inválida!")
      
      
      def Parente_Esquerdo (self):
            self.entry.insert(10, "(")
      
      
      def Parente_Direito (self):
            self.entry.insert(10, ")")
      
      
      def Subtracao (self):
            self.entry.insert(10, "-")

      
      def Multiplicacao (self):
            self.entry.insert(10, "*")
      
      
      def Divisao (self):
            self.entry.insert(10, "/")
            
      
      
      def Deletar (self):
            self.entry.delete(len(self.entry.get()) - 1)

      
      def Clear (self):
            self.entry.delete (0, END)
            self.label9 = Label(self.entrada, text="", font = "Times 15", bg = "white", fg = '#999999', anchor= W)
            self.label9.place (relx = 0.01, rely = 0.70,relwidth = 0.9, relheight = 0.20)
      

final4 = IntVar ()
final5 = IntVar ()
final6 = IntVar ()

class resolve ():
      
      def Um1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "1")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "1")
            
            if (final6.get () == 1):
                  self.c.insert(50, "1")
            

      
      def Dois1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "2")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "2")
            
            if (final6.get () == 1):
                  self.c.insert(50, "2")
      
      
      def Tres1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "3")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "3")
            
            if (final6.get () == 1):
                  self.c.insert(50, "3")
      
      def Quatro1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "4")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "4")
            
            if (final6.get () == 1):
                  self.c.insert(50, "4")

      
      def Cinco1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "5")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "5")
            
            if (final6.get () == 1):
                  self.c.insert(50, "5")
      
      def Seis1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "6")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "6")
            
            if (final6.get () == 1):
                  self.c.insert(50, "6")

     
      def Sete1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "7")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "7")
            
            if (final6.get () == 1):
                  self.c.insert(50, "7")
                  

      
      def Oito1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "8")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "8")
            
            if (final6.get () == 1):
                  self.c.insert(50, "8")

      
      def Nove1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "9")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "9")
            
            if (final6.get () == 1):
                  self.c.insert(50, "9")
     
      def Zero1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "0")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "0")
            
            if (final6.get () == 1):
                  self.c.insert(50, "0")


      def Ponto1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, ".")
                  
            if (final5.get () == 1):
                  self.b.insert(50, ".")
            
            if (final6.get () == 1):
                  self.c.insert(50, ".")
      
      def Adicao1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "+")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "+")
            
            if (final6.get () == 1):
                  self.c.insert(50, "+")
      
     
      def Parente_Esquerdo1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "(")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "(")
            
            if (final6.get () == 1):
                  self.c.insert(50, "(")
      
      
      def Parente_Direito1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, ")")
                  
            if (final5.get () == 1):
                  self.b.insert(50, ")")
            
            if (final6.get () == 1):
                  self.c.insert(50, ")")
      
      
      def Subtracao1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "-")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "-")
            
            if (final6.get () == 1):
                  self.c.insert(50, "-")
            

      
      def Multiplicacao1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "*")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "*")
            
            if (final6.get () == 1):
                  self.c.insert(50, "*")
      
      
      def Divisao1 (self):
            if (final4.get () == 1):
                  self.a.insert(50, "/")
                  
            if (final5.get () == 1):
                  self.b.insert(50, "/")
            
            if (final6.get () == 1):
                  self.c.insert(50, "/")
      
      
      def Delete1 (self):
            if (final4.get () == 1):
                  self.a.delete(len(self.a.get()) - 1)
                  
            if (final5.get () == 1):
                  self.b.delete(len(self.b.get()) - 1)
            
            if (final6.get () == 1):
                  self.c.delete(len(self.c.get()) - 1)

      
      def Clear1 (self):
            self.a.delete (0, END)
            self.b.delete (0, END)
            self.c.delete (0, END)
            final1.set ("")
            final2.set ("")
            final3.set ("")



class Matematica (calcula, resolve):
      def __init__(self):
            self.tela = tela
            self.frame2_cor = "#555555"
            self.bt_cor = "#777777"
            self.cor_de_fundo = "#dfe3ee"
            self.cor_menu = "#253248"
            self.janela ()
            self.widgets_calculadora ()
            self.menus ()
            
            
            self.tela.mainloop ()

#--------------------------------                 
      def janela (self):
            self.tela.geometry ("720x1080")
            self.tela ['bg'] = self.cor_de_fundo
            self.tela.title ('Operações Matemáticas')
            self.cor = "#236557"

#--------------------------------
     
      def sair (self):
          self.tela.destroy ()
      
            

#--------------------------------           
      def equacao (self):
            self.equacao = Toplevel ()
            self.equacao.title ("Equação x²")
            self.equacao.geometry ("720x1080")
            self.equacao ['bg'] = self.cor_de_fundo
            self.widgets_equacao ()


#--------------------------------           
      def configuracoes (self):
            self.configuracoes = Toplevel ()
            self.configuracoes.title ("Configurações")
            self.configuracoes.geometry ("720x1080")
            self.configuracoes ['bg'] = self.cor_de_fundo
      

#--------------------------------     
      def menus (self):          
            self.meu_menu = Menu (self.tela, bg= self.cor_menu, fg = self.cor_de_fundo, font= "Times 7")

#--------------------------------     
            
            
            self.meu_menu.add_command (label="Equações x²", command = self.equacao)
            self.meu_menu.add_command (label="| Sair", command = self.sair)
            
            
            self.tela.config(menu=self.meu_menu)

#--------------------------------     
      def widgets_calculadora (self): 
           
            self.entrada = Frame (self.tela, bg = "white")
            
            self.entrada.place (relx = 0.026, rely = 0.0227, relwidth = 0.95, relheight = 0.415)
            
            self.entry = Entry(self.entrada, font = "Times 30", fg = "#777777")
            self.entry.place (relx = 0.0, rely = 0.0, relwidth = 0.9999, relheight = 0.999)
            self.entry.insert(0, "")
            self.entry.focus ()
            
            self.label9 = Label(self.entrada, text="", font = "Times 15", bg = "white", fg = '#999999', anchor= W)
            self.label9.place (relx = 0.01, rely = 0.70,relwidth = 0.9, relheight = 0.20)
             
#--------------------------------
            self.frame2 = Frame (self.tela, bg = "#555555")
            self.frame2.place (relx = 0.00, rely = 0.50, relwidth = 0.75, relheight = 0.5)
            

#--------------------------------  
# Area de botões        
#--------------------------------  
  
            # Botão limpar 
            self.CLR = Button (self.tela, text= "CLR", bg = self.bt_cor, font = "Times 9", fg = "white", command = self.Clear)
            self.CLR.place (relx = 0.75, rely = 0.499, relwidth = 0.25, relheight = 0.08)
            
            # Botão deletar 
            self.DEL = Button (self.tela, text= "DEL", bg = self.bt_cor, font = "Times 9", fg = "white", command= self.Deletar)
            self.DEL.place (relx = 0.75, rely = 0.578, relwidth = 0.25, relheight = 0.08)
            
            # Botão de multiplicação 
            self.multiplicacao = Button (self.tela, text= "×", bg = self.bt_cor, font = "Times 15", fg = "white", command=self.Multiplicacao)
            self.multiplicacao.place (relx = 0.75, rely = 0.729, relwidth = 0.25, relheight = 0.08)
            
            # Botão de divisão 
            self.divisao = Button (self.tela, text= "÷", bg = self.bt_cor, font = "Times 15", fg = "white", command=self.Divisao)
            self.divisao.place (relx = 0.75, rely = 0.65, relwidth = 0.25, relheight = 0.08)
            
            # Botão de subtração 
            self.subtracao = Button (self.tela, text= "-", bg = self.bt_cor, font = "Times 15", fg = "white", command=self.Subtracao)
            self.subtracao.place (relx = 0.75, rely = 0.808, relwidth = 0.25, relheight = 0.08)
            
            # Botão de Adição
            self.adicao = Button (self.tela, text= "+", bg = self.bt_cor, font = "Times 15", fg = "white", command=self.Adicao)
            self.adicao.place (relx = 0.75, rely = 0.887, relwidth = 0.25, relheight = 0.12)
            
            # Botão de Raíz quadrada 
            self.raiz = Button (self.tela, text= "√", bg = self.bt_cor, font = "Times 10", fg = "white", command=self.Raiz, highlightbackground=self.bt_cor)
            self.raiz.place (relx = 0.00, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            
            
            # Botão de potência 
            self.potencia = Button (self.tela, text= "x²", bg = self.bt_cor, font = "Times 10", fg = "white", command = self.equacao, highlightbackground=self.bt_cor)
            self.potencia.place (relx = 0.255, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            # Botão de parente_esquerdo 
            self.parente_esquerdo = Button (self.tela, text= "(", bg = self.bt_cor, font = "Times 10", fg = "white", command = self.Parente_Esquerdo, highlightbackground=self.bt_cor)
            self.parente_esquerdo.place (relx = 0.510, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            
            # Botao Parente Direito 
            self.raiz = Button (self.tela, text= ")", bg = self.bt_cor, font = "Times 10", fg = "white", command = self.Parente_Direito, highlightbackground=self.bt_cor)
            self.raiz.place (relx = 0.75, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            
#--------------------------------
            self.sete = Button (self.frame2, text = "7", font = "Times 20", fg = "white", bg = self.frame2_cor, command= self.Sete, highlightbackground=self.bt_cor)
            self.sete.place (relx = 0.00, rely = 0.00, relwidth = 0.349, relheight = 0.2499)
            
            self.oito = Button (self.frame2, text = "8", font = "Times 20", fg = "white", bg = self.frame2_cor, command = self.Oito, highlightbackground=self.bt_cor)
            self.oito.place (relx = 0.34, rely = 0.00, relwidth = 0.349, relheight = 0.2499)
            
            
            self.nove = Button (self.frame2, text = "9", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Nove, highlightbackground=self.bt_cor)
            self.nove.place (relx = 0.68, rely = 0.00, relwidth = 0.349, relheight = 0.2499)
            
            
            self.quatro = Button (self.frame2, text = "4", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Quatro)
            self.quatro.place (relx = 0.00, rely = 0.249, relwidth = 0.349, relheight = 0.2499)
            
            self.cinco = Button (self.frame2, text = "5", font = "Times 20", fg = "white", bg = self.frame2_cor, command= self.Cinco)
            self.cinco.place (relx = 0.34, rely = 0.249, relwidth = 0.349, relheight = 0.2499)
            
            self.seis = Button (self.frame2, text = "6", font = "Times 20", fg = "white", bg = self.frame2_cor, command= self.Seis)
            self.seis.place (relx = 0.68, rely = 0.249, relwidth = 0.349, relheight = 0.2499)
            
            
            self.um = Button (self.frame2, text = "1", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Um)
            self.um.place (relx = 0.00, rely = 0.4899, relwidth = 0.349, relheight = 0.2499)
            
            self.dois = Button (self.frame2, text = "2", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Dois)
            self.dois.place (relx = 0.34, rely = 0.489, relwidth = 0.349, relheight = 0.2499)
            
            self.tres = Button (self.frame2, text = "3", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Tres)
            self.tres.place (relx = 0.68, rely = 0.489, relwidth = 0.349, relheight = 0.2499)
            
            
            self.ponto = Button (self.frame2, text = ".", font = "Times 20", fg = "white", bg = self.frame2_cor, justify=CENTER, command= self.Ponto)
            self.ponto.place (relx = 0.00, rely = 0.73, relwidth = 0.349, relheight = 0.28)
            
            self.zero = Button (self.frame2, text = "0", font = "Times 20", fg = "white", bg = self.frame2_cor, command = self.Zero)
            self.zero.place (relx = 0.34, rely = 0.73, relwidth = 0.349, relheight = 0.28)
            
            self.igual = Button (self.frame2, text = "=", font = "Times 20", fg = "white", bg = self.frame2_cor, command= self.Igual)
            self.igual.place (relx = 0.68, rely = 0.73, relwidth = 0.349, relheight = 0.28)
      
     
      def Igual (self):
             #Metodo responsavel por fazer os cálculos matemáticos 
            try:
                  self.label9.configure(text=str(eval(self.entry.get())))
            
            except:
                self.label9.configure (text = "Operação inválida!") 


#--------------------------------

      def widgets_equacao (self):
            global final1, final2, final3
           
            self.entrada1 = Frame (self.equacao, bg = "white", bd = 1, relief = 'solid')
            
            self.entrada1.place (relx = 0.026, rely = 0.0227, relwidth = 0.95, relheight = 0.415)
            
            self.a = Entry(self.equacao, font = "Times 8", fg = self.cor, justify = CENTER)
            self.a.place (relx = 0.10, rely = 0.12, relwidth = 0.15, relheight = 0.05)
            
            self.b = Entry(self.equacao, font = "Times 8", fg = self.cor, justify = CENTER)
            self.b.place (relx = 0.43, rely = 0.12, relwidth = 0.15, relheight = 0.05)
            
            self.c = Entry(self.equacao, font = "Times 8", fg = self.cor, justify = CENTER)
            self.c.place (relx = 0.75, rely = 0.12, relwidth = 0.15, relheight = 0.05)
            
            self.saida1 = Label(self.entrada1, textvariable=final1, font = "Times 8 italic", bg = "white", fg = self.cor)
            self.saida1.place (relx = 0.00, rely = 0.55,relwidth = 0.9999, relheight = 0.15)
            
            
            self.saida2 = Label(self.entrada1, textvariable = final2, font = "Times 8 italic", bg = "white", fg = self.cor)
            self.saida2.place (relx = 0.00, rely = 0.70,relwidth = 0.9999, relheight = 0.15)
            
            self.saida3 = Label(self.entrada1, textvariable = final3, font = "Times 8 italic", bg = "white", fg = self.cor)
            self.saida3.place (relx = 0.00, rely = 0.85,relwidth = 0.9999, relheight = 0.15)
            
            # Check editor a
            self.check_a = Checkbutton (self.entrada1, variable = final4, bg = "white", fg = self.cor)
            self.check_a.place (relx = 0.11, rely = 0.40)

            # Check editor b
            self.check_b = Checkbutton (self.entrada1, variable = final5, bg = "white", fg = self.cor)
            self.check_b.place (relx = 0.465, rely = 0.40)
            
            # Check editor c
            self.check_c = Checkbutton (self.entrada1, variable = final6, bg = "white", fg = self.cor)
            self.check_c.place (relx = 0.799, rely = 0.40)

            self.valor_de_a = Label (self.equacao, text= 'a', font = "Times 9 italic", bg = 'white', fg = self.cor)
            self.valor_de_a.place (relx = 0.15, rely = 0.06)
            
            self.valor_de_b = Label (self.equacao, text= 'b', font = "Times 9 italic", bg = 'white', fg = self.cor)
            self.valor_de_b.place (relx = 0.4899, rely = 0.06)
         
            self.valor_de_c = Label (self.equacao, text= 'c', font = "Times 9 italic", bg = 'white', fg = self.cor)
            self.valor_de_c.place (relx = 0.80, rely = 0.06)         
             
#--------------------------------
            self.frame3 = Frame (self.equacao, bg = "#555555")
            self.frame3.place (relx = 0.00, rely = 0.50, relwidth = 0.75, relheight = 0.5)
            

#--------------------------------            
            # Botão eliminar 
            self.CLR1 = Button (self.equacao, text= "CLR", bg = self.bt_cor, font = "Times 9", fg = "white", command = self.Clear1)
            self.CLR1.place (relx = 0.75, rely = 0.499, relwidth = 0.25, relheight = 0.08)
            
            # Botão deletar 
            self.DEL1 = Button (self.equacao, text= "DEL", bg = self.bt_cor, font = "Times 9", fg = "white", command = self.Delete1)
            self.DEL1.place (relx = 0.75, rely = 0.578, relwidth = 0.25, relheight = 0.08)
            
            # Botão de multiplicação 
            self.multiplicacao1 = Button (self.equacao, text= "×", bg = self.bt_cor, font = "Times 15", fg = "white", command = self.Multiplicacao1)
            self.multiplicacao1.place (relx = 0.75, rely = 0.729, relwidth = 0.25, relheight = 0.08)
            
            # Botão de divisão 
            self.divisao1 = Button (self.equacao, text= "÷", bg = self.bt_cor, font = "Times 15", fg = "white", command= self.Divisao1)
            self.divisao1.place (relx = 0.75, rely = 0.65, relwidth = 0.25, relheight = 0.08)
            
            # Botão de subtração 
            self.subtracao1 = Button (self.equacao, text= "-", bg = self.bt_cor, font = "Times 15", fg = "white", command = self.Subtracao1)
            self.subtracao1.place (relx = 0.75, rely = 0.808, relwidth = 0.25, relheight = 0.08)
            # Botão de Adição
            self.adicao1 = Button (self.equacao, text= "+", bg = self.bt_cor, font = "Times 15", fg = "white", command=self.Adicao1)
            self.adicao1.place (relx = 0.75, rely = 0.887, relwidth = 0.25, relheight = 0.12)
            
            # Botão de Raíz quadrada 
            self.raiz1 = Button (self.equacao, text= "√", bg = self.bt_cor, font = "Times 10", fg = "white")
            self.raiz1.place (relx = 0.00, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            
            
            # Botão de potência 
            self.potencia1 = Button (self.equacao, text= "x²", bg = self.bt_cor, font = "Times 10", fg = "white")
            self.potencia1.place (relx = 0.255, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            # Botão de parente_esquerdo 
            self.parente_esquerdo1 = Button (self.equacao, text= "(", bg = self.bt_cor, font = "Times 10", fg = "white")
            self.parente_esquerdo1.place (relx = 0.510, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            
            # Botao Parente Direito 
            self.raiz1 = Button (self.equacao, text= ")", bg = self.bt_cor, font = "Times 10", fg = "white")
            self.raiz1.place (relx = 0.75, rely = 0.457, relwidth = 0.26, relheight = 0.045)
            
#--------------------------------
            
            self.sete1 = Button (self.frame3, text = "7", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Sete1)
            self.sete1.place (relx = 0.00, rely = 0.00, relwidth = 0.349, relheight = 0.2499)
            
            self.oito1 = Button (self.frame3, text = "8", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Oito1)
            self.oito1.place (relx = 0.34, rely = 0.00, relwidth = 0.349, relheight = 0.2499)
            
            self.nove1 = Button (self.frame3, text = "9", font = "Times 20", fg = "white", bg = self.frame2_cor, command = self.Nove1)
            self.nove1.place (relx = 0.68, rely = 0.00, relwidth = 0.349, relheight = 0.2499)
            
            
            self.quatro1 = Button (self.frame3, text = "4", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Quatro1)
            self.quatro1.place (relx = 0.00, rely = 0.249, relwidth = 0.349, relheight = 0.2499)
            
            self.cinco1 = Button (self.frame3, text = "5", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Cinco1)
            self.cinco1.place (relx = 0.34, rely = 0.249, relwidth = 0.349, relheight = 0.2499)
            
            self.seis1 = Button (self.frame3, text = "6", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Seis1)
            self.seis1.place (relx = 0.68, rely = 0.249, relwidth = 0.349, relheight = 0.2499)
            
            
            self.um1 = Button (self.frame3, text = "1", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Um1)
            
            self.um1.place (relx = 0.00, rely = 0.4899, relwidth = 0.349, relheight = 0.2499)
            
            self.dois1 = Button (self.frame3, text = "2", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Dois1)
            self.dois1.place (relx = 0.34, rely = 0.489, relwidth = 0.349, relheight = 0.2499)
            
            self.tres1 = Button (self.frame3, text = "3", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Tres1)
            self.tres1.place (relx = 0.68, rely = 0.489, relwidth = 0.349, relheight = 0.2499)
            
            
            self.ponto1 = Button (self.frame3, text = ".", font = "Times 20", fg = "white", bg = self.frame2_cor, justify=CENTER, command=self.Ponto1)
            self.ponto1.place (relx = 0.00, rely = 0.73, relwidth = 0.349, relheight = 0.28)
            
            self.zero1 = Button (self.frame3, text = "0", font = "Times 20", fg = "white", bg = self.frame2_cor, command=self.Zero1)
            self.zero1.place (relx = 0.34, rely = 0.73, relwidth = 0.349, relheight = 0.28)
            
            self.igual1 = Button (self.frame3, text = "=", font = "Times 20", fg = "white", bg = self.frame2_cor, command = self.Igual1)
            self.igual1.place (relx = 0.68, rely = 0.73, relwidth = 0.349, relheight = 0.28)
    
      
      def Igual1 (self):
            try:
                  self.a1 = int (self.a.get ())
                  self.b1 = int (self.b.get ())
                  self.c1 = int (self.c.get ()) 
                  if self.a1 == 0:
                        final1.set ("")
                        final2.set ("A equação não é do segundo grau")
                        final3.set ("")
                  if self.a1 > 0:
                        self.delta = self.b1**2 - 4*self.a1*self.c1
                        self.raíz = -self.b1 +- (self.delta**(1/2))/2*self.a1
                        self.raíz1 = -self.b1 +- self.delta/2*self.a1
                        self.x1 = (-self.b1 - self.delta)/2*self.a1
                        self.x2 = (-self.b1 + self.delta)/2*self.a1
                  self.delta = self.b1**2-4*self.a1*self.c1
                  if self.delta < 0:
                        final1.set ("")
                        final2.set ("A equação não tem solução em R")
                        final3.set ("")
            
                  if self.a1 > 0 and self.delta >= 0:
                        final1.set ("Delta = %s"%self.delta)
                        final2.set ("x1 = %s"%self.x1)
                        final3.set ("x2 = %s"%self.x2)

            except:
                  final2.set ("Preencha os espaços vazios!")


if __name__ == "__main__":
    Matematica ()