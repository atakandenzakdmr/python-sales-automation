from Kayitlar import Kayitlar
import os
import time







# SATICI İŞLEMLERİ


def Menu():
        print("\n","#"*5, "Satıcı İşlem Menüsü\n", "#"*5)
        print("1) Satıcı ekle")
        print("2) Satıcı Giriş")
        print("3) Satıcı sil")
        print("4) Satıcı bilgilerini güncelle")
        print("5) Tüm satıcıları görüntüle")

        print('0) ## Çıkış İşlemi İçin', "#" * 2)


        secim = int(input("\n\nLütfen Yapacağınız İşlem İçin Seçim yapınız : "))
        return secim

def SaticiEkle():


    ad = input("Adı: ")
    soyad = input("Soyad: ")
    sehir = input("Yaşadığın şehir: ")
    firma = input("Firma Adı : ")
    dogum = int(input("Doğum tarihi: "))
    mail = input("Mail adresi: ")
    tel = input("Telefon numarası: ")
    gecmis = []
    while True:
        egt = input("Şuana kadar çalıştığı firmalar: ")
        if egt == "":
            break
        gecmis.append(egt)

    satici = {"dogum_tarihi": dogum, "gecmis": gecmis, "firma": firma, "soyadi": soyad,
              "sehir": sehir, "tel": tel, "adi": ad, "mail": mail}

    std = Kayitlar()
    std.addKayitlar(satici)
    print("#" * 5, "Satıcı Eklendi", "#" * 5)
    time.sleep(2)
    os.system("cls")
    Menu()

def SaticiBul():

    ad = input("Giriş Yapıcak satıcının adı: ")
    soyad = input("Giriş Yapıcak satıcının soyadı: ")

    os.system("cls")
    time.sleep(2)
    print ("############# SATICI BİLGİLERİ ##########")
    std = Kayitlar()
    std.viewKayitlar(ad, soyad)
    time.sleep(6)
    os.system("cls")
    Menu()

def SaticiSil():
    ad = input("Silinecek satıcının adı: ")
    soyad = input("Silinecek satıcının soyadı: ")

    std = Kayitlar()
    std.deleteKayitlar(ad, soyad)
    print("#" * 5, "Satıcı silindi", "#" * 5)
    time.sleep(2)
    os.system("cls")
    Menu()


def SaticiGuncelle():
    print("\nGüncellenecek Satıcı bilgilerini girin.")

    ad = input("Adı: ")
    soyad = input("Soyad: ")

    sehir = input("\nYaşadığın şehir: ")
    firma = input('Firma adı : ')
    dogum = int(input("Doğum tarihi: "))
    mail = input("Mail adresi: ")
    tel = input("Telefon numarası: ")
    gecmis = []
    while True:
        egt=input("Şuana kadar çalıştığı firmalar: ")
        if egt == "":
            break
        gecmis.append(egt)

    satici = {"dogum_tarihi": dogum, "gecmis": gecmis, "firma": firma, "soyadi": soyad,
              "sehir": sehir, "tel": tel, "adi": ad, "mail": mail}

    std = Kayitlar()
    std.uptadeKayitlar(ad, soyad, satici)
    print("#" * 5, "Satıcı güncellendi", "#" * 5)
    time.sleep(2)
    os.system("cls")
    Menu()


def SaticiGoster():
    std = Kayitlar()
    std.allKayitlar()
    time.sleep(2)
    os.system("cls")
    Menu()

devam = True
while devam:
    secim = Menu()
    if secim == 0:
        print("Programdan Çıkılıyor.. ")
        exit(0)

    elif secim == 1:
        print("Satici Ekleme Menüsü :")
        SaticiEkle()

    elif secim == 2:
        print("Satıcı İşlem Menüsü :")
        SaticiBul()
        MenuSatis()

    elif secim == 3:
        print("Satıcı Silme Menüsü: ")
        SaticiSil()

    elif secim == 4:
        print("Satıcı Güncelleme Menüsü:")
        SaticiGuncelle()

    elif secim == 5:
        print("Satıcı Gösterme Menüsü :")
        SaticiGoster()

    else:

        print("#"*5,"Geçersiz işlem","#"*5)
        print("#"*5,"Geçersiz İşlem Yapıldı.","#"*5)

Menu()