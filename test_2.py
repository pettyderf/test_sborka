import os
import shutil
import json
import subprocess
from datetime import datetime
import zipfile

url = 'https://github.com/paulbouwer/hello-kubernetes'
root_dir = '/temp'
dir = 'src'
version = '25.3000'

def clone_rep(url, root_dir):
    subprocess.run(['git', 'clone', url, root_dir], check=True)

def remove_dir(root_dir, dir):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)

        if os.path.isdir(item_path) and item != dir:
            shutil.rmtree(item_path, ignore_errors=True)

def create_f(root_dir,dir,version):
    files = []
    for dir_item in os.listdir(root_dir+'/'+dir):
        if os.path.isdir(root_dir+'/'+dir+'/'+dir_item):
            for item in os.listdir(root_dir + '/' + dir + '/' + dir_item):
                if item.endswith(('.py', '.js', '.sh')):
                    files.append(item)
            ver_json = {
                "name": "hello world ",
                "version": version,
                "files": files
            }
        else:
            for item in os.listdir(root_dir+'/'+dir):
                if item.endswith(('.py', '.js', '.sh')):
                    files.append(item)
            ver_json = {
                "name": "hello world ",
                "version": version,
                "files": files
            }
    with open(root_dir+'/'+dir + '/version.json', 'w') as file:
        json.dump(ver_json, file)

def create_archive(root_dir,dir):
    current_date = datetime.now().strftime('%d%m%Y')
    for dir_item in os.listdir(root_dir + '/' + dir):
        if os.path.isdir(root_dir + '/' + dir + '/' + dir_item):
            archive_name = root_dir+'/'+dir_item+current_date+'.zip'
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(root_dir+'/'+dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, start=(root_dir+'/'+dir))
                        zipf.write(file_path, arcname=arcname)


print("Начало процесса. ", datetime.now().time())
clone_rep(url, root_dir)
print("Выкачивание исходников завершено. ", datetime.now().time())
remove_dir(root_dir, dir)
print("Удаление директорий завершено. ", datetime.now().time())
create_f(root_dir,dir,version)
print("Создание служебного файла завершено. ", datetime.now().time())
create_archive(root_dir,dir)
print("Создание архива завершено. ", datetime.now().time())
print("Архив находится в директории /temp")