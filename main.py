import my_functions
import time
import json
from my_classes import Person, Experiment

if __name__ == "__main__":
    Alter = int(input("Bitte gib dein Alter ein: "))
    Geschlecht = input(str("male/female? "))
    Vorname = input(str("Vorname: "))
    Zuname = input(str("Nachname: "))
    Name_Experiment = input(str("Name des Experiments: "))
    Datum = time.strftime("%d/%m/%Y")
    Supervisor = input(str("Name des Betreuers: "))
    Thema =  input(str("Subjekt: "))
    
    person = Person(first_name=Vorname, last_name=Zuname, sex=Geschlecht, age_years=Alter)
    person.save()

    experiment = Experiment(experiment_name=Name_Experiment, date=Datum, supervisor=Supervisor, subjects=Thema)
    experiment.save()

    Dictionary = {
        "Maximale Herzrate:": person.estimate_max_hr,
        "Personen Angabe": person.__dict__(),
        "Experiment:": experiment.__dict__()
    
    }

    print(Dictionary)
    '''

    Dictionary = {"Maximale Herzrate:": my_functions.estimate_max_hr(age_years=Alter,sex = Geschlecht),
                  "Personen Angabe": my_functions.build_person(first_name=Vorname,last_name=Zuname,sex=Geschlecht,age=Alter),
                  "Experiment:": my_functions.build_experiment(experiment_name=Name_Experiment,date=Datum,supervisor=Supervisor,subject=Thema)
            }
    print(Dictionary)

'''
with open("sample.json", "a") as outfile: 
    json.dump(Dictionary, outfile)
    outfile.write("\n")
