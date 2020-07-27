
# Capstone Project
## Dignostic Questions
Udacity Data Science Nanodegree final project. The project technical writeup is in this repository and [here is the associated blog post](https://medium.com/@locmelis.audris/diagnostic-questions-recommender-c6dba9a632cf).

### Libraries used
The project is written in Python 3.7 and requires the following libraries to be installed:
- math, numpy, pandas
- sckit-learn
- plotly
- tqdm

### Project motivation
The project is initially motivated by a personal interest in EdTech and data science applications in personalized education.

This capstone project is a first attempt at predicting answers to diagnostic questions in a recently released machine learning competition [Diagnostic Questions: The NeurIPS 2020 Education Challenge](https://neurips.cc/Conferences/2020/CompetitionTrack).

The data set contains over 20 million recorded answers to diagnostic questions in mathematics from students all around the world. The project data is sourced from an educational platform Eedi with thousands of students interacting with the platform in school year 2018/2019. The data is accessible from the computer science competitions platform [CodaLab](https://competitions.codalab.org/competitions/25449#learn_the_details).

### Repository
The [current project directory](https://github.com/AudrisLocmelis/DSN/tree/master/diagnostic_questions_capstone) is a part of the general Udacity Data Science Nanodegree project [repository](https://github.com/AudrisLocmelis/DSN).

There are two main files:
1. [*diagnostic_questions_answer_prediction.ipynb*](https://github.com/AudrisLocmelis/DSN/blob/master/diagnostic_questions_capstone/diagnostic_questions_answer_prediction.ipynb) - the main jupyter notebook with the project code
2. [*Diagnostic_Questions_Capstone_Project.pdf*](https://github.com/AudrisLocmelis/DSN/blob/master/diagnostic_questions_capstone/Diagnostic_Questions_Capstone_Project.pdf) - a report for the project

### Summary
Two methods were used to predict the possible outcomes for user-item pairs not seen in the training data. Both, FunkSVD and the closed-form SVD (singular value decomposition) were used to make the predictions. While FunkSVD didn't perform very well, the change necessary to make the standard SVD calculations made the user-item matrix to both lose information and introduce very high class imbalance.

In short, the question classification is a non-trivial problem and the methods learned in the specialization were not sufficient to handle the challenging problem. However, the original data set is a very rich resource for further research in the exciting world of personalized education.

 