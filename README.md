# Parkinsons-Disease Prediction

Parkinson's disease (PD), or simply Parkinson's, is a long-term degenerative disorder of
the central nervous system that mainly affects the motor system. The symptoms usually emerge
slowly, and as the disease worsens, non-motor symptoms become more common. The most
obvious early symptoms are tremor, rigidity, slowness of movement, and difficulty with walking.
Cognitive and behavioral problems may also occur with depression, anxiety, and apathy occurring
in many people with PD. The rock sensation Ozzy Osbourne, dubbed as the God of Boxing, Mohd.
Ali were among few renowned personalities who have contracted this disorder.
Mostly, it goes un-noticed or is misdiagnosed as some other disorder due to which it often leads
to the patient finding himself in a fatal condition. Hence, I have deployed a model which shall take
attributes from the user and shall predict if they have contracted the disorder or not.

## Dataset

The dataset provided to me has 22 attributes which shall be taken as input from the user. Using
our prediction model over the provided inputs, we are going to predict whether the person has
Parkinson’s Disorder or not. The following were the attributes in the given dataset.


<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.56.13%20PM.png" width="600" height="400" />


## Graphical Depiction of the attributes

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.49.40%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.49.44%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.49.49%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.49.59%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.49.56%20PM.png" width="600" height="400" />

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.49.52%20PM.png" width="600" height="400" />




## Models Used:

• Decision Tree Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.04%20PM.png" width="500" height="600" />

• Logistic Regression

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.18%20PM.png" width="500" height="600" />

• Random Forest Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.23%20PM.png" width="500" height="600" />

• K-Neighbor Classifier

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.31%20PM.png" width="500" height="600" />

• SVC

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.37%20PM.png" width="500" height="600" />

• Multinomial NB

<img src="https://github.com/2000utkarsh/Water-Potability/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.23.49%20PM.png" width="500" height="600" />

## Approach:
During the very first phase of the model, I cleaned the data and made it more sensible in numeric form, i.e. converted all the categorical data to numerical data and removed the NULL and missing values.
In the Second Phase, I did some visualizations over the given dataset which gave me a great view and hints for the implementation of the model.
In the third phase, I implemented various methods over the given dataset, the ones I had mentioned previously. The model gave prediction taking each and every model into consideration and then took out the average value of all the models result and then gave the result which were based on the provided input by the user.
In the final phase, I developed the UI for the model and then linked my model with the created UI for to make it ready for deployment in Django.

## User Interface:



<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.50.41%20PM.png" width="500" height="400" />

<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.50.45%20PM.png" width="500" height="400" />


## Output Screen
<img src="https://github.com/2000utkarsh/Parkinsons-Disease/blob/master/app/imgs/Screenshot%202021-09-20%20at%208.50.49%20PM.png" width="500" height="400" />




## Future Scope

It is quiet a revealing fact that almost 70% cases of Parkinson’s disease either go un-noticed or are misdiagnosed. These happen due to lack of proper knowledge and improper ways of detecting the disorder. Because of rapid increase in the number of cases in the youth, it has become of utmost importance to develop a model so that a person can get his diagnosis within minutes after providing input to the model. Our model provides the same kind response that the user desires. He/She can directly get the results within minutes, hence saving them from some misdiagnosis and some visits to the doctor for the same.
















