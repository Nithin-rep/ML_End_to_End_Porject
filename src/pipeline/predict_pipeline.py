import sys
import pandas as pd
import pickle
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
    
        model_path= r"C:\Users\Nithin\Desktop\ML_End_to_End\notebook\model.pkl"
        preprocessor_path= r"C:\Users\Nithin\Desktop\ML_End_to_End\notebook\preprocessor.pkl"
        print("Before Loading")

        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)

        with open(preprocessor_path, 'rb') as processor_file:
            preprocessor = pickle.load(processor_file)

        print("After Loading")
        data_scaled=preprocessor.transform(features)

        print("Transformed")
        preds=model.predict(data_scaled)

        print("Obtained the results")
        return preds



    
class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        custom_data_input_dict = {
            "gender": [self.gender],
            "race_ethnicity": [self.race_ethnicity],
            "parental_level_of_education": [self.parental_level_of_education],
            "lunch": [self.lunch],
            "test_preparation_course": [self.test_preparation_course],
            "reading_score": [self.reading_score],
            "writing_score": [self.writing_score],
        }

        return pd.DataFrame(custom_data_input_dict)



     
