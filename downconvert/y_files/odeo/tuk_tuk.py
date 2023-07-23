import django
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template
from setuptools._distutils.file_util import write_file

from downconvert.forms import ContactForm
from downconvert.models import MenuItem
#импорт перезагрузки и возврата на страницу с которой начинал
from django.http import HttpResponseRedirect


from downconvert.forms import UserForm
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import Form
import os, subprocess

                 
global tyr
# https://www.youtube.com/watch?v=59rLWE0fMJo
def ytu_dowl(request):
    global  tyr
    import os
    import os, subprocess
    import time
 #   tyr = request.POST.get("description")
    my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "w+")
    my_file.write('@echo off \n')

    my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "a+")
    my_file.write(':loop \n')

    # my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat","a+")
    # my_file.write('set /p input="URL:')
    # my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat","a+")
    # my_file.write(''+str(tyr)+'" \n')

    my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "a+")
    my_file.write(
        'E:\dowl_youtub\downconvert\y_files\yt-dlp.exe -f mp4 ' + str(tyr) + ' E:\dowl_youtub\downconvert\y_files\ \n')

    # my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "a+")
    # my_file.write('goto loop \n')

    my_file.close()

    # Запускаем
    os.system("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat")
    time.sleep(120)
    os.remove("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat")

    # Читаем командную строку
    # time.sleep(0)
    # output = subprocess.getoutput('pyinstaller E:\dowl_youtub\downconvert\ytu_dowl.py')
    # print(output)
    return ()
#app = FastAPI()
#@app.post("/")
def fdownload(request):
   global tyr
#   pat = os.PathLike
#   if request.method == 'POST':
   description = request.POST.get("description")
   tyr = description
   context = {'any': any, 'description': description}
 #  print(ytu_dowl())
   return render(request,
                  'user_page.html',
                  context
                  )


#   return HttpResponseRedirect('/user_download')
# Create your views here.
