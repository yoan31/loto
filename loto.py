#!/usr/bin/python3
import tkinter as tk
import random

class LotoApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel1.configure(height=200, padx=10, pady=10, width=200)
        self.toplevel1.resizable(False, False)
        self.toplevel1.title("Loto Pthon")
        self.labelframe_choix = tk.LabelFrame(self.toplevel1)
        self.labelframe_choix.configure(
            height=200, text='Mes numéros :', width=200)
        self.entry1 = tk.Entry(self.labelframe_choix)
        self.vi_1 = tk.IntVar()
        self.entry1.configure(textvariable=self.vi_1)
        self.entry1.grid(column=0, ipadx=5, padx=10, pady=5, row=0)
        self.entry2 = tk.Entry(self.labelframe_choix)
        self.vi_2 = tk.IntVar()
        self.entry2.configure(textvariable=self.vi_2)
        self.entry2.grid(column=1, padx=10, row=0)
        self.entry3 = tk.Entry(self.labelframe_choix)
        self.vi_3 = tk.IntVar()
        self.entry3.configure(textvariable=self.vi_3)
        self.entry3.grid(column=2, padx=10, row=0)
        self.entry4 = tk.Entry(self.labelframe_choix)
        self.vi_4 = tk.IntVar()
        self.entry4.configure(textvariable=self.vi_4)
        self.entry4.grid(column=0, ipadx=5, padx=10, pady=5, row=1)
        self.entry5 = tk.Entry(self.labelframe_choix)
        self.vi_5 = tk.IntVar()
        self.entry5.configure(textvariable=self.vi_5)
        self.entry5.grid(column=1, padx=10, row=1)
        self.entry6 = tk.Entry(self.labelframe_choix)
        self.vi_6 = tk.IntVar()
        self.entry6.configure(textvariable=self.vi_6)
        self.entry6.grid(column=2, padx=10, row=1)
        self.labelframe_choix.grid(
            column=0, ipady=5, padx=5, pady=5, row=0, rowspan=1)
        self.labelframe_choix.rowconfigure(0, pad=5)
        self.labelframe_tirage = tk.LabelFrame(self.toplevel1)
        self.labelframe_tirage.configure(
            height=200, text='Tirages :', width=200)
        self.entry_r1 = tk.Entry(self.labelframe_tirage)
        self.vi_r1 = tk.IntVar()
        self.entry_r1.configure(textvariable=self.vi_r1)
        self.entry_r1.grid(column=0, ipadx=5, padx=10, pady=5, row=0)
        self.entry_r2 = tk.Entry(self.labelframe_tirage)
        self.vi_r2 = tk.IntVar()
        self.entry_r2.configure(textvariable=self.vi_r2)
        self.entry_r2.grid(column=1, padx=10, row=0)
        self.entry_r3 = tk.Entry(self.labelframe_tirage)
        self.vi_r3 = tk.IntVar()
        self.entry_r3.configure(textvariable=self.vi_r3)
        self.entry_r3.grid(column=2, padx=10, row=0)
        self.entry_r4 = tk.Entry(self.labelframe_tirage)
        self.vi_r4 = tk.IntVar()
        self.entry_r4.configure(textvariable=self.vi_r4)
        self.entry_r4.grid(column=0, ipadx=5, padx=10, pady=5, row=1)
        self.entry_r5 = tk.Entry(self.labelframe_tirage)
        self.vi_r5 = tk.IntVar()
        self.entry_r5.configure(textvariable=self.vi_r5)
        self.entry_r5.grid(column=1, padx=10, row=1)
        self.entry_r6 = tk.Entry(self.labelframe_tirage)
        self.vi_r6 = tk.IntVar()
        self.entry_r6.configure(textvariable=self.vi_r6)
        self.entry_r6.grid(column=2, padx=10, row=1)
        self.button1 = tk.Button(self.labelframe_tirage)
        self.button1.configure(text='1 an de tirage')
        self.button1.grid(column=0, pady=10, row=2)
        self.button1.configure(command=lambda: self.f_tirage(156))
        self.button2 = tk.Button(self.labelframe_tirage)
        self.button2.configure(text='1 vie de tirage')
        self.button2.grid(column=1, row=2)
        self.button2.configure(command=lambda: self.f_tirage(15600))
        self.button3 = tk.Button(self.labelframe_tirage)
        self.button3.configure(text="jusqu'a gagner")
        self.button3.grid(column=2, row=2)
        self.button3.configure(command=self.f_tiragevictoire)
        self.labelframe_tirage.grid(column=0, ipady=5, padx=5, pady=5, row=1)
        self.labelframe_tirage.rowconfigure(0, pad=5)
        self.labelfame_stats = tk.LabelFrame(self.toplevel1)
        self.labelfame_stats.configure(
            height=200, text='Statistiques : ', width=200)
        self.label1 = tk.Label(self.labelfame_stats)
        self.label1.configure(text='Nombre de tirage :')
        self.label1.grid(column=0, ipadx=10, padx=65, row=0)
        self.label2 = tk.Label(self.labelfame_stats)
        self.vi_nbrtirage = tk.IntVar()
        self.label2.configure(textvariable=self.vi_nbrtirage)
        self.label2.grid(column=1, ipadx=10, padx=50, row=0)
        self.label3 = tk.Label(self.labelfame_stats)
        self.label3.configure(text='Cout en € :')
        self.label3.grid(column=0, row=1)
        self.label4 = tk.Label(self.labelfame_stats)
        self.vi_coutcumule = tk.IntVar()
        self.label4.configure(textvariable=self.vi_coutcumule)
        self.label4.grid(column=1, row=1)
        self.label5 = tk.Label(self.labelfame_stats)
        self.label5.configure(text='Nombre de bon numéros :')
        self.label5.grid(column=0, row=2)
        self.label6 = tk.Label(self.labelfame_stats)
        self.vi_nbrbonnum = tk.IntVar()
        self.label6.configure(textvariable=self.vi_nbrbonnum)
        self.label6.grid(column=1, row=2)
        self.label7 = tk.Label(self.labelfame_stats)
        self.label7.configure(text='Nombres de 3 bon numéros :')
        self.label7.grid(column=0, row=3)
        self.label8 = tk.Label(self.labelfame_stats)
        self.vi_3bn = tk.IntVar()
        self.label8.configure(textvariable=self.vi_3bn)
        self.label8.grid(column=1, row=3)
        self.label9 = tk.Label(self.labelfame_stats)
        self.label9.configure(text='Nombres de 4 bon numéros :')
        self.label9.grid(column=0, row=4)
        self.label10 = tk.Label(self.labelfame_stats)
        self.vi_4bn = tk.IntVar()
        self.label10.configure(textvariable=self.vi_4bn)
        self.label10.grid(column=1, row=4)
        self.label11 = tk.Label(self.labelfame_stats)
        self.label11.configure(text='Nombres de 5 bon numéros :')
        self.label11.grid(column=0, row=5)
        self.label12 = tk.Label(self.labelfame_stats)
        self.vi_5bn = tk.IntVar()
        self.label12.configure(textvariable=self.vi_5bn)
        self.label12.grid(column=1, row=5)
        self.label13 = tk.Label(self.labelfame_stats)
        self.label13.configure(text='Nombres de 6 bon numéros :')
        self.label13.grid(column=0, row=6)
        self.label14 = tk.Label(self.labelfame_stats)
        self.vi_6bn = tk.IntVar()
        self.label14.configure(textvariable=self.vi_6bn)
        self.label14.grid(column=1, row=6)
        self.labelfame_stats.grid(column=0, ipady=5, padx=5, pady=5, row=2)
        self.labelfame_stats.rowconfigure(0, pad=5)
        self.toplevel1.grid_anchor("center")

        # Main widget
        self.mainwindow = self.toplevel1
        self.f_nombres_aleatoires()
        
    

    def run(self):
        self.mainwindow.mainloop()

    def f_tirage(self,nbrtirage):
        # 3 tirages semaine / 156 année
    
        cout = 2.52  
        bn3 = 0
        bn4 = 0
        bn5 = 0
        bn6 = 0
        x = 1

        while x < nbrtirage :
            
            numbers = set()

            while len(numbers) < 5:
                numbers.add(random.randint(1, 49))
            self.vi_r1.set(numbers.pop())
            self.vi_r2.set(numbers.pop())
            self.vi_r3.set(numbers.pop())
            self.vi_r4.set(numbers.pop())
            self.vi_r5.set(numbers.pop())
            self.vi_r6.set(random.randint(1,10))

            # on met tout ceci dans un tableau
            t_tirage = [self.entry_r1.get(), self.entry_r2.get(), self.entry_r3.get(), self.entry_r4.get(), self.entry_r5.get(), self.entry_r1.get()]
            t_monchoix = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()]
            
            # on compare les 2 tableaux
            nb_points_communs = 0

            for element in t_monchoix:
                if element in t_tirage:
                    nb_points_communs += 1
                if nb_points_communs == 3 :
                    bn3 +=1
                    self.vi_3bn.set(bn3)
                if nb_points_communs == 4 :
                    bn4 +=1
                    self.vi_4bn.set(bn4)
                if nb_points_communs == 5 :
                    bn5 +=1
                    self.vi_5bn.set(bn5)
                if nb_points_communs == 6 :
                    bn6 +=1
                    self.vi_3bn.set(bn6)


            self.vi_nbrbonnum.set(nb_points_communs)
           
            # on incrémentre le nombre de tirage
            self.vi_nbrtirage.set(x)

            # on incremente le cout
            cout += 2.52
            cout_formate = "{:,.2f}".format(cout).replace(","," ")
            self.vi_coutcumule.set(cout_formate)
            
            self.toplevel1.update_idletasks()

            x += 1

            
    def f_nombres_aleatoires(self):
        numbers = set()

        while len(numbers) < 5:
            numbers.add(random.randint(1, 49))
        self.vi_1.set(numbers.pop())
        self.vi_2.set(numbers.pop())
        self.vi_3.set(numbers.pop())
        self.vi_4.set(numbers.pop())
        self.vi_5.set(numbers.pop())
        self.vi_6.set(random.randint(1,10))   


    def f_tiragevictoire(self):
        # 3 tirages semaine / 156 année
        cout = 2.52  
        bn3 = 0
        bn4 = 0
        bn5 = 0
        bn6 = 0
        x = 1
        
        while bn6 < 1 :
            
            numbers = set()

            while len(numbers) < 5:
                numbers.add(random.randint(1, 49))
            self.vi_r1.set(numbers.pop())
            self.vi_r2.set(numbers.pop())
            self.vi_r3.set(numbers.pop())
            self.vi_r4.set(numbers.pop())
            self.vi_r5.set(numbers.pop())
            self.vi_r6.set(random.randint(1,10))

            # on met tout ceci dans un tableau
            t_tirage = [self.entry_r1.get(), self.entry_r2.get(), self.entry_r3.get(), self.entry_r4.get(), self.entry_r5.get(), self.entry_r1.get()]
            t_monchoix = [self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()]
            
            # on compare les 2 tableaux
            nb_points_communs = 0

            for element in t_monchoix:
                if element in t_tirage:
                    nb_points_communs += 1
                if nb_points_communs == 3 :
                    bn3 +=1
                    self.vi_3bn.set(bn3)
                if nb_points_communs == 4 :
                    bn4 +=1
                    self.vi_4bn.set(bn4)
                if nb_points_communs == 5 :
                    bn5 +=1
                    self.vi_5bn.set(bn5)
                if nb_points_communs == 6 :
                    bn6 +=1
                    self.vi_3bn.set(bn6)


            self.vi_nbrbonnum.set(nb_points_communs)
           
            # on incrémentre le nombre de tirage
            x += 1
            self.vi_nbrtirage.set(x)
            
            self.toplevel1.update_idletasks()
            

            # on incremente le cout
            cout += 2.52
            cout_formate = "{:,.2f}".format(cout).replace(","," ")
            self.vi_coutcumule.set(cout_formate)
            
            x += 1
    


if __name__ == "__main__":
    app = LotoApp()
    app.run()
