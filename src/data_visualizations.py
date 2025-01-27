# src/data_visualizations.py

import matplotlib.pyplot as plt
from src import DataAnalyzer

class DataVisualization:

    @staticmethod
    def plot_average_revenue_by_industry(average_revenue):
        """
        Rysuje wykres słupkowy przedstawiający średni przychód w każdej branży.

        :param average_revenue: Słownik z branżą jako kluczem i średnim przychodem jako wartością.
        """
        labels, values = zip(*average_revenue.items())
        
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='lightgreen')
        plt.xlabel('Branża')
        plt.ylabel('Średni przychód (mln USD)')
        plt.title('Średni przychód w każdej branży')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_revenue_vs_employees(df):
        """
        Rysuje wykres punktowy przedstawiający zależność między przychodem a liczbą pracowników.

        :param df: DataFrame zawierający kolumny 'Revenue (USD millions)' i 'Employees'.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Employees'], df['Revenue (USD millions)'], color='purple', alpha=0.6)
        plt.xlabel('Liczba pracowników')
        plt.ylabel('Przychód (mln USD)')
        plt.title('Zależność między przychodem a liczbą pracowników')
        plt.grid(True)
        plt.tight_layout()
        plt.show()