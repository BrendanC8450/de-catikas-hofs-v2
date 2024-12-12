from src.reimplementation_of_map import reimplementation_of_map
import pytest



@pytest.mark.it("Test 1: Returns same data type as collection passed")
def test_returns_same_data_type_as_collection_passed():
    # ASSIGN
    collection_list = ['a']

    def test_func(x):
        pass

    # ACT
    result = reimplementation_of_map(collection_list, test_func)
    
    # ASSERT
    assert type(result) is type(collection_list)

# test_invokes_the_function_for_element_in_collection
# test_uses_collection_element_for_function
# test_functions_returns_new_pure_collection
# test_checks_maps_data_type


@pytest.mark.it("Test 2: Invokes function for element in collection")
def test_invokes_the_function_for_element_in_collection():
    # A, A, A - 1
    collection_list = ['a']
    invoke_count = 0

    def test_func(x):
        nonlocal invoke_count
        invoke_count += 1

    # ACT
    result = reimplementation_of_map(collection_list, test_func)
 
    assert invoke_count is 1

@pytest.mark.it("Test 3: Invokes function for each element in collection")
def test_invokes_function_for_each_element_in_collection():
    # A, A, A - 1
    collection_list = ['a', 'b', 'c', 'd', 'e']
    invoke_count = 0

    def test_func(x):
        nonlocal invoke_count
        invoke_count += 1

    # ACT
    result = reimplementation_of_map(collection_list, test_func)
 
    assert invoke_count is 5


@pytest.mark.it("Test 4: Use collection element for function")
def test_uses_collection_element_for_function():
    # ASSIGN
    collection_list = ['a', 'b', 'c', 'd', 'e']
    passed_args = []

    def test_func(x):
        passed_args.append(x)
        
    result = reimplementation_of_map(collection_list, test_func)
    # print("Result: ", result)

    assert passed_args == ['a', 'b', 'c', 'd', 'e']
    

@pytest.mark.it("Test 5: Function behaviour maps to elements")
def test_function_behaviour_maps_to_each_element():
    # ASSIGN
    collection_list = [1, 2, 3, 4, 5]

    def test_func(x):
        print(f"{x * 2}")
        x * 2

        
    result = reimplementation_of_map(collection_list, test_func)
    # print("Result: ", result)

    assert result == [2, 4, 6, 8, 10]