from threading import Thread
from os import path, makedirs, listdir  # makedirs(шлях до створеної папки),
# path.dirname(); path.exists(path)->True; path.isdir(path)->True 
import shutil

folder_path = input('Введіть будь-ласка шлях до потрібної папки>>')

DOCUMENTS = ['.txt', '.rtf', '.docx', '.pptx', '.xlsx']
AUDIO = ['.mp3', '.waw']
MEDIA = ['.mp4', '.bmp']

documents_folder = path.join(folder_path, 'Documents')
audio_folder = path.join(folder_path, 'Audio')
media_folder = path.join(folder_path, 'Media')

def sort_folder(folder_path):
    for filename in listdir(folder_path):
        file_path = path.join(folder_path, filename)
        _, file_ext = path.splitext(file_path)

        if file_ext in DOCUMENTS:
            if path.exists(documents_folder) == False:
                makedirs(documents_folder)
                shutil.move(file_path, documents_folder)
            else:
                shutil.move(file_path, documents_folder)
        
        elif path.isdir(file_path) == True:
            sort_thread = Thread(target=sort_folder, args=(file_path,))
            sort_thread.start()
            sort_thread.join()
            
        elif file_ext in AUDIO:
            if path.exists(audio_folder) == False:
                makedirs(audio_folder)
                shutil.move(file_path, audio_folder)
            else:
                shutil.move(file_path, audio_folder)

        elif file_ext in MEDIA:
            if path.exists(media_folder) == False:
                makedirs(media_folder)
                shutil.move(file_path, media_folder)
            else:
                shutil.move(file_path, media_folder)

main_tread=Thread(target=sort_folder, args=(folder_path,))
main_tread.start()
main_tread.join()

