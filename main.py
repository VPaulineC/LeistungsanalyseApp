import my_functions
import time
import json


if __name__ == "__main__":
    eingabe = input("Bitte gib dein Alter ein: ")
    Alter = int(eingabe)
    Geschlecht = input(str("male/female? "))
    Vorname = input(str("Vorname: "))
    Zuname = input(str("Nachname: "))
    Name_Experiment = "Leistungsanalyse"
    Datum = time.strftime("%d/%m/%Y")
    Supervisor = "Max Mustermann"
    Thema =  "Leistung"
    


    Dictionary = {"Maximale Herzrate:": my_functions.estimate_max_hr(age_years=Alter,sex = Geschlecht),
                  "Personen Angabe": my_functions.build_person(first_name=Vorname,last_name=Zuname,sex=Geschlecht,age=Alter),
                  "Experiment:": my_functions.build_experiment(experiment_name=Name_Experiment,date=Datum,supervisor=Supervisor,subject=Thema)
            }
    print(Dictionary)


with open("sample.json", "a") as outfile: 
    json.dump(Dictionary, outfile)
