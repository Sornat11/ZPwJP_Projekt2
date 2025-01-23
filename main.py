from src import DataScraper

class Main:
    def __init__(self, url):
        self.url = url
        self.scraper = None  

    def run(self):
        print("Rozpoczynanie pobierania danych...")
        
        # Tworzenie instancji DataScraper
        self.scraper = DataScraper(self.url)
        
        # Pobieranie danych
        self.scraper.fetch_data()
        
        # Parsowanie danych
        self.scraper.parse_table()
        
        # Zwracanie przetworzonych danych
        self.show_data()

    def show_data(self):
        print("Dane zostały pobrane i przetworzone:")
        print(self.scraper.get_data())

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    
    main_app = Main(url)
    main_app.run()