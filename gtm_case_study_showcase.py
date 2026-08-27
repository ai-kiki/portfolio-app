from __future__ import annotations

import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st

from case_study_showcase import _BASE_STYLES, _icon
from portfolio_navigation import render_portfolio_navigation


_YTTV_STYLES = """
<style>
.yttv-case .cs-hero { gap:1.5rem; grid-template-columns:.72fr 1.28fr; padding:clamp(1.5rem,3.5vw,2.7rem); }
.yttv-case .cs-hero h1 { font-size:clamp(1.75rem,3.2vw,2.65rem); letter-spacing:-.045em; line-height:1.04; margin:.7rem 0 .9rem; }
.yttv-case .cs-hero-copy > p { font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; }
.yttv-case .cs-kicker { font-size:clamp(1rem,1.55vw,1.25rem); letter-spacing:.055em; line-height:1.3; }
.yttv-meta-strip { background:var(--surface); border:1px solid var(--line); border-top:5px solid var(--deep); display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); margin:.8rem 0; }
.yttv-meta-strip article { min-height:118px; padding:1.35rem 1.25rem; }
.yttv-meta-strip article + article { border-left:1px solid var(--line); }
.yttv-meta-strip span { color:var(--muted); display:block; font-size:.74rem; font-weight:850; letter-spacing:.13em; margin-bottom:.65rem; text-transform:uppercase; }
.yttv-meta-strip strong { color:var(--ink); display:block; font-size:.98rem; line-height:1.45; }
.yttv-fit { display:grid; gap:.7rem; grid-template-columns:repeat(2,1fr); }
.yttv-fit article { background:var(--bg); border-radius:13px; min-height:145px; padding:1.15rem; }
.yttv-fit svg { color:var(--accent); height:28px; width:28px; }
.yttv-fit strong { display:block; font-size:1.03rem; margin:.65rem 0 .35rem; }
.yttv-fit p { color:var(--muted); font-size:.92rem; line-height:1.45; margin:0; }
.yttv-clock { display:grid; gap:.7rem; grid-template-columns:repeat(3,1fr); }
.yttv-clock article { background:rgba(255,255,255,.075); border:1px solid rgba(255,255,255,.15); border-radius:13px; min-height:160px; padding:1.2rem; }
.yttv-clock span { color:var(--highlight); display:block; font-size:.78rem; font-weight:850; letter-spacing:.06em; text-transform:uppercase; }
.yttv-clock strong { display:block; font-family:"Manrope",sans-serif; font-size:2rem; margin:.7rem 0 .35rem; }
.yttv-clock p { color:var(--hero-copy); font-size:.91rem; line-height:1.45; margin:0; }
.yttv-actions { display:grid; gap:.7rem; grid-template-columns:repeat(5,1fr); }
.yttv-actions article { border-top:3px solid var(--accent); min-height:200px; padding:1rem .85rem; }
.yttv-actions article:nth-child(even) { border-color:var(--highlight); }
.yttv-actions span { color:var(--accent); font-size:.75rem; font-weight:850; text-transform:uppercase; }
.yttv-actions strong { display:block; font-size:1rem; margin:.65rem 0 .45rem; }
.yttv-actions p { color:var(--muted); font-size:.88rem; line-height:1.45; margin:0; }
.yttv-proof { align-items:center; display:grid; gap:1rem; grid-template-columns:.75fr 1.25fr; }
.yttv-proof-mark { align-items:center; background:var(--accent-gradient); border-radius:16px; color:#fff; display:flex; flex-direction:column; justify-content:center; min-height:190px; padding:1.25rem; text-align:center; }
.yttv-proof-mark svg { height:38px; width:38px; }
.yttv-proof-mark strong { font-family:"Manrope",sans-serif; font-size:2.2rem; margin-top:.65rem; }
.yttv-proof-copy p { color:var(--muted); font-size:.98rem; line-height:1.6; }
.yttv-proof-copy ul { color:var(--muted); font-size:.94rem; line-height:1.5; margin:.55rem 0 0; padding-left:1.15rem; }
.yttv-proof-copy li { margin:.32rem 0; }
.yttv-disclosure { margin-top:1.8rem !important; }
.yttv-hero-visual { align-self:center; border:1px solid rgba(255,255,255,.2); border-radius:18px; box-shadow:0 22px 55px rgba(0,0,0,.24); margin:0; overflow:hidden; position:relative; z-index:1; }
.yttv-hero-visual img { display:block; height:auto; width:100%; }
.yttv-hero-visual figcaption { background:rgba(8,16,34,.9); color:var(--hero-muted); font-size:.76rem; line-height:1.4; padding:.65rem .8rem; }
@media(max-width:980px){.yttv-case .cs-hero{grid-template-columns:1fr}.yttv-meta-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.yttv-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.yttv-meta-strip article:nth-child(4){border-top:1px solid var(--line)}.yttv-actions{grid-template-columns:repeat(2,1fr)}.yttv-actions article:last-child{grid-column:1/-1}.yttv-clock{grid-template-columns:1fr}}
@media(max-width:760px){.yttv-meta-strip{grid-template-columns:1fr}.yttv-meta-strip article + article,.yttv-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.yttv-fit,.yttv-proof{grid-template-columns:1fr}.yttv-actions{grid-template-columns:1fr}.yttv-actions article:last-child{grid-column:auto}}
</style>
"""


_TWITCH_STYLES = """
<style>
.twitch-case .cs-hero { gap:1.5rem; grid-template-columns:.72fr 1.28fr; padding:clamp(1.5rem,3.5vw,2.7rem); }
.twitch-case .cs-hero h1 { font-size:clamp(1.75rem,3.2vw,2.65rem); letter-spacing:-.045em; line-height:1.04; margin:.7rem 0 .9rem; }
.twitch-case .cs-hero-copy > p { font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; }
.twitch-case .cs-kicker { font-size:clamp(1rem,1.55vw,1.25rem); letter-spacing:.055em; line-height:1.3; }
.twitch-meta-strip { background:var(--surface); border:1px solid var(--line); border-top:5px solid var(--accent); display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); margin:.8rem 0; }
.twitch-meta-strip article { min-height:118px; padding:1.35rem 1.25rem; }
.twitch-meta-strip article + article { border-left:1px solid var(--line); }
.twitch-meta-strip span { color:var(--muted); display:block; font-size:.74rem; font-weight:850; letter-spacing:.13em; margin-bottom:.65rem; text-transform:uppercase; }
.twitch-meta-strip strong { color:var(--ink); display:block; font-size:.98rem; line-height:1.45; }
.twitch-hero-visual { align-self:center; border:1px solid rgba(255,255,255,.2); border-radius:18px; box-shadow:0 22px 55px rgba(0,0,0,.24); margin:0; overflow:hidden; position:relative; z-index:1; }
.twitch-hero-visual img { display:block; height:auto; width:100%; }
.twitch-hero-visual figcaption { background:rgba(12,9,32,.92); color:var(--hero-muted); font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; padding:.8rem .95rem; }
.twitch-fit { display:grid; gap:.7rem; grid-template-columns:repeat(2,1fr); }
.twitch-fit article { background:var(--bg); border-radius:13px; min-height:145px; padding:1.15rem; }
.twitch-fit svg { color:var(--accent); height:28px; width:28px; }
.twitch-fit strong { display:block; font-size:1.03rem; margin:.65rem 0 .35rem; }
.twitch-fit p { color:var(--muted); font-size:.92rem; line-height:1.45; margin:0; }
.twitch-metrics { display:grid; gap:.7rem; grid-template-columns:repeat(4,1fr); }
.twitch-metrics article { background:rgba(255,255,255,.075); border:1px solid rgba(255,255,255,.15); border-radius:13px; min-height:155px; padding:1.15rem; }
.twitch-metrics strong { color:#fff; display:block; font-family:"Manrope",sans-serif; font-size:2rem; margin-bottom:.45rem; }
.twitch-metrics span { color:var(--highlight); display:block; font-size:.77rem; font-weight:850; letter-spacing:.07em; margin-bottom:.45rem; text-transform:uppercase; }
.twitch-metrics p { color:var(--hero-copy); font-size:.89rem; line-height:1.45; margin:0; }
.twitch-actions { display:grid; gap:.7rem; grid-template-columns:repeat(5,1fr); }
.twitch-actions article { border-top:3px solid var(--accent); min-height:205px; padding:1rem .85rem; }
.twitch-actions article:nth-child(even) { border-color:var(--highlight); }
.twitch-actions span { color:var(--accent); font-size:.75rem; font-weight:850; text-transform:uppercase; }
.twitch-actions strong { display:block; font-size:1rem; margin:.65rem 0 .45rem; }
.twitch-actions p { color:var(--muted); font-size:.88rem; line-height:1.45; margin:0; }
.twitch-proof { align-items:center; display:grid; gap:1rem; grid-template-columns:.75fr 1.25fr; }
.twitch-proof-mark { align-items:center; background:var(--accent-gradient); border-radius:16px; color:#fff; display:flex; flex-direction:column; justify-content:center; min-height:190px; padding:1.25rem; text-align:center; }
.twitch-proof-mark svg { height:38px; width:38px; }
.twitch-proof-mark strong { font-family:"Manrope",sans-serif; font-size:2.45rem; margin-top:.6rem; }
.twitch-proof-mark span { font-size:.85rem; line-height:1.4; }
.twitch-proof-copy p { color:var(--muted); font-size:.98rem; line-height:1.6; }
.twitch-proof-copy ul { color:var(--muted); font-size:.94rem; line-height:1.5; margin:.55rem 0 0; padding-left:1.15rem; }
.twitch-proof-copy li { margin:.32rem 0; }
.twitch-disclosure { margin-top:1.8rem !important; }
@media(max-width:980px){.twitch-case .cs-hero{grid-template-columns:1fr}.twitch-meta-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.twitch-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.twitch-meta-strip article:nth-child(4){border-top:1px solid var(--line)}.twitch-actions{grid-template-columns:repeat(2,1fr)}.twitch-actions article:last-child{grid-column:1/-1}.twitch-metrics{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.twitch-meta-strip{grid-template-columns:1fr}.twitch-meta-strip article + article,.twitch-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.twitch-fit,.twitch-proof,.twitch-metrics{grid-template-columns:1fr}.twitch-actions{grid-template-columns:1fr}.twitch-actions article:last-child{grid-column:auto}}
</style>
"""


_MATRIX_STYLES = """
<style>
.matrix-case .cs-hero { gap:1.5rem; grid-template-columns:.72fr 1.28fr; padding:clamp(1.5rem,3.5vw,2.7rem); }
.matrix-case .cs-hero h1 { font-size:clamp(1.75rem,3.2vw,2.65rem); letter-spacing:-.045em; line-height:1.04; margin:.7rem 0 .9rem; }
.matrix-case .cs-hero-copy > p { font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; }
.matrix-case .cs-kicker { font-size:clamp(1rem,1.55vw,1.25rem); letter-spacing:.055em; line-height:1.3; }
.matrix-hero-visual { align-self:center; border:1px solid rgba(255,255,255,.2); border-radius:18px; box-shadow:0 22px 55px rgba(0,0,0,.24); margin:0; overflow:hidden; position:relative; z-index:1; }
.matrix-hero-visual img { display:block; height:auto; width:100%; }
.matrix-hero-visual figcaption { background:rgba(7,24,52,.93); color:var(--hero-muted); font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; padding:.8rem .95rem; }
.matrix-meta-strip { background:var(--surface); border:1px solid var(--line); border-top:5px solid var(--accent); display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); margin:.8rem 0; }
.matrix-meta-strip article { min-height:118px; padding:1.35rem 1.25rem; }
.matrix-meta-strip article + article { border-left:1px solid var(--line); }
.matrix-meta-strip span { color:var(--muted); display:block; font-size:.74rem; font-weight:850; letter-spacing:.13em; margin-bottom:.65rem; text-transform:uppercase; }
.matrix-meta-strip strong { color:var(--ink); display:block; font-size:.98rem; line-height:1.45; }
.matrix-logic { display:grid; gap:.7rem; grid-template-columns:repeat(2,1fr); }
.matrix-logic article { background:var(--bg); border-radius:13px; min-height:145px; padding:1.15rem; }
.matrix-logic svg { color:var(--accent); height:28px; width:28px; }
.matrix-logic strong { display:block; font-size:1.03rem; margin:.65rem 0 .35rem; }
.matrix-logic p { color:var(--muted); font-size:.92rem; line-height:1.45; margin:0; }
.matrix-metrics { display:grid; gap:.7rem; grid-template-columns:repeat(4,1fr); }
.matrix-metrics article { background:rgba(255,255,255,.075); border:1px solid rgba(255,255,255,.15); border-radius:13px; min-height:155px; padding:1.15rem; }
.matrix-metrics strong { color:#fff; display:block; font-family:"Manrope",sans-serif; font-size:2rem; margin-bottom:.45rem; }
.matrix-metrics span { color:var(--highlight); display:block; font-size:.77rem; font-weight:850; letter-spacing:.07em; margin-bottom:.45rem; text-transform:uppercase; }
.matrix-metrics p { color:var(--hero-copy); font-size:.89rem; line-height:1.45; margin:0; }
.matrix-actions { display:grid; gap:.7rem; grid-template-columns:repeat(5,1fr); }
.matrix-actions article { border-top:3px solid var(--accent); min-height:205px; padding:1rem .85rem; }
.matrix-actions article:nth-child(even) { border-color:var(--highlight); }
.matrix-actions span { color:var(--accent); font-size:.75rem; font-weight:850; text-transform:uppercase; }
.matrix-actions strong { display:block; font-size:1rem; margin:.65rem 0 .45rem; }
.matrix-actions p { color:var(--muted); font-size:.88rem; line-height:1.45; margin:0; }
.matrix-proof { align-items:center; display:grid; gap:1rem; grid-template-columns:.75fr 1.25fr; }
.matrix-proof-mark { align-items:center; background:var(--accent-gradient); border-radius:16px; color:#fff; display:flex; flex-direction:column; justify-content:center; min-height:190px; padding:1.25rem; text-align:center; }
.matrix-proof-mark svg { height:38px; width:38px; }
.matrix-proof-mark strong { font-family:"Manrope",sans-serif; font-size:2.45rem; margin-top:.6rem; }
.matrix-proof-mark span { font-size:.85rem; line-height:1.4; }
.matrix-proof-copy p { color:var(--muted); font-size:.98rem; line-height:1.6; }
.matrix-proof-copy ul { color:var(--muted); font-size:.94rem; line-height:1.5; margin:.55rem 0 0; padding-left:1.15rem; }
.matrix-proof-copy li { margin:.32rem 0; }
.matrix-disclosure { margin-top:1.8rem !important; }
@media(max-width:980px){.matrix-case .cs-hero{grid-template-columns:1fr}.matrix-meta-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.matrix-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.matrix-meta-strip article:nth-child(4){border-top:1px solid var(--line)}.matrix-actions{grid-template-columns:repeat(2,1fr)}.matrix-actions article:last-child{grid-column:1/-1}.matrix-metrics{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.matrix-meta-strip{grid-template-columns:1fr}.matrix-meta-strip article + article,.matrix-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.matrix-logic,.matrix-proof,.matrix-metrics{grid-template-columns:1fr}.matrix-actions{grid-template-columns:1fr}.matrix-actions article:last-child{grid-column:auto}}
</style>
"""


_PLAYBOOK_STYLES = """
<style>
.playbook-case .cs-hero { gap:1.5rem; grid-template-columns:.72fr 1.28fr; padding:clamp(1.5rem,3.5vw,2.7rem); }
.playbook-case .cs-hero h1 { font-size:clamp(1.75rem,3.2vw,2.65rem); letter-spacing:-.045em; line-height:1.04; margin:.7rem 0 .9rem; }
.playbook-case .cs-hero-copy > p { font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; }
.playbook-case .cs-kicker { font-size:clamp(1rem,1.55vw,1.25rem); letter-spacing:.055em; line-height:1.3; }
.playbook-hero-visual { align-self:center; border:1px solid rgba(255,255,255,.2); border-radius:18px; box-shadow:0 22px 55px rgba(0,0,0,.24); margin:0; overflow:hidden; position:relative; z-index:1; }
.playbook-hero-visual img { display:block; height:auto; width:100%; }
.playbook-hero-visual figcaption { background:rgba(34,16,24,.94); color:var(--hero-muted); font-size:clamp(.92rem,1.25vw,1.05rem); line-height:1.52; padding:.8rem .95rem; }
.playbook-meta-strip { background:var(--surface); border:1px solid var(--line); border-top:5px solid var(--accent); display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); margin:.8rem 0; }
.playbook-meta-strip article { min-height:118px; padding:1.35rem 1.25rem; }
.playbook-meta-strip article + article { border-left:1px solid var(--line); }
.playbook-meta-strip span { color:var(--muted); display:block; font-size:.74rem; font-weight:850; letter-spacing:.13em; margin-bottom:.65rem; text-transform:uppercase; }
.playbook-meta-strip strong { color:var(--ink); display:block; font-size:.98rem; line-height:1.45; }
.playbook-topics { display:grid; gap:.7rem; grid-template-columns:repeat(2,1fr); }
.playbook-topics article { background:var(--bg); border-radius:13px; min-height:145px; padding:1.15rem; }
.playbook-topics svg { color:var(--accent); height:28px; width:28px; }
.playbook-topics strong { display:block; font-size:1.03rem; margin:.65rem 0 .35rem; }
.playbook-topics p { color:var(--muted); font-size:.92rem; line-height:1.45; margin:0; }
.playbook-metrics { display:grid; gap:.7rem; grid-template-columns:repeat(4,1fr); }
.playbook-metrics article { background:rgba(255,255,255,.075); border:1px solid rgba(255,255,255,.15); border-radius:13px; min-height:155px; padding:1.15rem; }
.playbook-metrics strong { color:#fff; display:block; font-family:"Manrope",sans-serif; font-size:2rem; margin-bottom:.45rem; }
.playbook-metrics span { color:var(--highlight); display:block; font-size:.77rem; font-weight:850; letter-spacing:.07em; margin-bottom:.45rem; text-transform:uppercase; }
.playbook-metrics p { color:var(--hero-copy); font-size:.89rem; line-height:1.45; margin:0; }
.playbook-actions { display:grid; gap:.7rem; grid-template-columns:repeat(5,1fr); }
.playbook-actions article { border-top:3px solid var(--accent); min-height:205px; padding:1rem .85rem; }
.playbook-actions article:nth-child(even) { border-color:var(--highlight); }
.playbook-actions span { color:var(--accent); font-size:.75rem; font-weight:850; text-transform:uppercase; }
.playbook-actions strong { display:block; font-size:1rem; margin:.65rem 0 .45rem; }
.playbook-actions p { color:var(--muted); font-size:.88rem; line-height:1.45; margin:0; }
.playbook-proof { align-items:center; display:grid; gap:1rem; grid-template-columns:.75fr 1.25fr; }
.playbook-proof-mark { align-items:center; background:var(--accent-gradient); border-radius:16px; color:#fff; display:flex; flex-direction:column; justify-content:center; min-height:190px; padding:1.25rem; text-align:center; }
.playbook-proof-mark svg { height:38px; width:38px; }
.playbook-proof-mark strong { font-family:"Manrope",sans-serif; font-size:2.1rem; margin-top:.6rem; }
.playbook-proof-mark span { font-size:.85rem; line-height:1.4; }
.playbook-proof-copy p { color:var(--muted); font-size:.98rem; line-height:1.6; }
.playbook-proof-copy ul { color:var(--muted); font-size:.94rem; line-height:1.5; margin:.55rem 0 0; padding-left:1.15rem; }
.playbook-proof-copy li { margin:.32rem 0; }
.playbook-disclosure { margin-top:1.8rem !important; }
@media(max-width:980px){.playbook-case .cs-hero{grid-template-columns:1fr}.playbook-meta-strip{grid-template-columns:repeat(2,minmax(0,1fr))}.playbook-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.playbook-meta-strip article:nth-child(4){border-top:1px solid var(--line)}.playbook-actions{grid-template-columns:repeat(2,1fr)}.playbook-actions article:last-child{grid-column:1/-1}.playbook-metrics{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.playbook-meta-strip{grid-template-columns:1fr}.playbook-meta-strip article + article,.playbook-meta-strip article:nth-child(3){border-left:0;border-top:1px solid var(--line)}.playbook-topics,.playbook-proof,.playbook-metrics{grid-template-columns:1fr}.playbook-actions{grid-template-columns:1fr}.playbook-actions article:last-child{grid-column:auto}}
</style>
"""


def render_youtube_tv_case_study() -> None:
    render_portfolio_navigation()
    hero_path = Path(__file__).resolve().parent / "assets" / "youtube-tv-launch-hero.png"
    hero_src = "data:image/png;base64," + base64.b64encode(hero_path.read_bytes()).decode("ascii")
    contributions = [
        "Ad Operations team leadership",
        "Launch planning",
        "SOP development",
        "Product-fit criteria",
        "Process translation",
        "Sales training",
        "Client one-sheet",
        "Client training",
        "Launch support",
    ]
    contribution_html = "".join(f"<span>{item}</span>" for item in contributions)
    st.markdown(
        _BASE_STYLES
        + _YTTV_STYLES
        + dedent(f"""
        <div class="cs-shell yttv-case" style="--bg:#f3f5f8;--surface:#ffffff;--soft:#e5ecf7;--ink:#17233d;--muted:#637087;--line:#d5dce8;--deep:#101a32;--accent:#d83333;--highlight:#74c9e8;--glow:#d83333;--hero-copy:#dce5f4;--hero-muted:#b9c7dd;--shadow:rgba(16,26,50,.08);--accent-gradient:linear-gradient(135deg,#d83333,#a91f36);--bar-gradient:linear-gradient(90deg,#d83333,#74c9e8);--hero-radius:26px 8px 26px 8px;--card-radius:18px 6px 18px 6px;--section-radius:22px 7px 22px 7px;--icon-radius:50%;--kpi-count:4;--channel-count:3;--ring:100%;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/GTM_Strategy_and_Sales_Enablement" target="_self"><i>GTM</i> Portfolio case study</a><span class="cs-category">Sales Enablement</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">YouTube TV product launch · July 2023</span><h1>Turning new inventory into a <em>launch-ready sales process</em></h1><p>Google introduced YouTube TV inventory, and our organization began selling it the following week. As the manager of the Ad Operations team responsible for execution, I translated unfamiliar restrictions into qualification guidance, an operating process, and sales and client enablement that supported successful campaign launches.</p></div>
              <figure class="yttv-hero-visual"><img src="{hero_src}" alt="Sales professionals attending a YouTube TV launch-readiness training in a conference room, paired with a four-step launch process graphic"><figcaption>Translating product requirements into qualification, training, and launch readiness.</figcaption></figure>
            </section>
            <section class="yttv-meta-strip">
              <article><span>Project role</span><strong>Ad Operations Manager &amp; Team Lead</strong></article>
              <article><span>Initiative</span><strong>Internal GTM Initiative · Cox Media</strong></article>
              <article><span>Primary audience</span><strong>Sales Consultants, Sales Leaders, Digital Support Team &amp; Advertisers</strong></article>
              <article><span>Core deliverables</span><strong>Launch Plan, SOP, One-Sheet &amp; Training</strong></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The launch risk</small><h2>A familiar platform with unfamiliar rules</h2></div></div><div class="cs-list">
                <div>{_icon('search')}<p><strong>Limited inventory</strong><span>Availability had to be confirmed before every YouTube TV campaign.</span></p></div>
                <div>{_icon('calendar')}<p><strong>More lead time</strong><span>Google's internal inventory reservation and operational processes extended the normal fulfillment cycle.</span></p></div>
                <div>{_icon('target')}<p><strong>Different advertiser fit</strong><span>Clients had to accept broader targeting and flexible delivery expectations.</span></p></div>
                <div>{_icon('megaphone')}<p><strong>Immediate readiness need</strong><span>Sales needed accurate guidance before recommending the new inventory.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('users')}</span><div><small>Product-fit strategy</small><h2>Interest alone did not make an advertiser ready</h2></div></div><div class="yttv-fit">
                <article>{_icon('target')}<strong>Broader targeting</strong><p>Advertisers needed to loosen narrow audience requirements.</p></article>
                <article>{_icon('money')}<strong>Flexible delivery</strong><p>Fixed CPMs and guaranteed impression delivery were not available.</p></article>
                <article>{_icon('megaphone')}<strong>No ad-copy changes</strong><p>Advertisers had to approve final creative before submission because ad copy could not be revised.</p></article>
                <article>{_icon('calendar')}<strong>Deadline discipline</strong><p>Inputs and approvals had to arrive while inventory was still available.</p></article>
              </div></article>
            </section>
            <section class="cs-dark"><div class="cs-section-heading"><small>Expectation setting</small><h2>One workflow. Three timing realities.</h2></div><div class="yttv-clock">
              <article><span>Ad Operations standard</span><strong>5 business days</strong><p>Our team's normal SLA for Google- and Amazon-related campaigns, from receipt through setup, quality control, and launch.</p></article>
              <article><span>When everything aligned</span><strong>7–10 business days</strong><p>YouTube TV could launch faster when inventory, materials, and approvals remained aligned.</p></article>
              <article><span>Early launch guidance</span><strong>15 business days</strong><p>Three broadcast calendar weeks allowed for mandatory checks and Google-side dependencies.</p></article>
            </div><p style="color:var(--hero-copy);font-size:.92rem;line-height:1.55;margin:1rem 0 0;">During the first 60 days, launches generally approached the 15-business-day window. The added time reflected Google's internal inventory-confirmation and approval processes—not delays in Ad Operations setup, quality control, or execution. When every requirement aligned, the same launch path could be completed in seven to ten business days.</p></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('network')}</span><div><small>How the work unfolded</small><h2>From product briefing to repeatable execution</h2></div></div><div class="yttv-actions">
              <article><span>01 · Learn</span><strong>Identify what changed</strong><p>I translated Product's briefing into the inventory, restriction, timing, and execution requirements teams needed to act on.</p></article>
              <article><span>02 · Define</span><strong>Clarify advertiser fit</strong><p>Converted product limitations into practical criteria Sales could use before recommending YTTV.</p></article>
              <article><span>03 · Build</span><strong>Create the operating path</strong><p>I developed the launch plan and end-to-end SOP around the existing DV360 workflow.</p></article>
              <article><span>04 · Equip</span><strong>Prepare Sales and clients</strong><p>Created the one-sheet and delivered live, recorded, and requested client training.</p></article>
              <article><span>05 · Reinforce</span><strong>Protect launch viability</strong><p>Used office hours and real-time guidance to address timing and inventory risk after rollout.</p></article>
            </div><p class="cs-note">This sequence organizes the actions that occurred; it does not claim a formal methodology was used at the time.</p></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('briefcase')}</span><div><small>Enablement system</small><h2>Each deliverable answered a different launch question</h2></div></div><div class="cs-flow">
              <article><div>{_icon('megaphone')}<span>Training</span></div><p>Explained fulfillment, execution, product fit, and the new process to Sales.</p></article>{_icon('arrow')}<article><div>{_icon('monitor')}<span>One-sheet</span></div><p>Consolidated restrictions, budgets, targeting, required inputs, deadlines, and lead times.</p></article>{_icon('arrow')}<article><div>{_icon('network')}<span>SOP + support</span></div><p>Created repeatability through the launch plan, documented process, recording, client training, and office hours.</p></article>
            </div></section>
            <section class="cs-grid-2 cs-full">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('shield')}</span><div><small>Judgment in practice</small><h2>Recheck inventory or risk the launch</h2></div></div><p style="color:var(--muted);font-size:.98rem;line-height:1.65;margin:0;">A salesperson submitted an insertion order six business days after the original inventory check. Because limited inventory might be gone before Ad Operations reached the order, we recommended a new check. The recommendation created short-term friction, but it avoided treating outdated availability as a launch commitment.</p></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('check')}</span><div><small>Evidence of value</small><h2>Quality held steady through a new rollout</h2></div></div><div class="yttv-proof"><div class="yttv-proof-mark">{_icon('check')}<strong>98%</strong><span>Team accuracy rate maintained overall</span></div><div class="yttv-proof-copy"><p>All YouTube TV campaigns launched, with no Ad Operations-related launch failures.</p><p>The qualification process also identified advertisers whose campaign strategy did not align with Google's YouTube TV inventory restrictions:</p><ul><li>Broader audience targeting</li><li>Ad-copy and trafficking limitations</li><li>Flexibility around CPMs and fixed-impression delivery</li></ul><p>Issues that occurred were tied to Google's internal dependencies rather than Ad Operations execution.</p></div></div></article>
            </section>
            <section class="cs-bottom"><article class="cs-contribution"><div><small>My strategic contribution</small><h2>I built the launch system and led the team responsible for executing it.</h2></div><div class="cs-capabilities">{contribution_html}</div></article><article class="cs-takeaway">{_icon('lightbulb')}<small>Strategic takeaway</small><p>New inventory becomes sellable when teams can identify the right customer, explain the tradeoffs, and execute against a shared timeline.</p></article></section>
            <p class="cs-disclosure yttv-disclosure">Formal project-specific performance metrics were not tracked. Outcome statements are based on successful campaign launches, the absence of Ad Operations-related launch failures, and observed use of the qualification process.</p>
            <a class="cs-back" href="/GTM_Strategy_and_Sales_Enablement" target="_self">&larr; Return to GTM Strategy &amp; Sales Enablement</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )


def render_twitch_sales_enablement_case_study() -> None:
    render_portfolio_navigation()
    hero_path = Path(__file__).resolve().parent / "assets" / "twitch-sales-enablement-hero.png"
    hero_src = "data:image/png;base64," + base64.b64encode(hero_path.read_bytes()).decode("ascii")
    contributions = [
        "Opportunity identification",
        "Cross-market research",
        "Audience-fit strategy",
        "Training design",
        "Slide adaptation",
        "Live facilitation",
        "Sales coaching",
        "Client-call support",
        "Campaign activation",
    ]
    contribution_html = "".join(f"<span>{item}</span>" for item in contributions)
    st.markdown(
        _BASE_STYLES
        + _TWITCH_STYLES
        + dedent(f"""
        <div class="cs-shell twitch-case" style="--bg:#f5f3fa;--surface:#ffffff;--soft:#e9e4f5;--ink:#1d1833;--muted:#6e6780;--line:#ddd7e9;--deep:#171029;--accent:#7651c9;--highlight:#ea8b72;--glow:#7651c9;--hero-copy:#e9e3f4;--hero-muted:#c9bedb;--shadow:rgba(23,16,41,.09);--accent-gradient:linear-gradient(135deg,#8460dc,#51309f);--bar-gradient:linear-gradient(90deg,#7651c9,#ea8b72);--hero-radius:26px 8px 26px 8px;--card-radius:18px 6px 18px 6px;--section-radius:22px 7px 22px 7px;--icon-radius:50%;--kpi-count:4;--channel-count:3;--ring:100%;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/GTM_Strategy_and_Sales_Enablement" target="_self"><i>GTM</i> Portfolio case study</a><span class="cs-category">Pitch Decks &amp; Training</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">Twitch sales enablement · 2022</span><h1>Turning an available product into a <em>sellable story</em></h1><p>Twitch was already available through Amazon DSP, but product familiarity had not translated into confident selling. As Marketing Manager, Digital Strategy, I independently designed an experiential training that connected platform culture, audience behavior, and advertiser fit—then supported Sales as the opportunity moved into client conversations and live campaigns.</p></div>
              <figure class="twitch-hero-visual"><img src="{hero_src}" alt="A marketing manager leading an audience and advertiser fit training for media sales professionals"><figcaption>Showing the end-user experience helped sellers connect platform culture to advertiser fit.</figcaption></figure>
            </section>
            <section class="twitch-meta-strip">
              <article><span>Project role</span><strong>Marketing Manager, Digital Strategy</strong></article>
              <article><span>Initiative</span><strong>Internal Sales Enablement · Cox Media</strong></article>
              <article><span>Primary audience</span><strong>Sales Consultants, Sales Leadership, Digital Support &amp; Marketing</strong></article>
              <article><span>Core deliverables</span><strong>Live Demo, Adapted Slides, Recorded Training &amp; Sales Support</strong></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The enablement gap</small><h2>Availability did not equal sales readiness</h2></div></div><div class="cs-list">
                <div>{_icon('briefcase')}<p><strong>A tactic inside a larger portfolio</strong><span>Twitch had been introduced as part of Amazon's broader advertising offering rather than as a distinct sales story.</span></p></div>
                <div>{_icon('megaphone')}<p><strong>Limited pitch confidence</strong><span>Sellers knew the name, but needed a clearer way to explain the experience and opportunity to advertisers.</span></p></div>
                <div>{_icon('users')}<p><strong>An unfamiliar culture</strong><span>The platform's creators, communities, and interactive viewing behavior were difficult to convey through standard product slides alone.</span></p></div>
                <div>{_icon('search')}<p><strong>A visible adoption opportunity</strong><span>I reviewed how other regional sales offices were using Twitch and identified a practical reinforcement opportunity for our team.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('target')}</span><div><small>Audience-fit strategy</small><h2>Match the platform to the advertiser—not every advertiser to the platform</h2></div></div><div class="twitch-fit">
                <article>{_icon('users')}<strong>Younger audiences</strong><p>Twitch offered access to highly engaged viewers, with 70% of viewers ages 18–34.</p></article>
                <article>{_icon('monitor')}<strong>Experiential learning</strong><p>A live platform tour made its content, creators, and community dynamics tangible.</p></article>
                <article>{_icon('check')}<strong>Strong-fit categories</strong><p>Education, technology, recruiting, automotive, finance, events, and healthcare recruiting.</p></article>
                <article>{_icon('shield')}<strong>Brand-fit boundaries</strong><p>Highly conservative or tightly controlled brands required closer brand-safety and cultural-fit evaluation.</p></article>
              </div></article>
            </section>
            <section class="cs-dark"><div class="cs-section-heading"><small>From training to activation</small><h2>A focused session created visible selling momentum.</h2></div><div class="twitch-metrics">
              <article><strong>24</strong><span>Total attendees</span><p>Sales, Sales leadership, Digital Support, and Marketing participated.</p></article>
              <article><strong>14</strong><span>Sales Consultants</span><p>The primary group responsible for taking the story into advertiser conversations.</p></article>
              <article><strong>6</strong><span>Campaigns launched</span><p>Six advertiser commitments were confirmed and every campaign ran.</p></article>
              <article><strong>≈30 days</strong><span>Activation window</span><p>The six commitments followed within about a month of the training.</p></article>
            </div></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('network')}</span><div><small>How the work unfolded</small><h2>From an observed gap to active client conversations</h2></div></div><div class="twitch-actions">
              <article><span>01 · Spot</span><strong>Identify the selling gap</strong><p>I recognized that prior Amazon training had created awareness, but not a compelling way to pitch Twitch.</p></article>
              <article><span>02 · Map</span><strong>Define audience and fit</strong><p>I studied the platform and use in other sales offices, then connected audience behavior to relevant advertiser categories.</p></article>
              <article><span>03 · Design</span><strong>Build the experience</strong><p>Over two days, I mapped the session, selected the story flow, and adapted the slides needed to reinforce it.</p></article>
              <article><span>04 · Demonstrate</span><strong>Make the platform tangible</strong><p>I led a 90-minute recorded session with a live walkthrough of content, creators, targeting, campaign setup, and fit.</p></article>
              <article><span>05 · Activate</span><strong>Support the next conversation</strong><p>Sellers began pitching Twitch and invited me into client calls as the subject-matter expert.</p></article>
            </div><p class="cs-note">This sequence organizes the actions that occurred; it does not claim a formal methodology was used at the time.</p></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('briefcase')}</span><div><small>Enablement system</small><h2>Each component helped move knowledge closer to action</h2></div></div><div class="cs-flow">
              <article><div>{_icon('monitor')}<span>Live platform demo</span></div><p>Replaced abstraction with a first-hand look at Twitch content, creators, categories, and viewer behavior.</p></article>{_icon('arrow')}<article><div>{_icon('megaphone')}<span>Adapted story</span></div><p>Updated selected slides and paired them with existing Product one-sheets to clarify the pitch and campaign mechanics.</p></article>{_icon('arrow')}<article><div>{_icon('users')}<span>Sales reinforcement</span></div><p>Extended the session through the recording, follow-up coaching, and direct participation in client conversations.</p></article>
            </div></section>
            <section class="cs-grid-2 cs-full">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('shield')}</span><div><small>Judgment in practice</small><h2>Relevance mattered more than forcing adoption</h2></div></div><p style="color:var(--muted);font-size:.98rem;line-height:1.65;margin:0;">The goal was not to position Twitch as a universal answer. I gave sellers a practical way to distinguish strong-fit advertisers from brands whose audience, tone, or brand-safety requirements did not align with the environment. That made the training a qualification tool as well as a pitch resource.</p></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('check')}</span><div><small>Evidence of value</small><h2>The story moved from the room into market</h2></div></div><div class="twitch-proof"><div class="twitch-proof-mark">{_icon('check')}<strong>6</strong><span>confirmed advertiser campaigns launched</span></div><div class="twitch-proof-copy"><p>Within about 30 days, six advertisers committed to Twitch campaigns—and all six campaigns ran.</p><ul><li>Sellers began actively pitching the tactic</li><li>I was invited into multiple client calls as a subject-matter expert</li><li>Campaign funding included incremental budget, reallocated budget, and new campaign plans</li></ul></div></div></article>
            </section>
            <section class="cs-bottom"><article class="cs-contribution"><div><small>My strategic contribution</small><h2>I independently turned a product-awareness gap into an actionable sales narrative.</h2></div><div class="cs-capabilities">{contribution_html}</div></article><article class="cs-takeaway">{_icon('lightbulb')}<small>Strategic takeaway</small><p>When a platform is culturally unfamiliar, showing the end-user experience can build more selling confidence than another feature list.</p></article></section>
            <p class="cs-disclosure twitch-disclosure">Total attendance is approximate: about 24 people participated, including 14 Sales Consultants. The audience statistic—70% of Twitch viewers ages 18–34—is attributed to Twitch internal global data (2022) as published by Amazon Ads. Campaign counts reflect six confirmed advertiser commitments that proceeded to launch; individual revenue and spend were not tracked for this case story.</p>
            <a class="cs-back" href="/GTM_Strategy_and_Sales_Enablement" target="_self">&larr; Return to GTM Strategy &amp; Sales Enablement</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )


def render_streaming_video_decision_matrix_case_study() -> None:
    render_portfolio_navigation()
    hero_path = Path(__file__).resolve().parent / "assets" / "streaming-video-decision-matrix-hero.png"
    hero_src = "data:image/png;base64," + base64.b64encode(hero_path.read_bytes()).decode("ascii")
    contributions = [
        "Portfolio strategy",
        "Decision-framework design",
        "Institutional knowledge translation",
        "Excel solution design",
        "Product-to-market mapping",
        "Usability testing",
        "Sales enablement",
        "Live training",
        "Cross-functional collaboration",
    ]
    contribution_html = "".join(f"<span>{item}</span>" for item in contributions)
    st.markdown(
        _BASE_STYLES
        + _MATRIX_STYLES
        + dedent(f"""
        <div class="cs-shell matrix-case" style="--bg:#f2f6fa;--surface:#ffffff;--soft:#deebf3;--ink:#132b49;--muted:#60738a;--line:#d2dfe9;--deep:#071b3a;--accent:#2477b9;--highlight:#55c5bd;--glow:#2477b9;--hero-copy:#dce9f5;--hero-muted:#bed1e2;--shadow:rgba(7,27,58,.09);--accent-gradient:linear-gradient(135deg,#2477b9,#14528a);--bar-gradient:linear-gradient(90deg,#2477b9,#55c5bd);--hero-radius:26px 8px 26px 8px;--card-radius:18px 6px 18px 6px;--section-radius:22px 7px 22px 7px;--icon-radius:50%;--kpi-count:4;--channel-count:3;--ring:100%;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/GTM_Strategy_and_Sales_Enablement" target="_self"><i>GTM</i> Portfolio case study</a><span class="cs-category">Product Portfolio &amp; Target-Market Mapping</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">Streaming portfolio decision framework · 2022</span><h1>Turning product complexity into a <em>guided sales decision</em></h1><p>Six overlapping streaming and video platforms gave Sales flexibility—but also required sellers to navigate different pricing, targeting, eligibility, inventory, and attribution rules. As Marketing Manager, Digital Strategy, I independently converted a static portfolio matrix into a guided Excel workflow that progressively removed poor-fit options and surfaced the strongest platform choices for each campaign.</p></div>
              <figure class="matrix-hero-visual"><img src="{hero_src}" alt="A marketing manager presenting a guided platform selection workflow that narrows six streaming options to two ranked recommendations"><figcaption>Reconstructed concept: campaign requirements progressively narrow six platform options into one preferred recommendation or two ranked alternatives.</figcaption></figure>
            </section>
            <section class="matrix-meta-strip">
              <article><span>Project role</span><strong>Marketing Manager, Digital Strategy</strong></article>
              <article><span>Initiative</span><strong>Internal Portfolio Enablement · Cox Media</strong></article>
              <article><span>Primary audience</span><strong>Sales Consultants &amp; Digital Support</strong></article>
              <article><span>Core deliverables</span><strong>Guided Excel Tool, Live Demo &amp; Written Instructions</strong></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The portfolio problem</small><h2>More choice had created decision overload</h2></div></div><div class="cs-list">
                <div>{_icon('monitor')}<p><strong>Six overlapping platforms</strong><span>Each option carried different capabilities, commercial rules, and operational requirements.</span></p></div>
                <div>{_icon('money')}<p><strong>Easy shortcuts</strong><span>Sellers could default to the lowest CPM, network selection, or the platform they knew best.</span></p></div>
                <div>{_icon('briefcase')}<p><strong>Documentation without direction</strong><span>The existing matrix described the portfolio but still required sellers to interpret every option.</span></p></div>
                <div>{_icon('target')}<p><strong>Strategy at risk</strong><span>A convenient platform choice was not always the strongest fit for the client's goals and constraints.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('lightbulb')}</span><div><small>The strategic shift</small><h2>Convert product knowledge into decision logic</h2></div></div><div class="matrix-logic">
                <article>{_icon('money')}<strong>Commercial fit</strong><p>Budget model, fixed CPM, minimum spend, and client eligibility.</p></article>
                <article>{_icon('target')}<strong>Audience fit</strong><p>Geography, targeting type, keyword needs, and niche-audience requirements.</p></article>
                <article>{_icon('monitor')}<strong>Delivery fit</strong><p>Inventory type, network selection, reach, frequency, and screen mix.</p></article>
                <article>{_icon('search')}<strong>Measurement fit</strong><p>The type and level of tracking or conversion attribution available.</p></article>
              </div></article>
            </section>
            <section class="cs-dark"><div class="cs-section-heading"><small>Decision architecture</small><h2>Reduce the field without reducing strategic flexibility.</h2></div><div class="matrix-metrics">
              <article><strong>6</strong><span>Starting platforms</span><p>Overlapping streaming and video options entered the decision path.</p></article>
              <article><strong>12+</strong><span>Decision points</span><p>The exact number varied according to the seller's selections.</p></article>
              <article><strong>1–2</strong><span>Final recommendations</span><p>The tool aimed for one choice and ranked two when both remained viable.</p></article>
              <article><strong>5</strong><span>Tool testers</span><p>Two Sales Consultants and all three Digital Support team members.</p></article>
            </div></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('network')}</span><div><small>How the work unfolded</small><h2>From static product inventory to guided selection</h2></div></div><div class="matrix-actions">
              <article><span>01 · Diagnose</span><strong>Reframe the issue</strong><p>I recognized that inconsistent guideline use reflected portfolio complexity—not simply seller compliance.</p></article>
              <article><span>02 · Translate</span><strong>Define the criteria</strong><p>I combined institutional knowledge with the existing product matrix to identify the decisions that mattered.</p></article>
              <article><span>03 · Build</span><strong>Encode the workflow</strong><p>Over three weeks, I created dropdowns, branching logic, progressive filtering, and ranked recommendations.</p></article>
              <article><span>04 · Test</span><strong>Refine the experience</strong><p>Five users validated the logic and requested clearer formatting, progressive elimination, and guidance between final options.</p></article>
              <article><span>05 · Enable</span><strong>Prepare the users</strong><p>I demonstrated the tool live, then emailed instructions and access to the training.</p></article>
            </div><p class="cs-note">This sequence organizes the actions that occurred; it does not claim a formal methodology was used at the time.</p></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('briefcase')}</span><div><small>Guided recommendation system</small><h2>The workbook made complexity disappear as the strategy became clearer</h2></div></div><div class="cs-flow">
              <article><div>{_icon('search')}<span>Capture requirements</span></div><p>Sellers selected the campaign's budget, geography, targeting, inventory, delivery, and measurement needs.</p></article>{_icon('arrow')}<article><div>{_icon('network')}<span>Eliminate poor fits</span></div><p>Platforms that did not meet the selected criteria disappeared, reducing confusion and preventing mismatched choices.</p></article>{_icon('arrow')}<article><div>{_icon('check')}<span>Guide the final choice</span></div><p>The tool surfaced one preferred platform or ranked two viable options with guidance on tradeoffs such as screen mix or reach and frequency.</p></article>
            </div></section>
            <section class="cs-grid-2 cs-full">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('shield')}</span><div><small>Judgment in practice</small><h2>A second viable option needed context—not another comparison table</h2></div></div><p style="color:var(--muted);font-size:.98rem;line-height:1.65;margin:0;">When two platforms remained eligible, I did not leave the seller with an unresolved tie. I ranked the choices and added practical guidance—for example, selecting one option for a stronger balance of large- and small-screen inventory or another for better reach and frequency. The framework preserved seller judgment while making the tradeoff explicit.</p></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('users')}</span><div><small>Evidence of value</small><h2>Sellers could prepare for the conversation—not just react to it</h2></div></div><div class="matrix-proof"><div class="matrix-proof-mark">{_icon('check')}<strong>Clearer</strong><span>than the static portfolio matrix</span></div><div class="matrix-proof-copy"><p>Test users said the tool delivered the same underlying product information in a more concise, less confusing format.</p><ul><li>Supported pre-planning before client pitches</li><li>Made it easier to pivot around budget or targeting restrictions</li><li>Clarified options for niche audiences and attribution needs</li></ul></div></div></article>
            </section>
            <section class="cs-bottom"><article class="cs-contribution"><div><small>My strategic contribution</small><h2>I independently transformed institutional product knowledge into a usable sales decision system.</h2></div><div class="cs-capabilities">{contribution_html}</div></article><article class="cs-takeaway">{_icon('lightbulb')}<small>Strategic takeaway</small><p>When several products solve similar problems, the answer is not more documentation. Teams need decision architecture that makes the right tradeoffs easier to see.</p></article></section>
            <p class="cs-disclosure matrix-disclosure">Long-term adoption and campaign-performance metrics were not available because I was promoted shortly after rollout. Evidence is limited to feedback from the five-person testing group and early seller use.</p>
            <a class="cs-back" href="/GTM_Strategy_and_Sales_Enablement" target="_self">&larr; Return to GTM Strategy &amp; Sales Enablement</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )


def render_video_streaming_sales_playbook_case_study() -> None:
    render_portfolio_navigation()
    hero_path = Path(__file__).resolve().parent / "assets" / "video-streaming-sales-playbook-hero.png"
    hero_src = "data:image/png;base64," + base64.b64encode(hero_path.read_bytes()).decode("ascii")
    contributions = [
        "Sales funnel stage",
        "Audience strategy",
        "Targeting options",
        "Ideal-client guidance",
        "Integrated media strategy",
        "Attribution considerations",
        "Execution requirements",
        "Cross-functional development",
        "Market rollout",
    ]
    contribution_html = "".join(f"<span>{item}</span>" for item in contributions)
    st.markdown(
        _BASE_STYLES
        + _PLAYBOOK_STYLES
        + dedent(f"""
        <div class="cs-shell playbook-case" style="--bg:#f8f3f2;--surface:#ffffff;--soft:#f1e2df;--ink:#302035;--muted:#756774;--line:#e3d6d8;--deep:#28121f;--accent:#dc6756;--highlight:#58c1b8;--glow:#dc6756;--hero-copy:#f1e5e9;--hero-muted:#d7c2ca;--shadow:rgba(40,18,31,.09);--accent-gradient:linear-gradient(135deg,#dc6756,#a83f52);--bar-gradient:linear-gradient(90deg,#dc6756,#58c1b8);--hero-radius:26px 8px 26px 8px;--card-radius:18px 6px 18px 6px;--section-radius:22px 7px 22px 7px;--icon-radius:50%;--kpi-count:4;--channel-count:3;--ring:100%;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/GTM_Strategy_and_Sales_Enablement" target="_self"><i>GTM</i> Portfolio case study</a><span class="cs-category">Revenue Activation &amp; Sales Enablement</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">Revenue Activation Plan: Video &amp; Streaming Playbook · 2022–2023</span><h1>Building enterprise-wide fluency in <em>video and streaming</em></h1><p>As part of the corporate Revenue Activation Plan (RAP), I was selected for a six-person cross-functional team charged with creating the official Video &amp; Streaming Sales Playbook. As Marketing Manager, Digital Strategy, I developed content that helped sellers connect audience strategy, funnel stage, integrated media planning, attribution, and execution requirements to stronger client conversations.</p></div>
              <figure class="playbook-hero-visual"><img src="{hero_src}" alt="Two leaders presenting a video and streaming sales playbook with a funnel and integrated media strategy diagram"><figcaption>Reconstructed concept: a product-agnostic playbook connected video and streaming to funnel stage, audience strategy, and the broader media mix.</figcaption></figure>
            </section>
            <section class="playbook-meta-strip">
              <article><span>Project role</span><strong>Marketing Manager, Digital Strategy</strong></article>
              <article><span>Initiative</span><strong>Corporate Revenue Activation Plan</strong></article>
              <article><span>Primary audience</span><strong>Enterprise-Wide Sales Organization</strong></article>
              <article><span>Core deliverables</span><strong>35-Slide Playbook &amp; 1-Hour Market Rollout</strong></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The enablement need</small><h2>Sellers needed strategy—not another vendor catalog</h2></div></div><div class="cs-list">
                <div>{_icon('briefcase')}<p><strong>A broad solution category</strong><span>Video and streaming could serve different objectives, audiences, and roles within a client's media plan.</span></p></div>
                <div>{_icon('users')}<p><strong>Different levels of fluency</strong><span>Experienced sellers needed a refresher while newer sellers needed a dependable foundation.</span></p></div>
                <div>{_icon('target')}<p><strong>Capabilities to remember</strong><span>Audience data, targeting, attribution, and execution requirements needed to remain accessible during planning.</span></p></div>
                <div>{_icon('network')}<p><strong>Enterprise consistency</strong><span>Corporate leadership wanted an official resource with a uniform structure across RAP product playbooks.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('lightbulb')}</span><div><small>My content contribution</small><h2>Give sellers practical guidance for planning video and streaming campaigns</h2></div></div><div class="playbook-topics">
                <article>{_icon('network')}<strong>Sales funnel stage</strong><p>Positioned video and streaming primarily for awareness while showing how they support the customer journey.</p></article>
                <article>{_icon('target')}<strong>Audience and targeting</strong><p>Covered first- and third-party audiences, segmentation, and major targeting options.</p></article>
                <article>{_icon('monitor')}<strong>Integrated media strategy</strong><p>Positioned video and streaming as complementary tactics that could strengthen paid search, social media, linear television, email marketing, and other parts of the media plan.</p></article>
                <article>{_icon('check')}<strong>Planning readiness</strong><p>Clarified attribution considerations and the inputs required to execute a campaign.</p></article>
              </div></article>
            </section>
            <section class="cs-dark"><div class="cs-section-heading"><small>Corporate development and activation</small><h2>A standardized resource built for enterprise-wide reuse.</h2></div><div class="playbook-metrics">
              <article><strong>6</strong><span>Project-team members</span><p>Sales, Digital Sales leadership, Strategy, and Marketing were represented.</p></article>
              <article><strong>6 weeks</strong><span>Development cycle</span><p>The team shaped, reviewed, and finalized the official corporate resource.</p></article>
              <article><strong>35</strong><span>PowerPoint slides</span><p>A comprehensive guide housed in a standardized RAP playbook template.</p></article>
              <article><strong>1 hour</strong><span>Market rollout</span><p>The Digital Sales Manager and I co-presented the complete playbook.</p></article>
            </div></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('network')}</span><div><small>How the work unfolded</small><h2>From corporate mandate to an official field resource</h2></div></div><div class="playbook-actions">
              <article><span>01 · Align</span><strong>Join the RAP team</strong><p>I was selected for the cross-functional group responsible for the Video &amp; Streaming playbook.</p></article>
              <article><span>02 · Define</span><strong>Shape the sales guidance</strong><p>I focused my content on funnel stage, audiences, targeting, integrated strategy, attribution, and execution.</p></article>
              <article><span>03 · Build</span><strong>Author within the template</strong><p>I developed the assigned content inside the standardized design used across corporate RAP playbooks.</p></article>
              <article><span>04 · Finalize</span><strong>Deliver the official resource</strong><p>The six-person team completed a 35-slide PowerPoint approved for enterprise-wide use.</p></article>
              <article><span>05 · Activate</span><strong>Bring it to the market</strong><p>Following corporate communications, the Digital Sales Manager and I delivered a one-hour local rollout.</p></article>
            </div><p class="cs-note">This sequence organizes the actions that occurred; it does not claim a formal methodology was used at the time.</p></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('briefcase')}</span><div><small>Playbook architecture</small><h2>The resource moved sellers from product understanding to campaign readiness</h2></div></div><div class="cs-flow">
              <article><div>{_icon('users')}<span>Understand the opportunity</span></div><p>Research, funnel stage, ideal-client characteristics, audience strategy, and prospecting guidance established why video mattered.</p></article>{_icon('arrow')}<article><div>{_icon('network')}<span>Build the strategy</span></div><p>Targeting, segmentation, messaging, attribution, and complementary channels helped sellers shape the recommendation.</p></article>{_icon('arrow')}<article><div>{_icon('check')}<span>Prepare for execution</span></div><p>The playbook clarified the need for a completed 15- or 30-second video, destination URL, and trafficking instructions.</p></article>
            </div></section>
            <section class="cs-grid-2 cs-full">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('shield')}</span><div><small>Strategic decision</small><h2>Lead with the client need—not the platform name</h2></div></div><p style="color:var(--muted);font-size:.98rem;line-height:1.65;margin:0;">The playbook was intentionally product agnostic. Rather than organizing the story around individual vendors, it helped sellers begin with the objective, audience, funnel stage, and role of video within the larger media mix. The specific execution platform could follow after the strategy was clear.</p></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('check')}</span><div><small>Evidence of value</small><h2>An official resource that strengthened seller fluency</h2></div></div><div class="playbook-proof"><div class="playbook-proof-mark">{_icon('check')}<strong>Official</strong><span>enterprise-wide RAP resource</span></div><div class="playbook-proof-copy"><p>The finalized playbook was published on the corporate SharePoint site for all employees to access.</p><ul><li>Individual sellers said it supported better client conversations</li><li>Sellers used it to refresh targeting and audience knowledge</li><li>Sales leadership provided positive verbal feedback</li></ul></div></div></article>
            </section>
            <section class="cs-bottom"><article class="cs-contribution"><div><small>My strategic contribution</small><h2>I translated video and streaming capabilities into practical content for an enterprise sales playbook.</h2></div><div class="cs-capabilities">{contribution_html}</div></article><article class="cs-takeaway">{_icon('lightbulb')}<small>Strategic takeaway</small><p>A strong playbook does more than explain a product. It helps sellers understand when it fits, why it matters, and how it should work with the rest of the strategy.</p></article></section>
            <a class="cs-back" href="/GTM_Strategy_and_Sales_Enablement" target="_self">&larr; Return to GTM Strategy &amp; Sales Enablement</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )
