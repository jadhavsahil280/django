from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import profile
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

import pdfkit
import base64
import os

# Create your views here.
def index(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        job_title = request.POST.get('job_title', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        degree = request.POST.get('degree', '')
        college = request.POST.get('college', '')
        passing_year = request.POST.get('passing_year', '')
        percentage = request.POST.get('percentage', '')
        company_name = request.POST.get('company_name', '')
        experience = request.POST.get('experience', '')
        job_desc = request.POST.get('job_desc', '')
        skills = request.POST.get('skills', '')
        languages_known = request.POST.get('languages_known', '')
        photo = request.FILES.get('photo')


        profiledate = profile(name=name, email=email, phone=phone, jobtitle=job_title, dob=dob, gender = gender, address=address, degree=degree, college=college, passingyear=passing_year, percentage=percentage, previouscompanyname=company_name, experience=experience, jobdesc=job_desc, skills=skills, languagesknown=languages_known, photo=photo)
        
        profiledate.save()

        return redirect('generatecv', id = profiledate.id)


    

    return render(request, 'pdf/index.html')


def cvGenerator(request, id):
    profiledata = profile.objects.get(pk=id)

    print("photo path : " + str(profiledata.photo.path))

    photo_base64 = ""

    try:
        if profiledata.photo and profiledata.photo.path:

            print("base64 called")

            with open(profiledata.photo.path, "rb") as f:

                ext = os.path.splitext(profiledata.photo.path)[1].lower().strip(".")

                mime = "jpeg" if ext in ("jpg", "jpeg") else ext

                photo_base64 = f"data:image/{mime};base64,{base64.b64encode(f.read()).decode()}"

    except Exception as e:
        print("ERROR :", e)

    print("photo :", photo_base64[:100])

    return render(request, 'pdf/cv_template.html', {'profile' : profiledata, "photo_base64": photo_base64,})

def downloadCV(request, id):
    profiledata = profile.objects.get(pk=id)

    photo_base64 = ""
    try:
        if profiledata.photo:
            with open(profiledata.photo.path, "rb") as f:

                ext = os.path.splitext(profiledata.photo.path)[1].lower().strip(".")

                mime = "jpeg" if ext in ("jpg", "jpeg") else ext

                photo_base64 = f"data:image/{mime};base64,{base64.b64encode(f.read()).decode()}"
    except Exception:
        pass

    options = {
        'enable-local-file-access': '',
        'load-error-handling': 'ignore',
        'load-media-error-handling': 'ignore',
        'encoding': 'UTF-8',
    }

    html = render_to_string('pdf/download_template.html', {'profile': profiledata, 
        "photo_base64": photo_base64,})
    
    print(photo_base64)

    pdf = pdfkit.from_string(
        html,
        False,
        options=options
    )

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response