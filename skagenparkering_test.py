from sure import expect
import httpretty
from skagenparkering import SkagenParkering


@httpretty.activate
def test_skagen_return_200():
    httpretty.register_uri(httpretty.POST, "https://permit.parkingguru.com/no/Account/LogIn",
                           status=200)
    response = SkagenParkering("","","999").login()
    expect(response).to.equal(200)
