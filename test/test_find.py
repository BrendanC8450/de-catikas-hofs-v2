from src.find import find
import pytest

@pytest.mark.it("Test 1: Returns item in the list ")
def test_returns_item_from_the_list():
    # ASSIGN
    any_list = [1]
    expected = True
    
    def test_func(arg):
        pass

    # ACT
    result = find(any_list, test_func)

    # ASSERT
    assert result in any_list

@pytest.mark.it("Test 2: Invokes function")
def test_invokes_the_function():
    # ASSIGN
    any_list = [1]
    invoke_count = 0
    
    def test_func(arg):
        nonlocal invoke_count
        invoke_count += 1

    # ACT
    result = find(any_list, test_func)

    # ASSERT
    assert invoke_count == 1

@pytest.mark.it("Test 3: Invokes function more than once")
def test_invokes_function_more_than_once():
    # ASSIGN
    any_list = [1, 2, 3, 4, 5]
    invoke_count = 0

    def test_func(arg):
        nonlocal invoke_count
        invoke_count += 1
    
    # ACT
    result = find(any_list, test_func)

    # ASSERT
    assert invoke_count == len(any_list)

@pytest.mark.it("Test 4: Multiple of five function returns boolean")
def test_multiple_of_five_function_returns_boolean():
    # ASSIGN
    any_list = [1, 2, 3, 4, 5]
    index = 0

    def multiple_of_5(num):
        nonlocal index
        index += 1
        return num % 5 == 0
    
    # ACT
    result = multiple_of_5(any_list[index])
    # ASSERT
    assert isinstance(result, bool)

@pytest.mark.it("Test 5: Returns first element that matches function")
def test_returns_first_element_matching_function():
    # ASSIGN
    any_list = [1, 2, 3, 4, 5, 10, 15]

    def multiple_of_5(num):
        return num % 5 == 0

    result = find(any_list, multiple_of_5)

    assert result is 5


