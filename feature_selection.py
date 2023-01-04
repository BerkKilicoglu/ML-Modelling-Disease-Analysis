import numpy as np
import joblib
    
#These are the feature labels from our data set
feature_labels = np.array(['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 
                           'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 
                           'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 
                           'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income'])

#Load the trained model
model = joblib.load('trained_gbm_model.pkl')

#Create a numpy array based on the model's feature importances
importance = model.feature_importances_

#Sort the feature labels based on the feature importance rankings from the model
feauture_indexes_by_importance = importance.argsort()

#Print each feature label, from most important to least important (reverse order)
for index in feauture_indexes_by_importance:
    print("{} - {:.2f}%".format(feature_labels[index], (importance[index] * 100.0)))
