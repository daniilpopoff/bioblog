from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from .forms import HeartDiseaseForm
# Create your views here.

def about_me(request):
    return render(request, "about_me.html")




def heart(request):
	# Read the heart disease training data from a CSV file
	df = pd.read_csv('static/Heart_train.csv')
	data = df.values
	X = data[:, :-1] # Input features (all columns except the last one)
	Y = data[:, -1:] # Target variable (last column)


	value = ''


	if request.method == 'POST':
		form = HeartDiseaseForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
		else:
			return render(request, 'your_template.html', {'form': form})
		form_data = form.cleaned_data
		# Retrieve the user input from the form
		# age = form.cleaned_data['age']
		# sex = form.cleaned_data['sex']
		# cp = form.cleaned_data['cp']
		# trestbps = form.cleaned_data['trestbps']
		# chol = form.cleaned_data['chol']
		# fbs = form.cleaned_data['fbs']
		# restecg = form.cleaned_data['restecg']
		# thalach = form.cleaned_data['thalach']
		# exang = form.cleaned_data['exang']
		# oldpeak = form.cleaned_data['oldpeak']
		# slope = form.cleaned_data['slope']
		# ca = form.cleaned_data['ca']
		# thal = form.cleaned_data['thal']

		# form_fields_with_user_data = form.fields
		# Create a numpy array with the user's data

		# user_data = np.array(
		# 	for  field_name, user_data in  form_fields_with_user_data.values():
		# 		user_data
		# )
		user_data = np.array(list(form_data.values())).reshape(1, -1)
		# user_data = np.array(
		# 	(age,
		# 	sex,
		# 	cp,
		# 	trestbps,
		# 	chol,
		# 	fbs,
		# 	restecg,
		# 	thalach,
		# 	exang,
		# 	oldpeak,
		# 	slope,
		# 	ca,
		# 	thal)
		# ).reshape(1, 13)

		# Create and train a Random Forest Classifier model
		rf = RandomForestClassifier(
			n_estimators=16,
			criterion='entropy',
			max_depth=9
		)

		rf.fit(np.nan_to_num(X), np.ravel(Y)) # Train the model using the training data
		rf.score(np.nan_to_num(X), Y) # Evaluate the model's accuracy
		predictions = rf.predict(user_data) # Make predictions on the user's data

		if int(predictions[0]) == 1:
			value = 'have' # User is predicted to have heart disease
		elif int(predictions[0]) == 0:
			value = "don\'t have" # User is predicted to not have heart disease

		instance.predicted_value = predictions[0]
		instance.save()


	return render(request,
				'heart.html',
				{
					'context': value,
					'title': 'Heart Disease Prediction',
					'active': 'btn btn-success peach-gradient text-white',
					'heart': True,
					'form': HeartDiseaseForm(),
				})


def home(request):
	return render(request,
				'home.html')
