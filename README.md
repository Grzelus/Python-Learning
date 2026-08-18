# 🐍 Python Learning – Praktyczna Ścieżka Developerska

Repozytorium zawierające praktyczne zadania, ćwiczenia oraz mini-projekty do nauki języka **Python**, biblioteki standardowej oraz standardów i narzędzi wykorzystywanych komercyjnie w branży IT (*Industry Standard*, *Clean Code*, *PEP 8*).

---

## 📑 Spis Treści

* [📁 Struktura Repozytorium](#-struktura-repozytorium)
* [📦 Moduły i Zrealizowane Zadania](#-moduły-i-zrealizowane-zadania)
  * [1. Moduł `os` – Operacje na systemie plików](#1-moduł-os--operacje-na-systemie-plików)
  * [2. Moduł `pathlib` – Nowoczesne ścieżki obiektowe](#2-moduł-pathlib--nowoczesne-ścieżki-obiektowe)
* [🧭 Nadchodzące Moduły Branżowe](#-nadchodzące-moduły-branżowe)
* [🚀 Jak uruchomić lokalnie](#-jak-uruchomić-lokalnie)
* [🛠️ Technologie i narzędzia](#️-technologie-i-narzędzia)

---

## 📁 Struktura Repozytorium

```text
Python-Learning/
├── 📁 01_modul_os/                    # Tradycyjne operacje systemowe (moduł os)
│   ├── zadania_modul_os.md           # Kompendium i treści zadań
│   ├── zadanie_1.py                  # Eksplorator bieżącego katalogu
│   ├── zadanie_2.py                  # Generator struktury folderów projektu
│   ├── zadanie_3.py                  # Rekurencyjny szperacz plików (os.walk)
│   ├── zadanie_4.py                  # Zmienne środowiskowe (os.environ, os.getenv)
│   └── zadanie_5.py                  # Automatyczny sortownik i sprzątacz plików
│
├── 📁 02_pathlib/                     # Nowoczesne, obiektowe zarządzanie ścieżkami
│   ├── zadanie_pathlib.py            # Podstawy Path, tworzenie folderów i metadane
│   ├── zadanie_pathlib_2.py          # Błyskawiczne operacje I/O, backupy (.bak) i UTF-8
│   └── path lib/                     # Dane testowe i katalog roboczy zadań
│       ├── dane.csv
│       ├── raport_2026_01.txt
│       ├── raport_2026_02.txt
│       └── backup/
│
├── zadania_narzedzia_branzowe.md     # Pełna ścieżka edukacyjna narzędzi branżowych
├── README.md                         # Dokumentacja główna projektu
└── .gitignore
```

---

## 📦 Moduły i Zrealizowane Zadania

### 1. Moduł `os` – Operacje na systemie plików
Folder: **[`01_modul_os/`](01_modul_os/)** | Ściągawka: **[`zadania_modul_os.md`](01_modul_os/zadania_modul_os.md)**

* **[`01_modul_os/zadanie_1.py`](01_modul_os/zadanie_1.py)** – **Eksplorator bieżącego katalogu**
  * Pobieranie bieżącego katalogu roboczego (`os.getcwd()`) i listowanie zawartości (`os.listdir()`).
  * Rozróżnianie plików i folderów (`os.path.isfile`, `os.path.isdir`) oraz pobieranie rozmiaru (`os.path.getsize`).
* **[`01_modul_os/zadanie_2.py`](01_modul_os/zadanie_2.py)** – **Generator struktury projektu**
  * Bezpieczne sprawdzanie istnienia katalogu (`os.path.exists`) i rzucanie `FileExistsError`.
  * Automatyczne tworzenie struktur zagnieżdżonych (`os.makedirs`) i generowanie plików `.gitkeep`.
* **[`01_modul_os/zadanie_3.py`](01_modul_os/zadanie_3.py)** – **Rekurencyjny szperacz plików (`os.walk`)**
  * Przeszukiwanie całego drzewa katalogów w głąb za pomocą generatora `os.walk`.
  * Filtrowanie plików po rozszerzeniu oraz kalkulacja łącznego rozmiaru w KB.
* **[`01_modul_os/zadanie_4.py`](01_modul_os/zadanie_4.py)** – **Zmienne środowiskowe (`os.environ`)**
  * Odczyt użytkownika systemu i konfiguracji aplikacji (`os.getenv`).
  * Dynamiczne definiowanie zmiennych w środowisku wykonawczym.
* **[`01_modul_os/zadanie_5.py`](01_modul_os/zadanie_5.py)** – **Automatyczny Sprzątacz Plików**
  * Klasyfikacja plików na podstawie mapy rozszerzeń (`os.path.splitext`).
  * Automatyczne przenoszenie plików do folderów docelowych (`os.rename`).

---

### 2. Moduł `pathlib` – Nowoczesne ścieżki obiektowe
Folder: **[`02_pathlib/`](02_pathlib/)** | Przewodnik: **[`zadania_narzedzia_branzowe.md`](zadania_narzedzia_branzowe.md)**

* **[`02_pathlib/zadanie_pathlib.py`](02_pathlib/zadanie_pathlib.py)** – **Obiektowa obsługa ścieżek (`Path`)**
  * Tworzenie katalogów z automatycznymi rodzicami (`Path.mkdir(parents=True, exist_ok=True)`).
  * Łączenie ścieżek eleganckim operatorem `/`.
  * Wyszukiwanie wzorcem (`p.glob("*.txt")`, `p.rglob()`).
  * Odczyt metadanych systemu operacyjnego (`.name`, `.stem`, `.stat().st_size`).
* **[`02_pathlib/zadanie_pathlib_2.py`](02_pathlib/zadanie_pathlib_2.py)** – **Szybki procesor treści i backupy**
  * Bezpośredni odczyt i zapis z kodowaniem UTF-8 (`.read_text(encoding="utf-8")`, `.write_text(...)`).
  * Analiza treści tekstu (zliczanie linii i słów).
  * Tworzenie kopii zapasowych ze zmianą rozszerzenia (`.with_suffix(".bak")`).
  * Modyfikacja i dopisywanie stopek weryfikacyjnych do plików.

---

## 🧭 Nadchodzące Moduły Branżowe

Pełny plan nauki z opisami zadań znajduje się w pliku **[`zadania_narzedzia_branzowe.md`](zadania_narzedzia_branzowe.md)**:

| Moduł | Technologia | Zakres |
| :--- | :--- | :--- |
| **03** | `json` & `csv` | Przetwarzanie i konwersja danych biznesowych |
| **04** | `requests` | Komunikacja z publicznym REST API (kursy walut NBP) |
| **05** | `logging` | Profesjonalne rejestrowanie zdarzeń i rotacja logów |
| **06** | `argparse` | Budowanie konsolowych narzędzi CLI z flagami i `--help` |
| **07** | `dataclasses` & `typing` | Bezpieczne modelowanie obiektów i adnotacje typów |
| **08** | `pytest` | Testy jednostkowe, asercje i pokrycie kodu |
| **09** | **Projekt Integracyjny** | Kompletna aplikacja CLI łącząca wszystkie narzędzia |

---

## 🚀 Jak uruchomić lokalnie

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/Grzelus/Python-Learning.git
   cd Python-Learning
   ```

2. **Aktywuj wirtualne środowisko (opcjonalnie):**
   ```bash
   # Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   ```

3. **Uruchom wybrane zadanie:**
   ```bash
   # Zadania z modułu os:
   python 01_modul_os/zadanie_1.py
   python 01_modul_os/zadanie_5.py

   # Zadania z modułu pathlib:
   python 02_pathlib/zadanie_pathlib.py
   python 02_pathlib/zadanie_pathlib_2.py
   ```

---

## 🛠️ Technologie i narzędzia

* **Język:** Python 3.13+
* **System kontroli wersji:** Git & GitHub
* **Biblioteka standardowa:** `os`, `os.path`, `pathlib`, `json`, `csv`, `logging`, `argparse`, `dataclasses`, `typing`
* **Narzędzia zewnętrzne:** `requests`, `pytest`
* **Dobre praktyki:** *Clean Code*, *PEP 8*, type hinty, jawne kodowanie UTF-8
