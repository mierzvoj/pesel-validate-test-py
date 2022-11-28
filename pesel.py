"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from datetime import date

from validator import validate_pesel


class Pesel:
    def __init__(self, pesel):
        validate_pesel(pesel)
        self.pesel = pesel

    def get_date_of_birth(self):
        year = int(self.pesel[:2]) + 1800 + 100 * (4, 0, 1, 2, 3).index(int(self.pesel[2:4]) // 20)
        month = int(self.pesel[2:4]) % 20
        day = int(self.pesel[4:6])

        try:
            data = str(date(year, month, day))
        except ValueError:
            data = None

        return data

    def get_gender(self):
        return 'male' if int(self.pesel[9]) % 2 else 'female'
