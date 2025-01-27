import unittest
import pandas as pd
from collections import defaultdict
from src import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        # Przykładowe dane do testów
        data = {
            'Name': ['Company A', 'Company B', 'Company C', 'Company D'],
            'Industry': ['Retail', 'Tech', 'Retail', 'Healthcare'],
            'Revenue (USD millions)': ['100,000', '200,000', '150,000', '300,000'],
            'Revenue growth': ['10%', '20%', '15%', '5%'],
            'Employees': ['10,000', '20,000', '15,000', '30,000'],
            'Headquarters': ['New York', 'California', 'Texas', 'California']
        }
        self.df = pd.DataFrame(data)
        self.analyzer = DataAnalyzer(self.df)

    def test_sort_results(self):
        data = {'Retail': 2, 'Tech': 1, 'Healthcare': 1}
        sorted_data = self.analyzer.sort_results(data)
        expected = [('Retail', 2), ('Tech', 1), ('Healthcare', 1)]
        self.assertEqual(sorted_data, expected)

    def test_calculate_average_revenue_by_industry(self):
        average_revenue = self.analyzer.calculate_average_revenue_by_industry()
        expected = {'Retail': 125000.0, 'Tech': 200000.0, 'Healthcare': 300000.0}
        self.assertEqual(average_revenue, expected)

    def test_find_top_growth_companies(self):
        top_growth = self.analyzer.find_top_growth_companies(n=2)
        expected_names = ['Company B', 'Company C']
        self.assertEqual(list(top_growth['Name']), expected_names)

    def test_find_companies_with_most_employees(self):
        top_employees = self.analyzer.find_companies_with_most_employees(n=2)
        expected_names = ['Company D', 'Company B']
        self.assertEqual(list(top_employees['Name']), expected_names)

    def test_find_companies_by_headquarters_state(self):
        companies_in_california = self.analyzer.find_companies_by_headquarters_state('California')
        expected_names = ['Company B', 'Company D']
        self.assertEqual(list(companies_in_california['Name']), expected_names)

if __name__ == '__main__':
    unittest.main()