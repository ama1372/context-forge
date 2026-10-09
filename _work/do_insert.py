import io, re, sys
p = 'PROJECT_CONTEXT.md'
c = io.open(p, 'r', encoding='utf-8', newline='').read()
add = io.open('_work/insert.txt', 'r', encoding='utf-8', newline='').read()

patterns = [
    r'^##\s+.*Session Tracker',
    r'^#\s+.*Session Tracker',
    r'Session Tracker',
]
m = None
for pat in patterns:
    m = re.search(pat, c, re.M)
    if m:
        print(f'MATCHED: {pat!r} at offset {m.start()}')
        break

if not m:
    print('FAIL: section 13 heading not found')
    for i, ln in enumerate(c.split(chr(10))[:80], 1):
        if 'Session' in ln or 'Tracker' in ln or ln.startswith('##'):
            print(f'  line {i}: {ln!r}')
    sys.exit(1)

c = c[:m.start()] + add + c[m.start():]
io.open(p, 'w', encoding='utf-8', newline='').write(c)
print(f'OK inserted before offset {m.start()}')