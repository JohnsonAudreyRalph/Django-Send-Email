from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.utils.html import format_html
from django.conf import settings
from .models import Email_Content


# Create your views here.
def index(request):
    if request.method == 'POST':
        Name_ = request.POST.get("name")
        Email_ = request.POST.get("email")
        Subject_ = request.POST.get("subject")
        Message_ = request.POST.get("message")

        print(Name_, Email_, Subject_, Message_)
        message = format_html('Xin chào bạn ' + Name_ + '! <p>Xin cảm ơn bạn đã gửi ý kiến đóng góp của bạn đến với chúng tôi</p><p>Chúng tôi sẽ nhanh chóng xử lý ý kiến đó của bạn và phản hồi lại cho bạn một cách nhanh chóng nhất.</p><p><strong>Xin trân trọng cảm ơn</strong></p>')
        
        send_mail(
            'Thư phản hồi',
            message,
            'settings.EMAIL_HOST_USER',
            [Email_],
            html_message=message
        )
        save = Email_Content(User_name=Name_, User_email=Email_, User_subject=Subject_, User_message=Message_)
        save.save()

        return render(request, 'index.html', {'Name':Name_})
    # subject = 'Thư phản hồi'
    # message = format_html('Xin chào bạn! <p>Xin cảm ơn bạn đã gửi ý kiến đóng góp của bạn đến với chúng tôi</p><p>Chúng tôi sẽ nhanh chóng xử lý ý kiến đó của bạn và phản hồi lại cho bạn một cách nhanh chóng nhất.</p><p><strong>Xin trân trọng cảm ơn</strong></p>')
    # from_email = 'hoangphi11343@gmail.com'
    # recipient_list = ['hoangphi11343@gmail.com']
    
    # send_mail(subject, message, from_email, recipient_list, html_message=message)
    else:
        return render(request, 'index.html')

def reload(request):
    return redirect('/')