from pathlib import Path

p = Path(__file__).parent / 'path lib'

q = p / 'archiwum'

q.mkdir(parents=True, exist_ok=True)

backup_files = [file for file in p.rglob('*.bak')]

for file in backup_files:
    file.rename(q/file.name)

tempfile = (p / 'temp_trash.tmp')
tempfile.touch()

files = [file for file in p.glob('**/*') if file.is_file()]

for file in files:
    if file.stat().st_size == 0:
        file.unlink(missing_ok=True)
        continue

    print(file.resolve().relative_to(Path.cwd()))
    