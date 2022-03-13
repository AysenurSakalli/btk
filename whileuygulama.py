#kullanıcı adı ve şifre alınız.. kullanıcı adı olarak "admin" şifre olarak #123456 girilince "sisteme başarıyla giriş yaptınız" yazsın..
#yanlış girildikçe "kullanıcıadı veya şifre hatalı" yazıp
#tekrar kullanıcı adı ve şifre sorsun!
while True:
    kullaniciadı=input("Kullanıcı adınız:")
    sifre=input("Parolanız:")
    if kullaniciadı=="admin" and şifre=="123456":
        break
    else:
        print("Kullanıcı adı veya parola hatalı")