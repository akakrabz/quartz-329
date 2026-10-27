"""loss_check.py LNN  — every display-math block, figure marker and number-bearing inline formula of the
pre-restructure lecture page must appear in the new lecture page or in some concepts/*.md page."""
import re, sys, glob, os
PRE='pre/content-src/'; CUR='../../content/'
def norm(s): return re.sub(r"\s+","",re.sub(r"^\s*>\s?","",s,flags=re.M))
def lecture_file(root, n):
    for d in ['1-electrostatics','2-magnetostatics','3-maxwell-and-waves']:
        m=glob.glob(f"{root}{d}/{n:02d}-*.md")
        if m: return m[0]
n=int(sys.argv[1].lstrip('L'))
old=open(lecture_file(PRE,n)).read()
pool=norm(open(lecture_file(CUR,n)).read())
for f in glob.glob(CUR+'concepts/*.md'): pool+=norm(open(f).read())
for f in glob.glob(CUR+'problems/*.md'): pool+=norm(open(f).read())
# strip generated boxes from the old page
old=re.sub(r"> \[!tip\] Practice this lecture\n(?:>.*\n?)*","",old)
miss=[]
for m in re.findall(r"\$\$(.+?)\$\$", old, re.S):
    if norm(m) not in pool: miss.append(("display", norm(m)[:90]))
for m in re.findall(r"<!-- fig:[\w-]+ -->", old):
    if m.replace(" ","") not in pool.replace(" ",""): miss.append(("figure", m))
body=re.sub(r"\$\$.+?\$\$","",old,flags=re.S)
for m in re.findall(r"(?<!\$)\$([^$\n]+?)\$(?!\$)", body):
    k=norm(m)
    if re.search(r"\d",k) and len(k)>=6 and k not in pool: miss.append(("inline", k[:90]))
# dedupe
seen=set(); out=[]
for t,k in miss:
    if k not in seen: seen.add(k); out.append((t,k))
print(f"L{n}: {len(out)} items not found")
for t,k in out: print(f"  {t}: {k}")
if not out: print("OK")
