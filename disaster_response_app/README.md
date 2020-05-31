# Disaster Response Pipeline Project

### Summary:
This is an interactive app for classifying a message text into several disaster response categories. The classification model is trained on _Figure Eight_ disaster response data.

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


### App screenshot preview
![screenshot.png](https://github.com/AudrisLocmelis/DSN/blob/master/disaster_response_app/assets/screenshot.png)
