import pytest
import requests


# Test API: https://dog.ceo/dog-api/

def pytest_addoption(parser):
    parser.addoption(
        "--breedurl",
        default="https://dog.ceo/api/breed/",
        help="URL from a breed collection"
    )
    parser.addoption(
        "--url",
        default="https://dog.ceo/api/breeds/",
        help="URL from all dogs collection"
    )
    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post"],
        help="select method to execute"
    )


@pytest.fixture(scope='session')
def base_breed_url(request):
    return request.config.getoption("--breedurl")


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))
