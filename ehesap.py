#!/usr/bin/python3



#kütüphaneler
import datetime
from tkinter import *
import locale

#alanlar
alanlar = ("Poliçe Başlangıç Tarihi", "Hasar Tarihi", "Enflasyon Oranı", "Sigortalı Bedeli", "Enflasyonlu Sigorta Bedeli","Katsayı")

#Hesaplama ve girdi tanımları
def enflasyon_hesap(entries):
    if not entries["Enflasyon Oranı"].get() or not entries["Sigortalı Bedeli"].get():
     print("Lütfen tüm alanları doldurunuz.")
     return


    #Tarihli entryleri tanımlama
    police_ilk = str(entries["Poliçe Başlangıç Tarihi"].get())
    hasar_tar =  str(entries["Hasar Tarihi"].get())
    pit = datetime.datetime.strptime(police_ilk, "%d.%m.%Y")
    htt = datetime.datetime.strptime(hasar_tar, "%d.%m.%Y")

    try:
     enf_oran = (float(entries["Enflasyon Oranı"].get()) / 100)
     sig_bed = float(entries["Sigortalı Bedeli"].get())  
    except ValueError:
     print("Tarih formatı hatalı, lütfen gg.aa.YYYY formatında girin.")
     return

    #Hasarlı Gün Sayısını Hesaplama (Poliçe Başlangıç Tarihi - Hasar Tarihi )
    gunsayi = (htt - pit).days
    global sayi
    sayi = gunsayi

    #Vade Hesaplama
    vade=float(365)
    enflasyon_artis_katsayi = ((float(gunsayi) /vade) * enf_oran) + 1
    enf_sig_bed = enflasyon_artis_katsayi *sig_bed

    #Sigorta Bedeli * Katsayı
    enflasyon_artis_katsayi = ("%0.7f" % enflasyon_artis_katsayi).strip()

    #locale ayarkarı
    locale.setlocale(locale.LC_ALL, '')
    enf_sig_bed = locale.format_string("%0.2f", enf_sig_bed, grouping = True)
    f = enf_sig_bed + " TL"
    #Ekrana yazdırma
    entries["Katsayı"].delete(0,END)
    entries["Katsayı"].insert(0,enflasyon_artis_katsayi)
    #print("Katsayı Oran: %f8" % float(enflasyon_artis_katsayi))
    #enf_sig_bed = ("{:.2f}".format(enf_sig_bed))
    
    entries["Enflasyonlu Sigorta Bedeli"].delete(0,END)
    entries["Enflasyonlu Sigorta Bedeli"].insert(0,f)

    if 'left' in globals():
     left.destroy()  # Mevcut label'ı temizle
    
    labelframe = LabelFrame(root,text = "Hasarlı Gün Sayısı")
    labelframe.pack(fill = "both", expand = "yes")
    
    left = Label(labelframe, text = sayi)
    left.pack() 

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
   root.title("Enflasyon Hesap")

   b1 = Button(root, text='Enflasyon Hesapla', 
               command=(lambda e=ents: enflasyon_hesap(e)))
   b1.pack(side=LEFT, padx=5, pady=5)

   root.mainloop()
