import tkinter as tk
from tkinter import ttk

#creazione della finestra
window = tk.Tk()
window.title("Cassa")
window.minsize(width=500, height=200)
window.configure(background="grey")


#divisione della finestra in 3 aree
frame1 = tk.Frame(master=window, bg="grey")
frame1.pack(side="top", fill="y", expand=False)
frame2 = tk.Frame(master=window, bg="blue")
frame2.pack(side="left", fill="both", expand=True)
frame3 = tk.Frame(master=window, bg="green")
frame3.pack(side="right", fill="both", expand=True)


#inserimento di 7 bottoni in frame1
bImpostazioni = tk.Button(master=frame1, text="Impostazioni", width=15)
bImpostazioni.grid(row=0, column=0)
bFidelity = tk.Button(master=frame1, text="Fidelity", width=15)
bFidelity.grid(row=0, column=1)
bApCassetto = tk.Button(master=frame1, text="Apertura Cassetto", width=15)
bApCassetto.grid(row=0, column=2)
bScontrino = tk.Button(master=frame1, text="Scontrino", width=15)
bScontrino.grid(row=0, column=3)
bAggiungi = tk.Button(master=frame1, text="Aggiungi", width=15)
bAggiungi.grid(row=0, column=4)
bRimuovi = tk.Button(master=frame1, text="Rimuovi", width=15)
bRimuovi.grid(row=0, column=5)
bEsci = tk.Button(master=frame1, text="Esci", width=15)
bEsci.grid(row=0, column=6, columnspan=2)


#inserimento del treeview in frame2
columns = ('Descrizione', 'Quantità', 'Prezzo Unitario', 'Prezzo Totale')
listbox = ttk.Treeview(master=frame2, columns=columns, show='headings')
# Impostazione delle intestazioni delle colonne
for col in columns:
    listbox.heading(col, text=col)
# Inserimento del treeview nella finestra
listbox.grid(row=0, column=0, columnspan=2)


#inserimento di tre caselle di testo e di un tastierino in frame3
label1 = tk.Label(master=frame3, text="Nome Prodotto")
label1.grid(row=0, column=0)
entry1 = tk.Entry(master=frame3)
entry1.grid(row=1, column=0)
label2 = tk.Label(master=frame3, text="Quantita")
label2.grid(row=2, column=0)
entry2 = tk.Entry(master=frame3)
entry2.grid(row=3, column=0)
label3 = tk.Label(master=frame3, text="Prezzo")
label3.grid(row=4, column=0)
entry3 = tk.Entry(master=frame3)
entry3.grid(row=5, column=0)
#tastierino con nove pulsanti
tastiera = tk.Frame(master=frame3)
tastiera.grid(row=6, column=0, rowspan=7)
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
b0.grid(row=3, column=1)
bCancella = tk.Button(master=tastiera, text="Cancella", width=5)
bCancella.grid(row=3, column=2)
bInvio = tk.Button(master=tastiera, text="Invio", width=5)
bInvio.grid(row=3, column=0)



window.mainloop()
