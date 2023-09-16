# Haber Bot
* Telegramda belirlediğiniz bir kanala RSS beslemelerinden alınan haberleri atmak için yazılmış basit bir bottur.
* Not: Haberlerin kanala atılması için haberlerin atılacağı kanalın ```ID```'sini yazmalısınız, bot ise ```haberlerin atılacağı kanalda bulunmalı``` ve ```yetkili olmalıdır```.
## Gereksinimler:
* ```API_ID``` , ```API_HASH``` ve ```BOT_TOKEN``` değerlerini yazarak botu çalıştırabilirsiniz ancak bot kanalda olmalı ve yetkisi de bulunmak zorundadır.
## Bot Hakkında Çeşitli Bilgiler:
* Ek bir komut ihtiyacı kalmadan çalıştırılır çalıştırılmaz bot otomatik olarak haberleri atmaya başlar.
* Her zaman RSS beslemelerinde bulunan ```en son haberleri``` atar, yeni bir haber beslemelere düşünce ```otomatik olarak``` yeni haberi gönderir.
* Bot hiç bir zaman ```aynı haberi birden fazla``` göndermez, bir haberi kanala gönderdikten sonra ```yeni haberleri``` beklemeye başlar, beklerken ```90 saniyede bir``` beslemeleri teker teker kontrol eder.
* Haberleri RSS beslemelerinden çekeceği zaman ve çektiği haberleri kanala gönderirken pek çok bekleme ```(time.sleep)``` uygular, bu sayede botun flood wait e düşmesi büyük oranda engellenmiş olur.
* Belirlemiş olduğunuz kanala haber biçimi olarak ```Normal``` ve ```Fotoğraflı``` olacak şekilde 2 çeşit olarak gönderir.
## Botun Haberleri Almak İçin Kullandığı Örnek RSS Beslemeleri:
* Hürriyet - Siyaset
* Hürriyet - Ekonomi
* CNN Türk - Türkiye
* CNN Türk - Ekonomi
* Mynet - Son Dakika
