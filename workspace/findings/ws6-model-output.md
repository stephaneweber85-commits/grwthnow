# Modèle économique 5K€ + perf vs 25K€ cash — sorties chiffrées

## H0 — Hypothèses centrales

- Entrée : 5 000 € ; taux de perf testés : 10 % / 12,5 % / 15 % ; incumbent : 25 000 € cash
- Engagement : 12 mois ; montée en charge linéaire sur 4 mois (25/50/75/100 %)
- Base du % : CA incrémental ENCAISSÉ attribuable au-dessus d'une baseline contractuelle (moyenne 3 mois précédents)
- Archétypes clients (CA incrémental mensuel au plateau) : échec 500 €/mois (churn M5), moyen 6 000 €/mois, fort 20 000 €/mois
- Mix central : 30 % échec / 45 % moyen / 25 % fort ; collecte effective 85 % ; renouvellement des 'forts' 50 % (12 mois perf-only)

## T1 — Valeur totale par client selon l'archétype (taux 12,5 %, collecte 85 %)

| Archétype | Entrée | Perf 12 mois | Renouvellement espéré | Total client |
|---|---|---|---|---|
| échec | 5 000 € | 186 € | 0 € | 5 186 € |
| moyen | 5 000 € | 6 694 € | 0 € | 11 694 € |
| fort | 5 000 € | 22 312 € | 12 750 € | 40 062 € |

## T2 — Sensibilité : valeur espérée par client (€) selon taux de perf × mix de réussite
(collecte et renouvellement alignés sur le scénario du mix)

| Taux de perf | pessimiste | central | optimiste | vs 25K cash (central) |
|---|---|---|---|---|
| **10.0 %** | 9 566 € | 14 467 € | 22 082 € | -10 533 € |
| **12.5 %** | 10 707 € | 16 834 € | 26 353 € | -8 166 € |
| **15.0 %** | 11 849 € | 19 200 € | 30 623 € | -5 800 € |

## T3 — Sensibilité au taux de collecte effectif (mix central, taux 12,5 %)
Le taux de collecte proxifie la qualité de la mécanique d'attribution + le taux d'impayés.

| Collecte effective | EV par client | Perte vs collecte parfaite |
|---|---|---|
| 100 % | 18 922 € | -0 € |
| 90 % | 17 530 € | -1 392 € |
| 85 % | 16 834 € | -2 088 € |
| 75 % | 15 441 € | -3 480 € |
| 60 % | 13 353 € | -5 569 € |
| 50 % | 11 961 € | -6 961 € |

## T4 — Point mort : CA incrémental client nécessaire pour égaler 25K€ cash

| Taux de perf | CA incrémental total à générer (collecte 100 %) | Avec collecte 85 % | En €/mois sur 12 mois (85 %) |
|---|---|---|---|
| 10.0 % | 200 000 € | 235 294 € | 19 608 € / mois |
| 12.5 % | 160 000 € | 188 235 € | 15 686 € / mois |
| 15.0 % | 133 333 € | 156 863 € | 13 072 € / mois |

## T5 — Revenu par 100 appels de vente qualifiés (l'effet conversion de l'inversion du risque)

| Scénario | Close 25K cash | Revenu cash | Close 5K+12,5% | Clients | Cash immédiat | EV totale 12-24 mois |
|---|---|---|---|---|---|---|
| pessimiste | 8 % → 8 clients | 200 000 € | 20 % | 20 | 100 000 € | 214 144 € |
| central | 12 % → 12 clients | 300 000 € | 28 % | 28 | 140 000 € | 471 341 € |
| optimiste | 18 % → 18 clients | 450 000 € | 38 % | 38 | 190 000 € | 1 001 404 € |

Lecture : le modèle hybride convertit mieux (risque client réduit) mais encaisse moins vite ;
il crée aussi 2-3× plus de clients à livrer par lead — la CAPACITÉ devient la contrainte.

## T6 — À capacité de livraison égale (10-12 clients actifs, opérateur solo puis petite équipe)

| Configuration | Modèle 25K cash | Modèle 5K+12,5% (central) | Modèle 5K+15% (central) |
|---|---|---|---|
| 8 clients/an (solo) | 200 000 € | 134 669 € | 153 602 € |
| 10 clients/an (solo) | 250 000 € | 168 336 € | 192 003 € |
| 12 clients/an (équipe, -115 200 € coûts livraison) | 184 800 € | 86 803 € | 115 204 € |
| 16 clients/an (équipe, -153 600 € coûts livraison) | 246 400 € | 115 738 € | 153 605 € |

## T7 — Cash-flow cumulé, démarrage réaliste (2 nouveaux clients/mois pendant 6 mois, mix central, 12,5 %)

| Mois | Encaissement hybride | Cumul hybride | Encaissement cash (même flux de leads) | Cumul cash |
|---|---|---|---|---|
| M1 | 10 000 € | 10 000 € | 7 143 € | 7 143 € |
| M2 | 10 417 € | 20 417 € | 14 286 € | 21 429 € |
| M3 | 11 251 € | 31 668 € | 21 429 € | 42 857 € |
| M4 | 12 502 € | 44 170 € | 21 429 € | 64 286 € |
| M5 | 14 170 € | 58 341 € | 21 429 € | 85 714 € |
| M6 | 15 838 € | 74 179 € | 21 429 € | 107 143 € |
| M7 | 7 475 € | 81 654 € | 14 286 € | 121 429 € |
| M8 | 8 694 € | 90 348 € | 7 143 € | 128 571 € |
| M9 | 9 496 € | 99 844 € | 0 € | 128 571 € |
| M10 | 9 881 € | 109 725 € | 0 € | 128 571 € |
| M11 | 9 849 € | 119 574 € | 0 € | 128 571 € |
| M12 | 9 818 € | 129 392 € | 0 € | 128 571 € |
| M13 | 9 818 € | 139 209 € | 0 € | 128 571 € |
| M14 | 8 712 € | 147 922 € | 0 € | 128 571 € |
| M15 | 7 608 € | 155 529 € | 0 € | 128 571 € |
| M16 | 6 502 € | 162 032 € | 0 € | 128 571 € |
| M17 | 5 398 € | 167 429 € | 0 € | 128 571 € |
| M18 | 4 292 € | 171 722 € | 0 € | 128 571 € |

Croisement DURABLE des cumuls (hybride dépasse cash et y reste) : M12 — à MÊME flux de leads entrants (12/mois), le hybride signe 2 clients/mois (28 % de close) vs ~0,9 (12 % de close).

## T8 — Perspective CLIENT : ce que chaque modèle lui coûte selon son résultat (12 mois, 12,5 %)

| Résultat client | CA incrémental 12 mois | Coût 25K cash | Coût 5K+12,5% | ROI client cash | ROI client hybride |
|---|---|---|---|---|---|
| échec | 1 750 € | 25 000 € | 5 219 € | -93 % | -66 % |
| moyen | 63 000 € | 25 000 € | 12 875 € | +152 % | +389 % |
| fort | 210 000 € | 25 000 € | 31 250 € | +740 % | +572 % |

Lecture : en cas d'échec, le client hybride perd ~5,2K€ vs 25K€ — l'inversion du risque divise le downside client par ~5.
En cas de succès fort, il paie PLUS cher que 25K (≈31K) — c'est le « prix de l'assurance », argument de framing à assumer en vente.

## T9 — Tornado : impact de chaque paramètre sur l'EV par client (base : central, 12,5 % = point de référence)

EV de référence : 16 834 €

| Paramètre | Bas | EV bas | Haut | EV haut | Amplitude |
|---|---|---|---|---|---|
| Mix de réussite clients | pessimiste | 12 695 € | optimiste | 22 065 € | 9 370 € |
| Collecte/attribution (60→95 %) | 60 % | 13 353 € | 95 % | 18 226 € | 4 873 € |
| Taux de perf (10→15 %) | 10 % | 14 467 € | 15 % | 19 200 € | 4 733 € |
| Renouvellement forts (20→80 %) | 20 % | 14 921 € | 80 % | 18 746 € | 3 825 € |
| Plateau client 'moyen' (4→8K€/mois) | 4K | 15 830 € | 8K | 17 838 € | 2 008 € |

## T10 — Seuils de viabilité (mix central, 12,5 %, collecte 85 %)

- EV par client : 16 834 € → pour égaler 12 clients × 25K = 300K€/an, il faut 17.8 clients hybrides actifs/an.
- Qualification d'entrée : pour qu'un client 'moyen' atteigne +6K€/mois incrémental (hypothèse plateau), il doit partir d'une baseline ≥ 4-6K€/mois avec une offre déjà validée — le modèle IMPOSE une barre de qualification.
- Cash de survie : T7 montre le creux de trésorerie des 6 premiers mois — prévoir 6 mois de charges personnelles ou 3-4 ventes cash d'amorçage.