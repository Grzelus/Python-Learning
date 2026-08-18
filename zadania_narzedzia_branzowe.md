# 🚀 Narzędzia Branżowe w Pythonie – Zestaw Zadań Praktycznych

Zestaw zadań przygotowany z myślą o umiejętnościach, bibliotekach i narzędziach, z którymi programista Pythona spotyka się na co dzień w komercyjnych projektach (*Industry Standard*).

---

## 🧭 Spis Modułów

1. [Moduł 1: Nowoczesne ścieżki – `pathlib`](#1-nowoczesne-ścieżki--pathlib)
2. [Moduł 2: Formaty wymiany danych – `json` oraz `csv`](#2-formaty-wymiany-danych--json-oraz-csv)
3. [Moduł 3: Komunikacja z API – biblioteka `requests`](#3-komunikacja-z-api--biblioteka-requests)
4. [Moduł 4: Profesjonalne logowanie – moduł `logging`](#4-profesjonalne-logowanie--moduł-logging)
5. [Moduł 5: Budowanie narzędzi CLI – `argparse`](#5-budowanie-narzędzi-cli--argparse)
6. [Moduł 6: Struktura i typowanie danych – `dataclasses` & `typing`](#6-struktura-i-typowanie-danych--dataclasses--typing)
7. [Moduł 7: Testowanie kodu – `pytest`](#7-testowanie-kodu--pytest)
8. [🏆 Projekt Zwieńczający: Integracyjny Raportomat CLI](#-projekt-zwieńczający-integracyjny-raportomat-cli)

---

## 1. Nowoczesne ścieżki – `pathlib`
> **Dlaczego w branży?** Moduł `pathlib` (wprowadzony w Pythonie 3.4) jest obiektowym standardem pracy ze ścieżkami, który w nowym kodzie zastępuje starsze funkcje `os.path`.

### 📋 Szybka ściągawka
```python
from pathlib import Path

p = Path("folder/plik.txt")
p.exists()            # Czy istnieje?
p.is_file()           # Czy to plik?
p.name                # 'plik.txt'
p.stem                # 'plik' (bez rozszerzenia)
p.suffix              # '.txt' (rozszerzenie)
p.parent              # folder nadrzędny
p.with_suffix(".bak") # zmienia rozszerzenie na .bak (zwraca nowy obiekt Path)
p.with_name("nowa.txt") # zmienia nazwę pliku w tym samym folderze
p.unlink(missing_ok=True) # usuwa plik (z missing_ok=True nie rzuca błędu gdy pliku brak)
p.rename(cel)         # przenosi / zmienia nazwę pliku
p.relative_to(baza)   # zwraca ścieżkę względną względem katalogu bazowego
p.read_text("utf-8")  # szybki odczyt zawartości
p.write_text("tekst", "utf-8") # szybki zapis
Path.cwd()            # bieżący katalog
p / "podfolder" / "plik2.txt"  # operator `/` do łączenia ścieżek!
```

### 🟢 Zadanie 1.1: Refaktoryzacja i operacje na `Path`
**Cel:** Przejście z paradygmatu funkcyjnego (`os.path`) na obiektowy (`Path`).
**Treść:**
1. Stwórz skrypt `zadanie_pathlib.py`.
2. Za pomocą `Path` utwórz katalog `backup_dir/raporty` (użyj `.mkdir(parents=True, exist_ok=True)`).
3. Wygeneruj w nim 3 pliki: `raport_2026_01.txt`, `raport_2026_02.txt`, `dane.csv`.
4. Wykorzystaj metodę `.glob("*.txt")` lub `.rglob()`, aby znaleźć wyłącznie pliki tekstowe.
5. Dla każdego znalezionego pliku wypisz:
   - Jego pełną nazwę (`.name`)
   - Nazwę bez rozszerzenia (`.stem`)
   - Rozmiar w bajtach (`.stat().st_size`)

---

### 🟡 Zadanie 1.2: Błyskawiczny procesor treści i kopie zapasowe (`read_text`, `write_text`, `with_suffix`)
**Cel:** Nowoczesny odczyt i modyfikacja treści plików bez tradycyjnego `with open(...)` oraz operacje na rozszerzeniach.
**Treść:**
Napisz skrypt `zadanie_pathlib_2.py`, który:
1. Wyszukuje wszystkie pliki `.txt` w wybranym katalogu (np. `path lib/`) za pomocą `p.glob("*.txt")`.
2. Dla każdego pliku odczytuje jego zawartość za pomocą `file.read_text(encoding="utf-8")`.
3. Wypisuje statystyki tekstu dla każdego raportu:
   - Liczbę linii (`len(content.splitlines())`)
   - Liczbę słów (`len(content.split())`)
4. Tworzy kopię zapasową każdego pliku z rozszerzeniem `.bak` (użyj `file.with_suffix(".bak")`) i zapisuje w niej oryginalną treść za pomocą `.write_text(content, encoding="utf-8")`.
5. Do oryginalnego pliku `.txt` dopisuje na samym końcu stopkę weryfikacyjną:
   ```text
   
   --- Zweryfikowano pomyślnie ---
   ```

---

### 🟠 Zadanie 1.3: Inteligentny archiwizator i czyszczenie (`relative_to`, `rename`, `unlink`)
**Cel:** Przenoszenie plików, bezpieczne usuwanie oraz prezentacja ścieżek względnych.
**Treść:**
Napisz skrypt `zadanie_pathlib_3.py`, który:
1. Tworzy wewnątrz folderu `path lib/` podkatalog `archiwum/`.
2. Wyszukuje wszystkie pliki kopii zapasowych (`*.bak`).
3. Przenosi każdy plik `.bak` do folderu `path lib/archiwum/` (podpowiedź: `cel = folder_archiwum / plik.name`, następnie `plik.rename(cel)`).
4. Tworzy dla testu pusty plik tymczasowy `temp_trash.tmp` (rozmiar 0 bajtów).
5. Skanuje folder i jeśli jakikolwiek plik ma rozmiar równy 0 bajtów (`stat().st_size == 0`), usuwa go z dysku metodą `file.unlink(missing_ok=True)`.
6. Na koniec wypisuje ścieżki wszystkich zarchiwizowanych plików jako ścieżki względne wobec głównego folderu projektu (`file.relative_to(Path.cwd())`).

---

## 2. Formaty wymiany danych – `json` oraz `csv`
> **Dlaczego w branży?** JSON to uniwersalny format komunikacji z API i plikami konfiguracyjnymi. CSV to najczęstszy format eksportu i importu tabelarycznych danych biznesowych.

### 📋 Szybka ściągawka
```python
import json
import csv

# JSON
data = {"user": "Anna", "roles": ["admin", "dev"]}
json_str = json.dumps(data, indent=4)         # Serializacja do stringa
with open("config.json", "w") as f:
    json.dump(data, f, indent=4)              # Zapis do pliku
with open("config.json", "r") as f:
    loaded_data = json.load(f)                # Odczyt z pliku

# CSV
with open("dane.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "imie", "stanowisko"])
    writer.writeheader()
    writer.writerow({"id": 1, "imie": "Jan", "stanowisko": "Developer"})
```

### 🟡 Zadanie 2.1: Konwerter i filtr danych JSON -> CSV
**Cel:** Pobieranie danych strukturalnych, walidacja i generowanie raportu tabelarycznego.
**Treść:**
1. Stwórz plik `pracownicy.json` zawierający listę co najmniej 5 pracowników (każdy obiekt: `id`, `imie`, `dzial`, `wynagrodzenie`, `aktywny`).
2. Napisz skrypt wczytujący ten plik.
3. Skrypt filtruje tylko pracowników z statusem `aktywny: True` oraz zarabiających powyżej określonej kwoty.
4. Wynik zapisz do pliku `aktywni_pracownicy.csv` przy użyciu `csv.DictWriter`.

---

## 3. Komunikacja z API – biblioteka `requests`
> **Dlaczego w branży?** Python jest jednym z najpopularniejszych języków do integracji mikrousług, pobierania danych z zewnętrznych serwisów i automatyzacji.

*Instalacja biblioteki w wirtualnym środowisku:*
```bash
pip install requests
```

### 📋 Szybka ściągawka
```python
import requests

response = requests.get("https://api.example.com/data", timeout=5)
if response.status_code == 200:
    data = response.json()  # automatyczne parsowanie odpowiedzi JSON
else:
    print(f"Błąd HTTP: {response.status_code}")
```

### 🟠 Zadanie 3.1: Klient Kursów Walut NBP API
**Cel:** Odpytywanie darmowego publicznego API, obsługa wyjątków sieciowych i przetwarzanie odpowiedzi.
**Treść:**
1. Użyj oficjalnego API Narodowego Banku Polskiego: `https://api.nbp.pl/api/exchangerates/tables/A/?format=json`.
2. Napisz funkcję `get_currency_rate(code: str) -> float`, która:
   - Pobiera aktualną tabelę kursów.
   - Wyszukuje walutę o podanym kodzie (np. `EUR`, `USD`, `GBP`, `CHF`).
   - Zwraca aktualny średni kurs waluty.
3. Zadbaj o obsługę błędów:
   - Obsłuż błąd braku połączenia / timeout (`requests.exceptions.RequestException`).
   - Obsłuż sytuację, gdy użytkownik poda nieistniejący kod waluty.
4. Pozwól użytkownikowi przeliczyć np. 1500 PLN na wybraną walutę.

---

## 4. Profesjonalne logowanie – moduł `logging`
> **Dlaczego w branży?** W projektach komercyjnych funkcja `print()` jest zakazana na produkcji. Używa się modułu `logging`, który umożliwia rejestrowanie daty, poziomu błędu, nazwy modułu oraz jednoczesny zapis do konsoli i rotowanych plików logów.

### 📋 Poziomy logowania
| Poziom | Zastosowanie |
| :--- | :--- |
| `DEBUG` | Bardzo szczegółowe informacje przydatne podczas diagnozowania problemów. |
| `INFO` | Potwierdzenie, że wszystko działa zgodnie z planem (np. "Pobrano 50 rekordów"). |
| `WARNING` | Wskazanie czegoś nieoczekiwanego lub ostrzeżenie o zbliżającym się problemie. |
| `ERROR` | Poważniejszy błąd uniemożliwiający wykonanie konkretnej funkcji. |
| `CRITICAL` | Krytyczny błąd zagrażający działaniu całej aplikacji. |

### 📋 Szybka ściągawka
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Aplikacja uruchomiona pomyślnie.")
logger.error("Wystąpił błąd podczas pobierania danych.")
```

### 🟡 Zadanie 4.1: Logowanie audytowe operacji na plikach
**Cel:** Rejestracja zdarzeń w pliku `audit.log` z odpowiednimi poziomami.
**Treść:**
1. Skonfiguruj `logging` tak, aby zapisywał logi zarówno do konsoli, jak i do pliku `operations.log`.
2. Napisz funkcję, która w pętli przetwarza listę plików do odczytu (w tym podaj 2 pliki istniejące i 2 nieistniejące).
3. Przy udanym odczycie loguj informację na poziomie `INFO`.
4. Gdy plik nie istnieje (wyłap `FileNotFoundError`), zaloguj ostrzeżenie na poziomie `WARNING` lub błąd `ERROR` z pełnym tracebackiem (`logger.exception(...)`).

---

## 5. Budowanie narzędzi CLI – `argparse`
> **Dlaczego w branży?** Skrypty na serwerach i w potokach CI/CD (GitHub Actions, GitLab CI) są uruchamiane z konsoli z przekazanymi parametrami i flagami.

### 📋 Szybka ściągawka
```python
import argparse

parser = argparse.ArgumentParser(description="Program do przetwarzania danych.")
parser.add_argument("plik", help="Ścieżka do pliku wejściowego (argument wymagany)")
parser.add_argument("-v", "--verbose", action="store_true", help="Włącz szczegółowe logi")
parser.add_argument("-l", "--limit", type=int, default=10, help="Limit rekordów (domyślnie 10)")

args = parser.parse_args()
print(f"Plik: {args.plik}, Limit: {args.limit}, Verbose: {args.verbose}")
```

### 🟠 Zadanie 5.1: Terminalowy Inspektor Plików (CLI Tool)
**Cel:** Zbudowanie pełnoprawnego narzędzia konsolowego z obsługą `--help`, argumentami i flagami.
**Treść:**
1. Napisz program `file_inspector.py`.
2. Program przyjmuje:
   - Argument pozycyjny: ścieżkę do katalogu.
   - Opcjonalną flagę `--ext` / `-e` filtrującą po rozszerzeniu (np. `-e py`).
   - Opcjonalną flagę `--sort-size` sortującą wyniki od największego pliku.
   - Flagę `--json` zapisującą wynik analizy do pliku `raport.json`.
3. Uruchomienie `python file_inspector.py --help` powinno wyświetlić czytelną instrukcję obsługi.

---

## 6. Struktura i typowanie danych – `dataclasses` & `typing`
> **Dlaczego w branży?** Type hintingu (`typing`) oraz `dataclasses` wymaga się w nowoczesnym Pythonie, aby kod był czytelny, bezpieczny i dobrze współpracował z IDE oraz linterami (`mypy`, `ruff`).

### 📋 Szybka ściągawka
```python
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Produkt:
    id: int
    nazwa: str
    cena: float
    tagi: List[str] = field(default_factory=list)
    utworzono: datetime = field(default_factory=datetime.now)

    def cena_brutto(self, vat: float = 0.23) -> float:
        return round(self.cena * (1 + vat), 2)
```

### 🟢 Zadanie 6.1: Modelowanie domeny e-commerce
**Cel:** Wykorzystanie `dataclass`, adnotacji typów oraz metod pomocniczych.
**Treść:**
1. Zdefiniuj klasę `@dataclass` `ZamowienieItem` (`nazwa_produktu: str`, `ilosc: int`, `cena_jednostkowa: float`).
2. Zdefiniuj klasę `@dataclass` `Zamowienie`:
   - `id_zamowienia: str`
   - `klient_email: str`
   - `pozycje: List[ZamowienieItem]`
   - Metodę `laczna_wartosc() -> float`
3. Napisz funkcję, która wczytuje zamówienia z formatu słownikowego/JSON i tworzy instancje powyższych obiektów.

---

## 7. Testowanie kodu – `pytest`
> **Dlaczego w branży?** Brak testów automatycznych w projektach komercyjnych to ogromne ryzyko regresji. `pytest` to najpopularniejszy framework testowy w ekosystemie Pythona.

*Instalacja biblioteki:*
```bash
pip install pytest
```

### 📋 Szybka ściągawka
```python
# test_kalkulator.py
def dodaj(a: int, b: int) -> int:
    return a + b

def test_dodawania_liczb_dodatnich():
    assert dodaj(2, 3) == 5

def test_dodawania_zera():
    assert dodaj(10, 0) == 10
```
Uruchomienie testów w terminalu:
```bash
pytest
# lub
pytest -v
```

### 🟡 Zadanie 7.1: Napisz testy jednostkowe
**Cel:** Przetestowanie funkcji biznesowych za pomocą asercji i różnych przypadków brzegowych.
**Treść:**
1. Napisz moduł `walidator.py` z funkcjami:
   - `czy_poprawny_email(email: str) -> bool` (sprawdza obecność `@`, kropki w domenie itp.)
   - `oblicz_znizke(kwota: float, procent: float) -> float` (oblicza cenę po rabacie; rzuca `ValueError`, gdy procent < 0 lub > 100).
2. Stwórz plik `test_walidator.py`.
3. Napisz co najmniej 5 testów:
   - Poprawne adresy e-mail.
   - Błędne adresy e-mail (brak małpy, puste pole, brak domeny).
   - Standardowe naliczenie zniżki.
   - Sprawdzenie, czy rzucany jest oczekiwany wyjątek `ValueError` przy nieprawidłowym procencie (`with pytest.raises(ValueError): ...`).

---

## 🏆 Projekt Zwieńczający: Integracyjny Raportomat CLI
> **Scenariusz biznesowy:** Twoja firma potrzebuje automatycznego narzędzia do pobierania danych finansowych/walutowych, zapisywania ich do bazy raportów z pełnym logowaniem i możliwością uruchamiania w harmonogramie zadań.

### 🔴 Zadanie 8: Stwórz `ExchangeRateReporter`
**Treść projektu:**
Połącz wszystkie poznane narzędzia w jedną kompletną aplikację:

1. **Struktura projektu:**
   ```text
   currency_tool/
   ├── src/
   │   ├── __init__.py
   │   ├── api_client.py     # Obsługa zapytań HTTP do NBP (requests)
   │   ├── models.py         # Modele danych (dataclasses, typing)
   │   ├── storage.py        # Zapis do CSV/JSON z użyciem Pathlib
   │   └── logger_config.py  # Konfiguracja logging
   ├── tests/
   │   └── test_api_client.py # Testy jednostkowe (pytest)
   ├── main.py               # Punkt wejścia CLI (argparse)
   └── requirements.txt      # Zależności projektu
   ```

2. **Wymagania funkcjonalne:**
   - **CLI (`main.py`):** Użytkownik podaje w konsoli kod waluty (`--currency EUR`), format wyjściowy (`--format csv` lub `--format json`) oraz katalog docelowy (`--output ./raporty`).
   - **API:** Program łączy się z API NBP i pobiera aktualny kurs oraz kursy z ostatnich 5 dni.
   - **Data Classes:** Pobrane dane są mapowane na obiekty `@dataclass`.
   - **Pathlib & Storage:** Program upewnia się, że folder wyjściowy istnieje i zapisuje plik o nazwie np. `raport_EUR_2026-08-18.csv`.
   - **Logging:** Wszystkie kroki (połączenie z API, parsowanie, zapis do pliku, ewentualne błędy) trafiają do `app.log` z datą i poziomem zdarzenia.
   - **Pytest:** Zestaw testów weryfikuje poprawne działanie parsowania danych oraz modeli.

---

## 💡 Jak pracować z tym zestawem?
1. Realizuj zadania moduł po module w osobnym folderze lub gałęzi gita.
2. Korzystaj z wirtualnego środowiska (`python -m venv .venv`).
3. Commituj zmiany po każdym wykonanym zadaniu – dobra historia commitów w Git to również kluczowa umiejętność branżowa!
