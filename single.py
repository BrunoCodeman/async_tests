from datetime import datetime
from random import randint
from calculations import Person, calculate_person_age as cpa

def calculate_ages():
    start_time = datetime.now()
    for i in range(500000):
        birth_year = randint(1900, 2017)
        await cpa(Person(birth_year))
    
    end_time = datetime.now()
    print("total time with single thread: {0}".format(end_time - start_time))





if __name__ == '__main__':
    calculate_ages()