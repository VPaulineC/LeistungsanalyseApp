import time
import json
from my_classes import Person, Experiment,Subject ,Supervisor
import datetime

if __name__ == "__main__":
    Vorname = input(str("Vorname: "))
    Zuname = input(str("Nachname: "))
    Geschlecht = input(str("male/female? "))
    birthdate1 = input(str("Bitte gib dein Geburtstag ein (DD-MM-JJJJ): "))
    Name_Experiment = input(str("Name des Experiments: "))
    Datum = time.strftime("%d/%m/%Y")
    Betreuer = input(str("Name des Betreuers: "))
    Thema =  input(str("Subjekt: "))


    day,month,year = map(int, birthdate1.split("-"))
    today = datetime.date.today()
    age  = today.year - year - ((today.month, today.day) < (month, day))

    person = Subject(first_name=Vorname, last_name=Zuname, sex=Geschlecht, birthdate = birthdate1, age = age)
    person.introduce()
    experiment = Experiment(experiment_name=Name_Experiment, date=Datum, supervisor=Betreuer, subjects=Thema)
    Superb = Supervisor(first_name=Vorname, last_name=Zuname)
    Superb.introduce()

    Dictionary = {
        "Maximale Herzrate:": person.estimate_max_hr,
        "Personen Angabe": person.__dict__,
        "Experiment:": experiment.__dict__()
    
    }
    
    

with open("sample.json", "a") as outfile: 
    json.dump(Dictionary, outfile)
    outfile.write("\n")



