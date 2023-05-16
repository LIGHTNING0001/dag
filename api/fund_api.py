
import requests

from url import TOF_ESTIMATE_NAV

portfolioCode = 'tof_case_10'
date = '2022-03-14'

headers = {
    "token": "c4ca4238a0b923820dcc509a6f75849b"
}

url = TOF_ESTIMATE_NAV.format(portfolioCode, date)

print(url)

response = requests.request(method="get", url=url, headers=headers)

print(response.text)