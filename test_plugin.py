import requests

def auto_captioning(data):
    parsed_data = data.replace(" ", "_")
    url = "https://glorious-made-up-growth.anvil.app/_/api/colab/"

    r = requests.get(url + parsed_data)
    print(r.json())

data = input("present some data for auto captioning: ")

auto_captioning(data)