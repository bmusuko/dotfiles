#!/usr/bin/python3
import requests

data = requests.get('http://bmusuko.ninja:8081/').json()

def formater(x):
    return '{:,.0f}'.format(x).replace(',','.')


print(f' {formater(data["confirm"])}  {formater(data["up"])}')