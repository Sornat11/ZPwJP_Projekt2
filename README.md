# Analiza i Wizualizacja Danych z Web Scrapingu

Projekt wykorzystuje programowanie obiektowe w Pythonie do pobierania, analizy i wizualizacji danych pozyskanych ze stron internetowych. Proces obejmuje web scraping, przetwarzanie danych oraz ich prezentację w formie interaktywnych wykresów. Dodatkowo, przeprowadzono testy w celu weryfikacji poprawności działania funkcji.

## Główne Założenia

1. **Pobieranie danych**:
    - Automatyczne zbieranie informacji ze stron internetowych przy użyciu web scrapingu.
    - Przetwarzanie i przechowywanie danych w formacie Pandas DataFrame.

2. **Analiza danych**:
    - Identyfikacja kluczowych trendów i zależności.
    - Możliwość filtrowania i agregowania danych według różnych kryteriów.

3. **Wizualizacja danych**:
    - Tworzenie wykresów i interaktywnych elementów graficznych.
    - Prezentacja wyników w przejrzysty sposób przy użyciu narzędzi do wizualizacji.

4. **Testowanie**:
    - Przeprowadzono testy poprawności pobierania i analizy danych.
    - Weryfikacja zgodności wyników z oczekiwanymi wartościami.

## Instalacja i Konfiguracja

### Wymagania

- Python 3.x
- Wirtualne środowisko do zarządzania zależnościami (zalecane)

### Instalacja

1. Pobierz projekt z repozytorium.
2. Zainstaluj wymagane biblioteki, uruchamiając:

```bash
pip install -r requirements.txt
```

## Uruchomienie

Po zainstalowaniu zależności uruchom aplikację, aby zobaczyć analizę i wizualizacje danych:

```bash
streamlit run main.py
```

## Technologie

Projekt wykorzystuje:

- **Python** – główny język programowania
- **Pandas** – analiza danych
- **BeautifulSoup/Selenium** – web scraping
- **Matplotlib/Seaborn/Plotly** – wizualizacja danych
- **Streamlit** – interaktywny interfejs użytkownika
- **Pytest/Unittest** – testowanie poprawności kodu
