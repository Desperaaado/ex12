from nose.tools import *
from find import find

def setup():
    print("=====TEST: find.py=====")

def teardown():
    print("=====END TEST=====")

def test_find_file():
    result = find.find_file(
        'name',
        '*.py',
        r'C:\Users\xiao0\projects_pro\ex12'
    )
    answer = [
        'C:\\Users\\xiao0\\projects_pro\\ex12\\setup.py',
        'C:\\Users\\xiao0\\projects_pro\\ex12\\find\\find.py',
        'C:\\Users\\xiao0\\projects_pro\\ex12\\find\\__init__.py',
        'C:\\Users\\xiao0\\projects_pro\\ex12\\tests\\find_tests.py',
        'C:\\Users\\xiao0\\projects_pro\\ex12\\tests\\__init__.py'
    ]
    assert_equal(result, answer)

def test_print_file():
    pass

def test_exec_file():
    pass