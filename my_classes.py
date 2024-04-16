class Person():
    """A simple attempt to model a person."""
    def __init__(self, first, last, sex, age):
        self.first_name = first
        self.last_name = last
        self.sex = sex
        self.age_years = age
        self.estimated_max_hr = self.estimate_max_hr(sex,age)

    def estimate_max_hr(self, age_years : int , sex : str) -> int:
  
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age_years
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age_years
        else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
P1=("Pauline", "Voigtsberger", "female", 19)

my_dictionary=P1.__dict__
print(my_dictionary)







