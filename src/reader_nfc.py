import requests
from bs4 import BeautifulSoup


def find_nfc_data(id):
    url = f"https://www.fazenda.pr.gov.br/nfce/qrcode?p={id}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('tr', id=lambda x: x and x.startswith('Item'))
        
        buyer_cpf = None
        emission = None

        for li_tag in soup.find_all('li'):
            if "CPF: " in li_tag.text:
                buyer_cpf = li_tag.text.split("CPF: ")[1].strip() if "CPF: " in li_tag.text else "CPF not found"
            elif "Emissão: " in li_tag.text:
                emission = li_tag.text.split("Emissão: ")[1].strip() if "Emissão: " in li_tag.text else "Creation date not found"
        
        total_value = soup.find('span', class_='totalNumb txtMax').text.strip() if soup.find('span', class_='totalNumb txtMax') else "Total value not found"
        
        return soup, items, buyer_cpf, total_value, emission
    else:
        print(f"Error accessing the URL: {response.status_code}")


def nfc_parse_items(id):
    soup, items, cpf_comprador, total_value, emissao = find_nfc_data(id)

    item_data = []

    if not soup:
        return {}


    for item in items:
        try:
            name = item.find('span', class_='txtTit2').text.strip() if item.find('span', class_='txtTit2') else "Name not found"
            quantity = item.find('span', class_='Rqtd').text.split(':')[1].strip() if item.find('span', class_='Rqtd') else "Quantity not found"
            unit_value = item.find('span', class_='RvlUnit').text.split(':')[1].strip() if item.find('span', class_='RvlUnit') else "Unit value not found"
            total_value_item = item.find('span', class_='valor').text.strip() if item.find('span', class_='valor') else "Total item value not found"

            item_data.append({
                'name': name,
                'quantity': quantity,
                'unit_value': unit_value,
                'total_value_item': total_value_item,
            })
        except Exception as e:
            print(f"Erro ao processar o item: {e}")

    return {
            'cpf_comprador': cpf_comprador,
            'items': item_data,
            'valor_total': total_value,
            'data_criacao': emissao}


def convert_date_to_sheet_format(nfc_data):
    vendor = ["Supermercado"]
    cpf = [nfc_data["cpf_comprador"]]
    creation_date_str = nfc_data["data_criacao"]
    creation_date = [creation_date_str.split()[0]]
    total_value = [nfc_data ["valor_total"]]

    sheet_data = [vendor, cpf, creation_date, total_value]

    return sheet_data
