from main import *

# RSS listesi
rss_feeds = {
    "Hürriyet - Siyaset": "https://www.hurriyet.com.tr/rss/gundem",
    "Hürriyet - Ekonomi": "https://www.hurriyet.com.tr/rss/ekonomi",
    "CNN Türk - Türkiye": "https://www.cnnturk.com/feed/rss/turkiye/news",
    "CNN Türk - Ekonomi": "https://www.cnnturk.com/feed/rss/ekonomi/news",
    "Mynet - Son Dakika": "https://www.mynet.com/haber/rss/sondakika"
}

# Daha önce atılmış haberlerin tutulacağı sözlük
old_entries = {}


def send_to_telegram(chat_id, message, media_url):
    try:
        with app:
            if media_url:
                # Otherwise, assume it's an image
                app.send_photo(chat_id=chat_id,
                               photo=media_url, caption=message)
            else:
                # Send the normal message without any media
                app.send_message(chat_id=chat_id, text=message)
    except Exception as e:
        print(f"Telegram Kanalına gönderilemedi: {e}")


def check_feeds():
    new_entry_found = False

    for feed_name, feed_url in rss_feeds.items():
        print(f"{feed_name} kontrol ediliyor...")
        try:
            feed = feedparser.parse(feed_url)
            entries = feed['entries']

            if len(entries) > 0:
                old_entries.setdefault(feed_url, [])
                latest_entry_id = entries[0].get('id')

                if latest_entry_id not in old_entries[feed_url]:
                    # New entry found
                    old_entries[feed_url].append(latest_entry_id)
                    new_entry_found = True

                    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    title = entries[0].get('title')
                    description = entries[0].get('description')

                    if 'media_content' in entries[0]:
                        # If there is media content, download and send it
                        media_url = entries[0]['media_content'][0]['url']
                        media_data = requests.get(media_url).content
                        media_extension = media_url.split('.')[-1]
                        media_filename = f'{feed_name.replace(" ", "_")}_{date_time.replace(":", "-")}.{media_extension}'
                        with open(media_filename, 'wb') as f:
                            f.write(media_data)

                        message = f"📰 {title} \n\n{description} \n\nTarih: {date_time} \nKaynak: {feed_name}"
                        send_to_telegram(channel_id, message, media_filename)
                        print(
                            f"'{date_time}' Tarihinde '{feed_name}' Beslemesinden alınan 'Fotoğraf içerikli' haber başarıyla gönderildi ✅\n")
                        
                        # Delete the downloaded media file after sending it to the Telegram channel
                        os.remove(media_filename)
                    else:
                        # Otherwise, send the normal message without any media
                        message = f"📰 {title} \n\n{description} \n\nTarih: {date_time} \nKaynak: {feed_name}"
                        send_to_telegram(channel_id, message, None)
                        print(
                            f"'{date_time}' Tarihinde '{feed_name}' Beslemesinden alınan 'Normal' haber başarıyla gönderildi ✅\n")

                    # Wait for 10 seconds between each message to avoid Telegram API limits
                    time.sleep(10)
                else:
                    print(
                        f"{feed_name} beslemesi kontrol edildi, fakat yeni haber bulunamadı.\n")

        except Exception as e:
            print(f"{feed_name} beslemesi kontrol edilirken bir hata oluştu: {e}")

    if not new_entry_found:
        print("Beslemelerde yeni bir haber yok.\n\n")

    # Wait for 90 seconds before checking the feeds again
    time.sleep(90)


while True:
    check_feeds()
