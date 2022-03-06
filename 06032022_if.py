#KARŞILAŞTIRMA OPERATÖRLERİ
"""
<  :küçüktür
>  :büyüktür
<= :küçük eşit
>= :büyük eşit
== :eşittir
|= :eşit değildir
"""
cinsiyet=input("bir harf giriniz:")

if cinsiyet=="e"or cinsiyet== "E": #or: 2 şarttan biri doğru ise çalışır
    print("cinsiyet olarak erkek giriniz")
    print("if içerisinden selamlar")
print("şuanda if dışındasın")
elif cinsiyet=="k"or cinsiyet=="K":#or: 2.veya daha sonraki şartları eklemek için elif kullanılır
     print("cinsiyet olarak kadın girdiniz")
     print("şuanda elif bloğu içindenmesaj veriyorum")
else #şartların dışında herhangi birşey girilirse çalışır
     print("ben sana e ya da k gir demedim mi?")
     print("şuanda if dışındasın")
