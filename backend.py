from moviepy.editor import *
from pytube import Playlist, YouTube
import os


class Youtubedownloader:

    def download_single_video(self, url, save_path):
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
            print("Название видео:", yt.title)

            filename = yt.title.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('&', '_').replace('%', '_').replace('#', '_').replace('{', '_').replace('}', '_').replace('[', '_').replace(']', '_').replace('=', '_').replace('+', '_').replace('-', '_').replace('--', '_').replace(';', '_').replace('!', '_').replace('@', '_').replace('$', '_').replace('^', '_').replace('`', '_').replace('~', '_').replace(',', '_').replace('.', '_').replace(' ', '_')

            stream.download(output_path=save_path, filename=filename)
            print(f"Видео успешно загружено! Видео сохранено как -> {filename}.mp4 в {save_path}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def download_playlist(self, url, save_path):
        try:
            p = Playlist(url)
            for video_url in p.video_urls:
                print(f"Загрузка видео: {video_url}")
                self.download_single_video(video_url, save_path)
            print("Все видео были загружены")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def download_video_as_audio(self, url, save_path):
        try:
            print("Доступ к URL адресу")
            yt = YouTube(url)
            print(f"Загрузка аудио из: {yt.title}")

            audio_stream = yt.streams.filter(only_audio=True).first()
            if not audio_stream:
                print("Нет доступного аудио потока")
                return

            output_file = audio_stream.download(output_path=save_path)
            print("Аудио файл загружен:", output_file)

            new_file = os.path.splitext(output_file)[0] + '.mp3'
            print("Конвертация файла в MP3...")
            audio_clip = AudioFileClip(output_file)
            audio_clip.write_audiofile(new_file, codec='mp3')
            audio_clip.close()

            os.remove(output_file)
            print("Конвертация завершена. Файл сохранен как:", new_file)

        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def download_playlist_as_mp3(self, url, save_path):
        try:
            p = Playlist(url)
            for video_url in p.video_urls:
                print(f"Загрузка видео: {video_url}")
                self.download_video_as_audio(video_url, save_path)
            print("Все видео были загружены")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

downloader = Youtubedownloader()
link = "https://www.youtube.com/watch?v=YP2ilWcJ3AU"
path_test = "/home/status/Documents/You_Download_Project"

downloader.download_video_as_audio(link, path_test)