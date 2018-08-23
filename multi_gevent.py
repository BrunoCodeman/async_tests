import gevent
from datetime import datetime
from random import randint
from gevent import monkey
from calculations import Person, calculate_person_age as cpa

monkey.patch_all()

def calculate_ages():
    events = []
    for i in range(500000):
        birth_year = randint(1900, 2017)
        events.append(gevent.spawn(cpa, Person(birth_year)))
    start_time = datetime.now()
    gevent.joinall(events, timeout = 2)
    end_time = datetime.now()
    print("total time with gevent: {0}".format(end_time - start_time))





if __name__ == '__main__':
    calculate_ages()