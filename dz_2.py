
# задание 2

import re
import requests

sait = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

regex = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                 r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')

for parse in regex.findall(sait):
    remote_addr, request_datetime, request_type, requested_resource, response_code, response_size = parse
    print(remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
