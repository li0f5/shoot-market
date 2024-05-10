import tkinter as tk
from tkinter import ttk

import GraficaFidelity
import GraficaImpostazioni
from ConDB import MariaDB


def main():
    #-----------------------------#
    #funzioni generali
    #------------------------------------------------------------------------------#

    #TODO funzione che raccoglie i valori dei cibi dal db e ne calcola i prezzi
    #TODO funzione che aggiunge i cibi alla treeview dopo aver letto l'uid dell'utente (deve essere trasmesso anche a fidelity)
    def aggiunaCibo():
        db=MariaDB()
        db.execute("SELECT * FROM Cibo VALUES (descrizione, quantita, prezzo) where uid = self.uid") #self.uid è da creare



    #funzione del bottono bImpostazioni per aprire la finestra di impostazioni
    def apriImpostazioni():
        window.destroy()
        GraficaImpostazioni.main()

    #funzione del bottono bCassa per aprire la finestra fidelity
    def apriFidelity():
        window.withdraw()
        GraficaFidelity.main()
        window.deiconify()

    #funzione per il focus utilizzato per l'inserimento dalla tastiera
    def on_entry_focus(event, entry):
        global current_entry
        current_entry = entry

    #funzione dei bottoni
    def on_key_press(key):
        if current_entry:
            if key == "cancella":
                current_entry.delete(0, tk.END)
            elif key == "invio":
                current_entry.insert(tk.END, "\n")
            else:
                current_entry.insert(tk.END, key)

    #------------------------------------------------------------------------------#

    #-----------------------------#
    #creazione della finestra
    #-------------------------------------------------------------------------------------------------------#

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

    #inserimento di 7 bottoni in frame1
    bImpostazioni = tk.Button(master=frame1, text="Impostazioni", width=15, command=apriImpostazioni)
    bImpostazioni.grid(row=0, column=0, sticky="ew")
    bFidelity = tk.Button(master=frame1, text="Fidelity", width=15, command=apriFidelity)
    bFidelity.grid(row=0, column=1, sticky="ew")
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

    #inserimento del treeview in frame2
    columns = ('Descrizione', 'Quantità', 'Prezzo Unitario', 'Prezzo Totale')
    listbox = ttk.Treeview(master=frame2, columns=columns, show='headings')
    listbox.grid(sticky='nsew')
    # Impostazione delle intestazioni delle colonne
    for col in columns:
        listbox.heading(col, text=col)
    # Inserimento del treeview nella finestra
    listbox.grid(row=0, column=0, columnspan=2)

    #inserimento di tre caselle di testo e di un tastierino in frame3
    label1 = tk.Label(master=frame3, text="Nome Prodotto")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(master=frame3, width=50)
    entry1.bind("<FocusIn>", lambda event: on_entry_focus(event, entry1))
    entry1.grid(row=1, column=0)
    label2 = tk.Label(master=frame3, text="Quantita")
    label2.grid(row=2, column=0)
    entry2 = tk.Entry(master=frame3, width=50)
    entry2.bind("<FocusIn>", lambda event: on_entry_focus(event, entry2))
    entry2.grid(row=3, column=0)
    label3 = tk.Label(master=frame3, text="Prezzo")
    label3.grid(row=4, column=0)
    entry3 = tk.Entry(master=frame3, width=50)
    entry3.bind("<FocusIn>", lambda event: on_entry_focus(event, entry3))
    entry3.grid(row=5, column=0)

    frame3_layout = [
        [label1, entry1],
        [label2, entry2],
        [label3, entry3]
    ]

    for row, row_layout in enumerate(frame3_layout):
        for col, widget in enumerate(row_layout):
            widget.grid(row=row, column=col, sticky="ew")

    #inserimento del tastierino in frame3
    tastiera_layout = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["cancella", "0", "invio"]
    ]

    for row, row_layout in enumerate(tastiera_layout):
        for col, tasti in enumerate(row_layout):
            (tk.Button(master=frame3, text=tasti, width=5, command=lambda key=tasti: on_key_press(key), )
             .grid(row=row + 3, column=col, sticky="new"))

    window.mainloop()
    #-------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    main()
