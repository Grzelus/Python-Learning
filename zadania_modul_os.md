# Moduł `os` w Pythonie – Zestaw Zadań Praktycznych

---

## 📋 Krótka ściągawka (Najważniejsze funkcje)

| Funkcja | Co robi? |
| :--- | :--- |
| `os.getcwd()` | Zwraca ścieżkę do bieżącego katalogu roboczego (Current Working Directory). |
| `os.chdir(path)` | Zmienia bieżący katalog roboczy. |
| `os.listdir(path)` | Zwraca listę nazw plików i folderów w podanym katalogu. |
| `os.mkdir(path)` / `os.makedirs(path)` | Tworzy katalog / tworzy zagnieżdżoną strukturę katalogów (np. `a/b/c`). |
| `os.remove(path)` / `os.rmdir(path)` | Usuwa plik / usuwa pusty folder. |
| `os.rename(src, dst)` | Zmienia nazwę lub przenosi plik/folder. |
| `os.walk(top)` | Generator przechodzący rekurencyjnie przez całe drzewo katalogów. |
| `os.path.join(p1, p2, ...)` | Bezpiecznie łączy fragmenty ścieżek zgodnie z systemem operacyjnym (`\` w Windows, `/` w Linux/macOS). |
| `os.path.exists(path)` | Sprawdza, czy plik lub folder istnieje. |
| `os.path.isfile(path)` / `os.path.isdir(path)` | Sprawdza, czy ścieżka prowadzi do pliku / folderu. |
| `os.path.getsize(path)` | Zwraca rozmiar pliku w bajtach. |
| `os.path.splitext(path)` | Dzieli nazwę pliku na nazwę bazową i rozszerzenie (np. `("foto", ".jpg")`). |
| `os.getenv(key, default)` | Pobiera wartość zmiennej środowiskowej z opcjonalną wartością domyślną. |
| `os.environ` | Słownik reprezentujący zmienne środowiskowe systemu. |

---

## 🧩 Zadania do wykonania

### 🟢 Zadanie 1: Eksplorator bieżącego katalogu (Podstawy)
**Cel:** Pobranie informacji o miejscu uruchomienia programu i jego zawartości.

**Treść:**
1. Wypisz pełną ścieżkę do aktualnego katalogu roboczego.
2. Pobierz zawartość tego katalogu.
3. Dla każdego elementu sprawdź i wypisz:
   - Nazwę elementu.
   - Informację, czy jest to **plik** czy **katalog**.
   - Jeśli to plik — wypisz jego rozmiar w bajtach (`os.path.getsize`).

---

### 🟡 Zadanie 2: Generator struktury projektu (Tworzenie i sprawdzanie)
**Cel:** Bezpieczne tworzenie i zarządzanie strukturami folderów.

**Treść:**
Napisz funkcję `create_project_structure(base_dir)`, która:
1. Sprawdza, czy folder `base_dir` już istnieje. Jeśli tak, wypisuje ostrzeżenie i nie nadpisuje go.
2. Jeśli nie istnieje, tworzy za jednym razem następującą strukturę katalogów:
   ```text
   moj_projekt/
   ├── src/
   ├── tests/
   └── docs/
   ```
3. Wewnątrz każdego z podfolderów tworzy pusty plik `.gitkeep`.
4. *Podpowiedź:* Użyj `os.path.join`, `os.makedirs(..., exist_ok=True)` oraz standardowej funkcji `open()`.

---

### 🟠 Zadanie 3: Rekurencyjny szperacz plików (`os.walk`)
**Cel:** Przeszukiwanie zagnieżdżonych struktur folderów w głąb.

**Treść:**
Napisz funkcję `find_files_by_extension(root_dir, extension)`, która:
1. Przeszukuje katalog `root_dir` oraz **wszystkie jego podkatalogi** za pomocą generatora `os.walk`.
2. Wyszukuje pliki o zadanym rozszerzeniu (np. `.txt` lub `.py`).
3. Zwraca listę pełnych, bezwzględnych ścieżek do znalezionych plików.
4. *Bonus:* Zsumuj łączny rozmiar wszystkich znalezionych plików i wyświetl go w kilobajtach (KB).

---

### 🟣 Zadanie 4: Konfiguracja przez zmienne środowiskowe (`os.environ`)
**Cel:** Bezpieczne zarządzanie konfiguracją i zmiennymi systemu.

**Treść:**
Napisz skrypt, który:
1. Pobiera nazwę zalogowanego użytkownika systemu (`USERNAME` w Windowsie lub `USER` w Linuxie/macOS).
2. Sprawdza, czy istnieje zmienna środowiskowa `APP_MODE`:
   - Jeśli istnieje, wypisuje jej wartość.
   - Jeśli nie istnieje, przyjmuje wartość domyślną `"DEVELOPMENT"` (użyj `os.getenv`).
3. Ustawia w kodzie nową zmienną środowiskową o nazwie `SECRET_KEY` na wartość `"tajny_klucz_123"` (za pomocą `os.environ`) i odczytuje ją ponownie, aby potwierdzić zapis.

---

### 🔴 Zadanie 5 (Mini-projekt): Automatyczny Sprzątacz Plików
**Cel:** Praktyczne zastosowanie operacji na ścieżkach, rozszerzeniach i przenoszeniu plików.

**Treść:**
Stwórz skrypt, który porządkuje pliki w wybranym folderze (np. folderze testowym):
1. Zdefiniuj mapowanie rozszerzeń na nazwy folderów docelowych, np.:
   - Obrazy: `.png`, `.jpg`, `.jpeg` ➔ folder `Grafika`
   - Dokumenty: `.pdf`, `.docx`, `.txt` ➔ folder `Dokumenty`
   - Kody/Skrypty: `.py`, `.json`, `.sql` ➔ folder `Kod`
2. Skrypt powinien przejrzeć podany folder:
   - Ignorować podkatalogi (nie przenosić innych folderów).
   - Dla każdego pliku sprawdzić jego rozszerzenie (`os.path.splitext`).
   - Jeśli folder docelowy nie istnieje — utworzyć go.
   - Przenieść plik do odpowiedniego folderu za pomocą `os.rename`.
   - Pliki o nierozpoznanych rozszerzeniach pozostawić bez zmian.
