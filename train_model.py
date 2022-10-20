import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
import joblib
from sklearn.preprocessing import LabelEncoder


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

#Fit model
model = ensemble.GradientBoostingRegressor(
    n_estimators=700,
    learning_rate=0.05,
    max_depth=15,
    min_samples_leaf=8,
    min_samples_split=3,
    #max_features=1.0,
    loss='huber',
    subsample=0.5
)
model.fit(X_train, y_train)

#Save the trained model to a file so we can use it in other programs
joblib.dump(model, 'mymodel.pkl')

# Find the error rate on the training set
mse = mean_absolute_error(y_train, model.predict(X_train))
print("Training Set Mean Absolute Error: %.4f" % mse)

# Find the error rate on the test set
mse = mean_absolute_error(y_test, model.predict(X_test))
print("Test Set Mean Absolute Error: %.4f" % mse)

