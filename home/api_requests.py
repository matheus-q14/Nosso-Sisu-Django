import requests


def get_college_address(college_name):
    api_url = f"https://nominatim.openstreetmap.org/search?addressdetails=1&q={college_name}&format=jsonv2"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(api_url, headers=headers)
    data = response.json()

    street = data[0]["address"]["road"]
    try:
        number = data[0]["address"]["house_number"]
    except Exception as e:
        number = ""
    try:
        neighbor = data[0]["address"]["suburb"]
    except Exception as e:
        neighbor = data[0]["address"]["county"]
    city = data[0]["address"]["city"]

    return f"Rua {street} {number}, {neighbor}, {city}"
