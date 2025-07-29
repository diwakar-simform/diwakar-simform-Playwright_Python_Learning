# Question7: 22:02 - How do you use yield for WebDriver Setup and Teardown in pytest?
# In Python, yield is a keyword used in a function to turn it into a generator. Instead of returning a single value like return, yield lets the function produce a series of values, one at a time, pausing between each one.

#  Why use yield instead of return?
# return ➝ ends the function and returns once.
# yield ➝ pauses the function, remembers its state, and can resume later.

# This is perfect for:
# Large datasets (memory-efficient)
# Infinite sequences (like Fibonacci)
# Streams or pipelines



import pytest

@pytest.fixture
def sample_data():
    print("\nSetup: creating test data")
    data = {"name":"Diwakar", "age": 24}
    print("Data = ",data)
    yield data
    print("Cleaning up data")


def test_testingFixture(sample_data):
    assert sample_data["name"] == "Diwakar"
    assert sample_data["age"] == 24
    print("Execution Successfull")
