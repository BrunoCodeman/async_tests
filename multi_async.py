import asyncio
from async_generator import async_generator, yield_from_
from datetime import datetime
from random import  randint
from calculations import AsyncList, Person, calculate_person_age as cpa

async def calculate_ages():
    start_time = datetime.now()
    rng = AsyncList(range(1000000)) #await gen_thousand()
    async for i in rng:
        birth_year = randint(1900, 2017)
        cpa(Person(birth_year))
    
    
    end_time = datetime.now()
    msg = "total time with asyncio: {0}".format(end_time - start_time)
    print(msg)
    #return msg

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(calculate_ages())

if __name__ == '__main__':
    main()