import tkinter as tk
from tkinter import font
from tkinter import messagebox
import os

#iveidot galveno logu, kur likt elementus
logs = tk.Tk()
logs.title('Skaitļi')
logs.geometry('300x300')

#ieleik 2 labelus, katram skaitlim savu, nomainīt fontu, burtu izmēru
jaunsFonts = font.Font(family='Garamond', size=12, weight='bold')

label = tk.Label(logs, text='1. skaitlis', font= jaunsFonts)
label.pack(pady=10)
pirmaisSkaitlis = tk.Entry(logs) #pievieno ievades lauku
pirmaisSkaitlis.pack()

label = tk.Label(logs, text='2. skaitlis', font= jaunsFonts)
label.pack(pady=10)
otraisSkaitlis = tk.Entry(logs) #pievieno ievades lauku
otraisSkaitlis.pack()

izvele=tk.StringVar(value='konsole')
tk.Radiobutton(logs, text='Parādīt konsolē', variable=izvele, value='konsole').pack()
tk.Radiobutton(logs, text='Saglabāts failā', variable=izvele, value='fails').pack()

def nolasitDatus():
    #saņemt datus no entry box un saglabā minīgajā
    vertiba1 = pirmaisSkaitlis.get()
    vertiba2 = otraisSkaitlis.get()
    try:
    #pārbauda vai lietotājs ievadīja skitļus
        vertiba1 = float(vertiba1)
        vertiba2 = float(vertiba2)
    except ValueError:
        messagebox.showerror('Kļūda', 'Ievadiet skaitļus!')
        return

#gala izvēli nolasa no radio pogas
    galaIzvele=izvele.get()

    if galaIzvele == 'konsole':
        print(f'1. skaitlis: {vertiba1}\n2. skaitlis: {vertiba2}')
        
    elif galaIzvele == 'fails':
        failaNosaukums = 'lietotajs.txt'
        with open(failaNosaukums, 'a', encoding='UTF8') as datne:
            datne.write(f'Pirmais skaitlis:{vertiba1}\n')
            datne.write(f'Otrais skaitlis:{vertiba2}\n')
            datne.write(f'-'*10+'\n')
        messagebox.showinfo('Informācija', f'Dati saglabāti failā {failaNosaukums}!')

def paraditFailaSaturu():
    failaNosaukums = 'lietotajs.txt'
    #pārbauda vai fails eksistē un tajā ir informācija
    if os.path.exists(failaNosaukums) and os.path.getsize(failaNosaukums)>0:
        with open(failaNosaukums, 'r', encoding='UTF8') as datne:
            saturs = datne.readlines()

    #failu nolasa, jo datus kārtos
        skaitli = []
        for rinda in saturs:
            if 'Pirmais skaitlis' in rinda or 'Otrais skaitlis' in rinda:
                try:
                    numurs = float(rinda.split(':')[1].strip())
                    skaitli.append(numurs)
                except ValueError:
                    pass

        if skaitli:
            skaitli.sort()
            print('Sakārtoti augošā secībā:')
            for skaitlis in skaitli:
                print(skaitlis)
        else:
                print('Failā nav derīgu skaitļu!')
    else:
        messagebox.showwarning('Brīdinājums', 'Fails ir tukšs vai neeksistē.')

poga = tk.Button(logs, text='Apstiprināt', command=nolasitDatus)
poga.pack(pady=10)

pogaFailaSaturam = tk.Button(logs, text='Parādīt faila saturu', command=paraditFailaSaturu).pack(pady=20)

logs.mainloop()