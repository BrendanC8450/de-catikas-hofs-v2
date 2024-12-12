from src.some import some
import pytest

@pytest.mark.it("Test 1: Output returns boolean")
def test_output_returns_boolean():
    # ASSIGN
    any_list = []

    def predicate(arg):
        pass

    # ACT
    result = some(any_list, predicate)

    # ASSERT
    assert isinstance(result, bool)

@pytest.mark.it("Test 2: Some invokes the function")
def test_invokes_the_function():
    # ASSIGN
    any_list = [1]
    invoke_count = 0
    
    def predicate(arg):
        nonlocal invoke_count 
        invoke_count += 1
    

    # ACT
    result = some(any_list, predicate)

    # ASSERT
    assert invoke_count == 1

@pytest.mark.it("Test 3: Invokes function for every list element")
def test_invokes_func_for_every_list_element():
    # ASSIGN
    any_list = [1, 2, 3, 4]
    invoke_count = 0

    def predicate(arg):
        nonlocal invoke_count
        invoke_count += 1
    
    # ACT
    result = some(any_list, predicate)

    # ASSERT
    assert invoke_count == len(any_list)

@pytest.mark.it("Test 4: Some returns true if any list element is true")
def test_returns_true_if_any_element_is_true():
    # ASSIGN
    any_list = [1, 2, 3, 4, 5]
    expected = True

    def is_even(num):
        any_even = False
        # Is even
        if num % 2 == 0:
            any_even = True
    
        return any_even
    
    # ACT
    result = some(any_list, is_even)

    # ASSERT
    assert result == expected
