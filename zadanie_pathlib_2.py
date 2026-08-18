
from pathlib import Path

p = Path('./path lib')

if not p.exists():
    raise FileNotFoundError("File do not exist")

text_files = [file for file in p.glob('**/*.txt')]

backup_path = p / "backup"
backup_path.mkdir(parents=True, exist_ok=True)

for file in text_files:
    content = file.read_text(encoding='utf-8')
    lines_amount = content.splitlines()
    words_amount = content.split()
    print(f"================  {file.name}  ================")
    print(f"{len(lines_amount)} <-- ilosc linii")
    print(f"{len(words_amount)} <-- ilosc slow")

    backup_file = (backup_path / file.name).with_suffix(".bak")
    backup_file.write_text(content, encoding='utf-8')

    file.write_text(content + "\n\n\nZweryfikowano Pomyslnie", encoding='utf-8')


