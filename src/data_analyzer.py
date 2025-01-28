from collections import defaultdict

from collections import defaultdict

class DataAnalyzer:
    def __init__(self, df):
        """
        Inicjalizuje obiekt klasy DataAnalyzer.

        :param df: DataFrame z danymi do analizy.
        """
        self.df = df


    def sort_results(self, data, reverse=True):
        """
        Sortuje wyniki według wartości.

        :param data: Słownik lub lista krotek do posortowania.
        :param reverse: Czy sortować malejąco (domyślnie True).
        :return: Posortowana lista krotek.
        """
        return sorted(data.items(), key=lambda x: x[1], reverse=reverse)

    def calculate_average_revenue_by_industry(self):
        """
        Oblicza średni przychód dla każdej branży.

        :return: Słownik z branżą jako kluczem i średnim przychodem jako wartością.
        """
        industry_revenue = defaultdict(list)
        for index, row in self.df.iterrows():
            # Usuwamy przecinki i konwertujemy na float
            revenue = float(row['Revenue (USD millions)'].replace(',', ''))
            industry_revenue[row['Industry']].append(revenue)
        
        average_revenue = {industry: sum(revenues) / len(revenues) for industry, revenues in industry_revenue.items()}
        return average_revenue

    def find_top_growth_companies(self, n=5):
        """
        Znajduje firmy z największym wzrostem przychodu.

        :param n: Liczba firm do zwrócenia (domyślnie 5).
        :return: DataFrame z top N firmami z największym wzrostem przychodu.
        """
        # Usuwamy znak procentu i konwertujemy na float
        self.df['Revenue growth'] = self.df['Revenue growth'].str.rstrip('%').astype(float)
        top_growth = self.df.nlargest(n, 'Revenue growth')
        return top_growth[['Name', 'Industry', 'Revenue growth']]
    

    def find_companies_with_most_employees(self, n=5):
        """
        Znajduje firmy z największą liczbą pracowników.

        :param n: Liczba firm do zwrócenia (domyślnie 5).
        :return: DataFrame z top N firmami z największą liczbą pracowników.
        """
        # Usuwamy przecinki i konwertujemy na int
        self.df['Employees'] = self.df['Employees'].str.replace(',', '').astype(int)
        top_employees = self.df.nlargest(n, 'Employees')
        return top_employees[['Name', 'Industry', 'Employees']]
    
    def find_companies_by_headquarters_state(self, state):
        """
        Znajduje firmy z siedzibą w określonym stanie.

        :param state: Stan, w którym znajduje się siedziba firmy.
        :return: DataFrame z firmami z siedzibą w określonym stanie.
        """
        return self.df[self.df['Headquarters'].str.contains(state, case=False)]
    
    