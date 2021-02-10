# coding: utf-8

from tkinter import Entry, Label, StringVar, Tk , Button

root = Tk()
root.title('Annuaire')

ids = ["name", "last_name", "phone", "adress", "city"]
bouton = ["chercher", "inserer", "effacer"]

widgets_labs = {}
widgets_entry = {}
widgets_button = {}

for idi in range(0,len(ids)):
    lab = Label(root, text=ids[idi])
    widgets_labs[ids[idi]] = lab
    lab.grid(row=idi,column=0)

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[ids[idi]] = entry
    entry.grid(row=idi,column=1)

for idi in range(0,len(bouton)):
    button = Button(root, text = bouton[idi])
    widgets_button[bouton[idi]] = button
    button.grid(row=len(ids)+1,column=idi)

root.mainloop()