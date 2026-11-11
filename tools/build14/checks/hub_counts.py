#!/usr/bin/env python3
"""Point shares quoted on content/exams/index.md ("The papers" table).
Each part of each Spring/Fall Exam 3 is put in one of four groups:
  A waves in media (Lectures 21-26), B line basics (27), C bounce diagrams (28-30), D Lectures 31-34 (steady state on lines;
  outside the FA26 Midterm 3 scope, which is Lectures 1-30).
Points are the papers' own; multiple-choice items carry the per-item points printed on the paper."""
P = {
 "SP17": [("1a", 2, "A"), ("1b", 2, "A"), ("1c", 2, "A"),
          ("2(i)", 3, "A"), ("2(ii)", 3, "B"), ("2(iii)", 3, "A"), ("2(iv)", 3, "A"), ("2(v)", 3, "C"), ("2(vi)", 3, "C"),
          ("3", 27, "A"), ("4", 18, "A"), ("5", 20, "C"), ("6", 11, "D")],
 "SP18": [("1(i)", 3, "A"), ("1(ii)", 3, "B"), ("1(iii)", 3, "A"), ("1(iv)", 3, "A"), ("1(v)", 3, "B"), ("1(vi)", 3, "D"),
          ("1(vii)", 3, "C"), ("1(viii)", 3, "D"), ("1(ix)", 3, "D"), ("1(x)", 3, "D"),
          ("2", 20, "A"), ("3", 30, "C"), ("4", 20, "D")],
 "SP19": [("1", 25, "A"), ("2", 20, "B"), ("3", 15, "A"), ("4", 25, "C"), ("5", 15, "D")],
 "FA23": [("1", 11, "A"), ("2", 9, "A"), ("3", 12, "C"), ("4", 18, "C"), ("5", 24, "C"), ("6", 10, "A"), ("7", 16, "D")],
}
PAGE = {"FA23": (30, 0, 54, 16), "SP19": (40, 20, 25, 15), "SP18": (29, 6, 33, 32), "SP17": (60, 3, 26, 11)}
ok = True
for paper, parts in P.items():
    tot = sum(p for _, p, _ in parts)
    got = tuple(sum(p for _, p, g in parts if g == k) for k in "ABCD")
    good = tot == 100 and got == PAGE[paper]
    ok &= good
    print(("PASS " if good else "FAIL ") + f"{paper}: total {tot}; A, B, C, D = {got}; page says {PAGE[paper]}")
c = [PAGE[k][2] for k in PAGE]; d = [PAGE[k][3] for k in PAGE]
print(f"bounce-diagram share: {min(c)} to {max(c)} points (a quarter to a half); Lectures 31-34 (not on FA26 Midterm 3): {min(d)} to {max(d)} points")
print("SP18 without its Lecture 31-34 parts:", 100 - PAGE["SP18"][3], "points (page: 68)")
print("SUMMARY:", "all PASS" if ok else "FAIL")
