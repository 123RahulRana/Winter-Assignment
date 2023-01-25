# -*- coding: utf-8 -*-
"""CreditCardFraud.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/127hQ6cqLt_Gxm3R_FcMwroCAJq7y978d

Import Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data set to panda dataframe
credit_card_data = pd.read_csv('/content/creditcard.csv')

#first 5 row of data set
credit_card_data.head()

credit_card_data.tail()

#info data set
credit_card_data.info()

# or checking the missing values same as above
credit_card_data.isnull().sum()

#distribution of legit and fraud tranc.
credit_card_data['Class'].value_counts()

#unstable data set. use 0--> for normal tranc. and 1--> for fraud.
#seperate the data.
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

#printing how many data is valid or not
print(legit.shape)
print(fraud.shape)

#statiscal mesure od data
legit.Amount.describe()

fraud.Amount.describe()

#compare value of legit and fraud
credit_card_data.groupby('Class').mean()

#taking same value of normal trans as fraud for better result.
legit_sample = legit.sample(n=492)

#merge above two.
new_dataset = pd.concat([legit_sample,fraud],axis =0)

new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

#split the data into features and targets
x = new_dataset.drop(columns='Class',axis=1)
y = new_dataset['Class']

print(x)

print(y)

"""split the data into training data and testing data"""

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, stratify=y,random_state=2)

print(x.shape, x_train.shape,x_test.shape)

#model training 

model = LogisticRegression()

# training  the model on train data
model.fit(x_train, y_train)

#model evalution -->acurracy on train data
x_train_predict = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_predict,y_train)

print('Accuracy on traing data is ',training_data_accuracy)

# accuracy on test data
x_test_predict = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_predict, y_test)

print('Accuracy on test data is ', test_data_accuracy)

#check the given data is fraud or normal.
import pickle
filename = 'trained_model_froud_detection.sav'
pickle.dump(model,open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))

input = (406,-2.3122265423263,1.95199201064158,-1.60985073229769,3.9979055875468,-0.522187864667764,-1.42654531920595,-2.53738730624579,1.39165724829804,-2.77008927719433,-2.77227214465915,3.20203320709635,-2.89990738849473,-0.595221881324605,-4.28925378244217,0.389724120274487,-1.14074717980657,-2.83005567450437,-0.0168224681808257,0.416955705037907,0.126910559061474,0.517232370861764,-0.0350493686052974,-0.465211076182388,0.320198198514526,0.0445191674731724,0.177839798284401,0.261145002567677,-0.143275874698919,0)
# change input to m=numpy array
numpy_input = np.asarray(input)

# reshape array for predicting 1 instance
input_reshaped = numpy_input.reshape(1,-1)


prediction = loaded_model.predict(input_reshaped)
print(prediction)


