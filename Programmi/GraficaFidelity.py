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
    entry1.configure(state="readonly")
    entry2.configure(state="readonly")
    entry3.configure(state="readonly")
    entry4.configure(state="readonly")


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

frame2_layout = [
    [label1, entry1],
    [label2, entry2],
    [label3, entry3]
]

for row, row_layout in enumerate(frame2_layout):
    for col, widget in enumerate(row_layout):
        widget.grid(row=row, column=col, sticky="ew")

#funzione per il focus utilizzato per l'inserimento dalla tastiera
def on_entry_focus(event, entry):
    global current_entry
    current_entry = entry
#inserimento di text box in frame3 per conteggio punti e inserimento di due bottoni
label4 = tk.Label(master=frame3, text="Punti Posseduti")
entry4 = tk.Entry(master=frame3)
entry4.bind("<FocusIn>", lambda event: on_entry_focus(event, entry4))
label5 = tk.Label(master=frame3, text="Punti da aggiungere")
entry5 = tk.Entry(master=frame3)
entry5.bind("<FocusIn>", lambda event: on_entry_focus(event, entry5))
label6 = tk.Label(master=frame3, text="Punti da utilizzare")
entry6 = tk.Entry(master=frame3)
entry6.bind("<FocusIn>", lambda event: on_entry_focus(event, entry6))


frame3_layout = [
    [label4, entry4],
    [label5, entry5],
    [label6, entry6]
]

for row, row_layout in enumerate(frame3_layout):
    for col, widget in enumerate(row_layout):
        widget.grid(row=row, column=col, sticky="ew")
#tastiera numerica
def on_key_press(key):
    if current_entry:
        if key == "cancella":
            current_entry.delete(0, tk.END)
        elif key == "invio":
            current_entry.insert(tk.END, "\n")
        else:
            current_entry.insert(tk.END, key)

tastiera_layout = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["cancella", "0", "invio"]
]

for row, row_layout in enumerate(tastiera_layout):
    for col, tasti in enumerate(row_layout):
        (tk.Button(master=frame3, text=tasti, width=5, command=lambda key=tasti: on_key_press(key), )
         .grid(row=row + 3, column=col, sticky="ew"))



getDatiConDatabase()

window.mainloop()