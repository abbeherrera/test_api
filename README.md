# Список, создание, удаление репозитория https://github.com с помощью API 

файл test_api.py
## Системные требования
	Windows10 или Ubuntu >=20
## Установка и запуск
Скопировать файлы в директорию.
Переход в директорию для Windows:
```sh
cd C:\projects\example.py
```
для Linux:
```sh
cd /your_path
```
Установка окружения путем запуска в командной строке:
```sh
pip install -r requirements.txt
```

в файле .env  константы изменить  U_NAME= "<username>" имя аккаунта github.com, TOKEN="<your_token>" Ваш токен в кавычках, REPO_NAME="<My_hello_repo>" название репозитория (кавычки необходимы!). 
**TOKEN должен иметь доступ  repo и delete_repo !!**
Запуск
```sh
python test_api.py
```
или
```sh
python3 test_api.py
```


    
