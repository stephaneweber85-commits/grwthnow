#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modèle d'unit economics : « 5K€ entrée + 10-15% des résultats » vs « 25K€ cash ».
Toutes les hypothèses sont explicites et listées dans la sortie.
Sortie : markdown (tables) → findings/ws6-model-output.md
"""

OUT = []
def p(s=""):
    OUT.append(s)

# ----------------------------------------------------------------------------
# HYPOTHÈSES CENTRALES (à confronter aux données terrain du rapport)
# ----------------------------------------------------------------------------
ENTRY_FEE = 5_000          # € à l'entrée
PERF_RATES = [0.10, 0.125, 0.15]
CASH_PRICE = 25_000        # offre incumbent
ENGAGE_MONTHS = 12         # durée d'engagement du perf fee
RAMP = [0.25, 0.50, 0.75] + [1.0] * (ENGAGE_MONTHS - 3)  # montée en charge 4 mois

# Archétypes de résultat client (CA INCRÉMENTAL mensuel au plateau, € / mois)
# base = CA incrémental encaissé attribuable au-dessus de la baseline contractuelle
ARCHETYPES = {
    "échec":  {"plateau": 500,    "churn_month": 5},   # quitte à M5
    "moyen":  {"plateau": 6_000,  "churn_month": ENGAGE_MONTHS},
    "fort":   {"plateau": 20_000, "churn_month": ENGAGE_MONTHS},
}

# Mix de portefeuille (probabilités par archétype)
MIXES = {
    "pessimiste": {"échec": 0.50, "moyen": 0.35, "fort": 0.15},
    "central":    {"échec": 0.30, "moyen": 0.45, "fort": 0.25},
    "optimiste":  {"échec": 0.15, "moyen": 0.45, "fort": 0.40},
}

# Taux de collecte effectif du perf fee (sous-déclaration, litiges, impayés)
COLLECTION = {"pessimiste": 0.70, "central": 0.85, "optimiste": 0.95}

# Renouvellement des clients "fort" après 12 mois (perf-only, 12 mois de plus)
RENEWAL_PROBA = {"pessimiste": 0.30, "central": 0.50, "optimiste": 0.70}
RENEWAL_MONTHS = 12

# Funnel (par 100 appels de vente qualifiés)
CLOSE_RATE_CASH = {"pessimiste": 0.08, "central": 0.12, "optimiste": 0.18}
CLOSE_RATE_HYB  = {"pessimiste": 0.20, "central": 0.28, "optimiste": 0.38}

# Capacité de livraison
SOLO_CAPACITY = 10          # clients actifs max en solo
TEAM_DELIVERY_COST = 800    # €/client/mois si équipe (coach ops + outils)

# ----------------------------------------------------------------------------
# FONCTIONS
# ----------------------------------------------------------------------------
def perf_stream(arch, rate, collection):
    """Flux mensuel de perf fee pour un archétype (liste de 12 valeurs €)."""
    a = ARCHETYPES[arch]
    flux = []
    for m in range(ENGAGE_MONTHS):
        if m >= a["churn_month"]:
            flux.append(0.0)
        else:
            flux.append(a["plateau"] * RAMP[m] * rate * collection)
    return flux

def client_value_hybrid(arch, rate, collection, renewal_p):
    """Valeur totale d'un client (entrée + perf 12 mois + renouvellement espéré)."""
    base = ENTRY_FEE + sum(perf_stream(arch, rate, collection))
    if arch == "fort":
        renew = ARCHETYPES["fort"]["plateau"] * rate * collection * RENEWAL_MONTHS
        base += renewal_p * renew
    return base

def expected_value(mix, rate, collection, renewal_p):
    return sum(w * client_value_hybrid(a, rate, collection, renewal_p)
               for a, w in mix.items())

def fmt(x):
    return f"{x:,.0f}".replace(",", " ") + " €"

# ----------------------------------------------------------------------------
# 1. VALEUR PAR CLIENT PAR ARCHÉTYPE (taux 12,5 %, scénario central)
# ----------------------------------------------------------------------------
p("# Modèle économique 5K€ + perf vs 25K€ cash — sorties chiffrées")
p()
p("## H0 — Hypothèses centrales")
p()
p(f"- Entrée : {fmt(ENTRY_FEE)} ; taux de perf testés : 10 % / 12,5 % / 15 % ; incumbent : {fmt(CASH_PRICE)} cash")
p(f"- Engagement : {ENGAGE_MONTHS} mois ; montée en charge linéaire sur 4 mois (25/50/75/100 %)")
p("- Base du % : CA incrémental ENCAISSÉ attribuable au-dessus d'une baseline contractuelle (moyenne 3 mois précédents)")
p("- Archétypes clients (CA incrémental mensuel au plateau) : échec 500 €/mois (churn M5), moyen 6 000 €/mois, fort 20 000 €/mois")
p("- Mix central : 30 % échec / 45 % moyen / 25 % fort ; collecte effective 85 % ; renouvellement des 'forts' 50 % (12 mois perf-only)")
p()
p("## T1 — Valeur totale par client selon l'archétype (taux 12,5 %, collecte 85 %)")
p()
p("| Archétype | Entrée | Perf 12 mois | Renouvellement espéré | Total client |")
p("|---|---|---|---|---|")
for arch in ARCHETYPES:
    perf = sum(perf_stream(arch, 0.125, 0.85))
    ren = 0.0
    if arch == "fort":
        ren = 0.5 * ARCHETYPES["fort"]["plateau"] * 0.125 * 0.85 * RENEWAL_MONTHS
    p(f"| {arch} | {fmt(ENTRY_FEE)} | {fmt(perf)} | {fmt(ren)} | {fmt(ENTRY_FEE+perf+ren)} |")
p()

# ----------------------------------------------------------------------------
# 2. SENSIBILITÉ : taux de perf × mix de réussite (EV par client)
# ----------------------------------------------------------------------------
p("## T2 — Sensibilité : valeur espérée par client (€) selon taux de perf × mix de réussite")
p("(collecte et renouvellement alignés sur le scénario du mix)")
p()
header = "| Taux de perf | " + " | ".join(MIXES.keys()) + " | vs 25K cash (central) |"
p(header)
p("|" + "---|" * (len(MIXES) + 2))
for rate in PERF_RATES:
    row = [f"| **{rate*100:.1f} %**"]
    central_ev = None
    for mix_name, mix in MIXES.items():
        ev = expected_value(mix, rate, COLLECTION[mix_name], RENEWAL_PROBA[mix_name])
        if mix_name == "central":
            central_ev = ev
        row.append(fmt(ev))
    delta = central_ev - CASH_PRICE
    row.append(f"{'+' if delta>=0 else ''}{fmt(delta)}")
    p(" | ".join(row) + " |")
p()

# ----------------------------------------------------------------------------
# 3. SENSIBILITÉ : taux de collecte (le paramètre "attribution")
# ----------------------------------------------------------------------------
p("## T3 — Sensibilité au taux de collecte effectif (mix central, taux 12,5 %)")
p("Le taux de collecte proxifie la qualité de la mécanique d'attribution + le taux d'impayés.")
p()
p("| Collecte effective | EV par client | Perte vs collecte parfaite |")
p("|---|---|---|")
ev100 = expected_value(MIXES["central"], 0.125, 1.00, 0.50)
for c in [1.00, 0.90, 0.85, 0.75, 0.60, 0.50]:
    ev = expected_value(MIXES["central"], 0.125, c, 0.50)
    p(f"| {c*100:.0f} % | {fmt(ev)} | -{fmt(ev100-ev)} |")
p()

# ----------------------------------------------------------------------------
# 4. BREAKEVEN : CA incrémental nécessaire pour battre le 25K cash
# ----------------------------------------------------------------------------
p("## T4 — Point mort : CA incrémental client nécessaire pour égaler 25K€ cash")
p()
p("| Taux de perf | CA incrémental total à générer (collecte 100 %) | Avec collecte 85 % | En €/mois sur 12 mois (85 %) |")
p("|---|---|---|---|")
for rate in PERF_RATES:
    need = (CASH_PRICE - ENTRY_FEE) / rate
    need85 = need / 0.85
    p(f"| {rate*100:.1f} % | {fmt(need)} | {fmt(need85)} | {fmt(need85/12)} / mois |")
p()

# ----------------------------------------------------------------------------
# 5. FUNNEL : revenu par 100 appels qualifiés (l'argument conversion)
# ----------------------------------------------------------------------------
p("## T5 — Revenu par 100 appels de vente qualifiés (l'effet conversion de l'inversion du risque)")
p()
p("| Scénario | Close 25K cash | Revenu cash | Close 5K+12,5% | Clients | Cash immédiat | EV totale 12-24 mois |")
p("|---|---|---|---|---|---|---|")
for sc in ["pessimiste", "central", "optimiste"]:
    n_cash = CLOSE_RATE_CASH[sc] * 100
    rev_cash = n_cash * CASH_PRICE
    n_hyb = CLOSE_RATE_HYB[sc] * 100
    ev_hyb = n_hyb * expected_value(MIXES[sc], 0.125, COLLECTION[sc], RENEWAL_PROBA[sc])
    upfront = n_hyb * ENTRY_FEE
    p(f"| {sc} | {n_cash:.0f} % → {n_cash:.0f} clients | {fmt(rev_cash)} | {CLOSE_RATE_HYB[sc]*100:.0f} % | {n_hyb:.0f} | {fmt(upfront)} | {fmt(ev_hyb)} |")
p()
p("Lecture : le modèle hybride convertit mieux (risque client réduit) mais encaisse moins vite ;")
p("il crée aussi 2-3× plus de clients à livrer par lead — la CAPACITÉ devient la contrainte.")
p()

# ----------------------------------------------------------------------------
# 6. CAPACITÉ : revenu annuel à capacité constante (la vraie comparaison)
# ----------------------------------------------------------------------------
p("## T6 — À capacité de livraison égale (10-12 clients actifs, opérateur solo puis petite équipe)")
p()
p("| Configuration | Modèle 25K cash | Modèle 5K+12,5% (central) | Modèle 5K+15% (central) |")
p("|---|---|---|---|")
for n in [8, 10, 12, 16]:
    rev_cash = n * CASH_PRICE
    ev125 = n * expected_value(MIXES["central"], 0.125, 0.85, 0.50)
    ev150 = n * expected_value(MIXES["central"], 0.15, 0.85, 0.50)
    cost = 0 if n <= SOLO_CAPACITY else n * TEAM_DELIVERY_COST * 12
    note = " (solo)" if n <= SOLO_CAPACITY else f" (équipe, -{fmt(cost)} coûts livraison)"
    p(f"| {n} clients/an{note} | {fmt(rev_cash - cost)} | {fmt(ev125 - cost)} | {fmt(ev150 - cost)} |")
p()

# ----------------------------------------------------------------------------
# 7. CASH-FLOW : courbe cumulée mois par mois (démarrage réaliste)
# ----------------------------------------------------------------------------
p("## T7 — Cash-flow cumulé, démarrage réaliste (2 nouveaux clients/mois pendant 6 mois, mix central, 12,5 %)")
p()
NEW_PER_MONTH = 2
HORIZON = 18
mix = MIXES["central"]

def cohort_monthly_hybrid(rate, collection, renewal_p):
    """Flux mensuel d'UN client espéré (mois 0 = signature)."""
    flux = [ENTRY_FEE * 1.0]
    for m in range(ENGAGE_MONTHS):
        v = sum(w * perf_stream(a, rate, collection)[m] for a, w in mix.items())
        flux.append(v)
    # renouvellement des forts (mois 13-24)
    for m in range(RENEWAL_MONTHS):
        v = mix["fort"] * renewal_p * ARCHETYPES["fort"]["plateau"] * rate * collection
        flux.append(v)
    return flux

def cohort_monthly_cash():
    # 25K payé en 3 fois (pratique courante du marché)
    return [CASH_PRICE / 3, CASH_PRICE / 3, CASH_PRICE / 3]

hyb_flux = cohort_monthly_hybrid(0.125, 0.85, 0.50)
cash_flux = cohort_monthly_cash()

cum_h, cum_c = 0.0, 0.0
rows = []
for month in range(HORIZON):
    # clients signés du mois 0 au mois min(month,5) — hybride convertit ~2,3x mieux :
    # pour un MÊME flux de leads, cash signe 2/2,33 ≈ 0,86 client/mois
    inflow_h = 0.0
    inflow_c = 0.0
    for signed in range(0, min(month, 5) + 1):
        age = month - signed
        if age < len(hyb_flux):
            inflow_h += NEW_PER_MONTH * hyb_flux[age]
        if age < len(cash_flux):
            inflow_c += (NEW_PER_MONTH * CLOSE_RATE_CASH["central"] / CLOSE_RATE_HYB["central"]) * cash_flux[age]
    cum_h += inflow_h
    cum_c += inflow_c
    rows.append((month + 1, inflow_h, cum_h, inflow_c, cum_c))

p("| Mois | Encaissement hybride | Cumul hybride | Encaissement cash (même flux de leads) | Cumul cash |")
p("|---|---|---|---|---|")
for m, ih, ch, ic, cc in rows:
    p(f"| M{m} | {fmt(ih)} | {fmt(ch)} | {fmt(ic)} | {fmt(cc)} |")
last_below = max((m for m, _, ch, _, cc in rows if ch <= cc), default=0)
crossover = last_below + 1 if last_below < HORIZON else None
p()
p(f"Croisement DURABLE des cumuls (hybride dépasse cash et y reste) : {'M'+str(crossover) if crossover else 'pas sur 18 mois'} — à MÊME flux de leads entrants (12/mois), le hybride signe 2 clients/mois (28 % de close) vs ~0,9 (12 % de close).")
p()

# ----------------------------------------------------------------------------
# 8. PERSPECTIVE CLIENT (alimente l'équation de valeur, section 8 du rapport)
# ----------------------------------------------------------------------------
p("## T8 — Perspective CLIENT : ce que chaque modèle lui coûte selon son résultat (12 mois, 12,5 %)")
p()
p("| Résultat client | CA incrémental 12 mois | Coût 25K cash | Coût 5K+12,5% | ROI client cash | ROI client hybride |")
p("|---|---|---|---|---|---|")
for arch, a in ARCHETYPES.items():
    months_active = min(a["churn_month"], ENGAGE_MONTHS)
    ca_inc = sum(a["plateau"] * RAMP[m] for m in range(months_active))
    cost_h = ENTRY_FEE + 0.125 * ca_inc          # côté client : il paie sur le réel (pas de haircut)
    roi_cash = (ca_inc - CASH_PRICE) / CASH_PRICE * 100
    roi_h = (ca_inc - cost_h) / cost_h * 100
    p(f"| {arch} | {fmt(ca_inc)} | {fmt(CASH_PRICE)} | {fmt(cost_h)} | {roi_cash:+.0f} % | {roi_h:+.0f} % |")
p()
p("Lecture : en cas d'échec, le client hybride perd ~5,2K€ vs 25K€ — l'inversion du risque divise le downside client par ~5.")
p("En cas de succès fort, il paie PLUS cher que 25K (≈31K) — c'est le « prix de l'assurance », argument de framing à assumer en vente.")
p()

# ----------------------------------------------------------------------------
# 9. TORNADO : quel paramètre domine ?
# ----------------------------------------------------------------------------
p("## T9 — Tornado : impact de chaque paramètre sur l'EV par client (base : central, 12,5 % = point de référence)")
p()
base_ev = expected_value(MIXES["central"], 0.125, 0.85, 0.50)
p(f"EV de référence : {fmt(base_ev)}")
p()
p("| Paramètre | Bas | EV bas | Haut | EV haut | Amplitude |")
p("|---|---|---|---|---|---|")
tests = []
ev_lo = expected_value(MIXES["pessimiste"], 0.125, 0.85, 0.50)
ev_hi = expected_value(MIXES["optimiste"], 0.125, 0.85, 0.50)
tests.append(("Mix de réussite clients", "pessimiste", ev_lo, "optimiste", ev_hi))
ev_lo = expected_value(MIXES["central"], 0.10, 0.85, 0.50)
ev_hi = expected_value(MIXES["central"], 0.15, 0.85, 0.50)
tests.append(("Taux de perf (10→15 %)", "10 %", ev_lo, "15 %", ev_hi))
ev_lo = expected_value(MIXES["central"], 0.125, 0.60, 0.50)
ev_hi = expected_value(MIXES["central"], 0.125, 0.95, 0.50)
tests.append(("Collecte/attribution (60→95 %)", "60 %", ev_lo, "95 %", ev_hi))
ev_lo = expected_value(MIXES["central"], 0.125, 0.85, 0.20)
ev_hi = expected_value(MIXES["central"], 0.125, 0.85, 0.80)
tests.append(("Renouvellement forts (20→80 %)", "20 %", ev_lo, "80 %", ev_hi))
# plateau du client moyen : 4K vs 8K
saved = ARCHETYPES["moyen"]["plateau"]
ARCHETYPES["moyen"]["plateau"] = 4_000
ev_lo = expected_value(MIXES["central"], 0.125, 0.85, 0.50)
ARCHETYPES["moyen"]["plateau"] = 8_000
ev_hi = expected_value(MIXES["central"], 0.125, 0.85, 0.50)
ARCHETYPES["moyen"]["plateau"] = saved
tests.append(("Plateau client 'moyen' (4→8K€/mois)", "4K", ev_lo, "8K", ev_hi))
tests.sort(key=lambda t: abs(t[4] - t[2]), reverse=True)
for name, lo_l, lo, hi_l, hi in tests:
    p(f"| {name} | {lo_l} | {fmt(lo)} | {hi_l} | {fmt(hi)} | {fmt(abs(hi-lo))} |")
p()

# ----------------------------------------------------------------------------
# 10. SEUILS DE VIABILITÉ
# ----------------------------------------------------------------------------
p("## T10 — Seuils de viabilité (mix central, 12,5 %, collecte 85 %)")
p()
ev = expected_value(MIXES["central"], 0.125, 0.85, 0.50)
p(f"- EV par client : {fmt(ev)} → pour égaler 12 clients × 25K = 300K€/an, il faut {300000/ev:.1f} clients hybrides actifs/an.")
min_baseline = 25_000 / 0.30 / 12  # pour qu'un client 'moyen' (double son CA) génère 6K/mois incrémental il doit partir d'environ 6K
p(f"- Qualification d'entrée : pour qu'un client 'moyen' atteigne +6K€/mois incrémental (hypothèse plateau), il doit partir d'une baseline ≥ 4-6K€/mois avec une offre déjà validée — le modèle IMPOSE une barre de qualification.")
p(f"- Cash de survie : T7 montre le creux de trésorerie des 6 premiers mois — prévoir 6 mois de charges personnelles ou 3-4 ventes cash d'amorçage.")

with open("/home/user/grwthnow/workspace/findings/ws6-model-output.md", "w", encoding="utf-8") as f:
    f.write("\n".join(OUT))
print("\n".join(OUT[:80]))
print("...")
print(f"[OK] {len(OUT)} lignes écrites dans findings/ws6-model-output.md")
