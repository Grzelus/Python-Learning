# 🐍 Python Learning

Repozytorium zawierające praktyczne zadania, ćwiczenia oraz mini-projekty do nauki języka **Python**, biblioteki standardowej oraz dobrych praktyk programistycznych (*Clean Code*, *PEP 8*).

---

## 📂 Spis treści i zrealizowane tematy

### 📁 Moduł `os` – Operacje na systemie plików
Zestaw zadań praktycznych z wykorzystaniem wbudowanego modułu `os` oraz modułu ścieżek `os.path`:

* **[`zadanie_1.py`](zadanie_1.py)** – **Eksplorator bieżącego katalogu**
  * Pobieranie bieżącego katalogu roboczego (`os.getcwd()`).
  * Listowanie zawartości (`os.listdir()`).
  * Rozróżnianie plików i folderów (`os.path.isfile`, `os.path.isdir`).
  * Pobieranie rozmiaru plików w bajtach (`os.path.getsize`) oraz bezpieczne łączenie ścieżek (`os.path.join`).

* **[`zadanie_2.py`](zadanie_2.py)** – **Generator struktury projektu**
  * Sprawdzanie istnienia katalogów (`os.path.exists`) i rzucanie wyjątków (`FileExistsError`).
  * Automatyczne tworzenie zagnieżdżonych struktur katalogów (`os.makedirs`).
  * Tworzenie plików `.gitkeep` w podfolderach za pomocą menedżera kontekstu (`with open(...)`).

* **[`zadanie_3.py`](zadanie_3.py)** – **Rekurencyjny szperacz plików (`os.walk`)**
  * Przeszukiwanie całego drzewa katalogów w głąb za pomocą generatora `os.walk`.
  * Filtrowanie plików po rozszerzeniu.
  * Zliczanie sumarycznego rozmiaru plików i przeliczanie na kilobajty (KB).

* **[`zadanie_4.py`](zadanie_4.py)** – **Konfiguracja przez zmienne środowiskowe (`os.environ`)**
  * Pobieranie zmiennych systemowych (`os.getenv`).
  * Ustawianie wartości domyślnych i modyfikacja słownika środowiskowego (`os.environ`).

* **[`zadanie_5.py`](zadanie_5.py)** – **Automatyczny sortownik i sprzątacz plików**
  * Praktyczna automatyzacja porządkowania plików w katalogach w oparciu o rozszerzenia.
  * Łączenie `os.walk`, `os.path.splitext` oraz `os.rename`.

* **[`zadania_modul_os.md`](zadania_modul_os.md)** – Kompendium wiedzy i ściągawka z modułu `os`.

### 🧰 Narzędzia Branżowe (Industry Standard)
Nowoczesne technologie, biblioteki i wzorce używane w codziennej pracy developera:

* **[`zadanie_pathlib.py`](zadanie_pathlib.py)** – **Obiektowa obsługa ścieżek (`pathlib`)**
  * Tworzenie zagnieżdżonych struktur katalogów (`Path.mkdir(parents=True, exist_ok=True)`).
  * Łączenie ścieżek operatorem `/`.
  * Wyszukiwanie wzorcem (`p.glob("*.txt")`, `p.rglob()`).
  * Pobieranie metadanych (`.name`, `.stem`, `.stat().st_size`).

* **[`zadanie_pathlib_2.py`](zadanie_pathlib_2.py)** – **Błyskawiczny procesor treści i backupy**
  * Nowoczesny odczyt i zapis z kodowaniem UTF-8 (`.read_text(encoding="utf-8")`, `.write_text(...)`).
  * Analiza tekstu (zliczanie linii i słów).
  * Automatyczne tworzenie kopii zapasowych ze zmianą rozszerzenia (`.with_suffix(".bak")`).
  * Modyfikacja i dopisywanie stopek weryfikacyjnych do raportów.

* **[`zadania_narzedzia_branzowe.md`](zadania_narzedzia_branzowe.md)** – Pełny zestaw zadań, ściągawki i mini-projekty branżowe (`pathlib`, `json`, `csv`, `requests`, `logging`, `argparse`, `dataclasses`, `pytest`).

---

## 🚀 Jak uruchomić lokalnie

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/Grzelus/Python-Learning.git
   cd Python-Learning
   ```

2. **Uruchom wybrane zadanie:**
   ```bash
   python zadanie_pathlib.py
   python zadanie_pathlib_2.py
   ```

---

## 🛠️ Technologie i narzędzia
* **Python 3.x**
* **Git & GitHub**
* Standardowa biblioteka Pythona (`pathlib`, `os`, `os.path`, `json`, `csv`, `logging`, `argparse`, `dataclasses`)

