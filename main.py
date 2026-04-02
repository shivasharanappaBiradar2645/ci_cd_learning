import requests

BASEURL = "https://yurippe.vercel.app/api/quotes"  #fixed the url 


def get_by_character(character):
    payload = {"character":character,"random":1}
    response = requests.get(BASEURL,params=payload)
    if response.status_code != 200:
        raise Exception(f"API Request failed with status: {response.status_code}")
    
    data = response.json()
    return data[0]["quote"]
    
def get_by_show(show):
    payload = {"show":show,"random":1}
    response = requests.get(BASEURL,params=payload)
    if response.status_code != 200:
        raise Exception(f"API Request failed with status: {response.status_code}")
    
    data = response.json()
    return f"character: {data[0]['character']} \nquote: {data[0]['quote']}"


if __name__ == "__main__":
    print(get_by_character("oreki"))
    print()
    print(get_by_show("hyouka"))