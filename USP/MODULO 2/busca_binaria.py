# import unittest
"""
DocString for busca_binaria.

Created by Diógenes Ademir Domingos. (C)
Company Blue Continental Solutions. (R)
Occupation CEO | Data Analist
Contact 'k.fus@hotmail.com'

Notes: Module for element's search in one list.
"""


def busca_binaria(lista, element):
    """Binary search.

        This fuction receive one ordered number's list and
        search by one element in list. It begin verifying
        if element is in the middle of the list,
        if it does not, it verify if it is in the left
        or right side of the list, it will go to
        divide until find the element.
        If it find it goes return the element,
        if it doesn't find it goes return -1.

        Args:
            lista (list): One number's list
            element (int): The second parameter.

        Returns:
           int: Element position, otherside -1.

    """
    start = 0
    end = len(lista) - 1
    while start <= end:
        meio = (start + end) // 2
        if meio == element:
            return meio
        else:
            if element < meio:
                end = meio - 1
            else:
                start = meio + 1
    return -1


def busca(lista, element):
    """Binary search.

        This fuction receive one ordered data list and
        search by one element in list. It begin verifying
        if element is in the middle of the list,
        if it does not, it verify if it is in the left
        or right side of the list, it will go to
        divide until find the element.
        If it find it goes return the element position,
        if it doesn't find it goes return False.

        Args:
            lista (list): One data's list
            element (int): The second parameter.

        Returns:
           int: Element position , otherside False.

    """
    start = 0
    end = len(lista) - 1
    while start <= end:
        meio = (start + end) // 2
        print(meio)  # print the index of test
        if lista[meio] == element:
            return meio
        else:
            if element < lista[meio]:
                end = meio - 1
            else:
                start = meio + 1
    return False


# class TestBinarysearch(unittest.TestCase):
#     ''' It's internal class for unit test.'''

#     def test_binary_search(self):
#         lista = list(range(0, 100, 2))
#         req = lista[10]
#         self.assertEqual(busca_binaria(lista, req), req)

#     def test_search_strings(self):
#         self.assertEqual(busca(['a', 'e', 'i'], 'e'), 1)

#     def test_not_found(self):
#         self.assertEqual(busca([1, 2, 3, 4, 5], 6), False)

#     def test_integer_found(self):
#         self.assertEqual(busca([1, 2, 3, 4, 5], 4), 3)


# if __name__ == '__main__':
#     unittest.main()
