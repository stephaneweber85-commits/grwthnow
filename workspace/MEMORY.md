# MEMORY.md — index des findings (pointeurs)

## Ancrage
- Benoit Michaud = @benoit.mchd, co-fondateur Les Copywriters & Scaling Circle. Claim marketing : « +10M€ collectés pour ses clients », « scale to 100K/mois ». Snapshot IG indexé : ~2 366 abonnés (à vérifier). → findings/benoit-michaud.md (workflow)

## Findings (à remplir au fil de l'eau)
- MODÈLE ÉCONOMIQUE (findings/ws6-model-output.md, généré par models/unit_economics.py) :
  - EV/client hybride 12,5% central ≈ 16,8K€ vs 25K cash → par client, le cash gagne.
  - MAIS à flux de leads égal (close 28% vs 12%), l'hybride génère +57% d'EV par 100 calls et croise durablement le cash à M12.
  - Contrainte cachée = CAPACITÉ de livraison (T6 : à capacité égale, cash gagne toujours).
  - Paramètre dominant (tornado) : mix de réussite clients (amplitude 9,4K€), puis collecte/attribution (4,9K€), puis taux de perf (4,7K€).
  - Breakeven vs 25K : le client doit générer 156-235K€ de CA incrémental sur 12 mois selon taux.
  - Downside client divisé par ~5 (5,2K vs 25K en cas d'échec) ; en cas de succès fort le client paie ~31K > 25K (« prix de l'assurance »).
  - Viabilité : ~18 clients hybrides actifs/an pour égaler 12 ventes cash à 25K ; qualification d'entrée obligatoire (baseline ≥4-6K€/mois).
- Workflow discovery (wf_b94d4287-7b8) : lancé, ~28 agents. Résultats attendus dans findings/.
