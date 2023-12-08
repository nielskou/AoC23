"""
från matematik importera lcm som minsta_gemensamma_multipel
från itertools importera cycle som igenom
från functools importera reduce som reducera

sekvens, _, *regler = öppna("day8.txt")
sekvens = sekvens.strip()
vänster = {mening[:3]: mening[7:10] för mening i regler}
höger = {mening[:3]: mening[12:15] för mening i regler}
gå = {"L": vänster, "R": höger}


def sök(här, slut):
    för steg, sväng i räknaupp(igenom(sekvens), 1):
        här = gå[sväng][här]
        om här.slutarmed(slut):
            getillbaka steg

# del 1
skriv(sök("AAA", "ZZZ"))

# del 2
spöke_början = [plats för plats i höger om plats.slutarmed("A")]
spöke_steg = [sök(början, "Z") för början i spöke_början]
samtidigt = reducera(minsta_gemensamma_multipel, spöke_steg)
skriv(samtidigt)
"""
import re

code = __doc__
for sv, en in (('från', 'from'), ('importera', 'import'), ('matematik', 'math'),
    ('som', 'as'), ('skriv', 'print'), ('i', 'in'), ('för', 'for'),
    ('öppna', 'open'), ("räknaupp", "enumerate"), ("slutarmed", "endswith"),
    ("getillbaka", "return"), ("om", "if")):
    code = re.sub(fr"\b{sv}\b", en, code)

#print(code)
exec(code)
exit()
