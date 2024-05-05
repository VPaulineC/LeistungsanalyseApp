import json
import requests

class Person():
    """A simple attempt to model a person."""
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def put(self):
        # Define the URL of the API
        url = "http://127.0.0.1:5000/"
        # Define the data you want to send
        data = {
            "name": "TestName",
            "email": "TestName@mail.at"
        }
        # Convert the data to JSON format
        data_json = json.dumps(data)
        # Send a POST request to the API
        response = requests.post(url, data=data_json)
        # Print the response from the server
        print(response.text)



    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
            outfile.write("\n")
    
# Kindklasse Subject erstellen und die entsprechenden Attribute vererben bzw. erstellen
class Subject(Person):
    def __init__(self, first_name, last_name, sex, age_years, dateofbirth, email):
        super().__init__(first_name, last_name)
        self.__dateofbirth = dateofbirth
        self.sex = sex
        self.age_years = age_years
        self.email = email

    
    def estimate_max_hr(self, age_years, sex):
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = int(input("Enter maximum heart rate:"))
        return int(max_hr_bpm)
    
               
    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
            outfile.write("\n")


    def update_email(self):
        # Define the URL of the API
        url = "http://127.0.0.1:5000/"
        # Define the data you want to send
        data = {
            "name": "TestName"
        }
        # Convert the data to JSON format
        data_json = json.dumps(data)
        # Send a POST request to the API
        response = requests.put(url, data=data_json)
        # Print the response from the server
        print(response.text)


  
# Kindklasse Supervisor erstellen und die entsprechenden Attribute vererben bzw. erstellen 
class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


    def save(self):
         with open("sample.json", "a") as outfile: 
             json.dump(self.__dict__, outfile)
             outfile.write("\n")


class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject


    def save(self):
        with open("sample.json", "a") as outfile: 
            json.dump(self.__dict__, outfile)
            outfile.write("\n")