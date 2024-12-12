from src.every import every
import pytest

@pytest.mark.it("Test 1: Every returns boolean value")
def test_returns_boolean_true_or_false():
    # ASSIGN
    any_list = []
    
    def test_func(arg):
        pass
    # ACT
    result = every(any_list, test_func)

    # ASSERT
    assert isinstance(result, bool)

@pytest.mark.it("Test 2: Every invokes the function")
def test_invokes_the_function():
    # ASSIGN
    any_list = [1]
    invoke_count = 0
    
    def test_func(arg):
        nonlocal invoke_count 
        invoke_count += 1
        return invoke_count

    # ACT
    result = every(any_list, test_func)

    # ASSERT
    assert result == 1

@pytest.mark.it("Test 3: Invokes function for every list element")
def test_invokes_func_for_every_list_element():
    # ASSIGN
    any_list = [1, 2, 3, 4]
    invoke_count = 0

    def test_func(arg):
        nonlocal invoke_count
        invoke_count += 1
    
    # ACT
    result = every(any_list, test_func)

    # ASSERT
    assert invoke_count == len(any_list)

@pytest.mark.it("Test 4: Every returns false if any list element is false")
def test_returns_false_if_any_element_is_false():
    # ASSIGN
    any_list = [1, 2, 3, 4, 5]
    expected = False

    def is_even(num):
        all_even = True
        # Is odd
        if num % 2 == 1:
            all_even = False
    
        return all_even
    
    # ACT
    result = every(any_list, is_even)

    # ASSERT
    assert result == expected

            
    
    
