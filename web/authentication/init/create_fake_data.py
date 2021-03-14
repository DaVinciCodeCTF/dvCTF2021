from faker import Faker
import unidecode
import random

fake = Faker('fr_FR')

for i in range(25):
    address = unidecode.unidecode(fake.address().replace(',', '').replace('\n', ', '))
    name = unidecode.unidecode(fake.name())
    print(f"INSERT INTO members(name, address, payed_cotisation) VALUES ('{name}', '{address}', {random.randint(0, 1)});")
