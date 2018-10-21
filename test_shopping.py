from shopping import is_in_list
import pytest

@pytest.mark.parametrize("myIn, Expect", [

	('apple', True),
	('pear', True),
	#('apple', 'True'),

	])

def test_is_in_list(myIn,Expect):
	response = is_in_list(myIn)
	assert response == Expect