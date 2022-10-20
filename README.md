## ML Modelling - Drug Disease Analysis

[![Build Status](https://img.shields.io/badge/lang-T%C3%BCrk%C3%A7e-red)](https://github.com/BerkKilicoglu/ML-Modelling-Drug-Disease-Analysis/blob/main/README.tr.md) [![Build Status](https://img.shields.io/badge/lang-English-blue)](https://github.com/BerkKilicoglu/ML-Modelling-Drug-Disease-Analysis/blob/main/README.md)

`./dataset`: directory contains the dataset in the format ***.xlsx***. The dataset consists of only 4 types of classes. Null values were filled and Z-score normalization was applied.

> **Note**: 
> `grid_search.py` It performs hyper parameter scanning, the execution time of the code can be long depending on the given number of parameters. In the ./results directory; You can take a look at the grid search results that I have previously obtained with my own runs.



 - Original Dataset: [***Mice Protein Expression Data Set***](https://archive.ics.uci.edu/ml/datasets/Mice+Protein+Expression)

### Dataset Information

The data set consists of the expression levels of 77 proteins/protein. TThere are 19 control (normal) and 16 trisomic mice for a total of 35 mice. In experiments, 15 measurements were registered for each protein per sample/mouse, for a total of 525 measurements per protein.

Classes:  
c-CS-s: control mice, stimulated to learn, injected with saline (9 mice)  
c-CS-m: control mice, stimulated to learn, injected with memantine (10 mice)

t-CS-s: trisomy mice, stimulated to learn, injected with saline (7 mice)  
t-CS-m: trisomy mice, stimulated to learn, injected with memantine (9 mice)

The aim is to identify subsets of proteins that are discriminant between the classes.
