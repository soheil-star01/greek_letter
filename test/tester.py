import requests


# check whether the received letter is a valid one
def check_greek_letter(received_letter):
    letters = ['\u0391', '\u0392', '\u0393', '\u0394', '\u0395', '\u0396', '\u0397', '\u0398', '\u0399',
               '\u039A', '\u039B', '\u039C', '\u039D', '\u039E', '\u039F', '\u03A0', '\u03A1', '\u03A3',
               '\u03A4', '\u03A5', '\u03A6', '\u03A7', '\u03A8', '\u03A9', '\u03B1', '\u03B2', '\u03B3',
               '\u03B4', '\u03B5', '\u03B6', '\u03B7', '\u03B8', '\u03B9', '\u03BA', '\u03BB', '\u03BC',
               '\u03BD', '\u03BE', '\u03BF', '\u03C0', '\u03C1', '\u03C2', '\u03C3', '\u03C4', '\u03C5',
               '\u03C6', '\u03C7', '\u03C8', '\u03C9', '\u03D1', '\u03D2', '\u03D6']
    return received_letter in letters


# sending a request to the main app and checking its response
def request_letter():
    try:
        resp = requests.get(url='http://127.0.0.1/letter')
        if resp.status_code == 200:
            suggested_letter = resp.text
            print(suggested_letter)
            if check_greek_letter(suggested_letter):
                print('Test is passed!')
                return True

    except Exception as e:
        print(f"Exception on response: {e}")

    print('Test Failed!')
    return False


assert request_letter()
