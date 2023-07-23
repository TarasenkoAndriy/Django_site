from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from downconvert.forms import ContactForm
from downconvert.models import MenuItem
#импорт перезагрузки и возврата на страницу с которой начинал
from django.http import HttpResponseRedirect


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
    if request.method =='GET':
        #запрос к базе и достаем ранее загруженные файлы
        pictures = MenuItem.objects.all()
        return  render(request,
                       'user_page.html',
                        {'pictures':pictures})
    elif request.method =='POST':
        picture = MenuItem(
            description = request.POST['description'],
            image = request.FILES['picture']
        )
        picture.save()
        return HttpResponseRedirect('/dowl')

# Create your views here.
