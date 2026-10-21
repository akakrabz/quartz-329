"""Check a trimmed page keeps structure. Usage: trim_check.py OLD NEW"""
import re, sys
def norm(s): return re.sub(r"\s+", "", re.sub(r"^\s*>\s?", "", s, flags=re.M))
def parts(t):
    body = t.split("\n---", 2)[-1] if t.startswith("---") else t
    heads = re.findall(r"^#{2,4} .*$", t, re.M)
    figs = re.findall(r"<!-- fig:[\w-]+ -->", t)
    disp = [norm(m) for m in re.findall(r"\$\$(.+?)\$\$", t, re.S)]
    links = set(re.findall(r"\[\[([^\]|]+)", t))
    tip = re.search(r"> \[!tip\] Practice this lecture\n(?:>.*\n?)*", t)
    hdr = re.search(r"^\*Lecture \d+ ·.*$", t, re.M)
    prl = re.search(r"^\*\*Practice\.\*\*.*$", t, re.M)
    hdr = (hdr.group(0) if hdr else "") + (prl.group(0) if prl else "")
    words = len(re.findall(r"\S+", body))
    return heads, figs, disp, links, tip.group(0) if tip else None, hdr, words
o, n = (open(p).read() for p in sys.argv[1:3])
O, N = parts(o), parts(n)
bad = []
if O[0] != N[0]: bad.append(f"headings changed: {[h for h in O[0] if h not in N[0]]} / {[h for h in N[0] if h not in O[0]]}")
if O[1] != N[1]: bad.append(f"figure markers changed")
miss = [d for d in O[2] if d not in N[2]]
if miss: bad.append(f"{len(miss)} display-math blocks removed or edited: " + " | ".join(m[:70] for m in miss))
ml = O[3] - N[3]
if ml: bad.append(f"link targets dropped: {sorted(ml)}")
if O[4] != N[4]: bad.append("generated 'Practice this lecture' box changed")
if O[5] != N[5]: bad.append("header line or generated Practice line changed")
print(f"{sys.argv[2].split('/')[-1]}: words {O[6]} -> {N[6]} ({100*(N[6]-O[6])/O[6]:+.0f}%)")
for b in bad: print("  FAIL", b)
if not bad: print("  OK structure kept")
