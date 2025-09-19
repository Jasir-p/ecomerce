
import random
from django.core.mail import send_mail
from shopifyproject.settings import EMAIL_HOST_USER
from datetime import date, timedelta, timezone, datetime

def generate_otp_and_send_email(request,email):
    otp = random.randint(1000, 9999)
    otp_generated_at = datetime.now().isoformat()
    

    request.session["otp"] = otp 
    request.session["time"] = otp_generated_at

    send_mail(
        subject="Welcome",
        message=f"Your OTP for verification is: {otp}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


def validate_otp(request):
    otp1 = request.POST.get("otp1")
    otp2 = request.POST.get("otp2")
    otp3 = request.POST.get("otp3")
    otp4 = request.POST.get("otp4")

    full_otp = otp1 + otp2 + otp3 + otp4
    

    if "otp_email" in request.session:
        otp =request.session["otp"] 
        otp_generated =request.session["time"]
        delta = timedelta(minutes=2)
        time = datetime.fromisoformat(otp_generated)

        if datetime.now() > time + delta:
            if int(full_otp) != otp:
                    return "Incorrect OTP! Please try again."
            
            return "OTP has expired. Please request a new one."

        return "OTP session has expired or not set. Please request a new one."
    
    return None



def otp_resend(request):
    otp = random.randint(1000, 9999)
    otp_generated_at = datetime.now().isoformat()
    
    
    request.session["otp"] = otp
    request.session["time"] = otp_generated_at
    email = request.session["email"]

    send_mail(
        subject="Welcome",
        message=f"Your OTP for verification is: {otp}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
     
