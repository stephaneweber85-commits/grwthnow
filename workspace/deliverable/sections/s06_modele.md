# 6. Le modèle « 5 K€ + 10-15 % » : unit economics, sensibilité, cash-flow, attribution

Toutes les tables citées (T1-T10) sont reproduites intégralement en annexe technique ([findings/ws6-model-output.md](../findings/ws6-model-output.md)) et générées par un modèle reproductible ([models/unit_economics.py](../models/unit_economics.py)). Les pratiques de marché citées viennent de [findings/ws6-successfee.md](../findings/ws6-successfee.md).

## 6.1 Réponse d'abord

Le modèle hybride est **viable, mais pas pour la raison intuitive**. En calibrage marché conservateur, il rapporte MOINS que le 25 K€ cash par client (EV ≈ 16,8 K€ à 12,5 % et 19,2 K€ au taux retenu de 15 %, vs 25 K€) — le plan financier du scénario opérationnel retenu (5 K€ + 15 %, thèse de service ×3-4) est en §6.9. Il gagne sur trois autres terrains : (1) **la conversion** — à flux de leads égal, il signe ~2,3× plus de clients (inversion du risque), ce qui fait +57 % d'EV par 100 appels et un dépassement durable du modèle cash dès le mois 12 ; (2) **la vendabilité** pour un entrant sans track record — personne ne paie 25 K€ à un inconnu, beaucoup risquent 5 K€ ; (3) **la LTV des clients gagnants** (~40 K€ avec renouvellement). Ses trois conditions de viabilité : une **qualification d'entrée stricte** (baseline ≥ 4-6 K€/mois), une **mécanique d'attribution contractualisée avant signature**, et **6 mois de trésorerie** pour traverser le creux de cash initial.

## 6.2 Hypothèses du modèle (explicites, à challenger)

- Entrée 5 000 € ; perf 10 / 12,5 / 15 % ; incumbent 25 K€ cash ; engagement 12 mois ; montée en charge 4 mois (25/50/75/100 %).
- Base du % : **CA incrémental encaissé attribuable** au-dessus d'une baseline contractuelle (moyenne des 3 mois précédents).
- Archétypes clients (CA incrémental mensuel au plateau) : échec 500 €/mois avec churn à M5 ; moyen +6 000 €/mois ; fort +20 000 €/mois. Mix central : 30/45/25 (pessimiste 50/35/15, optimiste 15/45/40).
- Collecte effective du perf fee : 85 % central (sous-déclaration, litiges, impayés) ; renouvellement des « forts » : 50 % (12 mois perf-only).
- Funnel : close rate 25 K€ cash 8-18 % ; close rate hybride 20-38 % (l'écart est l'effet documenté de l'inversion du risque sur un marché défiant, cf. §3.4 ; benchmarks closing FR : 20-35 % des appels tenus, [vivre-de-son-site-internet.com](https://vivre-de-son-site-internet.com/augmenter-ventes-setting/)).

## 6.3 Unit economics par client (T1, T2)

| Archétype | Total client (12,5 %, collecte 85 %) |
|---|---|
| Échec (30 %) | 5 186 € |
| Moyen (45 %) | 11 694 € |
| Fort (25 %) | 40 062 € (dont renouvellement espéré 12 750 €) |
| **EV pondérée** | **16 834 €** |

Sensibilité taux × mix (EV/client) :

| Taux | Pessimiste | Central | Optimiste |
|---|---|---|---|
| 10 % | 9 566 € | 14 467 € | 22 082 € |
| 12,5 % | 10 707 € | 16 834 € | 26 353 € |
| 15 % | 11 849 € | 19 200 € | 30 623 € |

Lecture : même en optimiste à 15 %, on reste sous 25 K€ cash + upsells au niveau **par client**. Le combat ne se gagne pas là (cf. 6.4). À 10 % en mix pessimiste, l'EV (9,6 K€) couvre à peine une livraison sérieuse : **le taux plancher recommandé est 12,5 %, et 15 % si la cible est en bas de fourchette de baseline**.

## 6.4 L'argument décisif : le revenu par flux de leads, pas par client (T5, T7)

Par 100 appels qualifiés (scénario central) : le 25 K€ cash close 12 % → 12 clients → 300 K€. L'hybride close 28 % → 28 clients → 140 K€ immédiats + perf → **EV totale ~471 K€ sur 12-24 mois** (+57 %). En cash-flow cumulé, à même flux de leads (T7) : le cash mène jusqu'à M8 (~129 K€ vs ~90 K€), l'hybride le **croise durablement à M12** puis creuse l'écart (172 K€ vs 129 K€ à M18).

Contrepartie : 28 clients à livrer au lieu de 12. **La contrainte binding devient la capacité** (T6) : à capacité de livraison ÉGALE (8-12 clients actifs), le cash gagne toujours (250 K€ vs 168-192 K€ pour 10 clients). Autrement dit :

> Le modèle hybride est le bon choix quand la contrainte est la DEMANDE (entrant sans réputation, leads rares et chers, marché défiant). Le modèle cash devient supérieur quand la contrainte est la CAPACITÉ (réputation établie, leads abondants). **Trajectoire rationnelle : lancer en hybride, faire monter la part fixe à mesure que la preuve s'accumule** — exactement le chemin inverse de Jean Hollaender, parti 100 % performance puis pivoté vers le cash une fois la réputation faite (§4.8) : ce précédent valide la logique de trajectoire.

## 6.5 Ce qui tue le modèle : le tornado (T9)

Impact sur l'EV/client (base 16 834 €) : 1. **Mix de réussite clients** (pessimiste→optimiste : amplitude 9 370 €) ; 2. **Collecte/attribution** (60→95 % : 4 873 €) ; 3. Taux de perf (10→15 % : 4 733 €) ; 4. Renouvellement des forts (3 825 €) ; 5. Plateau du client moyen (2 008 €).

Les deux premiers paramètres sont pilotables par design :
- **Mix de réussite → qualification d'entrée.** Le paramètre dominant n'est pas commercial mais un choix de **sélection des clients**. Barre minimale : baseline ≥ 4-6 K€/mois, offre déjà validée par des ventes, capacité de livraison existante (T10). Refuser un mauvais client vaut mieux que le signer : un « échec » consomme la capacité pour 5,2 K€.
- **Collecte → mécanique d'attribution** (6.7). Passer de 85 % à 60 % de collecte coûte 3,5 K€/client (T3) — soit davantage que la différence entre 10 % et 12,5 % de taux. **Mieux vaut un taux modeste parfaitement encaissable qu'un taux élevé contestable.**

## 6.6 Point mort vs 25 K€ et perspective client (T4, T8)

Pour égaler 25 K€ cash, le client doit générer 133-200 K€ de CA incrémental sur l'engagement (156-235 K€ avec collecte 85 %), soit +13-20 K€/mois au plateau : c'est le profil « fort ». Côté client (T8) : en échec, il perd 5,2 K€ au lieu de 25 K€ (**downside divisé par ~5**) ; en succès fort, il paie ~31 K€ > 25 K€. Ce surcoût conditionnel est le « prix de l'assurance » — à assumer explicitement en vente : « si vous payez plus cher que 25 K€, c'est que vous avez encaissé plus de 200 K€ de plus ». C'est l'argument de framing central de l'offre (§8).

## 6.7 Le problème d'attribution — cartographie opérationnelle

C'est LE point de défaillance du modèle (2e paramètre du tornado ; « la complexité d'attribution » est la raison pour laquelle le pricing à la performance ne représente que ~10-15 % des contrats d'agences — [clicksgeek.com](https://clicksgeek.com/performance-based-marketing-agency-pricing/)). Pratiques observées et base recommandée :

**Bases de calcul observées** (findings WS6) : % du cash collecté (closers FR : 10-20 % — [closerevolution.com](https://closerevolution.com/commissions-prometteuses-closing-se-mefier)) ; % du contrat apporté (apporteurs d'affaires : 5-15 % — [referaly.fr](https://www.referaly.fr/blog/commission-apporteur-affaires-quel-pourcentage.html)) ; % du CA généré (growth partners anglo : 10-35 %, zéro retainer, clients ≥10 K$/mois — [ThinkNaz](https://highimpct.com/growth-partner)) ; % du salaire annuel (recrutement : 15-25 % — le seul vertical FR où le success fee est la norme, car le résultat est binaire et incontestable).

**Base recommandée** (la plus défendable au vu des pratiques) : **% du cash effectivement encaissé, attribuable, au-dessus de la baseline contractuelle** (moyenne 3 mois précédant la signature), net de remboursements, après délai de rétractation, versé sous 30 jours après encaissement — c'est la mécanique standard closer-infopreneur documentée ([infolawyers.fr](https://infolawyers.fr/infopreneur-et-closer-comment-securiser-votre-collaboration/)). Éviter le « CA incrémental toutes causes » (contestable : le client dira « c'est ma saisonnalité ») comme le « % sur ventes closées par le canal géré » seul (le client déplacera ses ventes hors canal).

**Dispositif de mesure opérable** (à contractualiser AVANT signature) :
1. Accès lecture seule au processeur de paiement (Stripe) ou reporting mensuel contractuel avec droit d'audit sur pièces comptables ;
2. CRM/registre partagé des leads et ventes (le CRM est la première pièce produite en contentieux — [jurisprudence commissions](https://simpliciter.ai/fr/recherche/decision/sujet/commission-apporteur-daffaire/)) ;
3. Fenêtre d'attribution 60-180 jours post-engagement pour les ventes retardées (standards affiliation high-ticket : 60-90 j+ — [postaffiliatepro.com](https://www.postaffiliatepro.com/faq/how-long-do-affiliate-cookies-last/)) ;
4. Précédent documenté de mécanique simple qui fonctionne : rev-share 25-30 % 1re année, Google Sheet partagé, paiement Net 30 ([REX George Pu](https://founderreality.com/blog/the-revenue-sharing-partnership-model-that-scaled-my-consulting-to-35k-month)).

**Points de vigilance contractuels FR** (cartographie, pas conseil juridique — consulter un avocat avant le premier contrat) :
- **Requalification en agent commercial** : risque élargi depuis l'arrêt Trendsetteuse (2020) ; conséquence type = indemnité ~2 ans de commissions ([kohenavocats.fr](https://kohenavocats.fr/2026/04/28/contrat-apporteur-affaires-commission-rupture-requalification-agent-commercial/)). Mitigation structurelle : l'offre est un accompagnement global (stratégie + systèmes), pas une négociation de ventes pour le compte du client.
- **TVA 20 %** sur les commissions vers mandants FR ([cpfac.com](https://cpfac.com/quel-taux-de-tva-appliquer-sur-les-factures-de-commissions-d-un-agent-commercial/)).
- **Impayés** : celui qui refuse de payer en invoquant l'impayé de son propre client doit le prouver (pièces comptables) — prévoir la clause miroir.
- Clause de sortie : earn-out sur la fenêtre d'attribution si le client rompt avant terme ; clawback écrit sur remboursements.
- À noter : le conseil en stratégie FR rejette massivement le success fee (mesurabilité, indépendance — [Consultor](https://www.consultor.fr/articles/les-success-fees-n-ont-pas-la-cote)) : le consensus des praticiens qui le gardent est **hybride fixe + variable sur clients pré-validés** — précisément la structure 5 K€ + %.

## 6.8 Cash-flow et seuils de viabilité (T7, T10)

- **Creux de trésorerie** : en démarrage réaliste (2 clients/mois), l'hybride encaisse 74 K€ cumulés à M6 (vs 107 K€ en cash aux mêmes leads) — prévoir ~6 mois de charges personnelles ou 3-4 ventes d'amorçage à part fixe majorée.
- **Volume d'équilibre** : EV 16,8 K€/client → ~18 clients/an pour égaler 12 ventes cash à 25 K€ (300 K€). Avec un plafond solo de 10-12 clients actifs, l'objectif d'année 1 est 12-20 signatures, soit 100-300 K€ encaissés (cohérent avec le SOM, §2.4).
- **Discipline de portefeuille** : chaque client « échec » évité (qualification) vaut ~11,6 K€ d'EV relative (différence échec→moyen) ; c'est le levier n°1 du modèle, avant le marketing.

## 6.9 Le plan financier retenu : 5 K€ + 15 %, thèse de service ×3-4 (section décisionnelle)

Suite aux arbitrages du commanditaire, l'offre retenue est **5 000 € de setup + 15 % du cash incrémental encaissé** (sans mensualité), adossée à sa thèse de service : porter le client de 5-10 K€/mois à **25-35 K€/mois minimum en ~4 mois** (thèse opérationnelle interne — statut d'hypothèse à démontrer publiquement sur les 5-10 premiers clients, cf. F0). Plan financier complet, reproductible : [findings/ws-finance-plan.md](../findings/ws-finance-plan.md) ([models/finance_scenario.py](../models/finance_scenario.py)). L'essentiel :

**Par client (année 1, collecte 85 %)** : trajectoire 5→25 K€/mois = 210 K€ de cash incrémental → l'agence encaisse **31,8 K€** ; trajectoire 10→35 K€ = 262,5 K€ → **38,5 K€** (44,4 K€ à collecte parfaite — cohérent avec les 44 K€ HT/an de l'étude interne). Le client, lui, gagne 210-262 K€ en payant 32-38 K€ : **ROI client +550 à +580 %** — l'alignement qui fait vendre l'offre et tenir les renouvellements (année 2 perf-only : 30,6-38,3 K€/client).

**Le moteur (1 K€/jour)** : 25-66 signatures/mois (central 40), CAC 460-1 194 € (central **762 €**) — **le setup de 5 K€ rembourse le CAC dès la signature** : l'acquisition s'autofinance client par client. LTV/CAC 42-51× en thèse pleine, encore 16× dans le pire scénario de robustesse.

**Trajectoires (thèse pleine, 85 %)** : ramp prudent → 210 actifs fin M12, **CA an 1 : 3,32 M€**, an 2 : 9,93 M€ ; ramp volontariste → 300 actifs fin M12, **CA an 1 : 5,39 M€**, an 2 : 11,3 M€. Point mort opérationnel : M2-M4. **P&L à pleine capacité : 10,5 M€ de CA, EBITDA 61 %** (pub 3,5 %, vente 10 %, livraison 13,3 %, ops+management 12,3 %).

**Le test de robustesse — la table à montrer aux associés** (hypothèses dégradées : les clients hors-thèse finissent 50 % « partiels » à +8 K€/mois, 50 % « échecs » sortis à M4) :

| Part des clients atteignant 25-35 K€ | EV/client an 1 | CA à 300 actifs | EBITDA |
|---|---|---|---|
| 100 % (thèse pleine) | 35,1 K€ | 10,54 M€ | **61 %** |
| 70 % | 27,8 K€ | 8,34 M€ | **53 %** |
| 50 % | 22,9 K€ | 6,87 M€ | **45 %** |
| 30 % | 18,0 K€ | 5,40 M€ | **33 %** |

Lecture décisionnelle : **la thèse n'a pas besoin d'être vraie pour que l'entreprise soit très rentable — elle a besoin d'être vraie pour atteindre le scénario haut et alimenter la machine de preuve.** Même si un client sur deux seulement atteint l'objectif, l'EBITDA reste à 45 % ; même à 30 %, chaque client signé rapporte 18 K€ pour ~760 € d'acquisition. Sous ~30 % de réussite, le facteur limitant devient la réputation (études de cas, renouvellements), pas le P&L. Les deux protections structurelles de la thèse : la sélection à l'entrée (le funnel produit 40 signatures possibles pour 25 nécessaires → on choisit les meilleures baselines) et les 4 KPI de pilotage mensuel (rendement réel/client, ratio clients/coach ≥ 12-15, collecte ≥ 85 %, coût/call ≤ 170 €).

Cohérence avec le reste de la section : le modèle marché-calibré (§6.1-6.8, mix 30/45/25) reste le **stress-test de référence** — il correspond peu ou prou à la ligne « 30 % » du tableau ci-dessus, et le plan reste rentable à ce niveau. L'écart entre les deux lectures est exactement ce que les 5-10 premiers clients doivent trancher (jauges M4-M6, §10.2).
