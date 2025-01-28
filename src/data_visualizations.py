# src/data_visualizations.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from src import DataAnalyzer

class DataVisualization:

    
    def plot_interactive_industry_revenue(self, industry_data: dict):
        """
        Generuje ciemny wykres z różnymi kolorami dla każdej branży
        """
        # Konwersja na DataFrame i sortowanie
        df = pd.DataFrame({
            'Industry': list(industry_data.keys()),
            'Average Revenue': list(industry_data.values())
        }).sort_values('Average Revenue', ascending=True)

        # Styl wykresu
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(12, 8), facecolor='#0e1117')
        ax.set_facecolor('#0e1117')

        # Generowanie różnych kolorów
        colors = plt.cm.tab10(np.linspace(0, 1, len(df)))

        # Tworzenie wykresu
        bars = ax.barh(df['Industry'], 
                      df['Average Revenue'], 
                      color=colors,
                      height=0.7,
                      edgecolor='white')

        # Formatowanie osi i tytułu
        ax.set_title('Średni przychód w wybranych branżach', 
                   color='white', 
                   fontsize=16,
                   pad=20)
        
        ax.set_xlabel('Średni przychód (miliony USD)', 
                    color='white',
                    fontsize=12)
        
        ax.tick_params(axis='both', 
                     colors='white',
                     labelsize=10)

        # Siatka i obramowanie
        ax.grid(color='gray', 
              linestyle='--', 
              linewidth=0.5,
              alpha=0.7)
        
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')

        # Etykiety wartości
        for i, (industry_data, revenue) in enumerate(zip(df['Industry'], df['Average Revenue'])):
            ax.text(revenue + 0.02 * max(df['Average Revenue']),  # Pozycja X
                  i,  # Pozycja Y
                  f'${revenue:,.2f}M', 
                  color='white',
                  va='center',
                  fontsize=10,
                  fontweight='bold')

        plt.tight_layout()
        return fig


    def plot_revenue_vs_employees(self, df):  
        """
        Generuje interaktywny wykres punktowy zależności przychodu od liczby pracowników.
        """
        
        df = df.copy()
        # Konwersja kolumn na string i czyszczenie
        df['Employees'] = (
            df['Employees']
            .astype(str)  # Wymuszamy typ tekstowy
            .str.replace(',', '')
            .astype(int)
        )
        
        df['Revenue (USD millions)'] = (
            df['Revenue (USD millions)']
            .astype(str)  # Wymuszamy typ tekstowy
            .str.replace(',', '')
            .astype(float)
        )

        # Tworzenie wykresu
        fig = px.scatter(
            df,
            x='Employees',
            y='Revenue (USD millions)',
            hover_name='Name',  # Wyświetla nazwę firmy przy hoverze
            color='Industry',   # Kolorowanie punktów według branży
            size='Revenue (USD millions)',  # Rozmiar punktu zależny od przychodu
            labels={
                'Employees': 'Liczba pracowników',
                'Revenue (USD millions)': 'Przychód (mln USD)'
            },
            title='<b>Zależność między przychodem a liczbą pracowników</b>',
            template='plotly_dark'  # Ciemny motyw
        )

        # Dostosowanie stylu
        fig.update_layout(
            hoverlabel=dict(
                bgcolor="black",
                font_size=14
            ),
            xaxis=dict(showgrid=True, gridcolor='gray'),
            yaxis=dict(showgrid=True, gridcolor='gray'),
            font=dict(color='white')
        )
        
        return fig
        
    