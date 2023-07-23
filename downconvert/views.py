# !/usr/bin/env python3
#python3 -m pip install yt_dlp
#python3 -m pip install --no-deps -U yt-dlp
from django.core.mail import EmailMultiAlternatives
# импорт перезагрузки и возврата на страницу с которой начинал
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
import glob


from downconvert.forms import ContactForm
from downconvert.forms import UserForm
from downconvert.models import MenuItem


def index(request):
    menu_brk = MenuItem.objects.filter(type__exact = 'BRK').order_by('?')[:6]
    menu_lun = MenuItem.objects.filter(type__exact ='LUN').order_by('?')[:6]
    menu_din = MenuItem.objects.filter(type__exact ='DIN').order_by('?')[:6]
    context = {'menu_brk' : menu_brk, 'menu_lun': menu_lun, 'menu_din': menu_din}
    return  render(
        request,
        'index.html',
         context=context
    )
def about(request):
    return  render(
        request,
        'about.html'
    )
def contacts(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form']  = form
    return  render(
        request,
        'contacts.html',
        context =  context
    )
def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Hello amigo'
    from_email = 'from@example.com'
    tex_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject,tex_content, from_email,['manager@example.com'])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def dowl(request):
    # ------
    import cgi, cgitb
    cgitb.enable()
    formcdi = cgi.FieldStorage()
    #   # получить имя файла
    # fileitem = formcdi['']
    # fn = os.path.basename(fileitem.filename)
    print(formcdi)
    # ---------sss
    if request.method =='GET':
        #запрос к базе и достаем ранее загруженные файлы
        pictures = MenuItem.objects.all()
        return  render(request,
                       'foto_download.html',
                        {'pictures':pictures})
    elif request.method =='POST':
        picture = MenuItem(
            description = request.POST['description'],
            image = request.FILES['picture']
        )
        picture.save()
        return HttpResponseRedirect('/dowl')

# для скачивания на user_downloud

def user_download(request):

    submitbutton = request.POST.get("submit")

    firstname = ''
    lastname = ''
    emailvalue = ''

    form = UserForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data.get("first_name")
        lastname = form.cleaned_data.get("last_name")
        emailvalue = form.cleaned_data.get("email")

    context = {'form': form, 'firstname': firstname,
               'lastname': lastname, 'submitbutton': submitbutton,
               'emailvalue': emailvalue}
    print(firstname)

    return render(request,
                  'user_download.html',
                  context=context
                 )


global tyr
# https://www.youtube.com/watch?v=59rLWE0fMJo
def ytu_dowl(quest):
   # description = ""
   # if quest.method == 'POST':
   #     descript = quest.POST.get('description')
   # elif quest.method == 'GET':
   #     descript = quest.GET.get('description')
    try:
        import os
        import glob
    except ModuleNotFoundError:
        os.system('pip install glob')
    try:
        import yt_dlp
    except ModuleNotFoundError:
        os.system('pip install yt-dlp')
        os.system('from yt-dlp import YoutubeDL')
    print("Developed by Asiben Tenager")
    ydl_opts = {'format': 'bestvideo[ext= mp4]+bestaudio[ext= m4a]/best[ext= mp4]',
                'outtmpl': 'E:/dowl_youtub/downconvert/y_files/%(uploader)s/%(title)s.%(ext)s',
                'ratelimit': 5000000}
    #ydl_opts = {'format': 'bestvideo+bestaudio/best'}
    #ydl_opts = {'outtmpl': 'E:/dowl_youtub/downconvert/y_files/%(uploader)s/%(title)s.%(ext)s'}
    #ydl_opts = {'ratelimit': 500000}
    URLS = quest['description']
    #URLS = input("URLS")
    video_url = ""
    video_id = ""
    video_title = ""
    video_uploader = ""
    video_ext = ""
    if URLS != " " or URLS is not None:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)
            info_dict = ydl.extract_info(URLS, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_uploader = info_dict.get('uploader', None)
            video_ext = info_dict.get('ext', None)
            x = ("E:\dowl_youtub\downconvert\y_files")
        fx ="\\"
        y = "\\*."
        line_1 = ""
        line_1 = f'{x}{fx}{video_uploader}{y}{video_ext}'

         # Читаем каталог и находим все файлы с рассширением
        partfiles = []
        for file in glob.glob(line_1):
            fileName_absolute = os.path.basename(file)
            partfiles.append(os.path.basename(file))
            vdeo_uploader = video_uploader
            vdeoext = video_ext
            an = partfiles
            description = URLS
            al = {'any': an, 'vdeoext': vdeoext, 'vdeo_uploader': vdeo_uploader, 'description': description}
            return (al)
            #return render(request,'user_page.html')
    else:
        return render('user_page.html' )
#app = FastAPI()
#@app.post("/")
def fdownload(request):
    video_url = ""
    video_id = ""
    video_title = ""
    video_uploader = ""
    video_ext = ""
    description = request.POST.get("description")
    if description == " " or description is None:
        return render(request, 'user_page.html')
    else:
        try:
            import os
            import glob
            import time
        except ModuleNotFoundError:
            os.system('pip install glob')
        try:
            import yt_dlp
        except ModuleNotFoundError:
            os.system('pip install yt-dlp -U')
            os.system('from yt-dlp import YoutubeDL')
            time.sleep(12)
            print("Developed by Asiben Tenager")
        ydl_opts = {'format': 'bestvideo[ext= mp4]+bestaudio[ext= m4a]/best[ext= mp4]',
                    'outtmpl': './y_files/%(id)s/%(title)s.%(ext)s',
                    'ratelimit': 5000000}
        
        URLS = description
        if URLS != " " or URLS is not None:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # ydl.download(URLS)
                info_dict = ydl.extract_info(URLS, download=False)
                video_url = info_dict.get("url", None)
                video_id = info_dict.get("id", None)
                video_title = info_dict.get('title', None)
                video_uploader = info_dict.get('uploader', None)
                video_ext = info_dict.get('ext', None)
        x = ("./y_files/")
        fx = "/"
        y = "/*."
        line_1 = ""
        line_1 = f'{x}{fx}{video_id}{y}{video_ext}'
        #Скачиваем
        ydl.download(URLS)
        # Читаем каталог и находим все файлы с рассширением
        partfiles = []
        fileName_absolute = ""
        #
        for file in glob.glob(line_1):
            fileName_absolute = os.path.basename(file)
            partfiles.append(os.path.basename(file))
            vdeo_uploader = video_uploader
            vdeoext = video_ext
            description = URLS
            vdeo_id = video_id
            cont = {'any': partfiles, 'vdeoext': vdeoext, 'vdeo_id': vdeo_id, 'description': description}
        return render(request, 'user_page.html', cont)
        pass




