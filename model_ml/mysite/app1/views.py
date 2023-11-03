from django.shortcuts import render

import pickle
model = pickle.load(open("/Users/satyam/Desktop/Sem5/IT307/project/Model/model_ml/mysite/app1/feature_selected_model.pkl", 'rb'))

def predictor(request):
    if request.method == 'POST':
        #['cp', 'oldpeak', 'thalach', 'thal', 'exang', 'ca', 'sex', 'fbs']
        cp = request.POST['cp']
        oldpeak = request.POST['oldpeak']
        thalach = request.POST['thalach']
        thal = request.POST['thal']
        exang = request.POST['exang']
        ca = request.POST['ca']
        fbs = request.POST['fbs']
        sex = request.POST['sex']
        if sex == 'Male':
            sex = 1
        else:
            sex = 0
        y_pred = model.predict([[cp, oldpeak, thalach, thal, exang, ca, sex, fbs]])
        if y_pred[0] == 0:
            return render(request, 'main.html', {'result' : 'You do not have heart disease'})
        elif y_pred[0] == 1:
            return render(request, 'main.html', {'result' : 'You have heart disease, visit the nearest hospital'})

    return render(request, 'main.html')