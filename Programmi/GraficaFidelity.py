import subprocess
import tkinter as tk
from tkinter import ttk

from Programmi.ConDB import MariaDB


#funzione che imposta i valori di default
def getDatiConDatabase():
    db=MariaDB()
    dati = db.execute("SELECT * FROM Utente where uid = 1")#uid è da aggiungere
    entry1.insert(0, dati[0][1])
    entry2.insert(0, dati[0][2])
    entry3.insert(0, dati[0][3])
    entry4.insert(0, dati[0][4])


#creazione della finestra
window = tk.Tk()
window.title("Cassa")
window.state("zoomed")
window.configure(background="grey")

#divisione della finestra in 3 aree
frame1 = tk.Frame(master=window, bg="grey")
frame1.pack(side="top", fill="both", expand=False)
frame2 = tk.Frame(master=window, bg="blue")
frame2.pack(side="left", fill="both", expand=True)
frame3 = tk.Frame(master=window, bg="green")
frame3.pack(side="right", fill="both", expand=True)


#funzione del bottono bImpostazioni per aprire la finestra di impostazioni
def apriimpostazioni():
    window.destroy()
    subprocess.Popen(["python", "GraficaCassa.py"])
#funzione del bottono bCassa per aprire la finestra di cassa
def apriCassa():
    window.destroy()
    subprocess.Popen(["python", "GraficaCassa.py"])
#inserimento di 7 bottoni in frame1
bImpostazioni = tk.Button(master=frame1, text="Impostazioni", width=15, command=apriimpostazioni)
bImpostazioni.grid(row=0, column=0, sticky="ew")
bCassa = tk.Button(master=frame1, text="Cassa", width=15, command=apriCassa)
bCassa.grid(row=0, column=1, sticky="ew")
bApCassetto = tk.Button(master=frame1, text="Apertura Cassetto", width=15)
bApCassetto.grid(row=0, column=2, sticky="ew")
bScontrino = tk.Button(master=frame1, text="Scontrino", width=15)
bScontrino.grid(row=0, column=3, sticky="ew")
bAggiungi = tk.Button(master=frame1, text="Aggiungi", width=15)
bAggiungi.grid(row=0, column=4, sticky="ew")
bRimuovi = tk.Button(master=frame1, text="Rimuovi", width=15)
bRimuovi.grid(row=0, column=5, sticky="ew")
bEsci = tk.Button(master=frame1, text="Esci", width=15)
bEsci.grid(row=0, column=6, sticky="ew")


#inserimento di textbox in frame2 conteneti dati utente
label1 = tk.Label(master=frame2, text="Nome")
label1.grid(row=0, column=0)
entry1 = tk.Entry(master=frame2)
entry1.grid(row=1, column=0)
label2 = tk.Label(master=frame2, text="Cognome")
label2.grid(row=0, column=1)
entry2 = tk.Entry(master=frame2)
entry2.grid(row=1, column=1)
label3 = tk.Label(master=frame2, text="data iscrizione")
label3.grid(row=0, column=2)
entry3 = tk.Entry(master=frame2)
entry3.grid(row=1, column=2)


#inserimento di text box in frame3 per conteggio punti e inserimento di due bottoni
label4 = tk.Label(master=frame3, text="Punti Posseduti")
label4.grid(row=0, column=0)
entry4 = tk.Entry(master=frame3)
entry4.grid(row=1, column=0)
label5 = tk.Label(master=frame3, text="Punti da aggiungere")
label5.grid(row=0, column=1)
entry5 = tk.Entry(master=frame3)
entry5.grid(row=1, column=1)
label6 = tk.Label(master=frame3, text="Punti da utilizzare")
label6.grid(row=0, column=2)
entry6 = tk.Entry(master=frame3)
entry6.grid(row=1, column=2)
#tastiera numerica
tastiera = tk.Frame(master=frame3)
tastiera.grid(row=2, column=0, rowspan=7)
b1 = tk.Button(master=tastiera, text="1", width=5)
b1.grid(row=0, column=0)
b2 = tk.Button(master=tastiera, text="2", width=5)
b2.grid(row=0, column=1)
b3 = tk.Button(master=tastiera, text="3", width=5)
b3.grid(row=0, column=2)
b4 = tk.Button(master=tastiera, text="4", width=5)
b4.grid(row=1, column=0)
b5 = tk.Button(master=tastiera, text="5", width=5)
b5.grid(row=1, column=1)
b6 = tk.Button(master=tastiera, text="6", width=5)
b6.grid(row=1, column=2)
b7 = tk.Button(master=tastiera, text="7", width=5)
b7.grid(row=2, column=0)
b8 = tk.Button(master=tastiera, text="8", width=5)
b8.grid(row=2, column=1)
b9 = tk.Button(master=tastiera, text="9", width=5)
b9.grid(row=2, column=2)
b0 = tk.Button(master=tastiera, text="0", width=5)
b0.grid(row=3, column=0)
bPunti = tk.Button(master=tastiera, text="Aggiorna punti", width=15)
bPunti.grid(row=3, column=1, sticky="w", columnspan=2)
bUtilizzaPunti = tk.Button(master=tastiera, text="Utilizza punti", width=15)
bUtilizzaPunti.grid(row=4, column=0, sticky="ew", columnspan=3)



getDatiConDatabase()
window.mainloop()