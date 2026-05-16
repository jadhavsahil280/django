from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def index(request):



    if request.method == "POST":
        link = request.POST.get('link', '')

        linkdata = requests.get(link)

        soup = BeautifulSoup(linkdata.text, 'html.parser')

        links = []



        for link in soup.find_all('a'):
            # links.append(link.get('href'))

            linkaddress = link.get('href')
            linkname = link.string

            links.append({
                'name': linkname,
                'address': linkaddress
            })

        

        


    
    return render(request, 'scraplink/index.html', {'links': links})