import json

class Person():
    """A simple attempt to model a person."""
    
    def __init__(self, first_name, last_name, sex, age_years):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age_years = age_years
        self.estimated_max_hr = self.estimate_max_hr(age_years, sex)

    
    def estimate_max_hr(self, age_years, sex):
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = int(input("Enter maximum heart rate:"))
        return int(max_hr_bpm)
    
    #Methode um Person() in ein Dictionary zu speichern
    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)


class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    #Methode um Experiment() in ein Dictionary zu speichern
    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
            