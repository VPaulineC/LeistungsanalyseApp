import time
import json
import my_classes



if __name__ == "__main__":

    #Inputs für die Klassen Person() und Experiment()
    eingabe=input ("Gib bitte dein Alter ein: ")
    age_years = int(eingabe)
    sex = input(str("male/female? "))
    Subject_first_name = input(str("Vorname Subject: "))
    Subject_last_name = input(str("Nachname Subject: "))
    dateofbirth = input(str("Gib bitte dein Geburtsdatum ein: "))
    experiment_name = input(str("Gib bitte einen Namen für das Experiment an: "))
    date = time.strftime("%d/%m/%Y")
    Supervisor_first_name = input(str("Vorname Subervisor: "))
    Supervisor_last_name = input(str("Nachname Supervisor: "))
    
    
    # Subject1, Supervisor1 und Experiment1 erstellen
    Subject1 = my_classes.Subject(Subject_first_name, Subject_last_name, sex, age_years, dateofbirth)
    Supervisor1 = my_classes.Supervisor(Supervisor_first_name, Supervisor_last_name)
    Experiment1 = my_classes.Experiment(experiment_name, date, Supervisor1.__dict__, Subject1.__dict__)
    
    #Subject1 und Experiment1 als Dictionarys printen
    print(Subject1.__dict__)
    #print(Supervisor1.__dict__)
    print(Experiment1.__dict__)
    
    #Dictionarys von Subject1 und Experiment1 in sample.json speichern
    my_classes.Subject.save(Subject1)
    #my_classes.Supervisor.save(Supervisor1)
    my_classes.Experiment.save(Experiment1)
    
 

