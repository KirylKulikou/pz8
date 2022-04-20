
# задание 1

import re

#
def email_parse(email):
    list = ['name', 'domain']
    email_p = re.match(r'(\w+)@(\w+)[.](\w+)', email)
    if email_p:
        parse = re.split(r'@', email)
        n_d = dict(zip(list, parse))
        print(n_d)
    else:
        None
        print(f'ValueError: {email}')

email_parse('7554!557@gmail.com')
email_parse('7554557@gmail.com')
