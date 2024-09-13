# Список, создание, удаление репозитория https://github.com с помощью API 

файл test_api.py
## Системные требования
	* selenium == 4.21.0
	* Python >= 3.8.10
## Установка и запуск
Скопировать файлы в директорию.
Установка окружения путем запуска в командной строке:
```sh
pip install -r requirements.txt
```
Переход в директорию для Windows:
```sh
cd C:\projects\example.py
```
для Linux:
```sh
cd /your_path
```
в файле .env  константы изменить  USERNAME= "<username>" имя аккаунта github.com, TOKEN="<your_token>" Ваш токен в кавычках, REPO_NAME="<My_hello_repo>" название репозитория (кавычки необходимы!). 
**TOKEN должен иметь доступ  repo и delete_repo !!**
Запуск
```sh
python test_api.py
```



    
