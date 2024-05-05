import tkinter as tk
from tkinter import ttk

def aggiungi_prodotto():
    descrizione = entry_descrizione.get()
    quantita = int(entry_quantita.get())
    prezzo_unitario = float(entry_prezzo_unitario.get())
    prezzo_totale = quantita * prezzo_unitario
    listbox.insert('', 'end', values=(descrizione, quantita, prezzo_unitario, prezzo_totale))

root = tk.Tk()
root.title("Lista Prodotti")

# Creazione del treeview con quattro colonne
columns = ('Descrizione', 'Quantità', 'Prezzo Unitario', 'Prezzo Totale')
listbox = ttk.Treeview(root, columns=columns, show='headings')

# Impostazione delle intestazioni delle colonne
for col in columns:
    listbox.heading(col, text=col)

# Inserimento del treeview nella finestra
listbox.grid(row=0, column=0, columnspan=2)

# Caselle di testo per l'inserimento dei dati
label_descrizione = tk.Label(root, text="Descrizione:")
label_descrizione.grid(row=1, column=0, sticky='w')
entry_descrizione = tk.Entry(root)
entry_descrizione.grid(row=1, column=1)

label_quantita = tk.Label(root, text="Quantità:")
label_quantita.grid(row=2, column=0, sticky='w')
entry_quantita = tk.Entry(root)
entry_quantita.grid(row=2, column=1)

label_prezzo_unitario = tk.Label(root, text="Prezzo Unitario:")
label_prezzo_unitario.grid(row=3, column=0, sticky='w')
entry_prezzo_unitario = tk.Entry(root)
entry_prezzo_unitario.grid(row=3, column=1)

# Bottone per aggiungere il prodotto alla lista
button_aggiungi = tk.Button(root, text="Aggiungi", command=aggiungi_prodotto)
button_aggiungi.grid(row=4, columnspan=2)

root.mainloop()
