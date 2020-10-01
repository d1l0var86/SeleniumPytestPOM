import pytest

@pytest.fixture(scope='session')
def my_cool_fixture():
    print("****************This is the Setup  fixture to run first********************")
    yield my_cool_fixture
    print("******** This is the TEARDOWN steps after each your scope ********************")