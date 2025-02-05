# NFC Reader
![A_stingy_parrot_examining_a_supermarket_NFC_receip](https://github.com/user-attachments/assets/d154c684-05f4-4f59-80fc-fc653f078fe0)

O **NFC Reader** é um projeto criado como base de estudo para ler e processar notas fiscais, como aquelas emitidas por supermercados e farmácias (NFC-e). O objetivo do projeto é permitir o controle de gastos mensais de forma automatizada, ao consumir as informações das notas fiscais e armazená-las em um lugar acessível, como o Google Sheets.

## Contexto

Sempre tive curiosidade de saber quanto gasto mensalmente com compras em supermercados e farmácias. A ideia surgiu de querer ter uma visão mais clara do meu orçamento, então resolvi criar uma solução para ler e armazenar esses dados de forma simples e acessível. Após buscar por APIs públicas de acesso a notas fiscais, não encontrei nenhuma que permitisse consultar as notas pelo CPF, então decidi construir uma aplicação para resolver esse problema.

## Funcionalidades

O projeto consiste em um serviço simples desenvolvido com **Flask**, que oferece duas rotas principais:

- **GET**: Recebe o ID de uma nota fiscal no formato de QR Code e busca os dados da nota na página do governo. A resposta dessa rota é um objeto JSON com as informações da nota fiscal.
  
  Exemplo de resposta do **GET**:
  ```json
  {
      "cpf_comprador": "123.456.789-00",
      "data_criacao": "01/11/2024 21:23:49 - Via Consumidor\n\n     \nProtocolo de Autorização: 141241695698525 01/11/2024 21:23:50\n     \nAmbiente de Produção - \nVersão XML: 4.00 - Versão XSLT: 2.03",
      "items": [
          {
              "name": "TOAL.PAPEL KIT",
              "quantity": "1",
              "total_value_item": "19,99",
              "unit_value": "19,99"
          },
          {
              "name": "PAPEL H.PERS.L",
              "quantity": "1",
              "total_value_item": "25,99",
              "unit_value": "25,99"
          }
      ],
      "total_value": "45,98"
  }
  ```

- **POST**: Recebe o ID da nota e armazena os dados coletados em um formato JSON. A resposta dessa rota é um status **204 No Content**, indicando que a operação foi bem-sucedida, mas não há conteúdo a ser retornado.

## Como Funciona

### Passo 1: Leitura do QR Code
O serviço consome o ID da nota fiscal, que é extraído do QR Code. O QR Code contém um link para a página da Secretaria da Fazenda do estado do Paraná, com o ID da nota fiscal.

O formato do link é:

```
https://www.fazenda.pr.gov.br/nfce/qrcode?p=<ID_DA_NOTA_FISCAL>
```

### Passo 2: Acesso e Extração de Dados
A aplicação acessa a URL acima usando o ID extraído do QR Code. Uma vez que a página é carregada, o conteúdo HTML da página é processado para extrair as informações relevantes da nota fiscal, como valores, CNPJ, data, entre outros, utilizando a biblioteca **BeautifulSoup** da `bs4`.

### Passo 3: Armazenamento
Com os dados extraídos da nota fiscal, o serviço gera uma lista de arrays contendo as informações, que pode ser facilmente armazenada em uma planilha do **Google Sheets** ou em outro banco de dados para controle financeiro.

## Tecnologias Utilizadas

- **Flask**: Framework web para criar a API.
- **BeautifulSoup (bs4)**: Biblioteca para parseamento de HTML e extração dos dados da página.
- **Google Sheets API**: Para armazenar as informações extraídas em uma planilha.
- **Python**: Linguagem de programação utilizada no desenvolvimento do serviço.

## Demonstração

Aqui está uma demonstração do funcionamento da aplicação:
![2025-02-05 14-28-15](https://github.com/user-attachments/assets/2cbe8df8-2ddd-4c32-9b52-c7326ba2e81c)



## Como Rodar

Para rodar o projeto, siga os passos abaixo:

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv myenv
   source myenv/bin/activate   # Para Linux/Mac
   myenv\Scripts\activate      # Para Windows
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o aplicativo:
   ```bash
   python app.py
   ```

O aplicativo estará rodando em **http://localhost:5000** e você poderá acessar as rotas **GET** e **POST** conforme descrito.

## Ideias Futuras

- **Criar um CRUD completo**: Desenvolver um sistema completo para gerenciar as notas fiscais, com funcionalidades de criação, leitura, atualização e exclusão de registros.
- **Armazenar as informações em um banco de dados**: Integrar o sistema a um banco de dados para armazenar as informações das notas fiscais de maneira mais eficiente e escalável.
- **Criar um aplicativo para ler os QR Codes**: Desenvolver um aplicativo (mobile ou desktop) para facilitar a leitura dos QR Codes diretamente, tornando o processo ainda mais ágil.
- **Melhorar a planilha para disposição dos dados**: Aperfeiçoar a apresentação dos dados na planilha do Google Sheets, facilitando a análise e o controle financeiro com gráficos e visualizações mais intuitivas.

---

Agora, o README também inclui as instruções para rodar o projeto. Caso precise de mais alguma modificação, estou à disposição!
