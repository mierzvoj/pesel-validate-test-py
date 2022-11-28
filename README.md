# PESEL tools
Validates PESEL number and returns date of birth and gender

## Usage

First install all requirements

```bash
$ python3.8 -m pip install -r requirements.txt
```
### How to validate PESEL
```python
from validator import validate_pesel, ValidationError

try:
    validate_pesel('98050169129')
except ValidationError as error:
     print(error)
``` 

### How to get date of birth and gender from PESEL
If you want to get data of birth and / or gender, you do not have to validate PESEL first.
`PeselInformation` class validates it in the constructor.

```python
from pesel import Pesel

pesel = Pesel('98050169129')
date_of_birth = pesel.get_date_of_birth()
gender = pesel.get_gender()
```

## Testing

### Unittest

```bash
$ python3.8 -m unittest
```

### Prospector
```bash
$ python3.8 -m prospector --without-tool pyflakes
```