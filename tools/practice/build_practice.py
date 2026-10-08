#!/usr/bin/env python3
"""Practice-bank tool: validate the practice pages, generate the hub and list
pages, and (re)insert the practice links on lecture, unit and concept pages.

usage:
    python3 build_practice.py [--src CONTENT_DIR] [--write]

    without --write: parse and validate only (prints one line per page).
    with    --write: also regenerate practice/index.md, easy.md, medium.md,
                     hard.md, topics.md and update the links elsewhere.
                     Safe to run repeatedly (every insertion is idempotent).

CONTENT_DIR defaults to /home/claude/work/content-src if it exists, else to
../../content relative to this script (the delivered layout tools/practice/).

Problem block (practice/SPEC.md §4):
    ### L.N Short title
    <blank>
    > [!easy] Easy · tag · tag          (or medium / hard)
    > statement ...
    > *Source: ....*
    <blank>
    > [!hint]- Hint                      (required for medium/hard)
    ...
    > [!solution]- Solution
    > ...
    > **Answer.** ...
"""
import os, re, sys, unicodedata, collections
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = "/home/claude/work/content-src"
if not os.path.isdir(SRC):
    SRC = os.path.normpath(os.path.join(HERE, "..", "..", "content"))
if "--src" in sys.argv:
    SRC = sys.argv[sys.argv.index("--src") + 1]
PDIR = os.path.join(SRC, "practice")

LECTURES = {
    2: ("1-electrostatics/02-coulombs-law-superposition-and-gauss", "Coulomb's law, superposition and Gauss"),
    3: ("1-electrostatics/03-gauss-law-at-work", "Gauss's law at work"),
    4: ("1-electrostatics/04-divergence-and-curl", "Divergence and curl"),
    5: ("1-electrostatics/05-curl-free-fields-and-the-electrostatic-potential", "The electrostatic potential"),
    6: ("1-electrostatics/06-circulation-and-boundary-conditions", "Circulation and boundary conditions"),
    7: ("1-electrostatics/07-poisson-and-laplace", "Poisson's and Laplace's equations"),
    8: ("1-electrostatics/08-conductors-dielectrics-and-polarization", "Conductors, dielectrics and polarization"),
    9: ("1-electrostatics/09-static-fields-in-dielectric-media", "Static fields in dielectric media"),
    10: ("1-electrostatics/10-capacitance-and-conductance", "Capacitance and conductance"),
    11: ("1-electrostatics/11-lorentz-drude-models-for-conductivity-and-susceptibility", "Lorentz–Drude models"),
    12: ("2-magnetostatics/12-magnetic-force-biot-savart-and-amperes-law", "Magnetic force, Biot–Savart and Ampère"),
    13: ("2-magnetostatics/13-current-sheets-solenoids-and-the-vector-potential", "Current sheets, solenoids and the vector potential"),
    14: ("2-magnetostatics/14-faradays-law-and-induced-emf", "Faraday's law and induced emf"),
    15: ("2-magnetostatics/15-inductance-magnetic-energy-and-the-potentials", "Inductance, magnetic energy and the potentials"),
    16: ("3-maxwell-and-waves/16-charge-conservation-displacement-current-and-maxwells-equations", "Charge conservation, displacement current and Maxwell's equations"),
    17: ("3-maxwell-and-waves/17-magnetization-and-maxwells-equations-in-matter", "Magnetization and Maxwell's equations in matter"),
    18: ("3-maxwell-and-waves/18-the-wave-equation-and-plane-tem-waves", "The wave equation and plane TEM waves"),
    19: ("3-maxwell-and-waves/19-dalembert-solutions-and-radiation-from-current-sheets", "d'Alembert solutions and radiation from current sheets"),
}
UNIT_INDEXES = ["1-electrostatics/index.md", "2-magnetostatics/index.md", "3-maxwell-and-waves/index.md"]
LEVELS = ["easy", "medium", "hard"]
EXPECT = {L: (5, 3, 4) for L in LECTURES}
EXPECT[11] = (4, 2, 2)

# ------------------------------------------------------------------ topics
TYPES = [("mc", "Quick checks: multiple choice and true or false"), ("fte", "Find the error")]
TOPICS = [
    ("coulomb", "Coulomb's law and point charges"),
    ("fivestep", "Continuous charge and the five-step program"),
    ("superposition", "Superposition"),
    ("gauss", "Gauss's law and flux"),
    ("symmetry", "Planar, cylindrical and spherical symmetry"),
    ("divcurl", "Divergence, curl and the integral theorems"),
    ("continuity", "Continuity, relaxation and displacement current"),
    ("potential", "Potential, work and the energy of charges"),
    ("circulation", "Circulation and Kirchhoff's voltage law"),
    ("bc", "Boundary conditions and refraction"),
    ("laplace", "Poisson's and Laplace's equations"),
    ("conductors", "Conductors, current and resistance"),
    ("polarization", "Polarization and bound charge"),
    ("dielectrics", "Fields in dielectric media"),
    ("capacitance", "Capacitance, stored energy and force"),
    ("conductance", "Conductance and lossy capacitors"),
    ("drude", "Drude and Lorentz models"),
    ("lorentzforce", "Magnetic force and charged particles"),
    ("biotsavart", "The Biot–Savart law"),
    ("ampere", "Ampère's law and current density"),
    ("sheets", "Current sheets, slabs, solenoids and toroids"),
    ("vecpot", "Vector potential, potentials and gauge"),
    ("dipole", "Current loops and the magnetic dipole"),
    ("faraday", "Magnetic flux, Faraday's law and Lenz"),
    ("motional", "Motional emf and generators"),
    ("induced", "Induced electric field and voltmeters"),
    ("inductance", "Inductance"),
    ("magenergy", "Magnetic energy and RL circuits"),
    ("magmedia", "Magnetization and magnetic media"),
    ("waves", "Plane waves and the wave equation"),
    ("radiation", "Current-sheet radiation and the Poynting vector"),
]
TOPIC_TITLE = dict(TYPES + TOPICS)

# tag -> list of topic keys, or (key, first lecture, last lecture) for lecture-dependent meaning
RULES = {
    "Coulomb's law": ["coulomb"], "Coulomb force": ["coulomb"], "vectors": ["coulomb"],
    "point charge": ["coulomb"], "point charges": ["coulomb"], "null point": ["coulomb", "superposition"],
    "dipole": ["coulomb"],
    "five-step program": ["fivestep"], "ring": ["fivestep"], "disk": ["fivestep"], "disk on axis": ["fivestep"],
    "finite line": ["fivestep"], "limits": ["fivestep"],
    "superposition": ["superposition"], "scalar superposition": ["superposition", "potential"],
    "null points": ["superposition"],
    "Gauss's law": ["gauss"], "Gauss's law for D": ["gauss", "dielectrics"], "flux": ["gauss"],
    "enclosed charge": ["gauss"], "closed surfaces": ["gauss"], "solid angle": ["gauss"],
    "surface normal": ["gauss"], "symmetry": ["gauss"],
    "delta functions": [("gauss", 1, 11), ("ampere", 12, 99)],
    "magnetic flux": [("gauss", 1, 11), ("faraday", 12, 99)],
    "planar symmetry": ["symmetry"], "cylindrical symmetry": ["symmetry"], "spherical symmetry": ["symmetry"],
    "spherical geometry": ["symmetry"], "charge sheets": ["symmetry"], "charged sheets": ["symmetry"],
    "slabs": ["symmetry"], "charge slabs": ["symmetry"], "graded density": ["symmetry"],
    "divergence": ["divcurl"], "curl": ["divcurl"], "divergence theorem": ["divcurl"],
    "Stokes' theorem": ["divcurl"], "curvilinear coordinates": ["divcurl"], "spherical coordinates": ["divcurl"],
    "divergence of B": ["divcurl"], "cylindrical coordinates": [("divcurl", 1, 4)],
    "continuity": ["continuity"], "relaxation time": ["continuity"], "displacement current": ["continuity"],
    "potential": ["potential"], "potential difference": ["potential"], "V from E": ["potential"],
    "gradient": ["potential"], "equipotentials": ["potential"], "electron-volts": ["potential"],
    "energy of charges": ["potential"], "reference point": ["potential"], "exact differentials": ["potential"],
    "path independence": ["potential", "circulation"], "path dependence": ["potential", "circulation"],
    "scaling": ["potential"],
    "circulation": ["circulation"], "KVL": ["circulation"],
    "voltmeters": [("circulation", 1, 13), ("induced", 14, 99)],
    "boundary conditions": ["bc"], "magnetic boundary conditions": ["bc"], "oblique interface": ["bc"],
    "cylindrical interface": ["bc"], "dielectric interface": ["bc"], "interface charge": ["bc"],
    "surface charge": ["bc"], "matching conditions": ["bc", "laplace"], "refraction": ["bc", "dielectrics"],
    "current sheet": ["bc", "sheets"],
    "Poisson's equation": ["laplace"], "Laplace's equation": ["laplace"], "piecewise Laplace": ["laplace"],
    "uniqueness": ["laplace"], "space charge": ["laplace"], "vacuum diode": ["laplace"], "pn junction": ["laplace"],
    "inhomogeneous media": ["laplace", "dielectrics"],
    "conductors": ["conductors"], "induced charge": ["conductors"], "Ohm's law": ["conductors"],
    "resistance": ["conductors"], "radial current": ["conductors"],
    "bound charge": ["polarization"], "susceptibility": ["polarization"], "electret": ["polarization"],
    "D-first chain": ["dielectrics"], "layered dielectrics": ["dielectrics"],
    "side-by-side dielectrics": ["dielectrics"], "graded permittivity": ["dielectrics"],
    "dielectric insertion": ["dielectrics", "capacitance"],
    "capacitance": ["capacitance"], "coax and spheres": ["capacitance"], "series capacitance": ["capacitance"],
    "series and parallel": ["capacitance"], "energy density": ["capacitance"],
    "fixed charge vs fixed voltage": ["capacitance"], "small-signal capacitance": ["capacitance"],
    "diode": ["capacitance"],
    "energy": [("capacitance", 1, 11), ("motional", 14, 14), ("magenergy", 15, 99)],
    "force": [("capacitance", 1, 11), ("lorentzforce", 12, 99)],
    "conductance": ["conductance"], "RC self-discharge": ["conductance"], "RC transients": ["conductance"],
    "transients": [("conductance", 1, 11), ("magenergy", 12, 99)],
    "Drude model": ["drude"], "Lorentz model": ["drude"], "mobility": ["drude"], "conductivity": ["drude"],
    "AC conductivity": ["drude"], "phasors": ["drude"], "plasma oscillation": ["drude"],
    "several species": ["drude"], "drift velocity": ["drude"], "polarization current": ["drude"],
    "current density": [("drude", 1, 11), ("ampere", 12, 99)],
    "Lorentz force": ["lorentzforce"], "velocity selector": ["lorentzforce"], "mass spectrometer": ["lorentzforce"],
    "circular motion": ["lorentzforce"], "magnetic force": ["lorentzforce"], "force between wires": ["lorentzforce"],
    "right-hand rule": ["lorentzforce"], "Newton's third law": ["lorentzforce"],
    "nonuniform field": [("lorentzforce", 12, 12), ("motional", 14, 14)],
    "Biot–Savart": ["biotsavart"],
    "Ampère's law": ["ampere"], "enclosed current": ["ampere"], "uniform field": ["ampere"],
    "coaxial cable": [("ampere", 12, 99)],
    "current sheets": ["sheets"], "current slab": ["sheets"], "current slabs": ["sheets"],
    "finite solenoid": ["sheets", "dipole"], "sheets and solenoids": ["sheets"], "cross product": ["sheets"],
    "solenoid": [("sheets", 1, 14), ("inductance", 15, 99)], "toroid": [("sheets", 1, 14), ("inductance", 15, 99)],
    "vector potential": ["vecpot"], "gauge": ["vecpot"], "potentials": ["vecpot"],
    "magnetic dipole": ["dipole"], "current loop": ["dipole"], "Helmholtz coils": ["dipole"],
    "Faraday's law": ["faraday"], "Lenz": ["faraday"], "transformer emf": ["faraday", "induced"],
    "motional emf": ["motional"], "generator": ["motional"], "rotating rod": ["motional"],
    "induced field": ["induced"],
    "inductance": ["inductance"], "mutual inductance": ["inductance"], "internal inductance": ["inductance"],
    "two-wire line": ["inductance"], "LC product": ["inductance"],
    "magnetic energy": ["magenergy"], "RL circuit": ["magenergy"], "RL decay": ["magenergy"], "power": ["magenergy"],
    "magnetization": ["magmedia"], "magnetization current": ["magmedia"], "permeability": ["magmedia"],
    "hysteresis": ["magmedia"],
    "plane waves": ["waves"], "wave equation": ["waves"], "intrinsic impedance": ["waves"],
    "moving pulses": ["waves"],
    "current sheet radiation": ["radiation"], "Poynting vector": ["radiation"], "wave parameters": ["waves"],
    "multiple choice": ["mc"], "true or false": ["mc"], "find the error": ["fte"],
}
# geometry words that carry no topic of their own (the problem's other tags place it)
IGNORE = {"parallel plates", "coax", "spheres", "coaxial cable"}

# concept page -> topics whose problems it should point to
CONCEPT_TOPICS = {
    "amperes-law": ["ampere"], "biot-savart-law": ["biotsavart"], "boundary-conditions": ["bc"],
    "capacitance": ["capacitance"], "conductance": ["conductance"],
    "conductivity-and-susceptibility-models": ["drude"], "conductors": ["conductors"],
    "conservative-field": ["circulation"], "continuity-equation": ["continuity"], "coulombs-law": ["coulomb"],
    "curl": ["divcurl"], "displacement-current": ["continuity"], "divergence-theorem": ["divcurl"],
    "divergence": ["divcurl"], "electric-flux-density": ["dielectrics"], "electromotive-force": ["faraday", "motional"],
    "electrostatic-energy": ["capacitance"], "electrostatic-potential": ["potential"], "faradays-law": ["faraday"],
    "five-step-recipe": ["fivestep"], "flux": ["gauss"], "gauss-law": ["gauss"], "inductance": ["inductance"],
    "lorentz-force": ["lorentzforce"], "magnetic-energy": ["magenergy"], "magnetic-flux": ["faraday"],
    "maxwells-equations": ["divcurl"], "permittivity": ["dielectrics"], "poissons-equation": ["laplace"],
    "polarization": ["polarization"], "stokes-theorem": ["divcurl"], "superposition": ["superposition"],
    "vector-potential": ["vecpot"],
    "magnetization": ["magmedia"], "permeability": ["magmedia"],
    "plane-waves": ["waves"], "wave-equation": ["waves"], "intrinsic-impedance": ["waves"],
    "current-sheet-radiation": ["radiation"], "poynting-vector": ["radiation"],
}

# lecture to draw a concept page's example problems from (default: where its topic has most problems)
CONCEPT_HOME = {"superposition": 3, "stokes-theorem": 4, "maxwells-equations": 4}

EXAM_RE = re.compile(r"(SP18 Exam \d #[0-9a-z()]+|Summer 20\d\d HE\d(?: \(conflict\))? #[0-9a-z()–-]+|FA26 Exam 1 #[0-9a-z(),–-]+)")


def gh_slug(s):
    s = s.lower()
    out = []
    for ch in s:
        if ch == " ":
            out.append("-")
        elif ch in "-_":
            out.append(ch)
        elif unicodedata.category(ch)[0] in ("L", "N") or unicodedata.category(ch) in ("Mn", "Mc"):
            out.append(ch)
    return "".join(out)


HEAD_RE = re.compile(r"^### (\d+)\.(\d+) (.+?)\s*$")
DIFF_RE = re.compile(r"^> \[!(easy|medium|hard)\] (Easy|Medium|Hard)((?: · [^·]+?)+)\s*$")
CALLOUT_RE = re.compile(r"^> \[!([a-z]+)\]([-+]?) ?(.*)$")


def parse_page(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    lines = text.split("\n")
    errs, probs = [], []
    section = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("## "):
            section = ln[3:].strip().lower()
        h = HEAD_RE.match(ln)
        if h:
            L, N, title = int(h.group(1)), int(h.group(2)), h.group(3)
            p = {"L": L, "N": N, "id": f"{L}.{N}", "title": title, "line": i + 1, "section": section,
                 "anchor": gh_slug(f"{L}.{N} {title}"), "level": None, "tags": [], "source": "", "answer": ""}
            j = i + 1
            block = []
            while j < len(lines) and not re.match(r"^#{1,3} ", lines[j]):
                block.append(lines[j]); j += 1
            nb = [b for b in block if b.strip()]
            if not nb:
                errs.append(f"{L}.{N}: empty block"); probs.append(p); i = j; continue
            d = DIFF_RE.match(nb[0])
            if not d:
                errs.append(f"{L}.{N}: first line is not a difficulty callout: {nb[0][:80]!r}")
            else:
                p["level"] = d.group(1)
                if d.group(2).lower() != d.group(1):
                    errs.append(f"{L}.{N}: callout type {d.group(1)} but title word {d.group(2)}")
                p["tags"] = [t.strip() for t in d.group(3).split(" · ") if t.strip()]
                if not 1 <= len(p["tags"]) <= 3:
                    errs.append(f"{L}.{N}: {len(p['tags'])} tags")
            seq = []
            for k, b in enumerate(block):
                c = CALLOUT_RE.match(b)
                if c:
                    seq.append((c.group(1), c.group(2), k))
            kinds = [s[0] for s in seq]
            if kinds.count("solution") != 1:
                errs.append(f"{L}.{N}: {kinds.count('solution')} solution callouts")
            if p["level"] in ("medium", "hard") and "hint" not in kinds:
                errs.append(f"{L}.{N}: no hint ({p['level']})")
            for kind, fold, _ in seq:
                if kind in ("hint", "solution") and fold != "-":
                    errs.append(f"{L}.{N}: {kind} callout not folded")
            exp_order = [p["level"]] + (["hint"] if "hint" in kinds else []) + ["solution"]
            if kinds != exp_order:
                errs.append(f"{L}.{N}: callouts {kinds}, expected {exp_order}")
            in_callout = False
            for b in block:
                if CALLOUT_RE.match(b):
                    in_callout = True; continue
                if in_callout and b.startswith(">"):
                    continue
                if in_callout and b.strip() == "":
                    in_callout = False; continue
                if in_callout:
                    errs.append(f"{L}.{N}: unprefixed line inside callout: {b[:60]!r}"); in_callout = False
                elif b.strip():
                    errs.append(f"{L}.{N}: text outside callouts: {b[:60]!r}")
            if seq:
                k0 = seq[0][2]
                k1 = seq[1][2] if len(seq) > 1 else len(block)
                stmt = [b for b in block[k0:k1] if b.startswith(">")]
                src = [b for b in stmt if b.startswith("> *Source:")]
                if not src:
                    errs.append(f"{L}.{N}: no *Source:* line")
                else:
                    p["source"] = src[-1][len("> *Source:"):].strip().rstrip("*").strip()
                    if stmt[-1] != src[-1]:
                        errs.append(f"{L}.{N}: *Source:* is not the last statement line")
            sol = [s for s in seq if s[0] == "solution"]
            if sol:
                ans = [b for b in block[sol[0][2]:] if b.startswith("> **Answer.**")]
                if not ans:
                    errs.append(f"{L}.{N}: no **Answer.** line in solution")
                p["answer"] = ans[-1] if ans else ""
            probs.append(p)
            i = j
            continue
        i += 1
    return fm, probs, errs


def topics_of(p):
    keys, unknown = [], []
    for t in p["tags"]:
        if t in IGNORE and t not in RULES:
            continue
        rule = RULES.get(t)
        if rule is None:
            if t not in IGNORE:
                unknown.append(t)
            continue
        for r in rule:
            if isinstance(r, tuple):
                k, a, b = r
                if a <= p["L"] <= b:
                    keys.append(k)
            else:
                keys.append(r)
    out = []
    for k in keys:
        if k not in out:
            out.append(k)
    return out, unknown


def load_all():
    pages = []
    for fn in sorted(os.listdir(PDIR)):
        m = re.match(r"^(\d\d)-.*\.md$", fn)
        if not m:
            continue
        L = int(m.group(1))
        fm, probs, errs = parse_page(os.path.join(PDIR, fn))
        slug = "practice/" + fn[:-3]
        if fm.get("lecture") != L:
            errs.append(f"frontmatter lecture={fm.get('lecture')} for file {fn}")
        if L not in LECTURES:
            errs.append(f"lecture {L} missing from LECTURES table")
        nums = [(p["L"], p["N"]) for p in probs]
        if nums != [(L, n) for n in range(1, len(probs) + 1)]:
            errs.append(f"numbering {nums}")
        counts = tuple(sum(1 for p in probs if p["level"] == lv) for lv in LEVELS)
        if L in EXPECT and counts != EXPECT[L]:
            errs.append(f"counts {counts}, expected {EXPECT[L]}")
        order = [LEVELS.index(p["level"]) if p["level"] in LEVELS else 9 for p in probs]
        if order != sorted(order):
            errs.append("difficulties not in easy→medium→hard order")
        for p in probs:
            if p["section"] != p["level"]:
                errs.append(f"{p['id']}: under section '{p['section']}' but tagged {p['level']}")
            p["slug"] = slug
            p["topics"], unknown = topics_of(p)
            for t in unknown:
                errs.append(f"{p['id']}: tag {t!r} has no topic rule (add it to RULES or IGNORE)")
            if not [k for k in p["topics"] if k not in ("mc", "fte")]:
                errs.append(f"{p['id']}: no subject topic (tags {p['tags']})")
            mm = EXAM_RE.search(p["source"])
            ex = mm.group(1) if mm else ""
            while ex.endswith(")") and ex.count(")") > ex.count("("):
                ex = ex[:-1]
            p["exam"] = ex.rstrip(",")
        desc = fm.get("description", "")
        mm = re.search(r"(\d+) practice problems \((\d+) easy, (\d+) medium, (\d+) hard\)", desc)
        if not mm:
            errs.append("description lacks 'N practice problems (a easy, b medium, c hard)'")
        elif (int(mm.group(1)),) + tuple(int(x) for x in mm.group(2, 3, 4)) != (len(probs),) + counts:
            errs.append(f"description counts {mm.group(0)!r} disagree with {len(probs)} {counts}")
        anchors = [p["anchor"] for p in probs]
        if len(set(anchors)) != len(anchors):
            errs.append("duplicate anchors")
        pages.append({"L": L, "file": fn, "slug": slug, "fm": fm, "probs": probs, "errs": errs, "counts": counts})
    return pages


# ------------------------------------------------------------------ generation helpers
def chip(level):
    return f'<span class="diff {level}">{level}</span>'


def plink(p, text=None, table=False):
    bar = "\\|" if table else "|"
    return f"[[{p['slug']}#{p['anchor']}{bar}{text or (p['id'] + ' ' + p['title'])}]]"


def lec_heading(L):
    return f"Lecture {L} · {LECTURES[L][1]}"


def write(path, text):
    full = os.path.join(SRC, path)
    old = open(full, encoding="utf-8").read() if os.path.exists(full) else None
    if old != text:
        with open(full, "w", encoding="utf-8") as f:
            f.write(text)
        print("  wrote", path)


NAV = ("*[[practice/index|Practice hub]] · by difficulty: {e} · {m} · {h} · [[practice/topics|by topic]]*")


def nav(current=None):
    def one(lv):
        return chip(lv) if lv == current else f"[[practice/{lv}|{lv}]]"
    return NAV.format(e=one("easy"), m=one("medium"), h=one("hard"))


RUBRIC = {
    "easy": "one law or definition and at most two steps: a plug-in with understanding, a direct symmetry argument, a units or direction question, or a conceptual multiple-choice item",
    "medium": "a standard exam sub-problem: one modelling decision (which surface, path, coordinates or region), a real integral, or a three- or four-step chain",
    "hard": "exam length, in several parts: superposition of several pieces, several regions with matching conditions, a non-trivial integral, a sign-heavy direction analysis, or two lectures combined",
}
TIME = {"easy": "2–5 min", "medium": "8–15 min", "hard": "20–40 min"}


def gen_level_page(pages, level):
    allp = [p for pg in pages for p in pg["probs"] if p["level"] == level]
    n = len(allp)
    Ls = [pg["L"] for pg in pages]
    out = ["---",
           f'title: "{level.capitalize()} problems"',
           f'description: "All {n} {level} practice problems for Lectures {Ls[0]}–{Ls[-1]}, by lecture. {level.capitalize()} = {RUBRIC[level].split(":")[0]}; about {TIME[level]} each."',
           "tags: [practice]", "---", "", nav(level), ""]
    intro = {
        "easy": "Start here. These build the reflexes the longer problems rely on, and they are the right first pass right after reading a lecture — or a warm-up the night before an exam.",
        "medium": "Each of these is the size of one part of an exam problem. The hint names the modelling decision; try to make it yourself first.",
        "hard": "Budget the time, write the setup before computing, and do the *Check* at the end — that habit is worth points. Problems marked *modelled on* follow a past ECE 329 exam problem with the numbers and at least one detail changed.",
    }[level]
    out += [f"**{level.capitalize()}** ({TIME[level]}): {RUBRIC[level]}. {intro}", ""]
    for pg in pages:
        ps = [p for p in pg["probs"] if p["level"] == level]
        if not ps:
            continue
        out += [f"## {lec_heading(pg['L'])}", ""]
        for p in ps:
            line = f"- {plink(p)} — {' · '.join(p['tags'])}"
            if p["exam"]:
                line += f" · *modelled on {p['exam']}*"
            out.append(line)
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def gen_topics_page(pages):
    allp = [p for pg in pages for p in pg["probs"]]
    by = collections.OrderedDict((k, []) for k, _ in TYPES + TOPICS)
    for p in allp:
        for k in p["topics"]:
            by[k].append(p)
    out = ["---", 'title: "Problems by topic"',
           f'description: "The {len(allp)} practice problems grouped by topic across lectures: follow one idea from its first appearance to exam level. Also the quick multiple-choice and true-or-false checks, and the find-the-error items."',
           "tags: [practice]", "---", "", nav(), "",
           "Topics cut across lectures: superposition is the same move in Lecture 2 (point charges), Lecture 3 (slabs and sheets) and Lecture 13 (current sheets); boundary conditions return with every new field. Each problem is listed under every topic its tags belong to, in course order, with its level.", ""]
    for k, title in TYPES + TOPICS:
        ps = by[k]
        if not ps:
            continue
        out += [f"## {title}", ""]
        if k == "mc":
            out += ["Two-minute concept checks — every wrong option is explained in the solution. Good for a quick self-test.", ""]
        elif k == "fte":
            out += ["A short student solution with one classic slip (a sign, a missing ε, a wrong normal, a wrong surface). Spotting it is the skill that saves points on an exam.", ""]
        for p in ps:
            out.append(f"- {plink(p)} {chip(p['level'])}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def gen_hub(pages):
    allp = [p for pg in pages for p in pg["probs"]]
    tot = len(allp)
    c = {lv: sum(1 for p in allp if p["level"] == lv) for lv in LEVELS}
    Ls = [pg["L"] for pg in pages]
    exams = [p for p in allp if p["exam"]]
    out = ["---", 'title: "Practice problems"',
           f'description: "{tot} practice problems for Lectures {Ls[0]}–{Ls[-1]} — {c["easy"]} easy, {c["medium"]} medium, {c["hard"]} hard — each with a folded hint and a worked solution, and every answer checked numerically twice. Browse by lecture, by difficulty or by topic."',
           "tags: [practice]", "---", "",
           f"Understanding a lecture and being able to *do* its problems are different skills, and only the second one is tested. This bank has **{tot} problems for Lectures {Ls[0]}–{Ls[-1]}**: short drills that build confidence, standard exam sub-problems, and full exam-length problems. {len(exams)} of them are modelled on past ECE 329 exams, with the numbers and a detail changed.",
           "",
           "> [!recipe] How to use the bank",
           "> 1. Pick a lecture you have read and do its **easy** problems first — a few minutes each, one idea per problem.",
           "> 2. Work on paper. Open the **hint** only after you have been stuck for a few minutes, and the **solution** only once you have an answer you would hand in.",
           "> 3. Compare with the **Answer.** line, then read the solution's *Check* step: it shows how to catch your own mistakes (units, a limit, a symmetry, a second route).",
           "> 4. Move on to **medium** (one modelling decision), then **hard** (exam length, several parts).",
           "> 5. A day later, redo every problem you got wrong, without looking.",
           "",
           "> [!tip] If you are behind",
           "> Go lecture by lecture: read the lecture's *key* and *recipe* boxes, then do its easy problems and one medium — about forty minutes per lecture. Leave the hard problems for a second pass before the exam, starting with the ones [[practice/index#modelled-on-past-exams|modelled on past exams]].",
           "",
           "## The tag system",
           "",
           "Every problem's title bar carries one **difficulty tag** and one to three **topic tags**, for example",
           "",
           "> [!easy] Easy · Gauss's law · charge sheets · superposition",
           "> The problem statement sits in this box; the folded *Hint* and *Solution* boxes below it open with a click.",
           "",
           "| difficulty | what it means | time |",
           "|---|---|---|"]
    for lv in LEVELS:
        out.append(f"| {chip(lv)} | {RUBRIC[lv]} | {TIME[lv]} |")
    out += ["",
            f"Browse: [[practice/easy|all {c['easy']} easy]] · [[practice/medium|all {c['medium']} medium]] · [[practice/hard|all {c['hard']} hard]] · [[practice/topics|by topic]] — {len(TOPICS)} topics that cut across lectures, plus the quick multiple-choice checks and the find-the-error items.",
            "",
            "## By lecture",
            "",
            "| L | lecture | practice | easy | medium | hard |",
            "|---|---|---|---|---|---|"]
    for pg in pages:
        L = pg["L"]
        sec = gh_slug(lec_heading(L))
        e, m, h = pg["counts"]
        out.append(f"| {L} | [[{LECTURES[L][0]}\\|{LECTURES[L][1]}]] | [[{pg['slug']}\\|{len(pg['probs'])} problems]] | "
                   f"[[practice/easy#{sec}\\|{e}]] | [[practice/medium#{sec}\\|{m}]] | [[practice/hard#{sec}\\|{h}]] |")
    out.append(f"| | **total** | **{tot}** | **{c['easy']}** | **{c['medium']}** | **{c['hard']}** |")
    out += ["",
            "Exam 1 covered Lectures 1–10. Lecture 1 has no practice page: its content (fields defined by force, the Maxwell roadmap) is exercised from Lecture 2 on.",
            "",
            "## Modelled on past exams",
            "",
            "These follow a past ECE 329 exam problem (Spring 2018 midterms, Summer 2017–2020 hour exams, Fall 2026 Exam 1) with new numbers and at least one changed detail, so the official keys do not apply — work them as exam practice. The full source note is on each problem's last line.",
            "",
            "| problem | level | modelled on |",
            "|---|---|---|"]
    for p in exams:
        out.append(f"| {plink(p, table=True)} | {chip(p['level'])} | {p['exam']} |")
    out += ["",
            "## How the answers were checked",
            "",
            "Each page was written together with a numerical script (numpy and scipy) that prints every number, sign and direction in its answers: brute-force integrals, finite-difference divergences and curls, explicit cross products, integrated circuit equations. A second reviewer then re-solved every problem from its statement alone, with a separate script — more than 2,500 comparisons in all — and tightened what it found: a few hints, distractor explanations and statements, and the problems that had kept a past exam's numbers. Problems changed in review were checked once more by a third pass.",
            "",
            "Notation follows the rest of the site ([[index#conventions-used-throughout|conventions]]). Problem sources are original problems, textbook classics reworded, course-notes examples with new numbers, and past exams re-parameterized; each problem names its source on its last line.",
            ""]
    return "\n".join(out).rstrip() + "\n"


# ------------------------------------------------------------------ link injection
def inject_lecture_pages(pages):
    for pg in pages:
        L = pg["L"]
        path = LECTURES[L][0] + ".md"
        full = os.path.join(SRC, path)
        text = open(full, encoding="utf-8").read()
        lines = text.split("\n")
        n = len(pg["probs"])
        e, m, h = pg["counts"]
        first = pg["probs"][0]
        # header line: "*Lecture N · ... *"
        for i, ln in enumerate(lines):
            if ln.startswith(f"*Lecture {L} ·"):
                ln = re.sub(r" · practice: \[\[practice/[^\]]+\]\]", "", ln)
                assert ln.endswith("*"), path
                lines[i] = ln[:-1] + f" · practice: [[{pg['slug']}|{n} problems]]*"
                break
        else:
            raise SystemExit(f"no header line in {path}")
        text = "\n".join(lines)
        # footer callout before "### Sources for this page"
        text = re.sub(r"\n> \[!tip\] Practice this lecture\n(?:>.*\n)*\n", "\n", text)
        block = ("> [!tip] Practice this lecture\n"
                 f"> [[{pg['slug']}|{n} practice problems]] — {e} easy, {m} medium, {h} hard — each with a folded hint and a worked solution. "
                 f"Start with {plink(first)}; the [[practice/index|practice hub]] has the whole bank by difficulty and by topic.\n\n")
        k = text.find("### Sources for this page")
        if k < 0:
            text = text.rstrip("\n") + "\n\n" + block.rstrip("\n") + "\n"
        else:
            text = text[:k] + block + text[k:]
        write(path, text)


def inject_unit_indexes(pages):
    byL = {pg["L"]: pg for pg in pages}
    for path in UNIT_INDEXES:
        full = os.path.join(SRC, path)
        lines = open(full, encoding="utf-8").read().split("\n")
        for i, ln in enumerate(lines):
            if ln.startswith("| # | page | one line |"):
                if not ln.rstrip().endswith("practice |"):
                    lines[i] = ln.rstrip() + " practice |"
                    lines[i + 1] = lines[i + 1].rstrip() + "---|"
                j = i + 2
                while j < len(lines) and lines[j].startswith("| "):
                    row = re.sub(r" (\[\[practice/[^\]]*\]\]|—) \|$", "", lines[j].rstrip())
                    if row == lines[j].rstrip():  # no practice cell yet
                        pass
                    mm = re.match(r"^\| (\d+) \|", row)
                    L = int(mm.group(1)) if mm else None
                    cell = f"[[{byL[L]['slug']}\\|{len(byL[L]['probs'])} problems]]" if L in byL else "—"
                    lines[j] = row + f" {cell} |"
                    j += 1
                break
        write(path, "\n".join(lines))


def inject_concepts(pages):
    allp = [p for pg in pages for p in pg["probs"]]
    for concept, keys in CONCEPT_TOPICS.items():
        path = f"concepts/{concept}.md"
        full = os.path.join(SRC, path)
        if not os.path.exists(full):
            print("  WARN missing concept page", path); continue
        text = open(full, encoding="utf-8").read()
        lines = [ln for ln in text.rstrip("\n").split("\n") if not ln.startswith("**Practice.**")]
        while lines and lines[-1] == "" and len(lines) > 1 and lines[-2] == "":
            lines.pop()
        ps = [p for p in allp if set(p["topics"]) & set(keys)]
        if not ps:
            continue
        tl = " · ".join(f"[[practice/topics#{gh_slug(TOPIC_TITLE[k])}|{TOPIC_TITLE[k]}]] ({sum(1 for p in allp if k in p['topics'])} problems)" for k in keys)
        # examples: one per level, taken from the lecture where the first topic has most problems
        home = CONCEPT_HOME.get(concept) or collections.Counter(
            p["L"] for p in allp if keys[0] in p["topics"]).most_common(1)[0][0]
        ex = []
        for lv in LEVELS:
            q = [p for p in ps if p["level"] == lv]
            if q:
                q.sort(key=lambda p: (abs(p["L"] - home), p["L"], p["N"]))
                ex.append(f"{plink(q[0])} ({lv})")
        line = f"**Practice.** {tl} — for example " + ", ".join(ex) + "."
        # insert before the "Related:" line (last such line), else at the end
        idx = max((i for i, ln in enumerate(lines) if ln.startswith("Related:")), default=None)
        if idx is None:
            lines += ["", line]
        else:
            # keep exactly one blank line between the practice line and Related
            ins = idx
            lines[ins:ins] = [line, ""]
        new = "\n".join(lines) + "\n"
        new = re.sub(r"\n{3,}", "\n\n", new)
        write(path, new)


def inject_practice_pages(pages):
    for i, pg in enumerate(pages):
        path = pg["slug"] + ".md"
        full = os.path.join(SRC, path)
        text = open(full, encoding="utf-8").read()
        lines = text.rstrip("\n").split("\n")
        # header nav line: make sure "by topic" is present
        for k, ln in enumerate(lines):
            if ln.startswith("*Practice for ") and "[[practice/topics" not in ln:
                lines[k] = ln[:-1] + " · [[practice/topics|by topic]]*"
                break
        # footer: previous / next practice pages
        while lines and (lines[-1].startswith("*Previous:") or lines[-1].startswith("*Next:") or lines[-1] == ""):
            lines.pop()
        parts = []
        if i > 0:
            parts.append(f"Previous: [[{pages[i-1]['slug']}|Lecture {pages[i-1]['L']} practice]]")
        if i + 1 < len(pages):
            parts.append(f"{'next' if parts else 'Next'}: [[{pages[i+1]['slug']}|Lecture {pages[i+1]['L']} practice]]")
        parts.append("[[practice/index|all practice]]")
        lines += ["", "*" + " · ".join(parts) + "*"]
        write(path, "\n".join(lines) + "\n")


if __name__ == "__main__":
    pages = load_all()
    total = bad = 0
    for pg in pages:
        total += len(pg["probs"])
        print(f"L{pg['L']:02d} {pg['file']:<58} {len(pg['probs']):>2} {pg['counts']}  errors={len(pg['errs'])}")
        for e in pg["errs"]:
            print("    ERR", e); bad += 1
    print("problems:", total, "errors:", bad)
    if "--write" in sys.argv:
        if bad:
            sys.exit("not writing: fix the errors first")
        write("practice/index.md", gen_hub(pages))
        for lv in LEVELS:
            write(f"practice/{lv}.md", gen_level_page(pages, lv))
        write("practice/topics.md", gen_topics_page(pages))
        inject_practice_pages(pages)
        inject_lecture_pages(pages)
        inject_unit_indexes(pages)
        inject_concepts(pages)
        cnt = collections.Counter(k for pg in pages for p in pg["probs"] for k in p["topics"])
        print("topics:", ", ".join(f"{k}={cnt[k]}" for k, _ in TYPES + TOPICS))
