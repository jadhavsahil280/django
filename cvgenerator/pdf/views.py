from django.shortcuts import render
from .models import profile

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
        photo = request.POST.get('photo', '')

        profiledate = profile(name=name, email=email, phone=phone, jobtitle=job_title, dob=dob, gender = gender, address=address, degree=degree, college=college, passingyear=passing_year, percentage=percentage, previouscompanyname=company_name, experience=experience, jobdesc=job_desc, skills=skills, languagesknown=languages_known, photo=photo)
        
        profiledate.save()
    

    return render(request, 'pdf/index.html')