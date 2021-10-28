import pytest
import unittest
from unittest import mock
from main import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf,\
    move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc


class Testfromlecturehm21:
    @pytest.mark.parametrize('number, expected_result',
                             [
        ('2207 876234', True),
        ('11-2', True),
        ('5455 028765', False),
        ('10006', True)
    ])

    def test_heck_document_existance(self, number, expected_result):
        print('check_document_existance')
        assert check_document_existance(number) == expected_result

    @pytest.mark.parametrize('number_, expected_result_',
                             [('2207 876234', 'Василий Гупкин'),
                              ('11-2', 'Геннадий Покемонов'),
                              ('10006', 'Аристарх Павлов')
                             ])

    def test_get_doc_owner_name(self, number_, expected_result_):
        print('get_doc_owner_name')
        with unittest.mock.patch('builtins.input', return_value=number_):
            assert get_doc_owner_name == expected_result_

    def test_get_all_doc_owners_names(self, ):
        print('get_all_doc_owners_names')
        assert get_all_doc_owners_names() == {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'}

    @pytest.mark.parametrize('_number, _expected_result',
                             [
        ('2207 876234', 'None'),
        ('11-2', 'None'),
        ('5455 028765', 'None'),
        ('10006', 'None')
    ])
    def test_remove_doc_from_shelf(self, _number, _expected_result):
        print('remove_doc_from_shelf')
        assert remove_doc_from_shelf(_number) == '_expected_result'

    def test_add_new_shelf(self):
        print('add_new_shelf')
        assert add_new_shelf(5) == ('5', True)

    def test_append_doc_to_shelf(self):
        print('append_doc_to_shelf')
        assert append_doc_to_shelf("11-43", '2') == 'None'

    @pytest.mark.parametrize('_number_, _expected_result_',
                             [
        ('2207 876234', ('2207 876234', True)),
        ('11-2', ('11-2', True)),
        ('5455 028765', 'None'),
        ('10006', ('10006', True))
    ])

    def test_delete_doc(self, _number_, _expected_result_):
        print('delete_doc')
        with unittest.mock.patch('builtins.input', return_value=_number_):
            assert delete_doc == _expected_result_

    @pytest.mark.parametrize('_number__, _expected_result__',
                             [
        ('2207 876234', 1),
        ('11-2', 1),
        ('5455 028765', 'None'),
        ('10006', 2)
    ])

    def test_get_doc_shelf(self, _number__, _expected_result__):
        print('get_doc_shelf')
        with unittest.mock.patch('builtins.input', return_value=_number__):
            assert get_doc_shelf == _expected_result__

    def test_move_doc_to_shelf(self,):
        print('move_doc_to_shel')
        with unittest.mock.patch('builtins.input', return_value=''):
            assert move_doc_to_shelf() == ''

    def test_show_document_info(self):
        print('show_document_info')
        assert show_document_info() == ''

    def test_show_all_docs_info(self):
        print('show_all_docs_info')
        assert show_all_docs_info() == 'Список всех документов: passport "2207 876234" "Василий Гупкин" invoice "11-2" "Геннадий Покемонов" insurance "10006" "Аристарх Павлов" None'


    def test_add_new_doc(self):
        print('add_new_doc')
        assert add_new_doc() == ''

