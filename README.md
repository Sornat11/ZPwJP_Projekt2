# Projekt Analizy i Wizualizacji Danych

Projekt ten oferuje funkcjonalność do pobierania, analizowania i wizualizowania danych dotyczących przychodów firm, wzrostu oraz statystyk zatrudnienia. Jest zaprojektowany do przetwarzania i analizy danych biznesowych za pomocą bibliotek Pythona do manipulacji danymi i wizualizacji.

## Funkcje

1. **Pobieranie Danych**:
    - Klasa `DataScraper` pobiera i analizuje dane z określonego URL.
    - Wydobywa tabele z strony i przechowuje dane w DataFrame Pandas.

2. **Analiza Danych**:
    - Klasa `DataAnalyzer` zawiera metody do:
        - Obliczania średnich przychodów według branży.
        - Znalezienia firm z największym wzrostem przychodów.
        - Identyfikowania firm z największą liczbą pracowników.
        - Filtrowania firm na podstawie stanu, w którym znajduje się ich siedziba.

3. **Wizualizacja Danych**:
    - Klasa `DataVisualization` oferuje metody do tworzenia interaktywnych i statycznych wykresów:
        - Wykres słupkowy pokazujący średni przychód według branży.
        - Wykres punktowy porównujący przychód z liczbą pracowników dla firm.

## Instalacja i Przygotowanie Środowiska

### Wymagania Wstępne

Upewnij się, że masz zainstalowanego Pythona w wersji 3.x. Zaleca się również utworzenie środowiska wirtualnego do zarządzania zależnościami.

### Kroki Instalacji

1. Sklonuj repozytorium lub pobierz pliki projektu.
2. Zainstaluj wymagane biblioteki Pythona, uruchamiając poniższe polecenie:

```bash
pip install -r requirements.txt
```