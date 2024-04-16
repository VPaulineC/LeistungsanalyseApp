import json

class Person():
    def __init__(self,first,last,sex,age,estimate_max_hr):
        self.first = first
        self.last = last
        self.sex = sex
        self.age = age
        self.estimate_max_hr = estimate_max_hr
         
    def __dict__(self):
            return {
                'first': self.first,
                'last': self.last,
                'sex': self.sex,
                'age': self.age,
                'estimate_max_hr': self.estimate_max_hr
            }

    def save(self):
        with open('person.json', 'w') as file:
            json.dump(self.__dict__(), file)
    

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