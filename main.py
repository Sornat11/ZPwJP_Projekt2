import streamlit as st
from src import DataScraper, DataAnalyzer, DataVisualization
import pandas as pd

# Konfiguracja strony
st.set_page_config(
    page_title="Największe spółki w USA - analiza",
    page_icon="💼",  # Ikona strony
    layout="wide"  # Szeroki layout
)

# Funkcja główna aplikacji
def main():
    st.title("Największe spółki w USA - analiza")
    
    # Wstęp
    st.write("""
        ## Projekt zaliczeniowy - Zaawansowane programowanie w języku Python
        **Rok akademicki 2024/2025**
        
        ### Autorzy:
        - Jakub Sornat
        - Marcin Mika
        - Filip Kopańko
        - Maciej Tajs
    """)

    st.write("""
        ### Podział ról:
        - **Jakub Sornat**: Web Scraping
        - **Marcin Mika**: Analiza i testy do analizy
        - **Filip Kopańko**: Streamlit i wykresy
        - **Maciej Tajs**: Testy i wykresy
    """)
    
    # Sekcja Analiza danych
    st.subheader("Analiza danych")
    
    # Podstawowe informacje o URL
    url = st.text_input(
        "Podaj URL strony do pobrania danych:",
        value='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
    )

    if url:
        st.write("Rozpoczynanie pobierania danych...")
        
        try:
            scraper = DataScraper(url)
            scraper.fetch_data()
            scraper.parse_table()

            # Wyświetlanie przetworzonych danych
            data = scraper.get_data()
            st.write("### Dane pobrane i przetworzone:")
            st.dataframe(data)

            # Analiza danych
            analyzer = DataAnalyzer(data)

            # Średni przychód wg branży
            st.write("#### Średni przychód wg branży:")
            average_revenue = analyzer.calculate_average_revenue_by_industry()
            st.write(average_revenue)

            # Firmy z największym wzrostem przychodu
            st.write("#### Top 5 firm z największym wzrostem przychodu:")
            top_growth = analyzer.find_top_growth_companies()
            st.write(top_growth)

            # Firmy z największą liczbą pracowników
            st.write("#### Top 5 firm z największą liczbą pracowników:")
            top_employees = analyzer.find_companies_with_most_employees()
            st.write(top_employees)

            # Firmy z siedzibą w określonym stanie
            state = st.text_input("Podaj nazwę stanu do analizy (np. California):", value="California")
            if state:
                companies_in_state = analyzer.find_companies_by_headquarters_state(state)
                st.write(f"#### Firmy z siedzibą w stanie {state}:")
                st.write(companies_in_state)

        except Exception as e:
            st.error(f"Błąd podczas analizy: {str(e)}")
    
    # Sekcja Wizualizacja danych
    st.subheader("Wizualizacja danych")
    
    # Wizualizacja danych
    st.write("### Wizualizacja danych:")
    visualization = DataVisualization()

    # Wykres średniego przychodu wg branży
    # Zakładamy, że dane zostały już pobrane w poprzednich sekcjach
    average_revenue_dict = analyzer.calculate_average_revenue_by_industry()
    
    average_revenue_df = pd.DataFrame({
        'Industry': list(average_revenue_dict.keys()),
        'Average Revenue': list(average_revenue_dict.values())
    })

        # Sekcja interaktywnego wykresu
        st.write("### Wykres średniego przychodu")
        
        all_industries = average_revenue_df['Industry'].tolist()
        selected_industries = st.multiselect(
            "Wybierz branże:",
            options=all_industries,
            default=all_industries[:3]
        )
        
        if selected_industries:
            # Filtrowanie słownika
            filtered_dict = {
                industry: average_revenue_dict[industry] 
                for industry in selected_industries
            }
            
            # Generowanie wykresu
            interactive_viz = DataVisualization()
            fig = interactive_viz.plot_interactive_industry_revenue(filtered_dict)
            st.pyplot(fig)
            
            # Opcjonalnie: tabela z danymi
            st.write("#### Dane dla wybranych branż:")
            st.dataframe(pd.DataFrame.from_dict(filtered_dict, orient='index', 
                       columns=['Średni przychód (M$']))
        else:
            st.warning("Wybierz przynajmniej jedną branżę z listy powyżej")

        # Wykres zależności między przychodem a liczbą pracowników
        st.write("#### Zależność między przychodem a liczbą pracowników:")
        fig2 = visualization.plot_revenue_vs_employees(analyzer.df)
        st.plotly_chart(fig2, use_container_width=True)
        
        
    except Exception as e:
        st.error(f"Błąd podczas analizy: {str(e)}")
        
if __name__ == "__main__":
    main()
