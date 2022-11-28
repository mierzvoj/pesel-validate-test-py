"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""


class ValidationError(RuntimeError):
    pass


def validate_pesel(pesel: str):
    if len(pesel) != 11:
        raise ValidationError('Incorrect pesel number')

    weight = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    control_sum = 0
    for i in range(10):
        control_sum += int(pesel[i]) * weight[i]

    if int(pesel[-1]) != (10 - control_sum % 10 if control_sum % 10 else 0):
        raise ValidationError('Incorrect pesel number')
