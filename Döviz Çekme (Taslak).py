"""
Yazan: Evrim Köylüoğlu
Resmi Gazetede yayınlanan döviz kurunu çekme
"""
#!/usr/bin/python3

#kütüphaneler
import datetime
from tkinter import *
from tkinter import messagebox
import urllib.request

haftasonu = 0
#alanlar1
alanlar = {"Döviz Tarihi"}
#Hesaplama ve girdi tanımları
def doviz(entries):
    hasar_tar =  str(entries["Döviz Tarihi"].get())
    pit = datetime.datetime.strptime(hasar_tar, "%d.%m.%Y") + datetime.timedelta(days=1)
    print(type(pit.date()))
    print(type(datetime.date.today()))
    print(datetime.date.today())
    print(pit)
    
    print(pit)
    print(pit.strftime("%d"))
    print(pit.strftime("%m"))
    print(pit.strftime("%Y"))
    
    global year
    year = pit.strftime("%Y")
    
    global ay
    ay = pit.strftime("%m")
    
    global day
    day = pit.strftime("%d")
    
    global haftasonu    
    haftasonu = pit.weekday()
    print(haftasonu)
    print(type(haftasonu))
    indir()
    
def indir():
    if haftasonu == (6):
        messagebox.showinfo("HATA", "Cumartesi Günü Döviz Kuru Bulunmamaktadır. Tekrar Deneyiniz")
    elif haftasonu == (0):
        messagebox.showinfo("HATA", "Pazar Günü Döviz Kuru Bulunmamaktadır. Tekrar Deneyiniz")
    else:     
        img = ("http://www.resmigazete.gov.tr/ilanlar/eskiilanlar/{yyyy}/{mm}/{yyyy}{mm}{dd}-5_dosyalar/image001.jpg".format(yyyy=year,mm=ay,dd=day))
        img3 = ("http://www.resmigazete.gov.tr/ilanlar/eskiilanlar/{yyyy}/{mm}/{yyyy}{mm}{dd}-5_dosyalar/image002.jpg".format(yyyy=year,mm=ay,dd=day))
        img2 = ("http://www.resmigazete.gov.tr/ilanlar/eskiilanlar/{yyyy}/{mm}/{yyyy}{mm}{dd}-5_dosyalar/image001.png".format(yyyy=year,mm=ay,dd=day))
        print(img)
        img_isim = "{dd}.{mm}.{yyyy} Tarihli MB Döviz Kuru.jpg".format(yyyy=year,mm=ay,dd=str((int(day)-1)))
        
        try:
            urllib.request.urlretrieve(img,img_isim)
                      
        except:    
            urllib.request.urlretrieve(img2,img_isim)
            
        finally:
            urllib.request.urlretrieve(img3,img_isim)
        
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
    root.iconbitmap(r"C:\Users\Evrim\Desktop\Döviz Çekme\add\.pirii.ico")
    b1 = Button(root, text='İndir', command=(lambda e=ents: doviz(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
