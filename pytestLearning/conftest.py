# conftest.py file is a global configuration file for pytest. It can be used to define fixtures, hooks, and other configurations that can be shared across multiple test files.
# Lets say if you have defined a fixture as with scope = "module" in conftest.py file, then it will run only once for the entire test file, even if you call it multiple times in the test file.

import pytest


@pytest.fixture(scope="function")  # runs before every function in test each test file
def returnFixture():
    print("This one is a fixture where I am testing the return value")
    return "passing"  # This return value can be used in the test function that uses this fixture

@pytest.fixture(scope="function") # runs each time when it called in test each test file
def beforeEveryFunction():
    print("This is a setup that runs before every function")
    # Code before yield will run before the test function and kown as setup
    yield # This yield statement allows you to run some code before and after the test function
    # Code after yield will run after the test function completes and known as teardown
    print("This is a teardown that runs after every function")
    return "passed"  # This return value can be used in the test function that uses this fixture

@pytest.fixture(scope="module") # runs oncer per module or test file
def beforeEveryModule():
    print("This is a setup that runs before every module")
    yield
    print("This is a teardown that runs after every module")



@pytest.fixture(scope="class") # runs once per class, if there are multiple classes in a test file, it will run for each class
def beforeEveryClass():
    print("This is a setup that runs before every class")
    yield
    print("This is a teardown that runs after every class")



@pytest.fixture(scope="session") # runs once per session, if there are multiple test files, it will run only once for the entire session
def beforeEverySession():
    print("This is a setup that runs before every session")
    yield
    print("This is a teardown that runs after every session")




@pytest.fixture(scope="package")
def beforeEveryPackage():
    print("This is a setup that runs before every package")
    yield
    print("This is a teardown that runs after every package")
