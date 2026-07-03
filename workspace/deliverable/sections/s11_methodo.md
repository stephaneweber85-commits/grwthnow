# 11. Sources, hypothèses & méthodologie

## 11.1 Méthodologie

**Dispositif.** Étude réalisée le 03/07/2026 sur infrastructure agentique (Claude Code) : 31 agents de recherche à contexte vierge (1 ancrage, 2 roster, 19 fiches acteurs, 2 sizing, 2 demande/influence, 1 success fee, 1 GTM, 1 réputation, + gap-fill), ~1 400 requêtes et lectures web, 100 % sources publiques gratuites (aucun achat, aucun franchissement de login/paywall), lecture seule. Modélisation économique : script Python reproductible ([models/unit_economics.py](../models/unit_economics.py)). Matière brute intégralement conservée dans [findings/](../findings/) (28 fichiers sourcés).

**Protocole de triangulation des revenus** (appliqué aux 19 acteurs, §5) : (1) source exacte et datée de chaque claim ; (2) qualification de nature (auto-déclaré / donnée légale / estimation tierce / calcul) ; (3) au moins deux méthodes indépendantes quand c'est possible — comptes déposés (annuaire-entreprises.data.gouv.fr, Pappers, societe.com, Companies House, CRO, e-krediidiinfo, BCE/KBO, companyweb.be) ET calcul bottom-up (audience datée × taux de conversion plausible 0,1-1 %/mois × prix) ET plausibilité (témoignages recoupables, taille d'équipe) ; (4) fourchette basse-haute + niveau de confiance ; (5) signalement systématique des incohérences. Règle : un chiffre à source unique auto-déclarée est toujours étiqueté « revendiqué, non vérifié ».

**Structure** : réponse d'abord (Pyramid Principle), sections MECE, sizing en double approche réconciliée, offre scorée sur l'équation de valeur, sensibilité sur les unit economics, Chain-of-Verification sur la recommandation (§1) et la section performances (§5) — les affirmations critiques ont été re-vérifiées par des agents indépendants sans accès au brouillon.

## 11.2 Hypothèses clés à challenger (registre)

| # | Hypothèse | Valeur retenue | Fragilité | Comment la tester |
|---|---|---|---|---|
| H1 | Appétence high-ticket de la cible qualifiée | 20-40 % | Aucune donnée publique | 50 premières conversations de vente |
| H2 | Propension d'achat annuelle | 8-15 %/an | Idem | Taux de réponse outbound qualifié |
| H3 | Close rate hybride vs cash | 20-38 % vs 8-18 % | Écart inféré de la défiance documentée, pas mesuré sur CE modèle (aucun verbatim FR acheteur sur le « fee + % ») | 20 premiers appels — jauge M6 (§10.2) |
| H4 | Mix de réussite clients 30/45/25 | Central | Dépend de la qualification réelle | Suivi mensuel du portefeuille (KPI §10.5) |
| H5 | Collecte effective du perf fee | 85 % | Dépend du contrat et des clients | Taux de collecte réel dès le client 1 |
| H6 | Plateaux d'incrément (moyen +6 K€/mois, fort +20 K€) | Modélisés | Calés sur les promesses/études de cas du marché, invérifiées | Résultats réels des 5 premiers clients |
| H7 | Marché coaching France 750 M€ (OPIIEC) | Fourchette élargie 0,4-0,75 Md€ | Source unique, construction multiplicative, en tension avec prorata ICF | Croisement avec la prochaine édition ICF/OPIIEC |
| H8 | Extension francophonie ×1,2 | Démographique | Pas de données BE/CH/QC dédiées | Non critique (la France domine le SOM) |
| H9 | Fourchettes de revenus estimés des acteurs | §5.2 | Bottom-up sensible au taux de conversion supposé (0,1-1 %) ; entités offshore invérifiables par construction | Non testable publiquement — c'est le point : personne ne peut prouver mieux |

## 11.3 Limites et données non trouvables (déclaration d'honnêteté)

- **Prix réels des offres à prix caché** (15 acteurs sur 19) : reconstitués via avis tiers, témoignages, interviews — jamais confirmés par les vendeurs. Marqués « estimation » partout.
- **Comptes des entités offshore** (Dubaï ×6, Fujairah, Hong Kong) : inexistants publiquement — les fourchettes reposent alors sur le seul bottom-up, à confiance dégradée. C'est une limite ET un résultat (l'opacité est un choix du marché, §5.3).
- **Pénétration du modèle à la performance en francophonie** : aucune donnée quantitative publique.
- **Verbatims d'acheteurs sur le modèle hybride fee+%** : introuvables publiquement (gap H3).
- **Trustpilot/Signal-Arnaques** : fetch direct bloqué (403) — compteurs et notes repris des index de recherche, avis non audités un à un.
- **Rapports Xerfi/Statista coaching** : paywall — utilisés uniquement via la presse qui les cite, ou écartés.
- **CA exacts confidentiels** (Squared, Scalezia — option PME) : seuls les résultats nets sont publics ; les CA restent estimés.
- Chiffres d'audience Instagram : snippets indexés (fetch direct bloqué), datés du 03/07/2026, précision ±10 %.

## 11.4 Index des sources primaires par catégorie

**Données légales et registres** : [annuaire-entreprises.data.gouv.fr](https://annuaire-entreprises.data.gouv.fr) ; [recherche-entreprises.api.gouv.fr](https://recherche-entreprises.api.gouv.fr) ; [Pappers](https://www.pappers.fr) ; [societe.com](https://www.societe.com) ; [Companies House UK](https://find-and-update.company-information.service.gov.uk) ; [CRO/solocheck Irlande](https://www.solocheck.ie) ; [e-krediidiinfo Estonie](https://www.e-krediidiinfo.ee) ; [KBO/BCE Belgique](https://kbopub.economie.fgov.be) ; [companyweb.be](https://www.companyweb.be) ; [URSSAF open data](https://open.urssaf.fr) ; [INSEE](https://www.insee.fr) ; [Bpifrance Création](https://bpifrance-creation.fr).
**Études sectorielles** : [ICF Global Coaching Study 2023](https://coachingfederation.org/wp-content/uploads/2023/04/2023ICFGlobalCoachingStudy_ExecutiveSummary.pdf) et [2025](https://www.coachfederation.fr/global-coaching-study-2025-de-licf/) ; [OPIIEC Coaching 2022](https://syntec-conseil.fr/wp-content/uploads/2022/10/OPIIEC_COACHING_Essentiels.pdf) ; [Syntec Conseil 2024-2025](https://syntec-conseil.fr/actualites/le-marche-du-conseil-en-france-2024-2025/) ; [PEPS portage 2025](https://www.peps-syndicat.fr/wp-content/uploads/2025/07/Rapport-de-branche-du-portage-salarial-2025.pdf) ; [Baromètre Achil 2025](https://www.achil.io/blog/barometre-recrutement-freelance-2025/).
**Enquêtes et régulation** : [DGCCRF influenceurs](https://www.economie.gouv.fr/actualites/influenceurs-bilan-des-controles-2022-et-2023-de-la-dgccrf) et [coaching bien-être](https://www.economie.gouv.fr/dgccrf/laction-de-la-dgccrf/les-enquetes/secteur-du-coaching-bien-etre-lenquete-de-la-dgccrf-releve) ; [loi influenceurs 2023](https://www.economie.gouv.fr/influenceur-createur-contenu-mesures-encadrement) ; [franceinfo 01/2026](https://www.franceinfo.fr/internet/reseaux-sociaux/enquete-c-est-un-mirage-la-formation-en-marketing-digital-ce-business-en-ligne-douteux-qui-promet-la-richesse-et-seduit-les-ados_7726411.html) ; [L'ADN 10/2025](https://www.ladn.eu/nouveaux-usages/pour-devenir-riche-cliquez-ici-enquete-chez-ceux-qui-ont-paye-leur-formation-business-en-ligne/) ; [Le Temps 01/2026](https://www.letemps.ch/suisse/d-etudiant-fauche-a-millionnaire-l-intrigante-recette-de-l-influenceur-suisse-yomi-denzel-pour-vendre-ses-formations-miracles) ; [Mr Mondialisation](https://mrmondialisation.org/coaching-pyramidal-larnaque-qui-veut-te-faire-passer-de-mcdo-a-millionnaire/) ; [Maddyness/PNF](https://www.maddyness.com/2026/01/14/oussama-ammar-le-co-fondateur-de-the-family-dans-le-viseur-du-parquet-national-financier-pour-fraude-fiscale/).
**Presse économique** : [Bilan.ch](https://www.bilan.ch/story/entrepreneurs-com-thang-nguyen-de-swissroc-rejoint-alec-henry-893004876403) ; [La Libre 02/2026](https://www.lalibre.be/economie/entreprises-startup/2026/02/03/le-business-du-coaching-dentrepreneurs-selon-marvin-ndiaye-mon-temps-est-limite-SL5KCA2V4VHYTAJWKZJPOVFDE4/) ; [Forbes.be 11/2025](https://www.forbes.be/fr/ultra-le-cercle-daffaires-ou-lentourage-et-lentraide-sont-ultra-importants/).
**Pratiques success fee** : [closerevolution](https://closerevolution.com/commissions-prometteuses-closing-se-mefier) ; [referaly](https://www.referaly.fr/blog/commission-apporteur-affaires-quel-pourcentage.html) ; [Consultor](https://www.consultor.fr/articles/les-success-fees-n-ont-pas-la-cote) ; [infolawyers](https://infolawyers.fr/infopreneur-et-closer-comment-securiser-votre-collaboration/) ; [kohenavocats](https://kohenavocats.fr/2026/04/28/contrat-apporteur-affaires-commission-rupture-requalification-agent-commercial/) ; [ThinkNaz](https://highimpct.com/growth-partner) ; [REX George Pu](https://founderreality.com/blog/the-revenue-sharing-partnership-model-that-scaled-my-consulting-to-35k-month).
**Acteurs** : l'ensemble des URLs primaires (sites, pages de vente, Skool, YouTube, podcasts, registres) est dans chaque fiche de [findings/](../findings/) — ~250 URLs uniques au total.
