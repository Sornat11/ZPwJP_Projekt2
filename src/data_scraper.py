from bs4 import BeautifulSoup
import requests
import pandas as pd

class DataScraper:
    def __init__(self, url):
        self.url = url  # URL strony do pobrania danych
        self.page = None  # Strona HTML
        self.soup = None  # Obiekt BeautifulSoup
        self.df = None    # DataFrame z danymi

    def fetch_data(self):
        page = requests.get(self.url)
        self.page = page
        self.soup = BeautifulSoup(page.text, 'lxml')

    def parse_table(self):
        # Znalezienie pierwszej tabeli na stronie
        table = self.soup.find_all('table')[0]
        
        # Pobranie nagłówków tabeli
        world_titles = table.find_all('th')
        world_table_titles = [title.text.strip() for title in world_titles]
        
        # Tworzenie pustego DataFrame z nagłówkami
        self.df = pd.DataFrame(columns=world_table_titles)
        
        # Pobieranie danych z wierszy tabeli
        column_data = table.find_all('tr')
        for row in column_data[1:]:  # Pomijamy pierwszy wiersz (nagłówki)
            row_data = row.find_all('td')
            individual_row_data = [data.text.strip() for data in row_data]
            
            # Dodanie danych do DataFrame
            length = len(self.df)
            self.df.loc[length] = individual_row_data

    def get_data(self):
        return self.df