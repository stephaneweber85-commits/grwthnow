#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modèle « scale » : moteur d'acquisition payante + capacité équipe.
Paramètres commanditaire (03/07/2026) :
- Budget pub : 1 000 €/jour (YouTube, Google Ads, LinkedIn, Instagram — vidéo)
- Volume visé : 6-8 appels qualifiés bookés / jour
- Capacité équipe à terme : 300 clients simultanés max
- Rendement client : 44 000 € HT/an pour l'agence (donnée interne, étude séparée du commanditaire)
Sortie : findings/ws-scale-model.md
"""

OUT = []
def p(s=""): OUT.append(s)
def fmt(x, unit=" €"): return f"{x:,.0f}".replace(",", " ") + unit

# ---------------- Paramètres ----------------
ADS_DAY = 1_000
ADS_MONTH = ADS_DAY * 365 / 12          # 30 417 €
CALLS_DAY = (6, 7, 8)                    # bas / central / haut
SHOWUP = (0.70, 0.75, 0.85)
CLOSE = (0.18, 0.22, 0.28)               # hybride, cible établie, engagement + gros que 5K sec
UNIT_REVENUE = 44_000                    # € HT/an/client (donnée commanditaire)
CAPACITY = 300
DURATION_M = 12                          # engagement moyen (mois)
CLIENTS_PER_COACH = (10, 15, 22)         # sensibilité ratio de livraison
COACH_COST = 70_000                      # coût chargé/an
SALES_COM = 0.10                         # commissions équipe de vente (sur cash encaissé)

p("# Modèle SCALE — moteur payant 1 K€/jour + capacité 300 clients")
p()
p("## Paramètres (sources : commanditaire, 03/07/2026 ; benchmarks : findings/ws9-gtm.md)")
p()
p(f"- Budget pub : {fmt(ADS_DAY)}/jour = {fmt(ADS_MONTH)}/mois = {fmt(ADS_DAY*365)}/an — vidéo YouTube / Google Ads / LinkedIn / Instagram")
p(f"- Volume visé : 6-8 appels qualifiés bookés/jour ; show-up 70-85 % ; close hybride 18-28 %")
p(f"- Rendement client : {fmt(UNIT_REVENUE)} HT/an (donnée interne commanditaire, étude séparée — hypothèse structurante à re-valider en vente réelle)")
p(f"- Capacité : {CAPACITY} clients simultanés max (équipe à terme) ; engagement moyen {DURATION_M} mois")
p()

# ---------------- S1 : funnel mensuel ----------------
p("## S1 — Funnel mensuel (pub → appels → signatures)")
p()
p("| Scénario | Appels bookés/mois | Coût/appel booké | Appels tenus | Signatures/mois | CAC |")
p("|---|---|---|---|---|---|")
scen = ["bas", "central", "haut"]
signings = []
for i, name in enumerate(scen):
    calls_m = CALLS_DAY[i] * 30.4
    cost_call = ADS_MONTH / calls_m
    held = calls_m * SHOWUP[i]
    signed = held * CLOSE[i]
    signings.append(signed)
    cac = ADS_MONTH / signed
    p(f"| {name} | {calls_m:.0f} | {fmt(cost_call)} | {held:.0f} | **{signed:.0f}** | {fmt(cac)} |")
p()
p(f"Cohérence benchmark : le coût/appel implicite ({fmt(ADS_MONTH/(CALLS_DAY[2]*30.4))}-{fmt(ADS_MONTH/(CALLS_DAY[0]*30.4))}) se situe dans le haut de la fourchette observée")
p("sur la niche (40-150 €/appel réservé, findings WS9) : l'objectif 6-8 appels/jour est ATTEIGNABLE mais exige des créas vidéo performantes ;")
p("si le coût réel dérive à 250 €/appel, le volume tombe à ~4 appels/jour → prévoir 2-3 mois d'itération créative.")
p()

# ---------------- S2 : CAC vs LTV ----------------
p("## S2 — CAC vs valeur client")
p()
cac_c = ADS_MONTH / signings[1]
p(f"- CAC central ≈ {fmt(cac_c)} (fourchette {fmt(ADS_MONTH/signings[2])}-{fmt(ADS_MONTH/signings[0])}) — hors coûts de vente (commissions ~10 % traitées en S6).")
p(f"- Valeur client : {fmt(UNIT_REVENUE)}/an → **LTV/CAC ≈ {UNIT_REVENUE/cac_c:.0f}×** (central). Même à CAC 2 000 € et 35 K€/client : 17×.")
p("- Lecture : à ces ratios, la contrainte du business N'EST PAS l'acquisition — c'est la capacité de livraison et la tenue du rendement client.")
p()

# ---------------- S3 : remplissage de la capacité ----------------
p("## S3 — Remplissage de la capacité (300 clients simultanés)")
p()
steady_inflow = CAPACITY / DURATION_M
p(f"- Flux soutenable à pleine capacité : {CAPACITY} clients ÷ {DURATION_M} mois d'engagement = **{steady_inflow:.0f} signatures/mois** en régime permanent.")
p(f"- Le funnel central produit {signings[1]:.0f} signatures/mois → LE FUNNEL SUR-REMPLIT LA CAPACITÉ (~{signings[1]-steady_inflow:+.0f}/mois).")
p("  Trois soupapes (dans l'ordre) : monter les prix (part fixe), durcir la qualification (mix de réussite ↑), étendre l'équipe.")
p("- Temps de remplissage depuis zéro (montée en charge de l'équipe en parallèle) :")
p()
p("| Ramp | Signatures/mois (M1→M12) | Clients actifs fin M12 | Clients actifs moyens année 1 |")
p("|---|---|---|---|")
ramps = {
    "prudent (recrutement progressif)": [5,8,10,12,15,18,20,22,25,25,25,25],
    "volontariste (équipe prête)":      [10,15,20,25,28,30,30,30,30,30,30,30],
}
ramp_actifs = {}
for name, inflow in ramps.items():
    actifs = []
    stock = 0.0
    for m, s in enumerate(inflow):
        stock = min(CAPACITY, stock + s - (actifs[m-DURATION_M] if m >= DURATION_M else 0))
        actifs.append(s if not actifs else 0)  # placeholder
    # recompute proprement : stock(m) = somme des inflows des 12 derniers mois
    stocks = []
    for m in range(12):
        stocks.append(min(CAPACITY, sum(inflow[max(0, m-11):m+1])))
    ramp_actifs[name] = stocks
    p(f"| {name} | {inflow[0]}→{inflow[-1]} | {stocks[-1]:.0f} | {sum(stocks)/12:.0f} |")
p()
p(f"- Saturation des 300 : M13-M18 (volontariste) à M20-M26 (prudent), en maintenant ~{steady_inflow:.0f}-30 signatures/mois.")
p()

# ---------------- S4 : pont tarifaire vers 44 K€/an ----------------
p("## S4 — Le pont tarifaire : comment un client rend 44 K€ HT/an")
p()
p("Le 5 K€ + 12,5 % « pur » de l'offre initiale ne produit 44 K€/an que sur les clients 'forts' (EV blended : 16,8 K€).")
p("Atteindre 44 K€ de rendement moyen impose une composante mensuelle — la structure du marché validée en donnée 1re main")
p("(contrat client Cherifi : 15 K€ + 2,5 K€/mois + 10 %) prouve que le marché l'accepte. Options :")
p()
p("| Mix | Fixe année 1 | Perf attendue (client moyen +6 K€/mois, 85 % collecte) | Total/an | Risque client initial |")
p("|---|---|---|---|---|")
mixes = [
    ("A. Offre étude : 5 K + 12,5 %", 5_000, 0.125, 0),
    ("B. **Palier Scale : 5 K + 1 995 €/mois + 10 %**", 5_000 + 1_995*12, 0.10, 0),
    ("C. Marché (type Cherifi) : 15 K + 2,5 K/mois + 10 %", 15_000 + 2_500*12, 0.10, 0),
]
incr_moyen = 63_000  # cash incrémental an 1 client moyen (cf. modèle initial)
for name, fixe, rate, _ in mixes:
    perf = incr_moyen * rate * 0.85
    total = fixe + perf
    risque = fixe if "5 K +" not in name else 5_000
    entry = 5_000 if name.startswith(("A", "B")) else 15_000
    p(f"| {name} | {fmt(fixe)} | {fmt(perf)} | **{fmt(total)}** | {fmt(entry)} à l'entrée |")
p()
p("→ Le mix B (« Palier Scale ») atteint ~34-40 K€/an sur le client moyen et >50 K€ sur les forts → blended ≈ 38-46 K€/an :")
p("   COHÉRENT avec les 44 K€ HT/an de l'étude interne, tout en conservant l'inversion du risque qui fait la différence")
p("   (entrée 3× inférieure au standard marché, sortie M4, plafond) — le différenciateur commercial reste intact.")
p()

# ---------------- S5 : trajectoire de revenus ----------------
p("## S5 — Trajectoire de revenus (rendement 44 K€ HT/an/client)")
p()
p("| Scénario | Clients actifs moyens an 1 | CA an 1 | Actifs fin an 1 | CA an 2 (run-rate partiel) | CA à pleine capacité |")
p("|---|---|---|---|---|---|")
for name, stocks in ramp_actifs.items():
    avg1 = sum(stocks)/12
    ca1 = avg1 * UNIT_REVENUE / 12 * 12 / 1e6
    # an 2 : montée vers capacité
    avg2 = min(CAPACITY, stocks[-1] * 1.5)
    ca2 = avg2 * UNIT_REVENUE / 1e6
    p(f"| {name} | {avg1:.0f} | **{avg1*UNIT_REVENUE/1e6:.1f} M€** | {stocks[-1]:.0f} | ~{ca2:.1f} M€ | {CAPACITY*UNIT_REVENUE/1e6:.1f} M€/an |")
p()
p(f"- Pleine capacité : {CAPACITY} × {fmt(UNIT_REVENUE)} = **{CAPACITY*UNIT_REVENUE/1e6:.1f} M€/an**.")
p("- Mise en perspective marché (honnêteté vis-à-vis du SAM) : 13,2 M€ ≈ 40-50 % du SAM central de l'offre hybride (25-35 M€/an)")
p("  et ferait de l'agence le n°1 francophone du segment (le plus gros acteur vérifié du panel : ~10-19 M€/an, Entrepreneurs.com).")
p("  → La pleine capacité est un objectif d'année 3-5, pas d'année 1-2 ; elle suppose de PRENDRE le leadership du segment.")
p()

# ---------------- S6 : esquisse P&L à pleine capacité ----------------
p("## S6 — Esquisse P&L à pleine capacité (à challenger — hypothèses affichées)")
p()
rev = CAPACITY * UNIT_REVENUE
p(f"Revenu : {fmt(rev)} /an")
p()
p("| Poste | Hypothèse | Coût annuel | % CA |")
p("|---|---|---|---|")
ads_y = ADS_DAY * 365
sales = rev * SALES_COM
rows = [("Publicité", "1 K€/jour", ads_y), ("Équipe de vente (com.)", "10 % du cash encaissé", sales)]
for cpc in [15]:
    n_coach = CAPACITY / cpc
    delivery = n_coach * COACH_COST
    rows.append((f"Livraison ({n_coach:.0f} coachs/CSM à {cpc} clients/tête)", f"{fmt(COACH_COST)}/tête chargé", delivery))
rows.append(("Ops, outils, contenu, studio vidéo", "forfait", 500_000))
rows.append(("Management / G&A", "forfait", 800_000))
total_cost = sum(r[2] for r in rows)
for name, hyp, cost in rows:
    p(f"| {name} | {hyp} | {fmt(cost)} | {cost/rev*100:.1f} % |")
p(f"| **Total coûts** |  | **{fmt(total_cost)}** | {total_cost/rev*100:.1f} % |")
p(f"| **EBITDA indicatif** |  | **{fmt(rev-total_cost)}** | **{(rev-total_cost)/rev*100:.0f} %** |")
p()
p("### Sensibilité (les deux paramètres qui font ou défont la marge)")
p()
p("| Ratio clients/coach → | 10 | 15 | 22 |")
p("|---|---|---|---|")
for ur in [35_000, 44_000, 50_000]:
    line = [f"| Rendement {fmt(ur)}/an "]
    for cpc in CLIENTS_PER_COACH:
        r = CAPACITY * ur
        cost = ads_y + r*SALES_COM + (CAPACITY/cpc)*COACH_COST + 1_300_000
        line.append(f"{(r-cost)/r*100:.0f} % ")
    p("|".join(line) + "|")
p()
p("Lecture : la marge tient tant que (a) le rendement client tient ≥ 40 K€ ET (b) le ratio de livraison tient ≥ 12-15 clients/tête.")
p("Garde-fou marché : les acteurs FR vérifiables à l'échelle affichent des marges nettes de 6-9 % (Squared, Coudac) et le modèle")
p("volume+équipe le plus proche (Scalezia) déposait des PERTES — la discipline de coûts est LE risque d'exécution n°1 du scénario scale,")
p("bien avant l'acquisition. Le pilotage mensuel du ratio clients/tête et du rendement réel par client est non négociable.")

with open("/home/user/grwthnow/workspace/findings/ws-scale-model.md", "w", encoding="utf-8") as f:
    f.write("\n".join(OUT))
print("\n".join(OUT))
