import yt_dlp
videoLink = input("Enter link: ")
yt_dlp.YoutubeDL({'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}).download([videoLink])