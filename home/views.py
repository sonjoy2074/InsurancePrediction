from django.shortcuts import render, HttpResponse
import joblib
model = joblib.load('static/insu_model.joblib') 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prediction(request):
    if request.method == "POST":
        try:
            age = int(request.POST.get('age'))
            sex = int(request.POST.get('sex'))
            bmi = float(request.POST.get('bmi'))
            children = int(request.POST.get('children'))
            smoker = int(request.POST.get('smoker'))
            region = int(request.POST.get('region'))
            
            prediction = model.predict([[age, sex, bmi, children, smoker, region]])
            return render(request, 'prediction.html', {'prediction': prediction[0]})
            
        except Exception as e:
            return render(request, 'prediction.html', {'error': str(e)})
    
    return render(request, 'prediction.html')