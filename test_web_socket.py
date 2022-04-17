import pytest


@pytest.mark.unittest
@pytest.mark.parametrize(
    "number_response", [(5, False), (10, True), (233213, False), (4, True)]
)
def test_is_par(number_response):
    from websockets import ManagementInformation

    management_information = ManagementInformation()
    res = management_information._is_even_odd(number_response[0])
    assert res is number_response[1]


@pytest.mark.unittest
@pytest.mark.parametrize(
    "number_response", [(5, 1), (100, 0)]
)
def test_sum_prime(number_response):
    from websockets import ManagementInformation

    management_information = ManagementInformation()
    res = management_information._sum_prime(number_response[0])
    assert res == number_response[1]



