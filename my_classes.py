import json

def estimate_max_hr(age_years: int, sex: str) -> int:
    if sex == "male":
        max_hr_bpm =  223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 *  age_years
    else:
        max_hr_bpm = int(input("Enter maximum heart rate:"))
    return max_hr_bpm

#Erstellung der Klasse Person
class Person():
    def __init__(self, first_name, last_name, sex, age_years):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age_years = age_years
        self.estimate_max_hr = estimate_max_hr(age_years, sex)

    def __dict__(self):
            return {
                'first': self.first_name,
                'last': self.last_name,
                'sex': self.sex,
                'age': self.age_years,
                'estimate_max_hr': self.estimate_max_hr
            }
    
    def save(self):
        with open('person.json', 'w') as file:
            json.dump(self.__dict__(), file)
    
#Erstellung der Klasse Experiment
class Experiment():
    def __init__(self, experiment_name, date, supervisor, subjects):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subjects = subjects
    
     
    def __dict__(self):
            return {
                'experiment_name': self.experiment_name,
                'date': self.date,
                'supervisor': self.supervisor,
                "subjects": self.subjects
            }
    
    def save(self):
        with open('experiment.json', 'w') as file:
            json.dump(self.__dict__(), file)
