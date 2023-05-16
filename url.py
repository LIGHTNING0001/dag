from conf.server import host, port

BASE_URL = 'http://' + host + ':' + str(port)

TOF_ESTIMATE_NAV = BASE_URL + "/api/tof/estimate/nav?portfolioCode={}&date={}"
