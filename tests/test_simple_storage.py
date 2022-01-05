from brownie import SimpleStorage, accounts

# tip1: brownie test -k <function name>  --- for single test 
# tip2: brownie test pdb --- debug in terminal
# tip3: brownie uses pytest for testing
def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()
