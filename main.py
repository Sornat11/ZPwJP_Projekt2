from src import DataScraper
from src import DataAnalyzer
class Main:
    def __init__(self, url):
        self.url = url
        self.scraper = None  
        self.analyzer = None

    def run(self):
        print("Rozpoczynanie pobierania danych...")
        
        # Tworzenie instancji DataScraper
        self.scraper = DataScraper(self.url)
        
        # Pobieranie danych
        self.scraper.fetch_data()
        
        # Parsowanie danych
        self.scraper.parse_table()
        
        # Tworzenie instancji DataAnalyzer
        self.analyzer = DataAnalyzer(self.scraper.get_data())
        
        # Wyświetlanie przetworzonych danych
        self.show_data()
        
        # Analiza danych
        self.analyze_data()

    def show_data(self):
        print("Dane zostały pobrane i przetworzone:")
        print(self.scraper.get_data())

    def analyze_data(self):
        print("\nAnaliza danych:")
        
        # Średni przychód wg branży
        average_revenue = self.analyzer.calculate_average_revenue_by_industry()
        print("\nŚredni przychód wg branży:")
        for industry, revenue in average_revenue.items():
            print(f"{industry}: {revenue:.2f} mln USD")
        
        # Firmy z największym wzrostem przychodu
        top_growth = self.analyzer.find_top_growth_companies()
        print("\nTop 5 firm z największym wzrostem przychodu:")
        print(top_growth)
    
        # Firmy z największą liczbą pracowników
        top_employees = self.analyzer.find_companies_with_most_employees()
        print("\nTop 5 firm z największą liczbą pracowników:")
        print(top_employees)
        
        # Firmy z siedzibą w określonym stanie (np. California)
        state = "California"
        companies_in_state = self.analyzer.find_companies_by_headquarters_state(state)
        print(f"\nFirmy z siedzibą w stanie {state}:")
        print(companies_in_state)

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    
    main_app = Main(url)
    main_app.run()

    # test