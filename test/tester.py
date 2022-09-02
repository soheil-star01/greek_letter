import requests

try:
    resp = requests.get(url='http://127.0.0.1/letter')
    if resp.status_code != 200:
        print('Test Failed!')

    else:
        suggested_letter = resp.text
        print(suggested_letter)

except Exception as e:
    print(f"Exception on response: {e}")
