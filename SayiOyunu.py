from random import randint
print("\t***Sayi Tahmin Oyununa Hoş Geldiniz***")
rand = randint(1,100)
while True:
    print("Yeni oyun için 1'e,\nÇıkmak için 2'ye basınız.")
    b=int(input())
    if b==1:
        while True:
            print("*********************************")
            print("Sayiyi giriniz")
            a = int(input())
            if rand == a:
                print("Doğru :)")
                print("*********************************")
                break
            else:
                if rand < a:
                    print("Daha küçük sayi giriniz.")
                else:
                    print("Daha büyük sayi giriniz.")
    elif b==2:
        print("Programdan çıkılıyor.")
        break
    else:
        print("Yanlış girdi...")