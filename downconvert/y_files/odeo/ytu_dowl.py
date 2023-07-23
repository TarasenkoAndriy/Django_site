import os
import os,subprocess
import time

                 
tyr = "https://www.youtube.com/watch?v=59rLWE0fMJo"
def ytu_dowl():
    global tyr
    import os
    import os, subprocess
    import time
#    description = request.POST.get("description")
    my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "w+")
    my_file.write('@echo off \n')

    my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "a+")
    my_file.write(':loop \n')

   #my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat","a+")
   #my_file.write('set /p input="URL:')
   #my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat","a+")
   #my_file.write(''+str(tyr)+'" \n')
    
    my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "a+")
    my_file.write('E:\dowl_youtub\downconvert\y_files\yt-dlp.exe -f mp4 ' + str(tyr) + ' E:\dowl_youtub\downconvert\y_files\ \n')

    #my_file = open("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat", "a+")
    #my_file.write('goto loop \n')

    my_file.close()

    # Запускаем
    os.system("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat")
    time.sleep(120)
    os.remove("E:\dowl_youtub\downconvert\y_files\Baby\BabyFile.bat")

    # Читаем командную строку
    #time.sleep(0)
    #output = subprocess.getoutput('pyinstaller E:\dowl_youtub\downconvert\ytu_dowl.py')
    #print(output)
    return()
print(ytu_dowl())
 #-----------------------------
    #strings = ["Concatenating", "strings", "in Python", "is easy!"]
    #result = ""
    #for string in strings:
    #result += string + " "
    #----------------------
