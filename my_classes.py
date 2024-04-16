class Person():
    """A simple attempt to model a person."""
    def __init__(self, first, last, sex, age_years):
        self.first_name = first
        self.last_name = last
        self.sex = sex
        self.age = age_years
        self.estimated_max_hr = self.estimate_max_hr(sex,age_years)

    def estimate_max_hr(self, age_years : int , sex : str) -> int:
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter Maximum heart rate:")
        return int(max_hr_bpm)

Person().__dict__

class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject







