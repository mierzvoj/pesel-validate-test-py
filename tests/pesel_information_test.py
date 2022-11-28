"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import unittest

from unittest_data_provider import data_provider

from pesel import PeselInformation


class Pesel(unittest.TestCase):
    correct_numbers = lambda: (
        ('98050169129', '1998-05-01', 'female'),
        ('74060572722', '1974-06-05', 'female'),
        ('94082145535', '1994-08-21', 'male'),
        ('67030955399', '1967-03-09', 'male'),
        ('75072332722', '1975-07-23', 'female'),
        ('69051228757', '1969-05-12', 'male'),
        ('80060178592', '1980-06-01', 'male'),
        ('98030745617', '1998-03-07', 'male'),
        ('03311247546', '2003-11-12', 'female'),
        ('56100671257', '1956-10-06', 'male'),
    )

    @data_provider(correct_numbers)
    def test_should_return_correct_birthday(self, pesel, birthday, _):
        self.assertEqual(birthday, PeselInformation(pesel).get_date_of_birth())

    @data_provider(correct_numbers)
    def test_should_return_correct_gender(self, pesel, _, gender):
        self.assertEqual(gender, PeselInformation(pesel).get_gender())
