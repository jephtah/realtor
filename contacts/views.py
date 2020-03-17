from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from .models import Contact


def contact(request):
    if request.method == 'POST':
        item = request.POST['item']
        item_id = request.POST['item_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(item_id=item_id, user_id=user_id)

            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this property')
                return redirect('/items/' + item_id)

        conc = Contact(item=item, item_id=item_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        conc.save()

        # send email
        send_mail(
            'Property Inquiry',
            'There has been an inquiry for ' + item + '. Sign into the admin panel for more info.',
            'jephtino@gmail.com',
            [realtor_email, 'jephtino@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted successfully to the realtor.')

        return redirect('/items/' + item_id)
