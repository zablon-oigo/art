from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
    Task to send e-mail notification when an order is successfully paid
    """
    order=Order.Objects.get(id=order_id)
    #Create invoice e-mail
    subject=f'Revived Artist - Invoice no. {order.id}'
    message='Please, find attached the invoice for your payment purchase.'
    email=EmailMessage(subject, message, 'imjunior254@gmail.com',[order.email])

    #generate PDF
    html=render_to_string('orders/pdf.html', {'order':order})
    out=BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)

    #attach PDF file
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')

    #send email
    email.send()