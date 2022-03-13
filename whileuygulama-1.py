#Kullanıcı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak 123456 girilince "sisteme
#başarıyla giriş yaptınız" yazsın:
#yanlış girildikçe "kullanıcı adı veya şifre hatalı" yazıp tekrar kullanıcı adı ve şifre sorsun!

while True:
    kullanicininadı=input("Adınızı Giriniz:")
    sifre=int(input("Şifrenizi Giriniz:"))
    if kullanicininadı=="admin" and sifre==123456:
         break
    else:
        print("Tekrar Deneyiniz...")

print("Sisteme başarıyla giriş yaptınız..")
