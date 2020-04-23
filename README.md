# Breast-cancer-risk-prediction

## Objective:

The repository is a learning exercise to:

Apply the fundamental concepts of machine learning from an available dataset
Evaluate and interpret my results and justify my interpretation based on observed data set
Create notebooks that serve as computational records and document my thought process.
The analysis is divided into four sections, saved in juypter notebooks in this repository

Identifying the problem and Data Sources
Exploratory Data Analysis
Pre-Processing the Data
Build model to predict whether breast cell tissue is malignant or Benign

# 1: Identifying the problem and Getting data.
Notebook goal:Identify the types of information contained in our data set In this notebook I used Python modules to import external data sets for the purpose of getting to know/familiarize myself with the data to get a good grasp of the data and think about how to handle the data in different ways. 

# 2 Exploratory Data Analysis
Notebook goal:  Explore the variables to assess how they relate to the response variable In this notebook, I am getting familiar with the data using data exploration and visualization techniques using python libraries (Pandas, matplotlib, seaborn. Familiarity with the data is important which will provide useful knowledge for data pre-processing)

# 3 Pre-Processing the data
Notebook goal:Find the most predictive features of the data and filter it so it will enhance the predictive power of the analytics model. In this notebook I use feature selection to reduce high-dimension data, feature extraction and transformation for dimensionality reduction. This is essential in preparing the data before predictive models are developed.

# 4 Predictive model using Machine Learning Algorithms
Notebook goal: Construct predictive models to predict the diagnosis of a breast tumor. In this notebook, I construct a predictive model using 	Random Forest and  machine learning algorithm to predict the diagnosis of a breast tumor. The diagnosis of a breast tumor is a binary variable (benign or malignant). I also evaluate the model using confusion matrix the receiver operating curves (ROC), which are essential in assessing and interpreting the fitted model.

# 5 Accuracy of the Model
## Model	Accuracy

#### 0 	Logistic Regression    	:   0.947368
#### 1 	Random Forest	          :   0.976608
#### 3 	XGBoost	                :   0.970760
#### 4 	Decision Tree	          :   0.935673
#### 5	Support Vector Machine	:   0.631579
