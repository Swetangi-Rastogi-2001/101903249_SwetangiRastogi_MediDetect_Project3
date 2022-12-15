from django.shortcuts import render
import numpy as np
import pandas as pd
from . import forms
import pickle
import os

# Create your views here.

def readData(filepath='app/data/parkinsons.csv'):
    df = pd.read_csv(filepath)
    X = df.iloc[:,1:len(df.columns)-1]
    y = df.iloc[:, -1]
    return X, y


def evaluateUserInput(data_features, X_test):
    # X_test = getUserInput(data_features)
    with open(f'app/result/scaler/MinMaxScaler.sav', 'rb') as f:
        scaler = pickle.load(f)
        print(scaler)
        X_test = scaler.transform([X_test])

    model_accuracy_scores = pd.read_csv(
        'app/result/model_evaluation/ModelEvaluationScores.csv'
    )['Accuracy']

    model_list=[]
    test_results = []
    prediction_score = 0
    model_files = os.listdir('app/result/models')
    for model_file in model_files:
        with open(f'app/result/models/{model_file}', 'rb') as f:
            model = pickle.load(f)
            model_list.append(model)
            test_results.append([str(model)[ : str(model).index('(')]])

    for index, classifier in enumerate(model_list):
        y_pred = classifier.predict(X_test)
        y_pred = 'Positive' if y_pred == 1 else 'Negative'

        if y_pred == 'Positive':
            prediction_score += 1 * model_accuracy_scores[index]
        else:
            prediction_score -= 1 * model_accuracy_scores[index]

        test_results[index].append(y_pred)

    
    prediction_score = prediction_score / sum(model_accuracy_scores)
    if prediction_score < 0:
        prediction_class = 'Negative'
    elif prediction_score > 0:
        prediction_class = 'Positive'
    else:
        prediction_class = 'Indeterminate'

    
    # print('\n\nResults :-')
    # for test_result in test_results:
    #     print(test_result[0], ':', test_result[1])
    # print('\n')
    # print(f'The weighted average of all the models: {prediction_score}')
    # print(f'The predicted label for given review is {prediction_class}')
    # print('\n\n')

    results = {}
    for test_result in test_results:
        results[test_result[0]] = test_result[1]
    
    final_result = []
    final_result.append(results)
    final_result.append(prediction_score)
    final_result.append(prediction_class)

    return final_result
    


def getUserInput(data_features):
    user_input = []
    for feature in data_features.columns:
        print(f'Enter value for {feature}')
        print(f'Range is {min(data_features[feature])} to {max(data_features[feature])}')
        user_input.append(input('Your input: '))
    return user_input
    

def Home(request):
    X, y = readData(filepath='app/data/parkinsons.csv')
    
    
    if request.method == 'POST':
        form = forms.InputDataForm(request.POST)
        if form.is_valid():
            mdvp_fo_hz = form.cleaned_data['mdvp_fo_hz']
            mdvp_fhi_hz = form.cleaned_data['mdvp_fhi_hz']
            mdvp_flo_hz = form.cleaned_data['mdvp_flo_hz']
            mdvp_jitter_per = form.cleaned_data['mdvp_jitter_per']
            mdvp_jitter_abs = form.cleaned_data['mdvp_jitter_abs']
            mdvp_rap = form.cleaned_data['mdvp_rap']
            mdvp_ppq = form.cleaned_data['mdvp_ppq']
            jitter_ddp = form.cleaned_data['jitter_ddp']
            mdvp_shimmer = form.cleaned_data['mdvp_shimmer']
            mdvp_shimmer_db = form.cleaned_data['mdvp_shimmer_db']
            shimmer_apq3 = form.cleaned_data['shimmer_apq3']
            shimmer_apq5 = form.cleaned_data['shimmer_apq5']
            mdvp_apq = form.cleaned_data['mdvp_apq']
            shimmer_dda = form.cleaned_data['shimmer_dda']
            nhr = form.cleaned_data['nhr']
            hnr = form.cleaned_data['hnr']
            rpde = form.cleaned_data['rpde']
            dfa = form.cleaned_data['dfa']
            spread_1 = form.cleaned_data['spread_1']
            spread_2 = form.cleaned_data['spread_2']
            d2 = form.cleaned_data['d2']
            ppe = form.cleaned_data['ppe']


            user_input = []
            user_input.append(mdvp_fo_hz)
            user_input.append(mdvp_fhi_hz)
            user_input.append(mdvp_flo_hz)
            user_input.append(mdvp_jitter_per)
            user_input.append(mdvp_jitter_abs)
            user_input.append(mdvp_rap)
            user_input.append(mdvp_ppq)
            user_input.append(jitter_ddp)
            user_input.append(mdvp_shimmer)
            user_input.append(mdvp_shimmer_db)
            user_input.append(shimmer_apq3)
            user_input.append(shimmer_apq5)
            user_input.append(mdvp_apq)
            user_input.append(shimmer_dda)
            user_input.append(nhr)
            user_input.append(hnr)
            user_input.append(rpde)
            user_input.append(dfa)
            user_input.append(spread_1)
            user_input.append(spread_2)
            user_input.append(d2)
            user_input.append(ppe)

            results = evaluateUserInput(X, user_input)
            
            return render(request, 'result.html', {'model_results': results[0], 'prediction_score': results[1], 'prediction_class': results[2]})
            

        else:
            print(form.errors)
    else:
        form = forms.InputDataForm()
        return render(request, 'home.html', {'form': form})




