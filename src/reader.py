import requests
from bs4 import BeautifulSoup

nfc_id = "41241178116670001994650030003781391004712248%7C2%7C1%7C1%7CFD45F10D884018801BC57F816F3552AC65BB0C10"


def find_nfc_data(id):
    url = f"https://www.fazenda.pr.gov.br/nfce/qrcode?p={id}"
    response = requests.get(url)

    if response.status_code == 200:
       soup = BeautifulSoup(response.text, 'html.parser')
       response = soup.find_all('tr', id=lambda x: x and x.startswith('Item'))

    return response


def nfc_parse_items(id):
    items = find_nfc_data(id)

    item_data = []
   
    for item in items:
        name = item.find('span', class_='txtTit2').text.strip()
        quantity = item.find('span', class_='Rqtd').text.split(':')[1].strip()
        unit_value = item.find('span', class_='RvlUnit').text.split(':')[1].strip()
        total_value = item.find('span', class_='valor').text.strip()

        item_data.append({
            'name': name,
            'quantity': quantity,
            'unit_value': unit_value,
            'total_value': total_value
        })


    return item_data
