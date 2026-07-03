#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLAN FINANCIER — scénario opérationnel du commanditaire (03/07/2026) :
- Offre : 5 000 € setup + 15 % du cash incrémental encaissé (pas de mensualité)
- Thèse de service : client 5-10 K€/mois → 25-35 K€/mois MINIMUM en ~4 mois (×3-4)
- Moteur : pub vidéo 1 000 €/jour (YT/Google/LinkedIn/IG), 6-8 calls/jour
- Capacité : 300 clients simultanés ; engagement 12 mois
Sortie : findings/ws-finance-plan.md
"""

OUT = []
def p(s=""): OUT.append(s)
def fmt(x, u=" €"): return f"{x:,.0f}".replace(",", " ") + u

# ---------- Paramètres ----------
SETUP = 5_000
RATE = 0.15
RAMP = [0.25, 0.50, 0.75] + [1.0] * 9          # plateau atteint M4 (thèse : ~4 mois)
PLATEAU_LOW, PLATEAU_HIGH = 20_000, 25_000      # incrément mensuel : 5→25K et 10→35K
COLLECT = (0.70, 0.85, 1.00)
ADS_MONTH = 1_000 * 365 / 12
CALLS_M = (182, 213, 243)                       # 6/7/8 par jour
SHOW = (0.70, 0.75, 0.85)
CLOSE = (0.20, 0.25, 0.32)                      # 5K seul à l'entrée : friction minimale
CAPACITY = 300
COACH_RATIO = 15
COACH_COST = 70_000
SALES_COM = 0.10

def incr_year(plateau, months=12):
    return plateau * sum(RAMP[:months])

def client_year1(plateau, collect):
    return SETUP + RATE * incr_year(plateau) * collect

p("# PLAN FINANCIER — offre 5 K€ + 15 %, thèse ×3-4 en 4 mois")
p()
p("## F0 — Paramètres et statut des hypothèses")
p()
p("| Paramètre | Valeur | Statut |")
p("|---|---|---|")
p(f"| Offre | {fmt(SETUP)} setup + 15 % du cash incrémental encaissé | Décision commanditaire |")
p(f"| Trajectoire client | 5-10 K€/mois → 25-35 K€/mois en ~4 mois (plateau M4) | **Thèse opérationnelle du commanditaire** (étude interne + expérience) — à démontrer publiquement sur les 5-10 premiers clients |")
p(f"| Incrément mensuel au plateau | +20 K€ (5→25) à +25 K€ (10→35) | Dérivé de la thèse |")
p(f"| Collecte effective du 15 % | 70 / 85 / 100 % | Fourchette prudente (mécanique d'attribution §6.7) |")
p(f"| Moteur | {fmt(ADS_MONTH)}/mois de pub, 6-8 calls/jour, close 20-32 % | Plan média commanditaire + benchmarks §9 |")
p(f"| Capacité | {CAPACITY} clients simultanés, 12 mois d'engagement | Dimensionnement équipe commanditaire |")
p()

# ---------- F1 : économie par client ----------
p("## F1 — Ce que rapporte UN client (année 1 = setup + 15 % sur l'incrément)")
p()
p("| Trajectoire | Cash incrémental client an 1 | Perf 15 % (collecte 85 %) | Total agence an 1 | Année 2 si renouvellement (perf seule) |")
p("|---|---|---|---|---|")
for plateau, label in [(PLATEAU_LOW, "5 K → 25 K€/mois"), (PLATEAU_HIGH, "10 K → 35 K€/mois")]:
    inc = incr_year(plateau)
    perf = RATE * inc * 0.85
    ren = RATE * plateau * 12 * 0.85
    p(f"| {label} | {fmt(inc)} | {fmt(perf)} | **{fmt(SETUP + perf)}** | {fmt(ren)} |")
p()
lo = client_year1(PLATEAU_LOW, 0.85); hi = client_year1(PLATEAU_HIGH, 0.85)
lo100 = client_year1(PLATEAU_LOW, 1.0); hi100 = client_year1(PLATEAU_HIGH, 1.0)
p(f"→ Un client qui suit la thèse rapporte **{fmt(lo)}-{fmt(hi)}/an** (collecte 85 %) et {fmt(lo100)}-{fmt(hi100)} à collecte parfaite —")
p(f"   cohérent avec le rendement de 44 K€ HT/an de l'étude interne du commanditaire (borne haute, bonne collecte).")
p(f"   Et le CLIENT y gagne massivement : il encaisse {fmt(incr_year(PLATEAU_LOW))}-{fmt(incr_year(PLATEAU_HIGH))} de plus en payant {fmt(lo)}-{fmt(hi)} → ROI client de +550 à +580 %.")
p("   C'est l'alignement parfait : notre revenu est une FRACTION de la valeur créée, jamais un pari du client.")
p()

# ---------- F2 : funnel ----------
p("## F2 — Le moteur d'acquisition (1 K€/jour)")
p()
p("| Scénario | Calls/mois | Coût/call | Tenus | Signatures/mois | CAC |")
p("|---|---|---|---|---|---|")
signs = []
for i, name in enumerate(["bas", "central", "haut"]):
    held = CALLS_M[i] * SHOW[i]
    s = held * CLOSE[i]
    signs.append(s)
    p(f"| {name} | {CALLS_M[i]} | {fmt(ADS_MONTH/CALLS_M[i])} | {held:.0f} | **{s:.0f}** | {fmt(ADS_MONTH/s)} |")
p()
p(f"- Le setup à {fmt(SETUP)} rembourse le CAC dès la signature (CAC {fmt(ADS_MONTH/signs[1])} central) : **l'acquisition s'autofinance client par client, dès le jour 1.**")
p(f"- LTV/CAC : {fmt(lo)}-{fmt(hi)} / {fmt(ADS_MONTH/signs[1])} ≈ **{lo/(ADS_MONTH/signs[1]):.0f}-{hi/(ADS_MONTH/signs[1]):.0f}×** en thèse pleine ; encore {19_200/(ADS_MONTH/signs[0]):.0f}× dans le pire cas de F4.")
p(f"- Régime soutenable à 300 actifs : 25 signatures/mois ; le funnel central en produit {signs[1]:.0f} → sur-remplissage = pouvoir de sélection (on choisit les baselines les plus saines, ce qui PROTÈGE la thèse de quadruplement).")
p()

# ---------- F3 : trajectoire & cash-flow ----------
p("## F3 — Trajectoire de revenus et cash-flow (24 mois)")
p()
inflow_prudent = [5,8,10,12,15,18,20,22,25,25,25,25] + [25]*12
inflow_vol =     [10,15,20,25,28,30,30,30,30,30,30,30] + [25]*12

def run(inflow, collect=0.85, achieve=1.0, plateau=22_500):
    """Simulation mensuelle : cohortes, perf selon ramp, setups. achieve = part de clients qui suivent la thèse ;
    les autres : 50 % partiels (+8K plateau), 50 % échec (churn M4, +2K)."""
    months = len(inflow)
    rev = []
    actives_hist = []
    for m in range(months):
        setup_rev = min(inflow[m], 40) * SETUP
        perf = 0.0
        actives = 0
        for c in range(m + 1):
            age = m - c
            n = inflow[c]
            if age < 12:
                actives += n
                full = n * achieve
                part = n * (1 - achieve) * 0.5
                fail = n * (1 - achieve) * 0.5
                r = RAMP[age]
                perf += full * plateau * r * RATE * collect
                perf += part * 8_000 * r * RATE * collect
                if age < 4:
                    perf += fail * 2_000 * r * RATE * collect
        rev.append(setup_rev + perf)
        actives_hist.append(min(actives, CAPACITY))
    return rev, actives_hist

for name, inflow in [("prudent", inflow_prudent), ("volontariste", inflow_vol)]:
    rev, act = run(inflow)
    p(f"**Ramp {name}** (signatures {inflow[0]}→{inflow[11]}/mois) — thèse pleine, collecte 85 %, plateau moyen +22,5 K€ :")
    p()
    p("| | M3 | M6 | M9 | M12 | M18 | M24 |")
    p("|---|---|---|---|---|---|---|")
    idx = [2, 5, 8, 11, 17, 23]
    p("| Clients actifs | " + " | ".join(f"{act[i]:.0f}" for i in idx) + " |")
    p("| Revenu du mois | " + " | ".join(fmt(rev[i]) for i in idx) + " |")
    p(f"| CA cumulé an 1 : **{fmt(sum(rev[:12]))}** — an 2 : **{fmt(sum(rev[12:24]))}** | | | | | | |")
    p()
p("Lecture cash : dès M2-M3, la perf des premières cohortes s'ajoute aux setups ; le point mort opérationnel")
p(f"(pub {fmt(ADS_MONTH)}/mois + équipe initiale) est franchi vers M2-M4 selon le ramp — le modèle est AUTOFINANCÉ passé l'amorçage.")
p()

# ---------- F4 : robustesse ----------
p("## F4 — LE TEST DE ROBUSTESSE (la section pour les associés sceptiques)")
p()
p("Question : que se passe-t-il si la thèse de quadruplement ne se réalise QUE partiellement ?")
p("Hypothèses dégradées : les clients hors-thèse se répartissent 50 % « partiels » (+8 K€/mois seulement) et 50 % « échecs » (sortie M4).")
p()
p("| Part des clients atteignant 25-35 K€ | EV par client an 1 (collecte 85 %) | CA à 300 actifs | EBITDA indicatif* |")
p("|---|---|---|---|")
def ev_client(achieve, collect=0.85, plateau=22_500):
    full = SETUP + RATE * incr_year(plateau) * collect
    partl = SETUP + RATE * incr_year(8_000) * collect
    fail = SETUP + RATE * 2_000 * sum(RAMP[:4]) * collect
    return achieve * full + (1 - achieve) * 0.5 * partl + (1 - achieve) * 0.5 * fail
ads_y = 365_000
for a in [1.0, 0.7, 0.5, 0.3]:
    ev = ev_client(a)
    ca = CAPACITY * ev
    costs = ads_y + ca * SALES_COM + (CAPACITY / COACH_RATIO) * COACH_COST + 1_300_000
    p(f"| {a*100:.0f} % | {fmt(ev)} | {fmt(ca)} | {(ca-costs)/ca*100:.0f} % |")
p()
p("*Coûts : pub 365 K€, commissions vente 10 %, 20 coachs à 15 clients/tête (1,4 M€), ops+management 1,3 M€.")
p()
p("**Les trois phrases qui rassurent une table d'associés :**")
p(f"1. À thèse PLEINE : {fmt(CAPACITY*ev_client(1.0))} de CA à pleine capacité, **EBITDA 61 %** — le haut du business case.")
p(f"2. À MOITIÉ de la thèse (1 client sur 2 seulement atteint 25 K€) : {fmt(CAPACITY*ev_client(0.5))} de CA, **EBITDA 45 %** — le plan reste un excellent business.")
p(f"3. Même à 30 % de réussite : {fmt(CAPACITY*ev_client(0.3))} de CA, **EBITDA 33 %**, et chaque client rapporte encore {fmt(ev_client(0.3))} pour ~{fmt(ADS_MONTH/signs[1])} d'acquisition : le setup couvre le coût d'acquisition dès le jour 1, la perf des réussites paie tout le reste.")
p()
p("**Le point mort de la thèse** : arithmétiquement, l'équilibre EBITDA tient même très en-dessous de 30 % de réussite —")
p("en pratique, sous ce seuil c'est la RÉPUTATION (études de cas, renouvellements, bouche-à-oreille), pas le P&L, qui")
p("deviendrait le facteur limitant. La thèse du commanditaire (×3-4 « en moyenne ») n'a donc pas besoin d'être vraie")
p("pour que l'entreprise vive ; elle a besoin d'être vraie pour atteindre le scénario haut ET pour alimenter la machine")
p("de preuve. La sélection à l'entrée (baseline saine, offre validée) et le sur-remplissage du funnel (F2 : 40 signatures")
p("possibles pour 25 nécessaires → on choisit les meilleurs dossiers) sont les deux mécanismes qui la protègent.")
p()

# ---------- F5 : P&L pleine capacité ----------
p("## F5 — P&L à pleine capacité (thèse pleine, collecte 85 %)")
p()
rev_cap = CAPACITY * ev_client(1.0)
rows = [
    ("Publicité (1 K€/jour)", ads_y),
    ("Commissions équipe de vente (10 %)", rev_cap * SALES_COM),
    (f"Livraison ({CAPACITY//COACH_RATIO} coachs/CSM à {COACH_RATIO} clients)", (CAPACITY/COACH_RATIO)*COACH_COST),
    ("Ops, outils, studio créa", 500_000),
    ("Management / G&A", 800_000),
]
tot = sum(r[1] for r in rows)
p(f"| Poste | Coût annuel | % CA ({fmt(rev_cap)}) |")
p("|---|---|---|")
for n, c in rows:
    p(f"| {n} | {fmt(c)} | {c/rev_cap*100:.1f} % |")
p(f"| **Total** | **{fmt(tot)}** | {tot/rev_cap*100:.1f} % |")
p(f"| **EBITDA** | **{fmt(rev_cap-tot)}** | **{(rev_cap-tot)/rev_cap*100:.0f} %** |")
p()
p("Garde-fous d'exécution (ce qui doit rester vrai, pilotage mensuel) : rendement réel/client vs modèle ;")
p("ratio clients/coach ≥ 12-15 ; collecte perf ≥ 85 % ; coût/call ≤ 170 €. Benchmark d'humilité : les acteurs FR")
p("vérifiables à l'échelle font 6-9 % de marge nette — notre écart s'explique par le levier perf (revenu/client 3-4×")
p("supérieur au coût de livraison), et il se PERD si le ratio de livraison ou la collecte dérivent. D'où les 4 KPI.")

with open("/home/user/grwthnow/workspace/findings/ws-finance-plan.md", "w", encoding="utf-8") as f:
    f.write("\n".join(OUT))
print("\n".join(OUT))
