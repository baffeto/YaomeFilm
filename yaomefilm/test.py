from faker import Faker
from yaome.models import Actor

fake = Faker()

for _ in range(50):
    name = fake.first_name()
    surname = fake.last_name()
    actor = Actor.objects.create(name=name, surname=surname)
    actor.save()