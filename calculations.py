import asyncio

class AsyncList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.i = 0
        self.stop = len(self)
    async def __aiter__(self):
        return self

    async def __anext__(self):
            i = self.i
            self.i += 1
            if self.i <= self.stop:
                await asyncio.sleep(1)
                return i * i
            else:
                raise StopAsyncIteration

class Person():

    def __init__(self, birth_year, age = None):
        self.birth_year = birth_year
        self.age = age


async def calculate_person_age(person):
    person.age =  2018 - person.birth_year
    await person