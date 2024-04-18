import time
import json
import my_classes



if __name__ == "__main__":

    #Inputs für Person() und Experiment()
    eingabe=input ("Gib bitte dein Alter ein: ")
    age_years = int(eingabe)
    sex = input(str("male/female? "))
    first_name = input(str("Vorname: "))
    last_name = input(str("Nachname: "))
    experiment_name = input(str("Gib bitte einen Namen für das Experiment an"))
    date = time.strftime("%d/%m/%Y")
    supervisor = input(str("Gib bitte den Supervisor an: "))
    subject =  input(str("Gib bitte das Subjekt an: "))
    
    # Person1 und Experiment1 erstellen
    Person1 = my_classes.Person(first_name, last_name, sex, age_years)
    Experiment1 = my_classes.Experiment(experiment_name, date, supervisor, subject)
    
    #Person1 und Experiment1 als Dictionarys printen
    print(Person1.__dict__)
    print(Experiment1.__dict__)
    
    #Dictionarys von Person1 und Experiment1 in sample.json speichern
    my_classes.Person.save(Person1)
    my_classes.Experiment.save(Experiment1)
    
 

