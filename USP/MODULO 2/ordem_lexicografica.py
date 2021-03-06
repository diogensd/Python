import unittest
"""
DocString for ordem_lexicografica.py.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Organized words in ord criteria

"""

words_tes = "ana banana ama cama casa aa Jose ai aab aba".split()


def ordem_lexicoGrafca(words):
    ''' funcion for find shorter word in ord criteria.

        The funcion recive a list of the words and based in
        number of ASCII for each character, calculate and find
        the shorter word.

        Parameters: A list of rand words.

        Return: The shorter word found.

    '''

    assert len(words) > 0
    menor = words[0].lower()
    for i in words:
        if i.lower() < menor:
            menor = i
    return menor


def maiusculas(frase):
    s = ""
    for x in frase:
        if ord(x) > 64 and ord(x) < 91:
            s += x
    return s


class TestMenorStringLexica(unittest.TestCase):
    ''' It's internal class for unit test.'''

    def test_equals(self):
        self.assertEqual(ordem_lexicoGrafca(words_tes), "aa")
        self.assertEqual(ordem_lexicoGrafca(words_tes[:4]), "ama")

    def test_not_equals(self):
        self.assertNotEqual(ordem_lexicoGrafca(words_tes), "ab")
        self.assertEqual(ordem_lexicoGrafca(words_tes[:5]), "ama")

    def test_equals_maiusculas(self):
        self.assertEqual(
            maiusculas("O carro Esta na Garagem"), 'OEG')
        self.assertEqual(
            maiusculas(""), "")

    def test_not_equals_maiusculas(self):
        self.assertNotEqual(
            maiusculas("O carro Esta na Garagem"), 'O')
        self.assertNotEqual(
            maiusculas("O carro Esta na Garagem"), '')


if __name__ == '__main__':
    unittest.main()
