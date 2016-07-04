from datetime import datetime
import time

class Shelter:
    def __init__(s):
        s.lastDog = s.firstDog = s.firstCat = s.lastCat = None

    def enqueue(s, animal):
        animal.date = datetime.now()
        if animal.race == "dog":
            if not s.firstDog and not s.lastDog:
                s.firstDog = s.lastDog = animal
            else:
                s.lastDog.next = animal
                s.lastDog = animal
        else:
            if not s.firstCat and not s.lastCat:
                s.firstCat = s.lastCat = animal
            else:
                s.lastCat.next = animal
                s.lastCat = animal

    def dequeueAny(s):
        if not s.firstDog and not s.firstCat: return
        if s.firstDog and not s.firstCat:
            return s.dequeueDog()
        elif s.firstCat and not s.firstDog:
            return s.dequeueCat()
        elif s.firstDog.date <= s.firstCat.date:
            return s.dequeueDog()
        else:
            return s.dequeueCat()

    def dequeueDog(s):
        if not s.firstDog: return
        dog = s.firstDog
        s.firstDog = s.firstDog.next
        if s.firstDog is None: s.lastDog = None
        return dog

    def dequeueCat(s):
        if not s.firstCat: return
        cat = s.firstCat
        s.firstCat = s.firstCat.next
        if s.firstCat is None: s.lastCat = None
        return cat


class AnimalNode:
    def __init__(self, race, name):
        self.race = race
        self.date = None
        self.name = name
        self.next = None

shelter = Shelter()
shelter.enqueue(AnimalNode("dog", "dog1"))
time.sleep(0.01)
shelter.enqueue(AnimalNode("dog", "dog2"))
time.sleep(0.01)
shelter.enqueue(AnimalNode("dog", "dog3"))
time.sleep(0.01)
shelter.enqueue(AnimalNode("cat", "cat2"))
time.sleep(0.01)
shelter.enqueue(AnimalNode("dog", "dog4"))
time.sleep(0.01)
shelter.enqueue(AnimalNode("cat", "cat1"))
time.sleep(0.01)
shelter.enqueue(AnimalNode("dog", "dog5"))

print shelter.dequeueCat().name
print shelter.dequeueDog().name

for i in range(5):
    print shelter.dequeueAny().name

