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

* **[`zadania_modul_os.md`](zadania_modul_os.md)** – Kompendium wiedzy, ściągawka z najważniejszych funkcji modułu `os` oraz treści zadań.

---

## 🚀 Jak uruchomić lokalnie

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/Grzelus/Python-Learning.git
   cd Python-Learning
   ```

2. **Uruchom wybrane zadanie:**
   ```bash
   python zadanie_1.py
   python zadanie_2.py
   python zadanie_3.py
   ```

---

## 🛠️ Technologie i narzędzia
* **Python 3.x**
* **Git & GitHub**
* Standardowa biblioteka Pythona (`os`, `os.path`)
