import os
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
from time import time

path = os.path.join('dataset','Memantine-4class-Normalize.xlsx')
#Load dataset and create dataframe
df = pd.read_excel(path)

#Copy dataframe for X (Features)
features_df = df.copy()

#Remove the class from the feature data
del features_df['class']

#Replace categorical data with label encoded data
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

# X: Attributes we will process       Y:Target attribute to predict
X = features_df.values
y = df['class'].values

#Split dataset into training(%70) and testing(%30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

#Utility function to report best scores
def report(results, n_top=3):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")


#Create the model
model = ensemble.GradientBoostingClassifier()

#Parameters we want to try
param_grid = {
    'n_estimators': [ 500, 750], #100 default
    'max_depth': [3, 6,15],          #3
    'min_samples_leaf': [1, 2, 4, 15],       #default=1
    'learning_rate': [0.05], #0.1
   # 'max_features': [0.1, 0.3,0.5,1.0], #n_features=auto
    'min_samples_split': [2, 5 ,15],      #2
    'loss': ['log_loss'],
    'subsample': [ 0.4, 0.3] #1.0
}

#Define the grid search we want to run. Run it with four cpus in parallel.
grid_search = GridSearchCV(model, n_jobs=-1, param_grid=param_grid, cv=5)
start = time()

#Run the grid search - on only the training data!
grid_search.fit(X_train, y_train)

#Print execution time and best combination parameters
print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
      % (time() - start, len(grid_search.cv_results_['params'])))

report(grid_search.cv_results_)

#Print the parameters that gave us the best result!
print("The parameters of the best result:", grid_search.best_params_)


# Find the accuracy rate on the training set
acc = accuracy_score(y_train, grid_search.predict(X_train))
print("\nTraining Set Accuracy_score: %.4f" % acc)


# Find the accuracy rate on the test set
acc = accuracy_score(y_test, grid_search.predict(X_test))
print("Test Set Accuracy_score: %.4f" % acc)
