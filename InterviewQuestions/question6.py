# Question6: 17:54 - What are Fixtures in Pytest? when they are used?
# Fixtures in pytest are nothing but functions that helpful in setup test environment before a test runs and cleanup afterward
# They help manage test dependcies, setup, teardown, and reusable data across multiple test class.
# Key features of Pytest Fixtures
# Reusability -> Define once, use in multiple tests.
# Automatic Setup & Teardown -> Handles pre-test and post-test actions
# Scope control -> Fixtures can run per test, per class, per module, or per session
# Dependency injection -> Pass fixtures as test function arguments.

import pytest

@pytest.fixture
def sample_data():
    print("\nSetup: creating test data")
    data = {"name":"Diwakar", "age": 24}
    print("Data = ",data)
    return data


def test_testingFixture(sample_data):
    assert sample_data["name"] == "Diwakar"
    assert sample_data["age"] == 24
    print("Execution Successfull")
