from pesel import Pesel
from validator import validate_pesel, ValidationError

try:
    validate_pesel('98050169129')
except ValidationError as error:
    print(error)

pesel = Pesel('98050169129')
date_of_birth = pesel.get_date_of_birth()
gender = pesel.get_gender()
print(date_of_birth)
print(gender)