## ML Modelling - Disease Analysis

[![Build Status](https://img.shields.io/badge/lang-T%C3%BCrk%C3%A7e-red)](https://github.com/BerkKilicoglu/ML-Modelling-Disease-Analysis/blob/main/README.tr.md) [![Build Status](https://img.shields.io/badge/lang-English-blue)](https://github.com/BerkKilicoglu/ML-Modelling-Disease-Analysis/blob/main/README.md)

> **Note:** In this repository is detailed analysis based on machine learning. You can also modify and use it in different datasets and to solve different problems.

`./dataset`: directory contains the dataset in the format ***.xlsx***. The dataset consists of only 2 types of classes.

> **Note**: 
> `grid_search.py` It performs hyper parameter scanning, the execution time of the code can be long depending on the given number of parameters. In the ./results directory; You can take a look at the grid search results that I have previously obtained with my own runs.



 - Original Dataset: [***Diabetes Health Indicators Dataset***](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

### Dataset Information

Features:
Diabetes_binary: person's diabetes status.
HighBP: High blood pressure (0:no high, 1:high)
HighChol: High Cholesterol (0:no high, 1:high)
CholCheck: Cholesterol control status (0: Didn't get it done in 5 years, 1: Got it done in 5 years)
BMI: Body mass index
Smoker: Have you smoked at least 100 cigarettes in your entire life? (0:no 1:yes)
Stroke: (Ever told) you had a stroke. (0:hayır 1:evet)
HeartDiseaseorAttack: coronary heart disease (CHD) or myocardial infarction (MI) (0:hayır 1:evet)
PhysActivity: physical activity in past 30 days - not including job (0:hayır 1:evet)
Fruits: Consume Fruit 1 or more times per day (0:hayır 1:evet)
Veggies: Consume Vegetables 1 or more times per day (0:hayır 1:evet)
HvyAlcoholConsump: Heavy alcohol consumption? (0:no 1:yes)
AnyHealthcare: Do you have any health insurance? (0:no 1:yes)
NoDocbcCost: Has there been a time in the last 12 months when you needed to see a doctor but couldn't go because of the cost? (0:no 1:yes)
GenHlth: Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor
MentHlth: Number of days with mental health problems in the last 30 days.
PhysHlth: Number of days with physical health problems in the last 30 days.
DiffWalk: Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes
Sex: Gender (0:Female, 1:Male)
Age: Age category with 13 levels (1 = 18-24, 9 = 60-64, 13 = +80 years)
Education: Education level
Income: Income level 1= 10,000$ 8= +75,000$