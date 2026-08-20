from __future__ import annotations

import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st

from portfolio_navigation import render_portfolio_navigation


def _hero_data_uri() -> str:
    image_path = Path(__file__).parent / "assets" / "client-performance-dashboard-hero-v2.png"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap');
[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppDeployButton"], .stAppDeployButton { display:none!important; }
#MainMenu, footer { visibility:hidden; }
[data-testid="stSidebar"] { background:#071c3b; }
[data-testid="stSidebar"] * { color:rgba(255,255,255,.88)!important; }
.stApp { background:#f5f8fc; }
.block-container { max-width:1280px; padding:1.5rem 1.25rem 4rem; }
.pd-case,.pd-case * { box-sizing:border-box; }
.pd-case { --blue:#075de8;--navy:#071c3b;--teal:#008f83;--ink:#10233f;--muted:#5f6f84;color:var(--ink);font-family:"DM Sans",sans-serif; }
.pd-case h1,.pd-case h2,.pd-case h3,.pd-case p { margin-block-start:0; }
.pd-topbar { align-items:center;display:flex;justify-content:space-between;margin:0 auto 1.15rem;max-width:1180px; }
.pd-brand { align-items:center;color:var(--ink)!important;display:flex;font-size:.8rem;font-weight:800;gap:.65rem;letter-spacing:.08em;text-decoration:none!important;text-transform:uppercase; }
.pd-brand i { align-items:center;background:var(--navy);border-radius:50%;color:white;display:flex;font-style:normal;height:2rem;justify-content:center;width:2rem; }
.pd-category { color:var(--blue);font-size:1.08rem;font-weight:800; }
.pd-wrap { background:white;box-shadow:0 18px 55px rgba(7,28,59,.09);margin:0 auto;max-width:1180px;overflow:hidden; }
.pd-hero { min-height:530px;overflow:hidden;position:relative; }
.pd-hero img { height:100%;inset:0;object-fit:cover;position:absolute;width:100%; }
.pd-hero::after { background:linear-gradient(90deg,rgba(255,255,255,.99) 0%,rgba(255,255,255,.95) 30%,rgba(255,255,255,.66) 47%,rgba(255,255,255,.03) 72%);content:"";inset:0;position:absolute; }
.pd-hero-copy { max-width:670px;padding:5.2rem 0 4.4rem 4.3rem;position:relative;width:60%;z-index:1; }
.pd-eyebrow,.pd-section-label { color:var(--blue);font-size:.72rem;font-weight:850;letter-spacing:.15em;text-transform:uppercase; }
.pd-hero h1 { color:#07182e!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2.6rem,4.55vw,4.05rem);font-weight:600;letter-spacing:-.045em;line-height:.94;margin:1.1rem 0 1.65rem; }
.pd-title-rule { background:var(--blue);border-radius:4px;height:5px;margin-bottom:1.35rem;width:54px; }
.pd-role { align-items:center;display:flex;font-size:.84rem;font-weight:800;gap:.7rem; }
.pd-role i { align-items:center;background:var(--blue);border-radius:50%;color:white;display:flex;font-style:normal;height:2.15rem;justify-content:center;width:2.15rem; }
.pd-summary { color:#10233f;font-size:1rem;font-weight:500;line-height:1.68;margin:1.25rem 0 0;max-width:565px; }
.pd-impact-highlight { color:#c62828;font-weight:850;white-space:nowrap; }
.pd-meta { background:#fbfcfe;border-bottom:1px solid #dfe6ee;border-top:1px solid #dfe6ee;display:grid;grid-template-columns:repeat(4,1fr); }
.pd-meta div { border-right:1px solid #dfe6ee;padding:1.35rem 1.55rem; }
.pd-meta div:last-child { border-right:0; }
.pd-meta span,.pd-metric-label { color:#7a899d;display:block;font-size:.58rem;font-weight:850;letter-spacing:.12em;margin-bottom:.45rem;text-transform:uppercase; }
.pd-meta strong { display:block;font-size:.76rem;line-height:1.45; }
.pd-section { padding:5.2rem 4.3rem; }
.pd-heading { max-width:740px; }
.pd-heading.center { margin:0 auto 2.9rem;text-align:center; }
.pd-heading h2,.pd-training h2 { color:#0a203d!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2.8rem,4.8vw,4.2rem);font-weight:600;letter-spacing:-.04em;line-height:1;margin:.7rem 0 0; }
.pd-heading p { color:var(--muted);line-height:1.7;margin:1rem 0 0; }
.pd-workflow-section { background:linear-gradient(180deg,#fff,#f5f9fe); }
.pd-workflow-section .pd-heading p { font-size:.68rem;line-height:1.65; }
.pd-workflow { align-items:stretch;display:grid;gap:.7rem;grid-auto-rows:1fr;grid-template-columns:1fr 30px 1fr 30px 1fr 30px 1fr; }
.pd-step { background:white;border:1px solid #dfe8f2;border-radius:20px;box-shadow:0 12px 28px rgba(17,56,102,.07);height:100%;min-height:285px;padding:0 1.1rem 1.25rem;text-align:center; }
.pd-step-label { background:linear-gradient(90deg,#063f9e,var(--blue));border-radius:20px 20px 8px 8px;color:white;display:block;font-size:.72rem;font-weight:800;margin:-1px -1.15rem 1.4rem;padding:.65rem; }
.pd-step-label.teal { background:linear-gradient(90deg,#00756e,#07a193); }
.pd-step p { color:var(--muted);font-size:.96rem;line-height:1.62;margin:1.15rem 0 0; }
.pd-arrow { align-self:center;color:var(--blue);font-size:1.65rem;text-align:center; }
.pd-platforms { display:grid;gap:.45rem;grid-template-columns:1fr 1fr;height:138px;margin:0 auto;width:138px; }
.pd-platforms i { align-items:center;background:#edf4ff;border:1px solid #cddffd;border-radius:9px;color:#0756c9;display:flex;font-size:.58rem;font-style:normal;font-weight:850;justify-content:center; }
.pd-platforms i:nth-child(even) { background:#eaf8f6;border-color:#c5e9e4;color:#00796f; }
.pd-sheet { border:1px solid #cfdbeb;border-radius:9px;box-shadow:0 9px 18px rgba(20,62,110,.1);display:grid;gap:4px;grid-template-columns:repeat(3,1fr);height:138px;margin:0 auto;padding:1rem;width:116px; }
.pd-sheet i { background:#dfe8f3;border-radius:2px; }
.pd-sheet i:nth-child(3n+1) { background:#9fc1f8; }
.pd-refresh { align-items:center;background:linear-gradient(145deg,#075de8,#0649b8);border:12px solid #dceaff;border-radius:50%;color:white;display:flex;font-size:3.4rem;height:118px;justify-content:center;margin:10px auto;width:118px; }
.pd-filters { display:grid;gap:.55rem;margin:0 auto;width:145px; }
.pd-filters i { background:white;border:1px solid #cfdbeb;border-radius:8px;box-shadow:0 5px 11px rgba(20,62,110,.07);color:#425b75;font-size:.58rem;font-style:normal;padding:.75rem;text-align:left; }
.pd-challenge { display:grid;gap:4rem;grid-template-columns:1.05fr .95fr;margin-top:2.7rem; }
.pd-body p { color:var(--muted);font-size:1.08rem;line-height:1.78; }
.pd-pressure { background:var(--navy);border-radius:22px;color:white;overflow:hidden;padding:2.1rem;position:relative; }
.pd-pressure::after { border:22px solid rgba(24,108,237,.24);border-radius:50%;bottom:-60px;content:"";height:145px;position:absolute;right:-60px;width:145px; }
.pd-pressure small { color:#9bc5ff;font-size:1rem;font-weight:850;letter-spacing:.12em;text-transform:uppercase; }
.pd-pressure strong { display:block;font-family:"Newsreader",Georgia,serif;font-size:2.25rem;font-weight:600;line-height:1.12;margin:1rem 0 .85rem;position:relative;z-index:1; }
.pd-pressure p { color:#d4deea;font-size:.82rem;line-height:1.6;margin-bottom:0;position:relative;z-index:1; }
.pd-role-section { background:var(--navy);color:white; }
.pd-role-section .pd-section-label { color:#ffffff; }
.pd-role-section h2 { color:white!important; }
.pd-role-section .pd-heading .pd-role-lead { color:#fff!important;-webkit-text-fill-color:#fff!important;font-size:1.15rem!important;line-height:1.75;max-width:860px;opacity:1!important; }
.pd-contributions { display:grid;gap:1rem;grid-template-columns:repeat(2,1fr);margin-top:3rem; }
.pd-contribution { background:#132c50;border:1px solid rgba(255,255,255,.16);border-radius:18px;box-shadow:0 16px 30px rgba(0,0,0,.13);min-height:275px;padding:1.5rem 1.55rem 1.7rem;position:relative; }
.pd-contribution:nth-child(1) { border-top:5px solid #4d9cff; }
.pd-contribution:nth-child(2) { border-top:5px solid #25d0ba; }
.pd-contribution:nth-child(3) { border-top:5px solid #a786ff; }
.pd-contribution:nth-child(4) { border-top:5px solid #ffa341; }
.pd-card-number { color:#4d9cff;display:block;font-family:"Newsreader",Georgia,serif;font-size:3rem;font-weight:600;letter-spacing:-.04em;line-height:1; }
.pd-contribution:nth-child(2) .pd-card-number { color:#25d0ba; }
.pd-contribution:nth-child(3) .pd-card-number { color:#a786ff; }
.pd-contribution:nth-child(4) .pd-card-number { color:#ffa341; }
.pd-card-icon { align-items:center;background:rgba(77,156,255,.10);border:1px solid rgba(77,156,255,.7);border-radius:12px;color:#4d9cff;display:flex;font-size:1.1rem;font-style:normal;height:3rem;justify-content:center;position:absolute;right:1.5rem;top:1.25rem;width:3rem; }
.pd-contribution:nth-child(2) .pd-card-icon { background:rgba(37,208,186,.10);border-color:rgba(37,208,186,.7);color:#25d0ba; }
.pd-contribution:nth-child(3) .pd-card-icon { background:rgba(167,134,255,.10);border-color:rgba(167,134,255,.7);color:#a786ff; }
.pd-contribution:nth-child(4) .pd-card-icon { background:rgba(255,163,65,.10);border-color:rgba(255,163,65,.7);color:#ffa341; }
.pd-contribution h3 { color:white!important;font-size:1.35rem!important;line-height:1.3!important;margin:2.3rem 0 1rem;max-width:80%; }
.pd-contribution h3 *,.pd-contribution h3 a { color:white!important;-webkit-text-fill-color:white!important;font-size:inherit!important;line-height:inherit!important; }
.pd-contribution p { color:#f2f6fb;font-size:1rem!important;line-height:1.7;margin-bottom:0;max-width:94%; }
.pd-dashboard-section { background:#f4f8fc; }
.pd-dashboard { background:#edf3f9;border:1px solid #d7e2ed;border-radius:20px;box-shadow:0 18px 40px rgba(18,54,94,.12);margin:2.8rem -2.25rem 0;padding:1.75rem; }
.pd-dashboard-head { align-items:flex-end;display:flex;justify-content:space-between;margin-bottom:1rem; }
.pd-dashboard-head small { color:#71829a;display:block;font-size:.6rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase; }
.pd-dashboard-head strong { color:#172a45;display:block;font-size:1.25rem;margin-top:.35rem; }
.pd-filter-row { display:flex;gap:.45rem; }
.pd-filter-row span { background:white;border:1px solid #d5e0eb;border-radius:8px;color:#536981;font-size:.58rem;padding:.6rem .75rem; }
.pd-tabs { background:#dfe7f1;border-radius:9px;display:grid;gap:4px;grid-template-columns:repeat(4,1fr);margin-bottom:.7rem;padding:4px; }
.pd-tabs span { border-radius:6px;color:#68798d;font-size:.58rem;font-weight:750;padding:.55rem;text-align:center; }
.pd-tabs span:first-child { background:var(--blue);color:white; }
.pd-kpis { display:grid;gap:.55rem;grid-template-columns:repeat(5,1fr); }
.pd-kpi { background:white;border-left:5px solid var(--blue);padding:1rem; }
.pd-kpi:nth-child(even) { border-left-color:var(--teal); }
.pd-kpi span { color:#718198;display:block;font-size:.52rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase; }
.pd-kpi strong { color:#111d33;display:block;font-size:1.65rem;margin:.35rem 0 .15rem; }
.pd-kpi small { color:#98a4b2;font-size:.48rem; }
.pd-dashboard-grid { display:grid;gap:.7rem;grid-template-columns:1.35fr .65fr;margin-top:.7rem; }
.pd-table,.pd-chart { background:white;border:1px solid #dce5ee;padding:1rem; }
.pd-table h3,.pd-chart h3 { color:#172941!important;font-size:.76rem;margin:0 0 .75rem; }
.pd-table div { display:grid;grid-template-columns:1.5fr repeat(3,1fr); }
.pd-table span { border-bottom:1px solid #e4eaf0;color:#46586f;font-size:.52rem;padding:.55rem .4rem; }
.pd-table span:not(:first-child) { text-align:right; }
.pd-table .pd-table-head span { background:#11213a;color:white;font-weight:800; }
.pd-chart { align-items:center;display:grid;grid-template-columns:1fr 1fr; }
.pd-chart h3 { grid-column:1/-1; }
.pd-donut { align-items:center;background:conic-gradient(#075de8 0 38%,#51a0ff 38% 65%,#2249aa 65% 80%,#008f83 80%);border-radius:50%;display:flex;height:112px;justify-content:center;margin:auto;position:relative;width:112px; }
.pd-donut::after { background:white;border-radius:50%;content:"";height:60px;position:absolute;width:60px; }
.pd-donut b { color:#253954;font-size:.9rem;position:relative;z-index:1; }
.pd-chart ul { list-style:none;margin:0;padding:0; }
.pd-chart li { align-items:center;color:#52647b;display:flex;font-size:.5rem;gap:.4rem;margin:.55rem 0; }
.pd-chart li i { background:var(--blue);height:7px;width:7px; }
.pd-chart li:nth-child(2) i { background:#51a0ff; }.pd-chart li:nth-child(3) i{background:#2249aa}.pd-chart li:nth-child(4) i{background:var(--teal)}
.pd-dashboard-sequence { border-top:5px solid var(--blue); }
.pd-dashboard-sequence.teal { border-top-color:var(--teal); }
.pd-tabs.search span:first-child,.pd-tabs.keyword span:first-child { background:transparent;color:#68798d; }
.pd-tabs.search span:nth-child(3),.pd-tabs.keyword span:nth-child(4) { background:var(--blue);color:white; }
.pd-search-kpis { grid-template-columns:repeat(3,1fr); }
.pd-search-visuals { display:grid;gap:.7rem;grid-template-columns:1.35fr .65fr;margin-top:.7rem; }
.pd-search-panel { background:white;border:1px solid #dce5ee;padding:1rem; }
.pd-search-panel h3 { color:#172941!important;font-size:1rem;margin:0 0 1rem; }
.pd-bar-row { align-items:center;display:grid;gap:.7rem;grid-template-columns:110px 1fr 58px;margin:.8rem 0; }
.pd-bar-row span,.pd-bar-row b { color:#52647b;font-size:.76rem; }
.pd-bar-row b { text-align:right; }
.pd-bar-track { background:#e3eaf2;border-radius:8px;height:12px;overflow:hidden; }
.pd-bar-track i { background:linear-gradient(90deg,#075de8,#51a0ff);border-radius:8px;display:block;height:100%;width:var(--bar); }
.pd-search-visuals .pd-donut { background:conic-gradient(#075de8 0 var(--donut),#dce6f0 var(--donut) 100%);height:138px;width:138px; }
.pd-search-visuals .pd-donut::after { height:78px;width:78px; }
.pd-search-visuals .pd-donut b { font-size:1.05rem; }
.pd-donut-copy { color:#52647b;font-size:.76rem;line-height:1.5;margin:.75rem auto 0;max-width:170px;text-align:center; }
.pd-search-table-wrap { background:white;border:1px solid #dce5ee;margin-top:.7rem;overflow-x:auto;padding:1rem; }
.pd-search-table-wrap h3 { color:#172941!important;font-size:1rem;margin:0 0 .85rem; }
.pd-search-table { min-width:980px; }
.pd-search-table>div { display:grid;grid-template-columns:minmax(175px,1.5fr) repeat(7,minmax(88px,.75fr)); }
.pd-search-table span { border-bottom:1px solid #e4eaf0;color:#46586f;font-size:.7rem;padding:.62rem .42rem; }
.pd-search-table span:not(:first-child) { text-align:right; }
.pd-search-table .pd-search-table-head span { background:#11213a;color:white;font-weight:800; }
.pd-search-table .pd-search-table-head span:first-child { border-radius:5px 0 0 5px; }
.pd-search-table .pd-search-table-head span:last-child { border-radius:0 5px 5px 0; }
.pd-social-platforms { color:#52647b;font-size:.72rem;font-weight:750;letter-spacing:.02em;margin:.35rem 0 0; }
.pd-social-platforms b { color:#075de8;font-weight:800; }
.pd-social-bars .pd-bar-track i { background:linear-gradient(90deg,#075de8,#008f83); }
.pd-social-table { min-width:960px; }
.pd-social-table>div { display:grid;grid-template-columns:minmax(80px,.7fr) minmax(120px,1.05fr) minmax(150px,1.25fr) minmax(88px,.75fr) repeat(5,minmax(74px,.65fr)); }
.pd-social-table span { border-bottom:1px solid #e4eaf0;color:#46586f;font-size:.68rem;padding:.62rem .42rem; }
.pd-social-table span:nth-child(n+5) { text-align:right; }
.pd-social-table .pd-search-table-head span { background:#11213a;color:white;font-weight:800; }
.pd-social-table .pd-search-table-head span:first-child { border-radius:5px 0 0 5px; }
.pd-social-table .pd-search-table-head span:last-child { border-radius:0 5px 5px 0; }
.pd-disclosure { color:#74849a;font-size:.65rem;line-height:1.55;margin:1rem 0 0;text-align:center; }
.pd-solution-notes { align-items:stretch;display:grid;gap:1rem;grid-template-columns:1fr 1fr;margin-top:2.5rem; }
.pd-note { background:white;border:1px solid #dce6f1;border-radius:14px;display:flex;flex-direction:column;height:100%;min-height:235px;padding:1.6rem 1.6rem 1.6rem; }
.pd-note.teal { border-left:4px solid var(--teal); }
.pd-note span { color:var(--teal);font-size:.6rem;font-weight:850;letter-spacing:.1em;text-transform:uppercase; }
.pd-note h3 { color:var(--ink)!important;font-family:"Newsreader",Georgia,serif!important;font-size:1.45rem;margin:1rem 0 .8rem;min-height:3.1rem; }
.pd-note p { color:var(--muted);font-size:.78rem;line-height:1.65;margin:0; }
.pd-process { background:#eef3f7;color:var(--ink); }
.pd-process .pd-section-label { color:var(--blue); }
.pd-process h2 { color:#0a203d!important;font-size:clamp(3.1rem,5.2vw,4.6rem); }
.pd-timeline { display:grid;gap:1rem;grid-template-columns:repeat(3,1fr);margin-top:2.8rem; }
.pd-phase { background:white;border:1px solid #d8e2ec;border-radius:16px;box-shadow:0 14px 30px rgba(19,49,84,.10);display:flex;flex-direction:column;min-height:390px;padding:1.75rem;position:relative; }
.pd-phase:nth-child(1) { border-top:5px solid #1769d5; }
.pd-phase:nth-child(2) { border-top:5px solid #008f83; }
.pd-phase:nth-child(3) { border-top:5px solid #7659c8; }
.pd-phase-top { align-items:center;display:flex;justify-content:space-between; }
.pd-phase-top>span { color:#1769d5;font-family:"Newsreader",Georgia,serif;font-size:2.2rem;font-weight:600;line-height:1; }
.pd-phase:nth-child(2) .pd-phase-top>span { color:#008f83; }
.pd-phase:nth-child(3) .pd-phase-top>span { color:#7659c8; }
.pd-phase-icon { align-items:center;background:#eaf3ff;border:1px solid #1769d5;border-radius:11px;color:#1769d5;display:flex;font-style:normal;height:3rem;justify-content:center;width:3rem; }
.pd-phase:nth-child(2) .pd-phase-icon { background:#e8f7f4;border-color:#008f83;color:#008f83; }
.pd-phase:nth-child(3) .pd-phase-icon { background:#f0ecfb;border-color:#7659c8;color:#7659c8; }
.pd-phase-icon svg { height:1.35rem;width:1.35rem; }
.pd-phase h3 { color:#0a203d!important;font-family:"Newsreader",Georgia,serif!important;font-size:1.75rem;margin:1.65rem 0 .85rem; }
.pd-phase>p { color:#42556e;font-size:1.02rem;line-height:1.72; }
.pd-phase small { background:#eaf3ff;border-left:4px solid #1769d5;color:#10233f;display:block;font-size:.94rem;line-height:1.65;margin-top:auto;padding:1rem; }
.pd-phase:nth-child(2) small { background:#e8f7f4;border-left-color:#008f83; }
.pd-phase:nth-child(3) small { background:#f0ecfb;border-left-color:#7659c8; }
.pd-phase small b { color:#1769d5;display:block;font-size:.78rem;letter-spacing:.1em;margin-bottom:.45rem;text-transform:uppercase; }
.pd-phase:nth-child(2) small b { color:#008f83; }
.pd-phase:nth-child(3) small b { color:#7659c8; }
.pd-training { align-items:center;background:#fff;display:grid;gap:4rem;grid-template-columns:1.05fr .95fr; }
.pd-training>div>p { color:var(--muted);line-height:1.75;margin:1.2rem 0 0; }
.pd-tags { display:flex;flex-wrap:wrap;gap:.55rem;margin-top:1.3rem; }
.pd-tags span { background:#e3f4f0;border-radius:7px;color:#075082;font-size:.68rem;font-weight:750;padding:.52rem .72rem; }
.pd-handoff { background:#eef5fb;border-radius:20px;padding:2rem; }
.pd-handoff i { align-items:center;background:var(--teal);border-radius:50%;color:white;display:flex;font-style:normal;height:3rem;justify-content:center;margin-bottom:1.3rem;width:3rem; }
.pd-handoff span { color:var(--teal);font-size:.62rem;font-weight:850;letter-spacing:.12em;text-transform:uppercase; }
.pd-handoff h3 { color:var(--ink)!important;font-family:"Newsreader",Georgia,serif!important;font-size:2rem;margin:1rem 0 .7rem; }
.pd-handoff p { color:var(--muted);font-size:1.02rem;line-height:1.7; }
.pd-results { background:white;color:var(--ink);padding:0; }
.pd-results-band { align-items:stretch;background:var(--navy);color:white;display:grid;gap:0;grid-template-columns:repeat(3,1fr);padding:0;position:relative; }
.pd-results-band div { display:flex;flex-direction:column;justify-content:center;min-height:230px;padding:1.75rem;text-align:center; }
.pd-results-band>i { color:#7fb1ff;font-size:1.8rem;font-style:normal;left:calc(33.333% - 18px);position:absolute;text-align:center;top:50%;transform:translateY(-50%);width:36px;z-index:2; }
.pd-results-band b { color:#8fbaff;display:block;font-size:.82rem;letter-spacing:.12em;margin-bottom:.5rem;text-transform:uppercase; }
.pd-results-band strong { display:block;font-family:"Newsreader",Georgia,serif;font-size:3.55rem;font-weight:600;line-height:1;white-space:nowrap; }
.pd-results-band span { color:#d1dced;display:block;font-size:1.02rem;line-height:1.5;margin-top:.65rem; }
.pd-results-band .pd-reduction { background:var(--teal);padding:1.75rem; }
.pd-results-band .pd-reduction b,.pd-results-band .pd-reduction span { color:#e0f7f3; }
.pd-reflection { display:grid;gap:0;grid-template-columns:repeat(3,1fr);margin:0; }
.pd-reflection article { border-right:1px solid #abc7db;min-height:350px;padding:2.4rem 2.2rem; }
.pd-reflection article:last-child { border-right:0; }
.pd-reflection article:nth-child(1) { background:#dce8f4; }
.pd-reflection article:nth-child(2) { background:#dcefeb; }
.pd-reflection article:nth-child(3) { background:#edf1f7; }
.pd-reflection span { color:#08234b;font-size:1rem;font-weight:850;letter-spacing:.1em;text-transform:uppercase; }
.pd-reflection h3 { color:#08234b!important;font-family:"DM Sans",sans-serif!important;font-size:1.45rem;font-weight:800;letter-spacing:.06em;line-height:1.4;margin:2rem 0 .85rem;text-transform:uppercase; }
.pd-reflection p { color:#173456;font-size:1.05rem;line-height:1.72; }
.pd-back { color:var(--navy)!important;display:block;font-size:.82rem;font-weight:800;margin:1rem 0 0;text-align:center;text-decoration:none!important; }
/* Readability pass: the case study is designed to be reviewed at normal browser size. */
.pd-eyebrow { font-size:1.08rem; }
.pd-section-label { font-size:1.08rem; }
.pd-summary { font-size:1.08rem;line-height:1.72; }
.pd-meta span,.pd-metric-label { font-size:.7rem; }
.pd-meta strong { font-size:.9rem; }
.pd-heading p { font-size:1.04rem; }
.pd-step-label { font-size:.82rem; }
.pd-step p { font-size:.96rem;line-height:1.62; }
.pd-platforms i,.pd-filters i { font-size:.7rem; }
.pd-pressure small { font-size:1rem; }
.pd-pressure p { font-size:.82rem;line-height:1.6; }
.pd-role-lead { font-size:1.15rem!important; }
.pd-card-number { font-size:3rem; }
.pd-contribution h3 { color:#fff!important;font-size:1.35rem!important; }
.pd-contribution h3 *,.pd-contribution h3 a { color:#fff!important;-webkit-text-fill-color:#fff!important;font-size:inherit!important; }
.pd-contribution p { font-size:1rem!important;line-height:1.7; }
.pd-dashboard-head small { font-size:.7rem; }
.pd-dashboard-head strong { font-size:1.4rem; }
.pd-filter-row span,.pd-tabs span { font-size:.78rem; }
.pd-kpi span { font-size:.72rem; }
.pd-kpi small { font-size:.68rem; }
.pd-table h3,.pd-chart h3 { font-size:1rem; }
.pd-table span { font-size:.76rem; }
.pd-chart li { font-size:.75rem; }
.pd-disclosure { font-size:.82rem; }
.pd-note span { font-size:.7rem; }
.pd-note p { font-size:.94rem;line-height:1.7; }
.pd-phase-top>span { font-size:2.2rem; }
.pd-phase>p { font-size:1.02rem;line-height:1.72; }
.pd-phase small { font-size:.94rem;line-height:1.65; }
.pd-phase small b { font-size:.78rem; }
.pd-training>div>p { font-size:1.02rem; }
.pd-tags span { font-size:.78rem; }
.pd-handoff span { font-size:.72rem; }
.pd-handoff p { font-size:1.02rem;line-height:1.7; }
.pd-results-band span { font-size:1.02rem; }
.pd-reflection span { font-size:1rem; }
.pd-reflection p { font-size:1.05rem;line-height:1.72; }
.pd-back { font-size:.95rem; }
@media(max-width:920px){.pd-meta{grid-template-columns:repeat(2,1fr)}.pd-workflow{grid-template-columns:repeat(4,1fr)}.pd-arrow{display:none}.pd-contributions{grid-template-columns:repeat(2,1fr)}.pd-dashboard-grid,.pd-search-visuals{grid-template-columns:1fr}.pd-timeline,.pd-reflection{grid-template-columns:1fr}.pd-results-band{grid-template-columns:1fr}.pd-results-band>i{left:auto;position:static;top:auto;transform:rotate(90deg);width:auto}}
@media(max-width:700px){.block-container{padding:1rem .7rem 3rem}.pd-category{display:none}.pd-hero{min-height:680px}.pd-hero img{bottom:0;height:40%;top:auto}.pd-hero::after{background:linear-gradient(180deg,#fff 0 58%,rgba(255,255,255,.1) 84%)}.pd-hero-copy{padding:3rem 1.5rem 18rem;width:100%}.pd-hero h1{font-size:2.8rem}.pd-section{padding:3.5rem 1.35rem}.pd-results{padding:0}.pd-results-band{padding:0}.pd-workflow,.pd-contributions,.pd-challenge,.pd-training,.pd-solution-notes{grid-template-columns:1fr}.pd-step{min-height:250px}.pd-dashboard{margin:2.8rem 0 0;padding:1rem}.pd-dashboard-head{display:block}.pd-filter-row{flex-wrap:wrap;margin-top:1rem}.pd-tabs{overflow-x:auto}.pd-kpis{grid-template-columns:repeat(2,1fr)}.pd-kpi:last-child{grid-column:1/-1}.pd-table{overflow-x:auto}.pd-table>div{min-width:500px}.pd-results-band>i{transform:rotate(90deg)}}
</style>
"""


def render_dashboard_case_study(*, configure_page: bool = True) -> None:
    if configure_page:
        st.set_page_config(
            page_title="Client-Facing Performance Dashboard | L.C. Felton",
            page_icon="PD",
            layout="wide",
            initial_sidebar_state="expanded",
        )
    render_portfolio_navigation()
    hero = _hero_data_uri()
    st.markdown(
        _STYLES
        + dedent(f"""
        <div class="pd-case">
          <header class="pd-topbar"><a class="pd-brand" href="/" target="_self"><i>PD</i> Dashboard &amp; insights case study</a><span class="pd-category">Reporting Automation</span></header>
          <main class="pd-wrap">
            <section class="pd-hero">
              <img src="{hero}" alt="Colleagues reviewing a digital workflow together at a laptop">
              <div class="pd-hero-copy">
                <span class="pd-eyebrow">Reporting Automation &middot; 2021</span>
                <h1>Client-Facing Performance Dashboard</h1>
                <div class="pd-title-rule"></div>
                <p class="pd-summary">A self-directed reporting redesign that consolidated 25&ndash;30 monthly campaigns into four interactive pages and reduced weekly reporting time by <span class="pd-impact-highlight">94&ndash;96%</span>&mdash;from six hours to 15&ndash;20 minutes.</p>
              </div>
            </section>
            <section class="pd-meta">
              <div><span>Project role</span><strong>Independent Project Lead &amp; Dashboard Designer</strong></div>
              <div><span>Client</span><strong>Regional hospital</strong></div>
              <div><span>Systems</span><strong>Google Data Studio, Excel, Google Sheets</strong></div>
              <div><span>Delivery</span><strong>30-day build &middot; six-week handoff</strong></div>
            </section>

            <section class="pd-section pd-workflow-section">
              <div class="pd-heading center"><span class="pd-section-label">How the solution worked</span><h2>One repeatable path from platform data to client insight</h2><p>A structured weekly workflow replaced a sprawling spreadsheet and made campaign performance easier to update, validate, and explore.</p></div>
              <div class="pd-workflow">
                <article class="pd-step"><span class="pd-step-label">Source Exports</span><div class="pd-platforms"><i>SEM</i><i>SOCIAL</i><i>DSP</i><i>VIDEO</i></div><p>Download performance data from search, social, programmatic, video, and email platforms.</p></article><span class="pd-arrow">&rarr;</span>
                <article class="pd-step"><span class="pd-step-label teal">Structured Dataset</span><div class="pd-sheet"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><p>Organize, clean, and normalize each export in one central query sheet.</p></article><span class="pd-arrow">&rarr;</span>
                <article class="pd-step"><span class="pd-step-label">Dashboard Refresh</span><div class="pd-refresh">&#8635;</div><p>Refresh Google Data Studio and verify totals, calculations, and campaign coverage.</p></article><span class="pd-arrow">&rarr;</span>
                <article class="pd-step"><span class="pd-step-label teal">Client Exploration</span><div class="pd-filters"><i>Department &#9662;</i><i>Campaign &#9662;</i><i>Date &#9662;</i></div><p>Use filters to move from a department overview to the right campaign and tactic.</p></article>
              </div>
            </section>

            <section class="pd-section">
              <div class="pd-heading"><span class="pd-section-label">01 &middot; The challenge</span><h2>Reporting had consumed the time needed for analysis</h2></div>
              <div class="pd-challenge">
                <div class="pd-body"><p>A regional hospital ran 25&ndash;30 campaigns each month across seven or more advertising platforms and channels. The existing visual dashboard was difficult to navigate, while the supporting spreadsheet had grown into a six-hour Monday reporting task.</p><p>Scaling the old dashboard would have required more than 100 pages. The marketing director and department heads needed a faster way to move among departments, campaigns, products, tactics, and dates without exposing confidential budget information.</p></div>
                <aside class="pd-pressure"><small>Observed impact</small><strong>One full workday each week went to data preparation</strong><p>The manual reporting burden left less time for the performance storytelling and analysis the client actually needed.</p></aside>
              </div>
            </section>

            <section class="pd-section pd-role-section">
              <div class="pd-heading"><span class="pd-section-label">02 &middot; My contribution</span><h2>Independent Project Lead &amp; Dashboard Designer</h2><p class="pd-role-lead">This was an informal, self-initiated project. I sought technical and legal guidance where needed, then independently designed, built, tested, documented, and launched the dashboard.</p></div>
              <div class="pd-contributions">
                <article class="pd-contribution"><span class="pd-card-number">01</span><i class="pd-card-icon" aria-hidden="true">&#9671;</i><h3>Initiate the project</h3><p>Recognized that reporting was limiting higher-value work and proposed a self-directed redesign.</p></article>
                <article class="pd-contribution"><span class="pd-card-number">02</span><i class="pd-card-icon" aria-hidden="true">&#9638;</i><h3>Design and build</h3><p>Created the four-page architecture, data model, calculations, filters, drills, and visualizations.</p></article>
                <article class="pd-contribution"><span class="pd-card-number">03</span><i class="pd-card-icon" aria-hidden="true">&#10003;</i><h3>Validate the data</h3><p>Compared totals with source platforms and manually spot-checked calculations before release.</p></article>
                <article class="pd-contribution"><span class="pd-card-number">04</span><i class="pd-card-icon" aria-hidden="true">&#8644;</i><h3>Enable continuity</h3><p>Documented the workflow, trained users, supported launch, and transferred ownership after six weeks.</p></article>
              </div>
            </section>

            <section class="pd-section pd-dashboard-section">
              <div class="pd-heading"><span class="pd-section-label">03 &middot; The solution</span><h2>Four pages replaced a maze of reports</h2><p>The final dashboard paired channel-specific metrics with shared filters, so users could answer both high-level and detailed questions without leaving one reporting environment.</p></div>
              <figure class="pd-dashboard">
                <div class="pd-dashboard-head"><div><small>Campaign intelligence</small><strong>Hospital performance overview</strong></div><div class="pd-filter-row"><span>Department: All &#9662;</span><span>Campaign: All &#9662;</span><span>Last 30 days &#9662;</span></div></div>
                <div class="pd-tabs"><span>Overview</span><span>Products &amp; tactics</span><span>Paid search</span><span>Keywords &amp; ad groups</span></div>
                <div class="pd-kpis"><div class="pd-kpi"><span>Impressions</span><strong>1.84M</strong></div><div class="pd-kpi"><span>Clicks</span><strong>96.3K</strong></div><div class="pd-kpi"><span>CTR</span><strong>5.24%</strong></div><div class="pd-kpi"><span>Conversions</span><strong>4,207</strong></div><div class="pd-kpi"><span>Video completion</span><strong>71.8%</strong></div></div>
                <div class="pd-dashboard-grid">
                  <div class="pd-table"><h3>Campaign performance</h3><div class="pd-table-head"><span>Campaign</span><span>Impressions</span><span>Clicks</span><span>CTR</span></div><div><span>Regional awareness</span><span>328,410</span><span>15,892</span><span>4.84%</span></div><div><span>Service line A</span><span>241,830</span><span>13,106</span><span>5.42%</span></div><div><span>Community outreach</span><span>198,760</span><span>9,412</span><span>4.74%</span></div><div><span>Recruitment</span><span>176,290</span><span>8,633</span><span>4.90%</span></div></div>
                  <div class="pd-chart"><h3>Engagement by channel</h3><div class="pd-donut"><b>7+</b></div><ul><li><i></i>Social</li><li><i></i>Paid search</li><li><i></i>Programmatic</li><li><i></i>Video &amp; audio</li></ul></div>
                </div>
              </figure>
              <figure class="pd-dashboard pd-dashboard-sequence teal">
                <div class="pd-dashboard-head"><div><small>Social performance &middot; Channel overview</small><strong>Cross-platform campaign performance</strong><p class="pd-social-platforms"><b>Facebook</b> &middot; LinkedIn &middot; YouTube &middot; TikTok</p></div><div class="pd-filter-row"><span>Department: All &#9662;</span><span>Campaign: All &#9662;</span><span>Last 30 days &#9662;</span></div></div>
                <div class="pd-tabs"><span>Social overview</span><span>Creative formats</span><span>Video performance</span><span>Ad details</span></div>
                <div class="pd-kpis pd-search-kpis"><div class="pd-kpi"><span>Impressions</span><strong>697.0K</strong></div><div class="pd-kpi"><span>Clicks</span><strong>22.6K</strong></div><div class="pd-kpi"><span>Engagements</span><strong>44.8K</strong></div></div>
                <div class="pd-search-visuals">
                  <div class="pd-search-panel pd-social-bars"><h3>Engagements by platform</h3><div class="pd-bar-row"><span>Facebook</span><div class="pd-bar-track"><i style="--bar:94%"></i></div><b>15.8K</b></div><div class="pd-bar-row"><span>LinkedIn</span><div class="pd-bar-track"><i style="--bar:39%"></i></div><b>6.6K</b></div><div class="pd-bar-row"><span>YouTube</span><div class="pd-bar-track"><i style="--bar:56%"></i></div><b>9.4K</b></div><div class="pd-bar-row"><span>TikTok</span><div class="pd-bar-track"><i style="--bar:77%"></i></div><b>13.0K</b></div></div>
                  <div class="pd-search-panel"><h3>Conversion share</h3><div class="pd-donut" style="--donut:41%"><b>41%</b></div><p class="pd-donut-copy">Facebook generated the largest share of social conversions.</p></div>
                </div>
                <div class="pd-search-table-wrap"><h3>Ad performance</h3><div class="pd-social-table"><div class="pd-search-table-head"><span>Platform</span><span>Adset</span><span>Ad name</span><span>Ad type</span><span>Impressions</span><span>Clicks</span><span>CTR</span><span>Engagements</span><span>Conversions</span></div><div><span>Facebook</span><span>Service awareness</span><span>Care Close to Home</span><span>Carousel</span><span>184,200</span><span>6,940</span><span>3.77%</span><span>15,820</span><span>312</span></div><div><span>LinkedIn</span><span>Healthcare careers</span><span>Join Our Care Team</span><span>Image</span><span>72,600</span><span>2,140</span><span>2.95%</span><span>6,580</span><span>96</span></div><div><span>YouTube</span><span>Patient stories</span><span>A Better Recovery</span><span>Video</span><span>241,800</span><span>5,620</span><span>2.32%</span><span>9,420</span><span>184</span></div><div><span>TikTok</span><span>Wellness education</span><span>Three Ways to Stay Well</span><span>Native video</span><span>198,400</span><span>7,860</span><span>3.96%</span><span>12,980</span><span>168</span></div></div></div>
              </figure>
              <figure class="pd-dashboard pd-dashboard-sequence">
                <div class="pd-dashboard-head"><div><small>Paid search &middot; Search visibility</small><strong>Geographic performance and market visibility</strong></div><div class="pd-filter-row"><span>Department: All &#9662;</span><span>Campaign: All &#9662;</span><span>Last 30 days &#9662;</span></div></div>
                <div class="pd-tabs search"><span>Overview</span><span>Products &amp; tactics</span><span>Paid search</span><span>Keywords &amp; ad groups</span></div>
                <div class="pd-kpis pd-search-kpis"><div class="pd-kpi"><span>Impressions</span><strong>486.2K</strong></div><div class="pd-kpi"><span>Clicks</span><strong>28.7K</strong></div><div class="pd-kpi"><span>Absolute imp. share</span><strong>68.9%</strong></div></div>
                <div class="pd-search-visuals">
                  <div class="pd-search-panel"><h3>CTR by market</h3><div class="pd-bar-row"><span>Virginia</span><div class="pd-bar-track"><i style="--bar:88%"></i></div><b>5.84%</b></div><div class="pd-bar-row"><span>Maryland</span><div class="pd-bar-track"><i style="--bar:79%"></i></div><b>5.22%</b></div><div class="pd-bar-row"><span>North Carolina</span><div class="pd-bar-track"><i style="--bar:72%"></i></div><b>4.76%</b></div></div>
                  <div class="pd-search-panel"><h3>Top-position visibility</h3><div class="pd-donut" style="--donut:68.9%"><b>68.9%</b></div><p class="pd-donut-copy">Absolute impression share across the selected paid-search campaigns.</p></div>
                </div>
                <div class="pd-search-table-wrap"><h3>Top geographies</h3><div class="pd-search-table"><div class="pd-search-table-head"><span>City / state</span><span>Impressions</span><span>Clicks</span><span>CTR</span><span>CPC</span><span>All conversions</span><span>Phone calls</span><span>Abs. imp. share</span></div><div><span>Richmond, VA</span><span>82,460</span><span>5,214</span><span>6.32%</span><span>$3.18</span><span>386</span><span>149</span><span>72.8%</span></div><div><span>Virginia Beach, VA</span><span>71,280</span><span>4,016</span><span>5.63%</span><span>$3.06</span><span>294</span><span>112</span><span>69.7%</span></div><div><span>Baltimore, MD</span><span>68,910</span><span>3,782</span><span>5.49%</span><span>$3.44</span><span>271</span><span>101</span><span>67.5%</span></div><div><span>Bethesda, MD</span><span>54,370</span><span>2,986</span><span>5.49%</span><span>$3.72</span><span>218</span><span>76</span><span>66.2%</span></div><div><span>Raleigh, NC</span><span>63,840</span><span>3,264</span><span>5.11%</span><span>$3.21</span><span>236</span><span>88</span><span>64.8%</span></div><div><span>Charlotte, NC</span><span>59,420</span><span>2,814</span><span>4.74%</span><span>$3.35</span><span>204</span><span>71</span><span>62.9%</span></div></div></div>
              </figure>
              <figure class="pd-dashboard pd-dashboard-sequence teal">
                <div class="pd-dashboard-head"><div><small>Paid search &middot; Lead performance</small><strong>Keyword conversion and call performance</strong></div><div class="pd-filter-row"><span>Department: All &#9662;</span><span>Campaign: All &#9662;</span><span>Last 30 days &#9662;</span></div></div>
                <div class="pd-tabs keyword"><span>Overview</span><span>Products &amp; tactics</span><span>Paid search</span><span>Keywords &amp; ad groups</span></div>
                <div class="pd-kpis pd-search-kpis"><div class="pd-kpi"><span>All conversions</span><strong>1,842</strong></div><div class="pd-kpi"><span>Phone calls</span><strong>694</strong></div><div class="pd-kpi"><span>Average CPC</span><strong>$3.28</strong></div></div>
                <div class="pd-search-visuals">
                  <div class="pd-search-panel"><h3>Conversions by Adgroup</h3><div class="pd-bar-row"><span>Emergency care</span><div class="pd-bar-track"><i style="--bar:94%"></i></div><b>612</b></div><div class="pd-bar-row"><span>Urgent care</span><div class="pd-bar-track"><i style="--bar:72%"></i></div><b>438</b></div><div class="pd-bar-row"><span>Hospital services</span><div class="pd-bar-track"><i style="--bar:51%"></i></div><b>286</b></div><div class="pd-bar-row"><span>Specialists</span><div class="pd-bar-track"><i style="--bar:43%"></i></div><b>241</b></div></div>
                  <div class="pd-search-panel"><h3>Call contribution</h3><div class="pd-donut" style="--donut:37.7%"><b>37.7%</b></div><p class="pd-donut-copy">694 phone calls out of 1,842 total conversions.</p></div>
                </div>
                <div class="pd-search-table-wrap"><h3>Keyword performance</h3><div class="pd-search-table"><div class="pd-search-table-head"><span>Keyword</span><span>Impressions</span><span>Clicks</span><span>CTR</span><span>CPC</span><span>All conversions</span><span>Phone calls</span><span>Abs. imp. share</span></div><div><span>emergency care near me</span><span>124,820</span><span>8,714</span><span>6.98%</span><span>$3.42</span><span>612</span><span>248</span><span>72.4%</span></div><div><span>urgent care open now</span><span>98,410</span><span>6,208</span><span>6.31%</span><span>$3.16</span><span>438</span><span>171</span><span>68.9%</span></div><div><span>hospital services</span><span>86,730</span><span>4,218</span><span>4.86%</span><span>$2.74</span><span>286</span><span>94</span><span>63.7%</span></div><div><span>specialist appointment</span><span>71,260</span><span>3,782</span><span>5.31%</span><span>$3.88</span><span>241</span><span>81</span><span>59.6%</span></div></div></div>
                <figcaption class="pd-disclosure">Representative reconstructions based on the original dashboard&rsquo;s structure and functionality. Client information and performance data have been anonymized; all values shown are illustrative.</figcaption>
              </figure>
            </section>

            <section class="pd-section pd-process">
              <div class="pd-heading center"><span class="pd-section-label">04 &middot; The process</span><h2>From approval to a sustainable weekly rhythm</h2></div>
              <div class="pd-timeline">
                <article class="pd-phase"><div class="pd-phase-top"><span>01</span><i class="pd-phase-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3 5 6v5c0 4.7 2.8 8.2 7 10 4.2-1.8 7-5.3 7-10V6l-7-3Z"/><path d="m9 12 2 2 4-5"/></svg></i></div><h3>Define and secure approval</h3><p>Mapped the problem, confirmed required KPIs, and consulted the Product Team about APIs, data-lake options, legal boundaries, and security.</p><small><b>My contribution</b>Recommended Google Data Studio as a no-cost approved path when direct connectors were unavailable.</small></article>
                <article class="pd-phase"><div class="pd-phase-top"><span>02</span><i class="pd-phase-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M9 9v11"/></svg></i></div><h3>Build and validate</h3><p>Learned the platform, structured the source files, built custom calculations, configured filters, and tested every campaign, product, and tactic.</p><small><b>My contribution</b>Owned the interface, connections, logic, visualizations, and accuracy checks end to end.</small></article>
                <article class="pd-phase"><div class="pd-phase-top"><span>03</span><i class="pd-phase-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3"/><path d="M3.5 20c.5-4 2.3-6 5.5-6s5 2 5.5 6M15 11l2 2 4-4"/></svg></i></div><h3>Launch and transfer</h3><p>Walked the client through the dashboard, trained the digital team, refined the date selector, and supported the live workflow for six weeks.</p><small><b>My contribution</b>Created the SOP and transitioned routine management to the digital marketing analyst.</small></article>
              </div>
            </section>

            <section class="pd-section pd-training">
              <div><span class="pd-section-label">05 &middot; Rollout and support</span><h2>Built to be maintained without me</h2><div class="pd-tags"><span>Internal SOP</span><span>Hands On Training</span><span>Client Kickoff &amp; Rollout</span></div></div>
              <aside class="pd-handoff"><i>&#10003;</i><span>Ownership transferred</span><h3>From creator to analyst</h3><p>I documented the complete update and validation workflow in an internal SOP, trained a teammate, and transferred routine dashboard ownership within six weeks. After the handoff, she could manage the weekly reporting process independently.</p></aside>
            </section>

            <section class="pd-section pd-results">
              <div class="pd-results-band"><div><b>Before</b><strong>6 hours</strong><span>Previous weekly reporting time</span></div><i>&rarr;</i><div><b>After</b><strong>15&ndash;20 min</strong><span>Routine update time by week three</span></div><div class="pd-reduction"><b>Time reduction</b><strong>94&ndash;96%</strong><span>More time available for analysis</span></div></div>
              <div class="pd-reflection">
                <article><span>Impact</span><h3>More time for insight</h3><p>The dashboard was used weekly through at least 2024. It eliminated spreadsheet delivery, met the four-page target, and returned hours each week for analysis and performance storytelling.</p></article>
                <article><span>What I learned</span><h3>Automation changes the work</h3><p>The achievement was not simply building a dashboard. It was redesigning a process so reporting supported better thinking instead of crowding it out.</p></article>
                <article><span>What I would revisit</span><h3>Connect the sources directly</h3><p>Approved API or data-lake connectors could remove the remaining export step, make updates nearly instant, and create more time for optimization.</p></article>
              </div>
            </section>
          </main>
          <a class="pd-back" href="/" target="_self">&larr; Return to portfolio</a>
        </div>
        """).replace("\n\n", "\n"),
        unsafe_allow_html=True,
    )
