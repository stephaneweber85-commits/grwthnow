#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit le PDF « dossier ultra complet » : rapport + annexes A-D."""
import re, subprocess, markdown, html
from pathlib import Path

WS = Path("/home/user/grwthnow/workspace")
OUT_HTML = WS / "deliverable" / "dossier_complet.html"
OUT_PDF = WS / "deliverable" / "etude_marche_growth_partner_perf_COMPLET.pdf"

def demote(md_text, levels=1):
    """Descend tous les titres d'un cran pour l'imbrication en annexe."""
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" * min(6, len(m.group(1)) + levels) + " ", md_text)

report = (WS / "deliverable" / "etude_marche_growth_partner_perf.md").read_text()

# ---------------- Annexes ----------------
annexes = []

annexes.append(("Annexe A — Modèle économique : hypothèses et tables complètes (T1-T10)",
                demote((WS / "findings" / "ws6-model-output.md").read_text())))

annexes.append(("Annexe A2 — Modèle scale : moteur payant 1 K€/jour, capacité 300 clients",
                demote((WS / "findings" / "ws-scale-model.md").read_text())))

annexes.append(("Annexe A3 — Plan financier : 5 K€ + 15 %, thèse ×3-4, test de robustesse et P&L",
                demote((WS / "findings" / "ws-finance-plan.md").read_text())))

annexes.append(("Annexe B — Chain-of-Verification : les 12 verdicts détaillés",
                demote((WS / "findings" / "cov-verdicts.md").read_text())))

FICHES = [
    ("benoit-michaud.md", "Benoit Michaud (ancrage WS1)"),
    ("benoit-michaud-joseph-atallah-scaling-circle-les-copywriters.md", "Benoit Michaud & Joseph Atallah — Scaling Circle / Les Copywriters (contre-fiche)"),
    ("karim-cherifi-agence-business-partner-business-partner-ia-dubai.md", "Karim Cherifi — Business Partner IA"),
    ("matis-clouet-the-ecosystem-dubai.md", "Matis Clouet — The Ecosystem"),
    ("marvin-ndiaye-marvin-ndaye-ultra-belgique.md", "Marvin Ndiaye — ULTRA"),
    ("antoine-blanco-abcorporate-freedom-operator-dubai.md", "Antoine Blanco — Freedom Operator"),
    ("alec-henry-entrepreneurs-com.md", "Alec Henry — Entrepreneurs.com"),
    ("franck-rocca-propulser.md", "Franck Rocca — Propulser"),
    ("jean-hollaender-webinaire-agency.md", "Jean Hollaender — Webinaire Agency / Liberty Webi"),
    ("matthias-nezzar-closing-agency-closing-school.md", "Matthias Nezzar — Closing Agency / Closing School"),
    ("romain-collignon-squared-incubateur-56-mastermind-67.md", "Romain Collignon — Squared"),
    ("maxime-augiat-scaling-max.md", "Maxime Augiat — Scaling MAX"),
    ("maxence-rigottier.md", "Maxence Rigottier"),
    ("scalezia-benoit-dubos.md", "Scalezia — Benoît Dubos"),
    ("enzo-honore-la-tribu.md", "Enzo Honoré — La Tribu"),
    ("sommetis.md", "Sommetis"),
    ("theo-lion-coudac.md", "Théo Lion — Coudac"),
    ("yomi-denzel.md", "Yomi Denzel — Mindeo"),
    ("max-piccinini.md", "Max Piccinini"),
    ("david-laroche.md", "David Laroche — Paradox"),
    ("addendum-cherifi-firsthand.md", "Addendum — donnée de première main sur Karim Cherifi (conditions réelles d'un contrat client, source confidentielle)"),
]
fiches_md = []
for i, (fname, title) in enumerate(FICHES, 1):
    p = WS / "findings" / fname
    if p.exists():
        fiches_md.append(f"## C.{i} — {title}\n\n" + demote(p.read_text(), 2))
annexes.append(("Annexe C — Fiches acteurs détaillées (recherche brute sourcée)", "\n\n".join(fiches_md)))

WS_FILES = [
    ("ws4-topdown.md", "D.1 — Sizing top-down (sources sectorielles)"),
    ("ws4-bottomup.md", "D.2 — Sizing bottom-up (populations et entonnoir)"),
    ("ws5-demande.md", "D.3 — Voix du client (verbatims, WTP, matière personas)"),
    ("ws5-influence.md", "D.4 — Carte d'influence de la cible"),
    ("ws6-successfee.md", "D.5 — Pratiques du success fee et attribution"),
    ("ws9-gtm.md", "D.6 — Go-to-market : funnels et économie des canaux"),
    ("ws-critique.md", "D.7 — Réputation, exposés, régulation (face B du marché)"),
    ("roster-a.md", "D.8 — Roster A : balayage écosystème (candidats bruts)"),
    ("roster-b.md", "D.9 — Roster B : balayage par plateformes (candidats bruts)"),
]
ws_md = []
for fname, title in WS_FILES:
    p = WS / "findings" / fname
    if p.exists():
        ws_md.append(f"## {title}\n\n" + demote(p.read_text(), 2))
annexes.append(("Annexe D — Dossiers workstreams (matière brute sourcée)", "\n\n".join(ws_md)))

full_md = report + "\n\n"
for title, body in annexes:
    full_md += f"\n\n# {title}\n\n{body}\n\n"

# ---------------- Conversion HTML ----------------
body_html = markdown.markdown(full_md, extensions=["tables", "toc", "sane_lists"], output_format="html5")

css = """
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body { font-family: 'DejaVu Sans', 'Liberation Sans', Arial, sans-serif; font-size: 9.6pt; line-height: 1.45; color: #1a1a1a; margin: 0; }
h1 { page-break-before: always; font-size: 17pt; color: #0f2b46; border-bottom: 2.5px solid #0f2b46; padding-bottom: 5px; margin: 0 0 14px 0; line-height: 1.25; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 12.5pt; color: #14385c; margin: 16px 0 7px 0; page-break-after: avoid; line-height: 1.3; }
h3 { font-size: 10.8pt; color: #1d4d7a; margin: 12px 0 5px 0; page-break-after: avoid; }
h4, h5, h6 { font-size: 10pt; color: #24557f; margin: 10px 0 4px 0; page-break-after: avoid; }
p { margin: 0 0 7px 0; text-align: justify; }
a { color: #14538c; text-decoration: none; word-break: break-all; }
strong { color: #0f2b46; }
blockquote { border-left: 3px solid #b8cbdd; margin: 8px 0; padding: 4px 12px; color: #33475c; background: #f4f7fa; }
ul, ol { margin: 4px 0 8px 0; padding-left: 20px; }
li { margin-bottom: 3px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px 0; font-size: 7.6pt; page-break-inside: auto; }
th, td { border: 0.6px solid #9db4c8; padding: 3px 4.5px; vertical-align: top; text-align: left; overflow-wrap: anywhere; }
th { background: #0f2b46; color: #ffffff; font-size: 7.6pt; }
tr:nth-child(even) td { background: #f1f5f9; }
hr { border: none; border-top: 1px solid #c9d6e2; margin: 14px 0; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.5pt; background: #eef2f6; padding: 0 3px; }
.cover { page-break-after: always; padding-top: 220px; text-align: center; }
.cover h1 { border: none; page-break-before: avoid; font-size: 24pt; line-height: 1.3; }
.cover .sub { font-size: 12pt; color: #33475c; margin-top: 18px; }
.cover .verdict { display: inline-block; margin-top: 46px; padding: 14px 30px; border: 2.5px solid #0f2b46; font-size: 13pt; font-weight: bold; color: #0f2b46; }
.cover .meta { margin-top: 60px; font-size: 9.5pt; color: #5a6b7c; line-height: 1.8; }
"""

cover = """
<div class="cover">
<h1>Accompagnement business<br/>à résultats partagés<br/>5 K€ de setup + 15 % à la performance</h1>
<div class="sub">Étude de marché décisionnelle — dossier complet avec annexes<br/>
Rapport (11 sections) · Plan financier & robustesse · Chain-of-Verification · 20 fiches acteurs · 9 dossiers workstreams</div>
<div class="verdict">VERDICT : GO CONDITIONNEL</div>
<div class="meta">Commanditaire : Stéphane Weber · 3 juillet 2026<br/>
Sources publiques gratuites exclusivement · ~250 URL sources · revenus des 19 acteurs triangulés<br/>
Vérification indépendante : 10 affirmations critiques sur 12 confirmées au chiffre près, 2 précisées, 0 contredite</div>
</div>
"""

html_doc = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8"><title>Étude de marché — accompagnement à résultats partagés (dossier complet)</title>
<style>{css}</style></head><body>{cover}{body_html}</body></html>"""

OUT_HTML.write_text(html_doc)
print(f"HTML : {len(html_doc)} chars → {OUT_HTML}")

r = subprocess.run([
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "--headless", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage",
    "--no-pdf-header-footer", "--virtual-time-budget=20000",
    f"--print-to-pdf={OUT_PDF}",
    f"file://{OUT_HTML}",
], capture_output=True, text=True, timeout=300)
print(r.stderr.strip()[-400:] if r.stderr else "(pas de stderr)")
print(f"PDF : {OUT_PDF.stat().st_size/1e6:.1f} Mo" if OUT_PDF.exists() else "ÉCHEC PDF")
