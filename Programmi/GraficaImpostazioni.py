#finestra che si apre quando viene premuto il pulsante bImpostazioni nel file GraficaCassa.py
import tkinter as tk
import GraficaCassa
import GraficaFidelity
from Programmi.ConDB import MariaDB


def main():
    #-----------------------------#
    #funzioni generali
    #------------------------------------------------------------------------------#

    #funzione che cambia dati collegamento al database
    def updateServer():
        db = MariaDB()
        db.writeConfig(entry1.get(), entry2.get(), entry3.get(), entry4.get())

    #funzione che imposta i valori di default
    def getDatiConDatabase():
        if entry1.get() == "" or entry2.get() == "" or entry3.get() == "" or entry4.get() == "":
            db = MariaDB()
            entry1.insert(0, db.getHost())
            entry2.insert(0, db.getUser())
            entry3.insert(0, db.getPassword())
            entry4.insert(0, db.getDatabase())
        else:
            db = MariaDB()

    #funzione del bottono bCassa per aprire la finestra di cassa
    def arpiCassa():
        window.destroy()
        GraficaCassa.main()

    #funzione del bottono bFidelity per aprire la finestra di fidelity
    def apriFidelity():
        window.destroy()
        GraficaFidelity.main()

    #funzione per il focus utilizzato per l'inserimento dalla tastiera
    def on_entry_focus(event, entry):
        global current_entry
        current_entry = entry

    #funzione dei bottoni
    def on_key_press(key):
        if current_entry:
            if key == "Backspace":
                current_entry.delete(0, tk.END)
            elif key == "Space":
                current_entry.insert(tk.END, " ")
            elif key == "Enter":
                updateServer()
            else:
                current_entry.insert(tk.END, key)

    #------------------------------------------------------------------------------#

    #-----------------------------#
    #creazione della finestra
    #-------------------------------------------------------------------------------------------------------#

    #creazione della finestra
    window = tk.Tk()
    window.title("Impostazioni")
    window.state("zoomed")
    window.configure(background="grey")

    #divisione della finestra in 3 aree
    frame1 = tk.Frame(master=window, bg="grey", width=window.winfo_width())
    frame1.pack(side="top", fill="both", expand=False)
    frame2 = tk.Frame(master=window, bg="blue")
    frame2.pack(side="top", fill="both", expand=True)
    frame3 = tk.Frame(master=window, bg="green")
    frame3.pack(side="bottom", fill="both", expand=True)

    #inserimento di 7 bottoni in frame1
    bCassa = tk.Button(master=frame1, text="Cassa", width=15, command=arpiCassa)
    bCassa.grid(row=0, column=0, sticky="ew")
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
    bEsci.grid(row=0, column=6, columnspan=2, sticky="w")

    #divido il frame 2 in due righe
    frame2.rowconfigure(0, weight=1)
    frame2.rowconfigure(1, weight=1)

    #inserisco dei textbox, in cui sono presenti i dati per la connesione a un database, nella prima riga del frame 2
    label1 = tk.Label(master=frame2, text="Host")
    entry1 = tk.Entry(master=frame2)
    entry1.bind("<FocusIn>", lambda event: on_entry_focus(event, entry1))
    label2 = tk.Label(master=frame2, text="Username")
    entry2 = tk.Entry(master=frame2)
    entry2.bind("<FocusIn>", lambda event: on_entry_focus(event, entry2))
    label3 = tk.Label(master=frame2, text="Password")
    entry3 = tk.Entry(master=frame2)
    entry3.bind("<FocusIn>", lambda event: on_entry_focus(event, entry3))
    label4 = tk.Label(master=frame2, text="Database")
    entry4 = tk.Entry(master=frame2)
    entry4.bind("<FocusIn>", lambda event: on_entry_focus(event, entry4))
    getDatiConDatabase()

    frame2_layout = [
        [label1, entry1],
        [label2, entry2],
        [label3, entry3],
        [label4, entry4]
    ]

    for row in frame2_layout:
        for col in row:
            col.pack(side="left", fill="both", expand=True, padx=5, pady=5)


    #tastiera intera in frame3
    keyboard_layout = [
        ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
        ['Space', 'Backspace', 'Enter']
    ]

    for row in keyboard_layout:
        key_frame = tk.Frame(frame3)
        key_frame.pack()
        for key in row:
            button = tk.Button(key_frame, text=key, width=5, height=2,
                               command=lambda k=key: on_key_press(k))
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    window.mainloop()
    #-------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    main()
