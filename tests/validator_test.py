"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import unittest

from unittest_data_provider import data_provider

from validator import ValidationError, validate_pesel


class ValidationTest(unittest.TestCase):
    incorrect_numbers = lambda: (('12345678',), ('98050169128',), ('980501691291',))
    correct_numbers = lambda: (
        ('98050169129',), ('74060572722',), ('94082145535',), ('67030955399',), ('75072332722',), ('69051228757',),
        ('80060178592',), ('98030745617',), ('03311247546',), ('56100671257',),
    )

    @data_provider(incorrect_numbers)
    def test_should_raise_error_with_incorrect_pesel(self, pesel):
        with self.assertRaises(ValidationError):
            validate_pesel(pesel)

    @data_provider(correct_numbers)
    def test_should_pass_with_correct_numbers(self, pesel):
        validate_pesel(pesel)
