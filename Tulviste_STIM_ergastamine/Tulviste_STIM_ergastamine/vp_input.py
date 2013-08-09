#!/usr/bin/python
# This Python file uses the following encoding: utf-8
# Dialog box at the beginning of the experiment

from Tkinter import *
import tkMessageBox
import os

def ok(event=None):
    datafile_all = open('Subjects.txt', 'a')
    datafile_all.write(str(subj_nr.get()) + '\t'
        + str(sex.get()) + '\t' + str(age.get()) + '\t' + str(TMScnd.get()) + '\t'
        + time.ctime() + '\n')
    datafile_all.close()

    # make a file with variable names for the subject
    datafile = open('KI_' + str(subj_nr.get()) + '.dat','a')
    datafile.write('KI' + '\t' + 'TMS/SHAM' + '\t'+ 'Trial' + '\t' + 'Condition' + '\t' + 'Answ' + '\t' + 'RT' + '\t' + 'Points' + '\n')
    datafile.close()
    session_data={'KI-Nr':str(subj_nr.get()),'Vanus': str(age.get()), 'Sugu': str(sex.get()), 'TMS condition' : str(TMScnd.get())}
    print session_data
    all_ok()

def all_ok():
    if tkMessageBox.askokcancel('K6ik 6ige?'):
        root.quit()


root = Tk() # root (main) window
top = Frame(root) # create frame
top.bbox(column=5, row=5)
top.pack(side='top') # pack frame in main window

font = 'arial 18 bold'
nr_text = Label(top, text='KI-number:', font=font)
nr_text.grid(row=0, column=0, sticky='w')
subj_nr = IntVar() # variable to be attached to vp_nr_entry
subj_nr.set('99') # default value
subj_nr_entry = Entry(top, width=2, textvariable=subj_nr, font=font)
subj_nr_entry.grid(row=0, column=1, sticky='w')

age_text = Label(top, text='Vanus:', font=font)
age_text.grid(row=1, column=0, sticky='w')
age = StringVar()
age.set('00') # default value
age_entry = Entry(top, width=2, textvariable=age, font=font)
age_entry.grid(row=1, column=1, sticky='w')


sex_text = Label(top, text='Sugu:', font=font)
sex_text.grid(row=2, column=0, columnspan=4, sticky='w')
sex = StringVar()
sex.set('f') # default value
rbutt1 = Radiobutton(top, text='naine', variable=sex, value='f', font=font,
    activebackground='red', activeforeground='green')
rbutt2 = Radiobutton(top, text='mees', variable=sex, value='m', font=font,
    activebackground='red', activeforeground='green')
rbutt1.grid(row=2, column=1, sticky='w', columnspan=2)
rbutt2.grid(row=2, column=3, sticky='w', columnspan=2)

TMScnd_text = Label(top, text='TMS:', font=font)
TMScnd_text.grid(row=3, column=0, columnspan=8, sticky='w')
TMScnd = StringVar()
TMScnd.set('SHAM') # default value
TMScndbutt1 = Radiobutton(top, text='H', variable=TMScnd, value='SHAM', font=font,
    activebackground='red', activeforeground='green')
TMScndbutt2 = Radiobutton(top, text='M', variable=TMScnd, value='TMS', font=font,
    activebackground='red', activeforeground='green')
TMScndbutt1.grid(row=3, column=1, sticky='w', columnspan=2)
TMScndbutt2.grid(row=3, column=3, sticky='w', columnspan=2)

blokk_text = Label(top, text='Blokk:', font=font)
blokk_text.grid(row=4, column=0, sticky='w')
blokk = StringVar()
blokk.set('1') # default value
blokk_entry = Entry(top, width=1, textvariable=blokk, font=font)
blokk_entry.grid(row=4, column=1, sticky='w')

okbutt = Button(top, text=' OK ', foreground='red', command=ok, font=font)
okbutt.grid(row=5, columnspan=6, sticky='ew')

root.mainloop()
