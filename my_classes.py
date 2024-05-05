import requests
import json


#Erstellung der Klasse Person
class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
       
    def save(self):
        with open('person.json', 'w') as file:
            json.dump(self.__dict__(), file)

    def put(self):
        url = "http://127.0.0.1:5000/person/"

        data = {
            "name": self.first_name
            }
        
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)

#Erstellung der Subklasse Subject
class Subject(Person):
    
    def __init__(self, first_name, last_name,sex,birthdate,age,email):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__birthdate = birthdate
        self.age = age
        self.estimate_max_hr = self.estimate_max_h()
        self.email=email

    def estimate_max_h(self) -> int:
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            max_hr_bpm = int(input("Enter maximum heart rate:"))
        return max_hr_bpm

    def introduce(self):
        print("Mein Name lautet: {} {}".format(self.first_name,self.last_name))
        print("Meine Herzrate lautet: {}".format(self.estimate_max_hr))
    
    def update_email(self, new_email):
        self.email = new_email
        url = "http://127.0.0.1:5000/person/Testname2"
        data = {
            "name": self.first_name,
            "email": self.email,
            "age" : self.age}

        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)

class Supervisor(Person):
    def __init__(self,first_name, last_name):
        super().__init__(first_name, last_name)
    
    def introduce(self):
        print("Der Name des Patienten lautet: {} {}".format(self.first_name,self.last_name))

#Erstellung der Subklasse Experiment
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