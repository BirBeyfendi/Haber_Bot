# Haber_Bot
## Telegramda belirlediğiniz bir kanala RSS beslemelerinden alınan haberleri atmak için yazılmış bir bottur.
### Not: Haberlerin kanala atılması için haberlerin atılacağı kanalın id si yerine ```kullanıcı adını``` yazmalısınız, bot ise ```haberlerin atılacağı kanalda bulunmalı``` ve ```yetkili olmalıdır```.
### ```API_ID``` , ```API_HASH``` ve ```BOT_TOKEN``` değerlerini yazarak botu çalıştırabilirsiniz ancak bot kanalda olmalı ve yetkisi de bulunmak zorundadır. Ek bir komut ihtiyacı kalmadan çalıştırılır çalıştırılmaz bot otomatik olarak haberleri atmaya başlar.
### Her zaman RSS beslemelerinde bulunan ```en son haberleri``` atar, yeni bir haber beslemelere düşünce ```otomatik olarak``` yeni haberi gönderir.
### Haberleri RSS beslemelerinden çekeceği zaman ve çektiği haberleri kanala gönderirken pek çok bekleme uygular ```(time.sleep)```, bu sayede botun flood wait e düşmesi büyük oranda engellenmiş olur.
