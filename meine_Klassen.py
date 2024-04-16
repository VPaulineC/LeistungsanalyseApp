class Person():
    """A simple attempt to model a person."""
    def __init__(self, first, last, sex, age):
        self.first_name = first
        self.last_name = last
        self.sex = sex
        self.age_years = age
        #self.estimated_max_hr = self.estimate_max_hr(sex,age)

P1=Person("Pauline", "Voigtsberger", "female", 19)
my_dictionary=P1.__dict__
print(my_dictionary)
