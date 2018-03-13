# self referes to the object of the class created, even tho it doesnt exist when the class
# and its methods are created, it is still important

class Human:

    avg_life_span = 80

    def __init__(self, race, race_population, life_span):
        self.race = race
        self.race_population = race_population
        self.life_span = life_span

    def return_race_info(self):
        return 'race {} race population {} average life span {}'.format(
            self.race, self.race_population, self.avg_life_span
        )    

    def calculate_life_span(self):
        self.life_span = int(self.avg_life_span + self.life_span)
        return self.life_span

human1 = Human('asian', 3000000000, 75)

print(human1.calculate_life_span())
print(human1.return_race_info())

class Person(Human):
     def __init__(self, race, race_population, life_span, name):
         super().__init__(race,race_population,life_span) #lets the super class handel this args
         self.name = name

     def reveal_object(self):
        return self.__dict__
        # return dir(self)

print(("\n") * 3)
person1 = Person('not human', 1, 10000, 'Kev')
print(person1.reveal_object())