import string

LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _translate_iban(iban):
    iban = iban[:2] + "00" + iban[4:]
    num_iban = (iban[4:] + iban[:4]).translate(LETTERS)
    return "{:0>2}".format(98 - (int(num_iban) % 97))


def is_iban(iban_string):
    modulo = iban_string[2:2]
    iban_constructed = _translate_iban(iban_string)
    return modulo == iban_constructed[2:2]


def is_blz(blz_string):
    return blz_string.isdigit() and len(blz_string) == 8
