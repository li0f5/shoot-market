import subprocess
import tkinter as tk

import GraficaImpostazioni


def main():
    def apriCassa():
        window.destroy()
        print("ciaone")
        GraficaImpostazioni.main()

    window = tk.Tk()
    window.title("Test")
    window.state("zoomed")
    window.configure(background="grey")


    b1 = tk.Button(master=window, text="Cassa", width=15, command=apriCassa)
    b1.grid(row=0, column=0, sticky="ew")
    window.mainloop()

if __name__ == '__main__':
    main()


