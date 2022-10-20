from pytube import YouTube

link = ""

SAVE_PATH = ""

try:
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution')[-1].download(SAVE_PATH)
    print('Video Downloaded!')
except Exception as e:
    print("Error occurred!\n", e)