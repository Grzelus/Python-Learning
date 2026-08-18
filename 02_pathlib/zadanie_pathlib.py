from pathlib import Path

p = Path(__file__).parent / 'path lib'

p.mkdir(parents=True, exist_ok=True)

#==========SETUP=================================================================
files = ['raport_2026_01.txt', 'raport_2026_02.txt', 'dane.csv']

for file in files:
    q = p / file
    print(q)
    q.touch(mode=0o777, exist_ok=True)

#================================================================================

text_files = [file for file in p.rglob('*.txt')]

for file in text_files:
    print(file.name)
    print(file.stem)
    print(file.stat().st_size)


