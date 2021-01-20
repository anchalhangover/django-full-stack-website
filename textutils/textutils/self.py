#fjeiteg
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
#     return HttpResponse('''<h1>hello anchal</h1> <a href=" http://127.0.0.1:8000/about">click me </a>''')
# def analyse(request):
#       return HttpResponse('''<a href=" http://127.0.0.1:8000/removepunch">click me</a> about <a href="/">back</a>''')
def analyse(request):
      djtext=request.GET.get('text')
      #get the text
      print(djtext)
      removepunch= request.GET.get('removepunch', 'off')
      fullcaps= request.GET.get('fullcaps', 'off')
      newlineremover = request.GET.get('newlineremover', 'off')
      extraspaceremover=request.GET.get('extraspaceremover','off')
      print(removepunch)
      if (removepunch == "on"):
            punctuations='''!@#$%^&*()_+|{}":?><;'/.,[]'''
            analysed=""
            for char in djtext:
                  if char not in punctuations:
                        analysed =analysed + char

            param={'purpose':'remove punctuations','analysed_text':analysed}


            return render(request,'analyse.html',param)
      elif(fullcaps=="on"):
            analysed=""
            for char in djtext:
                  analysed = analysed + char.upper()
            param = {'purpose': 'changed to upper case', 'analysed_text':analysed}
            return render(request,'analyse.html',param)
      elif (extraspaceremover== "on"):
            analysed = ""

            for index, char in enumerate(djtext):
                        if not(djtext[index] ==" " and djtext[index+1] == " "):
                              analysed = analysed + char
            param = {'purpose': 'remove extra space', 'analysed_text': analysed}
            return render(request, 'analyse.html', param)


      elif (newlineremover== "on"):
            analysed = ""
            for char in djtext:
                  if (char !='\n'):
                   analysed = analysed + char
            param = {'purpose': 'changed to newline', 'analysed_text': analysed}
            return render(request, 'analyse.html', param)
      else:
            analysed=" "
            for char in djtext:

                        analysed =analysed + char
            param = {'purpose': '', 'analysed_text': analysed}


            return render(request,'analyse.html',param)


