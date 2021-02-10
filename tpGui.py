# coding: utf-8

from tkinter import Entry, Label, StringVar, Tk , Button

root = Tk()
root.title('Annuaire')

ids = ["name", "last_name", "phone", "adress", "city"]
bouton = ["chercher", "inserer", "effacer"]

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

for idi in ids:
    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.pack()

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.pack()

for idi in bouton:
    button = Button(root, text = idi)
    widgets_button[idi] = button
    button.pack()

root.mainloop()