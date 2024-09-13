#Скрипт должен использовать API GitHub для выполнения следующих операций:
#1. Создание нового публичного репозитория.
#2. Проверка списка репозиториев для подтверждения создания.
#3. Удаление репозитория.
import dotenv.version
import requests
#import json
import time
import os
import dotenv
from dotenv import load_dotenv

print("requests=",requests.__version__)
#print(time.__version__)
#print(os.__version__)
#print("dotenv=",dotenv..version)






dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
print(dotenv_path)

USERNAME= os.getenv("USERNAME")
TOKEN= os.getenv("TOKEN")
REPO_NAME=os.getenv("REPO_NAME")

print()



PATH_GIT="https://api.github.com"
PATH_GET=f"{PATH_GIT}/users/{USERNAME}/repos"
PATH_POST=f"{PATH_GIT}/user/repos"
PATH_DEL=f"{PATH_GIT}/repos/{USERNAME}/{REPO_NAME}"

AUTO=f"Authorization: Bearer {TOKEN}"



#List of public repository
def listRepos():
    response_get = requests.get(PATH_GET ,AUTO,json={"Cache-Control": "no-cache"})
    st_code_lst=response_get.status_code
    print(st_code_lst)
    if st_code_lst==200:
        print("Ok, passed")
    lst_json_response=response_get.json()
    print("repositories: ", len(lst_json_response))
    dict_json={}
    for cnt_url in range(len(lst_json_response)):
        dict_json=lst_json_response[cnt_url]
        print(dict_json["svn_url"],"private=", dict_json["private"] )
#Create repository
def createRepo():
    #data = { "name": f"{REPO_NAME}", "description": "New repo", "private": false }
    #response_post = requests.post(f'{PATH_GIT}/user/repos',headers={"Authorization": f"Bearer {TOKEN}"},  json=data)
    response_post = requests.post(f'{PATH_GIT}/user/repos',headers={"Authorization": f"Bearer {TOKEN}" }, json= { "name": f"{REPO_NAME}" , "description": "New"})#,"private": "1",
    
    st_code_create=response_post.status_code
    print(st_code_create)
    if st_code_create==201:
        print(f"Orlait, Created {REPO_NAME}")
#Delete repository
def deleteRepo():
    
    response_del=requests.delete(f"{PATH_GIT}/repos/{USERNAME}/{REPO_NAME}",auth=( 'Bearer', TOKEN))
    st_code_delete=response_del.status_code
    print(st_code_delete)
    if st_code_delete==204:
        print(f"Orlait, No content. {REPO_NAME} deleted")


listRepos()
createRepo()
time.sleep(10)
deleteRepo()
#time.sleep(5)
#createRepo()
#timeout before control
time.sleep(20)
listRepos()



