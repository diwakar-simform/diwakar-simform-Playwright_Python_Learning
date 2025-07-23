# fixtures in pytest:
import pytest

# we can also define the scope to when it should run, if scope = "function" it will run for before every function/test scope = "module" then it will only run once for the entire test file.
# @pytest.fixture(scope="class") run only once for entire class
@pytest.fixture(scope="function") 
def preSetup():
    print("This is the pre-setup we have to do to test how fixtures work")
    return "passed"  # This return value can be used in the test function that uses this fixture

def test_initialCheck(preSetup, returnFixture, beforeEveryFunction): # you can use multiple fixtures in a test function
    print("*******Initial check**********")
    # assert preSetup == "failed"  # Example assertion to ensure the test fails
    assert preSetup == "passed"  # Example assertion to ensure the test passes
    # assert True  # Example assertion to ensure the test passes
    assert returnFixture == "passing"  # Example assertion to ensure the test passes
    assert beforeEveryFunction == None  # Example assertion to ensure the test passes

@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_skipTest():
    print("-------------This test is skipped-----------")

@pytest.mark.xfail(reason="Expected to fail for demonstration purposes")
def test_expectedFail():
    print("This test is expected to fail")
    assert False

@pytest.mark.skipif("1 + 1 == 2", reason="Skipping this test because the condition is true")
def test_skipIfCondition():
    print("This test is skipped because the condition is true")

@pytest.mark.sanitytest 
def test_postCheck(returnFixture): # it is compulsory to add test_ prefix for both file and the function.
    print("Test is running correctly")
    returnFixture == "passing"  # Example assertion to ensure the test passes


# preSetup() # Fixture "preSetup" called directly. Fixtures are not meant to be called directly,
# but are created automatically when test functions request them as parameters.

def test_fixture(preSetup):
    print("Verifying fixture working correctly or not")

def test_fixture2(beforeEveryFunction):
    print("Verifying fixture working correctly or not for beforeEveryFunction")