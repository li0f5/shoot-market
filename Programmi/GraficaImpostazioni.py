#finestra che si apre quando viene premuto il pulsante bImpostazioni nel file GraficaCassa.py
import subprocess
import tkinter as tk


#creazione della finestra
window = tk.Tk()
window.title("Cassa")
window.state("zoomed")
window.configure(background="grey")


#divisione della finestra in 3 aree
frame1 = tk.Frame(master=window, bg="grey", width=window.winfo_width())
frame1.pack(side="top", fill="both", expand=False)
frame2 = tk.Frame(master=window, bg="blue")
frame2.pack(side="top", fill="both", expand=True)
frame3 = tk.Frame(master=window, bg="green")
frame3.pack(side="bottom", fill="both", expand=True)


#funzione del bottono bCassa per aprire la finestra di cassa
def arpiCassa():
    window.destroy()
    subprocess.Popen(["python", "GraficaCassa.py"])
#funzione del bottono bFidelity per aprire la finestra di fidelity
def apriFidelity():
    window.destroy()
    subprocess.Popen(["python", "GraficaFidelity.py"])
#inserimento di 7 bottoni in frame1
bCassa = tk.Button(master=frame1, text="Cassa", width=15, command=arpiCassa)
bCassa.grid(row=0, column=0, sticky="ew")
bFidelity = tk.Button(master=frame1, text="Fidelity", width=15, command=apriFidelity)
bFidelity.grid(row=0, column=1, sticky="ew")
bApCassetto = tk.Button(master=frame1, text="Apertura Cassetto", width=15)
bApCassetto.grid(row=0, column=2, sticky="ew")
bScontrino = tk.Button(master=frame1, text="Scontrino", width=15)
bScontrino.grid(row=0, column=3,sticky="ew")
bAggiungi = tk.Button(master=frame1, text="Aggiungi", width=15)
bAggiungi.grid(row=0, column=4,sticky="ew")
bRimuovi = tk.Button(master=frame1, text="Rimuovi", width=15)
bRimuovi.grid(row=0, column=5,sticky="ew")
bEsci = tk.Button(master=frame1, text="Esci", width=15)
bEsci.grid(row=0, column=6, columnspan=2, sticky="w")


#divido il frame 2 in due righe
frame2.rowconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)
#funzione per il focus utilizzato per l'inserimento dalla tastiera
def on_entry_focus(event, entry):
    global current_entry
    current_entry = entry
#inserisco dei textbox, in cui sono presenti i dati per la connesione a un database, nella prima riga del frame 2
label1 = tk.Label(master=frame2, text="Host")
label1.grid(row=0, column=0, padx=10, sticky="nw")
entry1 = tk.Entry(master=frame2)
entry1.grid(row=1, column=0, padx=10, sticky="nw")
entry1.bind("<FocusIn>", lambda event: on_entry_focus(event, entry1))
label2 = tk.Label(master=frame2, text="Username")
label2.grid(row=0, column=1, padx=10, sticky="nw")
entry2 = tk.Entry(master=frame2)
entry2.bind("<FocusIn>", lambda event: on_entry_focus(event, entry2))
entry2.grid(row=1, column=1, padx=10, sticky="nw")
label3 = tk.Label(master=frame2, text="Password")
label3.grid(row=0, column=2, padx=10, sticky="nw")
entry3 = tk.Entry(master=frame2)
entry3.bind("<FocusIn>", lambda event: on_entry_focus(event, entry3))
entry3.grid(row=1, column=2, padx=10, sticky="nw")
label4 = tk.Label(master=frame2, text="Database")
label4.grid(row=0, column=3, padx=10, sticky="nw")
entry4 = tk.Entry(master=frame2)
entry4.bind("<FocusIn>", lambda event: on_entry_focus(event, entry4))
entry4.grid(row=1, column=3, padx=10, sticky="nw")


#tastiera intera in frame3
def on_key_press(key):
    if current_entry:
        current_entry.insert(tk.END, key)


keyboard_layout = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ['Space', 'Backspace']
]

for row in keyboard_layout:
    key_frame = tk.Frame(frame3)
    key_frame.pack()
    for key in row:
        button = tk.Button(key_frame, text=key, width=5, height=2,
                           command=lambda k=key: on_key_press(k))
        button.pack(side=tk.LEFT)


window.mainloop()