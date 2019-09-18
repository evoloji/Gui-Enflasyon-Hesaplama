#!/usr/bin/python3
# -*- coding: utf-8 -*-

#kütüphaneler
import datetime
from tkinter import *
import locale
#from decimal import Decimal
#import re

#alanlar
alanlar = {"Döviz Tarihi"}
    
#Hesaplama ve girdi tanımları
def doviz(entries):
    hasar_tar =  str(entries["Döviz Tarihi"].get())
    pit = datetime.datetime.strptime(hasar_tar, "%d.%m.%Y")
    
    print(pit.strftime("%d"))
    print(pit.strftime("%m"))
    print(pit.strftime("%Y"))
    year = pit.strftime("%Y")
    ay = pit.strftime("%m")
    day = pit.strftime("%d")
    fu = ("http://www.resmigazete.gov.tr/ilanlar/eskiilanlar/{yyyy}/{mm}/{yyyy}{mm}{dd}-5_dosyalar/image002.jpg".format(yyyy=year,mm=ay,dd=day))
    print(fu)
    
#Şablon oluşturması    
def makeform(root, alanlar):
   entries = {}
   for field in alanlar:
      row = Frame(root)
      lab = Label(row, width=30, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      row.pack(side=TOP, fill=X, padx=10, pady=10)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, alanlar)
   #root.bind('<Return>', (lambda event, e=ents: fetch(e))) 
   def fetch(entries): 
    for entry in entries: 
        field = entry[0]
        text = entry[1].get() 
        print ("%s: %s" %(field,text)) 
   root.title("Döviz Kuru Çekme")
   b1 = Button(root, text='İndir', 
               command=(lambda e=ents: doviz(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
   b1 = Button(root, text='İndir',
              command=(lambda e=ents: doviz(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
