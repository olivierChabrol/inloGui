# coding: utf-8

from tkinter import Entry, Label, StringVar, Tk 

root = Tk()
root.title('Annuaire')

ids = ["name", "last_name", "phone", "adress", "city"]

widgets_labs = {}
widgets_entry = {}

for idi in ids:

    lab = Label(root, text=idi)
    widgets_labs[idi] = lab
    lab.pack()

    var = StringVar()
    entry = Entry(root, text=var)
    widgets_entry[idi] = entry
    entry.pack()

root.mainloop()
"""
label_name = Label(root, text='Nom')
label_last_name = Label(root, text='Prénom')
label_phone = Label(root, text='portable')
label_adresse = Label(root, text='Adresse')
label_city = Label(root, text='ville')

var_name = StringVar()
var_last_name = StringVar()
var_phone = StringVar()
var_adresse = StringVar()
var_city = StringVar()

entry_name = Entry(root, text=var_name)
entry_last_name = Entry(root, text=var_last_name)
entry_phone = Entry(root, text=var_phone)
entry_adresse = Entry(root, text=var_adresse)
entry_city = Entry(root, text=var_city)

label_name.pack()
label_last_name.pack()
label_phone.pack()
label_adresse.pack()
label_city.pack()


for i in range(5):
    Entry(root, text='').pack()


entry_name.pack()
entry_last_name.pack()
entry_phone.pack()
entry_adresse.pack()
entry_city.pack()


"""