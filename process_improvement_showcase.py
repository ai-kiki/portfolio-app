from __future__ import annotations

import base64
import html
from pathlib import Path
from textwrap import dedent

import streamlit as st


def _safe(value: object) -> str:
    return html.escape(str(value))


def _hero_data_uri() -> str:
    image_path = Path(__file__).parent / "assets" / "insertion-order-automation-hero.png"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def _training_data_uri() -> str:
    image_path = Path(__file__).parent / "assets" / "rpa-training-rollout-visual.png"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap');
[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppDeployButton"], .stAppDeployButton { display: none !important; }
#MainMenu, footer { visibility: hidden; }
[data-testid="stSidebar"] { background: #071c3b; }
[data-testid="stSidebar"] * { color: rgba(255,255,255,.88) !important; }
.stApp { background: #f5f8fc; }
.block-container { max-width: 1280px; padding: 1.5rem 1.25rem 4rem; }
.io-case, .io-case * { box-sizing: border-box; }
.io-case { --blue:#075de8; --navy:#071c3b; --teal:#008f83; --coral:#ee765d; --ink:#10233f; --muted:#5f6f84; color:var(--ink); font-family:"DM Sans",sans-serif; }
.io-case h1, .io-case h2, .io-case h3, .io-case p { margin-block-start:0; }
.io-topbar { align-items:center; display:flex; justify-content:space-between; margin:0 auto 1.15rem; max-width:1180px; }
.io-brand { align-items:center; color:var(--ink)!important; display:flex; font-size:.92rem; font-weight:800; gap:.65rem; letter-spacing:.08em; text-decoration:none!important; text-transform:uppercase; }
.io-brand i { align-items:center; background:var(--navy); border-radius:50%; color:white; display:flex; font-style:normal; height:2rem; justify-content:center; width:2rem; }
.io-category { color:var(--blue); font-size:1.2rem; font-weight:800; }
.io-wrap { background:white; box-shadow:0 18px 55px rgba(7,28,59,.09); margin:0 auto; max-width:1180px; overflow:hidden; }
.io-hero { min-height:530px; overflow:hidden; position:relative; }
.io-hero img { height:100%; inset:0; object-fit:cover; position:absolute; width:100%; }
.io-hero::after { background:linear-gradient(90deg,rgba(255,255,255,.99) 0%,rgba(255,255,255,.95) 30%,rgba(255,255,255,.66) 47%,rgba(255,255,255,.03) 72%); content:""; inset:0; position:absolute; }
.io-hero-copy { max-width:650px; padding:5.2rem 0 4.4rem 4.3rem; position:relative; width:58%; z-index:1; }
.io-eyebrow, .io-section-label { color:var(--blue); font-size:.84rem; font-weight:850; letter-spacing:.13em; text-transform:uppercase; }
.io-hero h1 { color:#07182e!important; font-family:"Newsreader",Georgia,serif!important; font-size:clamp(2.4rem,3.5vw,3.3rem); font-weight:600; letter-spacing:-.04em; line-height:.96; margin:1.1rem 0 1.65rem; max-width:560px; }
.io-title-rule { background:var(--blue); border-radius:4px; height:5px; margin-bottom:1.35rem; width:54px; }
.io-role { align-items:center; display:flex; font-size:1rem; font-weight:800; gap:.7rem; }
.io-role i { align-items:center; background:var(--blue); border-radius:50%; color:white; display:flex; font-style:normal; height:2.15rem; justify-content:center; width:2.15rem; }
.io-summary-band { background:white; border-top:1px solid #e6ebf1; padding:1.5rem 4.3rem; }
.io-summary { color:#344760; font-size:1.2rem!important; line-height:1.62; margin:0; max-width:940px; }
.io-meta { background:#fbfcfe; border-bottom:1px solid #dfe6ee; border-top:1px solid #dfe6ee; display:grid; grid-template-columns:1.2fr 1fr 1.1fr 1fr; }
.io-meta div { border-right:1px solid #dfe6ee; padding:1.35rem 1.55rem; }
.io-meta div:last-child { border-right:0; }
.io-meta span { color:#7a899d; display:block; font-size:.7rem; font-weight:850; letter-spacing:.11em; margin-bottom:.45rem; text-transform:uppercase; }
.io-meta strong { display:block; font-size:1rem; line-height:1.45; }
.io-section { padding:5.2rem 4.3rem; }
.io-heading { max-width:710px; }
.io-heading.center { margin:0 auto 2.9rem; text-align:center; }
.io-heading h2 { color:#0a203d!important; font-family:"Newsreader",Georgia,serif!important; font-size:clamp(2.8rem,4.8vw,4.2rem); font-weight:600; letter-spacing:-.04em; line-height:1; margin:.7rem 0 0; }
.io-heading p { color:var(--muted); font-size:1.2rem; line-height:1.65; margin:1rem 0 0; }
.io-section-label { font-size:1.12rem; letter-spacing:.11em; }
.io-section .io-heading h2 { font-size:clamp(2rem,3.35vw,2.95rem); }
.io-workflow-section { background:linear-gradient(180deg,#fff,#f5f9fe); }
.io-workflow-section .io-section-label { font-size:1.25rem; letter-spacing:.08em; }
.io-workflow-section .io-heading { max-width:850px; }
.io-workflow-section .io-heading h2 { font-size:clamp(2rem,3vw,2.75rem); line-height:1.06; }
.io-workflow { align-items:center; display:grid; gap:.7rem; grid-template-columns:1fr 30px 1fr 30px 1fr 30px 1fr; }
.io-step { --card:#1769e0; --tint:#eef5ff; background:linear-gradient(180deg,#fff 0%,var(--tint) 100%); border:1px solid #dce5f0; border-radius:20px; box-shadow:0 12px 28px rgba(17,56,102,.08); display:flex; flex-direction:column; height:470px; overflow:hidden; padding:0 1.05rem 1.75rem; text-align:center; }
.io-step.guided { --card:#1769e0; --tint:#edf5ff; }
.io-step.rules { --card:#059b83; --tint:#ebf9f5; }
.io-step.order { --card:#6d55c7; --tint:#f3f0ff; }
.io-step.adoption { --card:#dd7b18; --tint:#fff5e8; }
.io-step-label { background:var(--card); border-radius:19px 19px 8px 8px; color:white; display:flex; font-size:.86rem; font-weight:850; justify-content:center; margin:-1px -1.1rem 0; min-height:45px; padding:.75rem .45rem; }
.io-step-visual { align-items:center; display:flex; flex:0 0 205px; justify-content:center; padding:.8rem 0 .25rem; }
.io-step-visual svg { filter:drop-shadow(0 8px 9px rgba(27,55,91,.1)); height:185px; max-width:100%; width:190px; }
.io-step p { color:#43546b; font-size:.92rem; line-height:1.45; margin:auto 0 .45rem; min-height:145px; }
.io-arrow { color:var(--blue); font-size:1.65rem; text-align:center; }
.io-challenge-grid { display:grid; gap:1rem; grid-template-columns:repeat(4,1fr); margin-top:2.7rem; }
.io-pain-card { --pain:#1769e0; --pain-bg:#eef5ff; background:linear-gradient(180deg,#fff,var(--pain-bg)); border:1px solid #dce5ef; border-radius:18px; display:flex; flex-direction:column; min-height:310px; padding:1.45rem; }
.io-pain-card.requirements { --pain:#df6b53; --pain-bg:#fff1ed; }
.io-pain-card.variation { --pain:#6d55c7; --pain-bg:#f3f0ff; }
.io-pain-card.risk { --pain:#d8861e; --pain-bg:#fff5e8; }
.io-pain-icon { align-items:center; background:var(--pain); border-radius:14px; display:flex; height:54px; justify-content:center; margin-bottom:1.35rem; width:54px; }
.io-pain-icon svg { height:30px; stroke:#fff; stroke-linecap:round; stroke-linejoin:round; stroke-width:2; width:30px; }
.io-pain-card small { color:var(--pain); font-size:.7rem; font-weight:850; letter-spacing:.08em; line-height:1.4; min-height:34px; text-transform:uppercase; }
.io-pain-card h3 { color:var(--ink)!important; font-family:"Newsreader",Georgia,serif!important; font-size:1.45rem; line-height:1.08; margin:.65rem 0 .85rem; }
.io-pain-card p { color:#4c5e74; font-size:.94rem; line-height:1.55; margin:0; }
.io-friction-summary { align-items:center; background:var(--navy); border-radius:14px; color:white; display:flex; flex-wrap:wrap; gap:.65rem 1.1rem; justify-content:center; margin-top:1.25rem; padding:1rem 1.25rem; }
.io-friction-summary strong { color:#8db9ff; font-size:.72rem; letter-spacing:.12em; text-transform:uppercase; }
.io-friction-summary span { align-items:center; display:flex; font-size:.92rem; font-weight:750; gap:.5rem; }
.io-friction-summary span::before { background:#21a99a; border-radius:50%; content:""; height:7px; width:7px; }
.io-role-section { background:var(--navy); color:white; }
.io-role-section .io-section-label { color:#70a9ff; }
.io-role-section h2 { color:white!important; }
.io-role-section .io-role-lead { color:#f3eee4!important; font-size:1.18rem!important; line-height:1.65; max-width:800px; }
.io-contributions { display:grid; gap:1rem; grid-template-columns:repeat(3,1fr); margin-top:3rem; }
.io-contribution { --accent:#4f9cff; background:linear-gradient(160deg,rgba(255,255,255,.08),rgba(255,255,255,.025)); border:1px solid rgba(255,255,255,.14); border-radius:18px; display:flex; flex-direction:column; min-height:320px; overflow:hidden; padding:1.45rem; position:relative; }
.io-contribution:nth-child(2) { --accent:#2dc6ad; }
.io-contribution:nth-child(3) { --accent:#a98cff; }
.io-contribution:nth-child(4) { --accent:#f2a64c; }
.io-contribution:nth-child(5) { --accent:#ed6f91; }
.io-contribution:nth-child(6) { --accent:#63c5da; }
.io-contribution::before { background:var(--accent); content:""; height:5px; inset:0 0 auto; position:absolute; }
.io-contribution-top { align-items:center; display:flex; justify-content:space-between; margin-bottom:2rem; }
.io-contribution-top span { color:var(--accent); font-family:"Newsreader",Georgia,serif; font-size:2.8rem; font-weight:650; letter-spacing:-.04em; line-height:1; }
.io-contribution-top i { align-items:center; background:color-mix(in srgb,var(--accent) 18%,transparent); border:1px solid color-mix(in srgb,var(--accent) 55%,transparent); border-radius:13px; display:flex; height:50px; justify-content:center; width:50px; }
.io-contribution-top svg { fill:none; height:27px; stroke:var(--accent); stroke-linecap:round; stroke-linejoin:round; stroke-width:2; width:27px; }
.io-contribution h3 { color:white!important; font-size:1.35rem; line-height:1.2; margin:0 0 1rem; }
.io-contribution p { color:#c5d1e1; font-size:1rem; line-height:1.62; margin:0; }
.io-paths { align-items:center; display:grid; gap:1rem; grid-template-columns:1fr 42px 1.1fr; grid-template-rows:1fr 1fr; margin-top:2.8rem; }
.io-paths article { background:white; border:1px solid #dce6f1; border-radius:14px; box-shadow:0 8px 18px rgba(18,54,94,.06); min-height:155px; padding:1.45rem; }
.io-paths article:nth-child(1) { grid-column:1; grid-row:1; }
.io-paths article:nth-child(2) { grid-column:1; grid-row:2; }
.io-paths > i { color:var(--blue); font-size:1.8rem; font-style:normal; grid-column:2; grid-row:1/3; text-align:center; }
.io-paths .io-output { background:linear-gradient(150deg,#064fbf,#0872ed); border:0; color:white; display:flex; flex-direction:column; grid-column:3; grid-row:1/3; justify-content:center; padding:3.25rem 1.9rem; }
.io-paths span { color:#7a899d; display:block; font-size:.72rem; font-weight:850; letter-spacing:.1em; margin-bottom:.45rem; text-transform:uppercase; }
.io-paths .io-output span { color:#bed8ff; }
.io-paths strong { font-family:"Newsreader",Georgia,serif; font-size:1.58rem; }
.io-paths p { color:#596b80; font-size:.95rem; line-height:1.55; margin:.7rem 0 0; }
.io-paths .io-output p { color:#e4efff; }
.io-training { background:#fff; display:grid; gap:2.4rem; grid-template-columns:1fr; }
.io-training .io-heading { max-width:900px; }
.io-training-media { align-items:stretch; display:grid; gap:1.3rem; grid-template-columns:minmax(0,1.45fr) minmax(260px,.75fr); }
.io-training-visual { aspect-ratio:1/1; background:#f6f8fb; border:1px solid #d6e0eb; border-radius:18px; box-shadow:0 14px 30px rgba(18,54,94,.1); margin:0; overflow:hidden; width:100%; }
.io-training-visual img { display:block; height:auto; max-width:none; min-height:100%; object-fit:cover; transform:translateX(-33.8%); width:326%; }
.io-tags { display:flex; flex-wrap:wrap; gap:.55rem; margin-top:1.3rem; }
.io-tags span { background:#e3f4f0; border-radius:999px; color:#075082; font-size:.82rem; font-weight:750; padding:.58rem .78rem; }
.io-training-tags { display:grid; gap:.85rem; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,1fr); margin:0; }
.io-training-tags span { align-items:center; border:1px solid #cce4df; border-radius:16px; display:flex; font-size:.92rem; justify-content:center; min-height:0; padding:1rem; text-align:center; }
.io-training-tags span:nth-child(3) { box-sizing:border-box; grid-column:1/3; justify-self:center; width:calc((100% - .85rem)/2); }
.io-reflection { background:#c4d1df; color:var(--navy); display:grid; gap:1px; grid-template-columns:repeat(3,1fr); padding:0; }
.io-reflection article { border-right:1px solid rgba(7,28,59,.16); min-height:300px; padding:2.45rem; }
.io-reflection article:nth-child(1) { background:#dfe9f3; }
.io-reflection article:nth-child(2) { background:#dff1ee; }
.io-reflection article:nth-child(3) { background:#edf0f6; }
.io-reflection article:last-child { border-right:0; }
.io-reflection span { color:#082651; font-size:1.08rem; font-weight:850; letter-spacing:.08em; text-transform:uppercase; }
.io-reflection h3 { color:#071c3b!important; font-family:"DM Sans",Arial,sans-serif!important; font-size:2.15rem; font-weight:750; letter-spacing:-.025em; line-height:.9; margin:1.15rem 0 .75rem; text-transform:none; }
.io-reflection p { color:#102d53; font-size:1.05rem; line-height:1.65; }
.io-disclosure { color:#76869a; font-size:.95rem; line-height:1.55; margin:0 auto .7rem; max-width:1000px; padding-top:2.4rem; text-align:center; }
.io-back { color:var(--navy)!important; display:block; font-size:.94rem; font-weight:800; margin:1rem 0 0; text-align:center; text-decoration:none!important; }
@media(max-width:920px){.io-meta{grid-template-columns:repeat(2,1fr)}.io-workflow{grid-template-columns:repeat(4,1fr)}.io-arrow{display:none}.io-contributions,.io-challenge-grid{grid-template-columns:repeat(2,1fr)}.io-reflection{grid-template-columns:1fr}}
@media(max-width:700px){.block-container{padding:1rem .7rem 3rem}.io-category{display:none}.io-hero{min-height:650px}.io-hero img{bottom:0;height:42%;top:auto}.io-hero::after{background:linear-gradient(180deg,#fff 0 55%,rgba(255,255,255,.1) 82%)}.io-hero-copy{padding:3rem 1.5rem 18rem;width:100%}.io-hero h1{font-size:3.55rem}.io-summary-band{padding:1.3rem 1.5rem}.io-meta{grid-template-columns:1fr 1fr}.io-section{padding:3.5rem 1.35rem}.io-workflow,.io-contributions,.io-challenge-grid,.io-training,.io-training-media{grid-template-columns:1fr}.io-training-tags{grid-template-columns:1fr 1fr;min-height:260px}.io-step{height:auto;min-height:430px}.io-step p{min-height:auto}.io-paths{grid-template-columns:1fr;grid-template-rows:auto}.io-paths article:nth-child(1),.io-paths article:nth-child(2),.io-paths>i,.io-paths .io-output{grid-column:1;grid-row:auto}.io-paths>i{transform:rotate(90deg)}}
</style>
"""


def render_process_improvement_case_study() -> None:
    st.set_page_config(
        page_title="Robotic Process Automation (RPA) | L.C. Felton",
        page_icon="IO",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    hero = _hero_data_uri()
    training_visual = _training_data_uri()
    st.markdown(
        _STYLES
        + dedent(f"""
        <div class="io-case">
          <header class="io-topbar"><a class="io-brand" href="/" target="_self"><i>IO</i> Process improvement case study</a><span class="io-category">Process Automation</span></header>
          <main class="io-wrap">
            <section class="io-hero">
              <img src="{hero}" alt="Three colleagues collaborating over a laptop and workflow map">
              <div class="io-hero-copy">
                <span class="io-eyebrow">Workflow automation &middot; Summer 2022</span>
                <h1>Robotic Process Automation <span style="white-space:nowrap;">(RPA)</span></h1>
                <div class="io-title-rule"></div>
              </div>
            </section>
            <section class="io-summary-band"><p class="io-summary">A cross-functional team transformed complex campaign rules into guided and direct-entry workflows, using automation to reduce guesswork and create a faster, more controlled path to the existing insertion-order platform.</p></section>
            <section class="io-meta">
              <div><span>My role</span><strong>Automation Business Lead &amp; Market Champion</strong></div>
              <div><span>Partners</span><strong>Sales, Digital Support, Product Management, and Dev Ops</strong></div>
              <div><span>Systems</span><strong>Zoho, Excel, Zapier, web-based IO</strong></div>
              <div><span>Team model</span><strong>Peer business leads representing regional teams</strong></div>
            </section>

            <section class="io-section io-workflow-section">
              <div class="io-heading center"><span class="io-section-label">How the solution worked</span><h2>From campaign criteria to a complete insertion order</h2><p>Users could choose a guided decision path or direct-entry path. Business rules validated campaign requirements and, when needed, selected appropriate platforms and products before generating the insertion order.</p></div>
              <div class="io-workflow">
                <article class="io-step guided"><span class="io-step-label">Two Input Paths</span><div class="io-step-visual">
                  <svg viewBox="0 0 200 180" aria-hidden="true"><rect x="10" y="22" width="72" height="50" rx="10" fill="#fff" stroke="#bfd0e4"/><rect x="10" y="108" width="72" height="50" rx="10" fill="#fff" stroke="#bfd0e4"/><rect x="118" y="65" width="70" height="50" rx="12" style="fill:var(--card)"/><path d="M82 47h18c11 0 18 9 18 20v8M82 133h18c11 0 18-9 18-20v-8" fill="none" style="stroke:var(--card)" stroke-width="3"/><path d="M110 70l8 8 8-8M110 110l8-8 8 8" fill="none" style="stroke:var(--card)" stroke-linecap="round" stroke-linejoin="round" stroke-width="3"/><circle cx="28" cy="39" r="7" style="fill:var(--card)"/><path d="M22 58h48M22 64h36" stroke="#b3c5d9" stroke-width="5" stroke-linecap="round"/><path d="M22 121h48M22 132h48M22 143h32" stroke="#b3c5d9" stroke-width="5" stroke-linecap="round"/><path d="M137 83h32M137 94h32M137 105h22" stroke="#fff" stroke-width="5" stroke-linecap="round"/></svg>
                </div><p>Guided Zoho decision support or streamlined Excel entry based on what the user already knew</p></article><span class="io-arrow">&rarr;</span>
                <article class="io-step rules"><span class="io-step-label">Rule-Based Decisions</span><div class="io-step-visual">
                  <svg viewBox="0 0 200 180" aria-hidden="true"><path d="M100 14l38 32-38 32-38-32z" style="fill:var(--card)"/><path d="M100 78v22M100 100H45v19M100 100h55v19" fill="none" style="stroke:var(--card)" stroke-width="3"/><rect x="10" y="119" width="70" height="43" rx="9" fill="#fff" stroke="#c7ddd9"/><rect x="120" y="119" width="70" height="43" rx="9" fill="#fff" stroke="#c7ddd9"/><path d="M83 43l12 12 23-27" fill="none" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="6"/><circle cx="30" cy="140" r="9" style="fill:var(--card)"/><path d="M27 140l3 3 6-7" fill="none" stroke="#fff" stroke-width="2"/><path d="M45 134h23M45 145h17M135 134h40M135 145h30" stroke="#98b3af" stroke-linecap="round" stroke-width="5"/></svg>
                </div><p>Campaign criteria evaluated to validate requirements and determine appropriate platform and product selections when needed</p></article><span class="io-arrow">&rarr;</span>
                <article class="io-step order"><span class="io-step-label">Automated IO</span><div class="io-step-visual">
                  <svg viewBox="0 0 200 180" aria-hidden="true"><path d="M42 12h92l28 28v126H42z" fill="#fff" stroke="#c8c0e5"/><path d="M134 12v28h28" style="fill:var(--card)" opacity=".8"/><rect x="58" y="34" width="58" height="10" rx="3" style="fill:var(--card)"/><rect x="58" y="55" width="82" height="7" rx="3" fill="#d7d2ec"/><g fill="none" stroke="#c8c0e5"><rect x="58" y="78" width="86" height="54"/><path d="M58 96h86M58 114h86M78 78v54M119 78v54"/></g><g style="fill:var(--card)"><circle cx="68" cy="87" r="3"/><circle cx="68" cy="105" r="3"/><circle cx="68" cy="123" r="3"/></g><rect x="58" y="145" width="67" height="7" rx="3" style="fill:var(--card)" opacity=".85"/><g style="stroke:var(--card)" stroke-width="2" opacity=".65"><path d="M13 45h22M20 60h15M10 75h25M20 119h15M12 134h23"/></g></svg>
                </div><p>A complete insertion order populated automatically through the workflow</p></article><span class="io-arrow">&rarr;</span>
                <article class="io-step adoption"><span class="io-step-label">Adoption</span><div class="io-step-visual">
                  <svg viewBox="0 0 200 180" aria-hidden="true"><circle cx="100" cy="90" r="64" fill="none" style="stroke:var(--card)" stroke-width="2" stroke-dasharray="5 5" opacity=".55"/><rect x="57" y="62" width="86" height="54" rx="6" fill="#fff" stroke="#d5c6ae"/><rect x="64" y="69" width="72" height="39" rx="3" fill="#fdf3e6"/><circle cx="100" cy="88" r="15" style="fill:var(--card)"/><path d="M93 88l5 5 10-12" fill="none" stroke="#fff" stroke-width="3"/><path d="M48 124h104l-8 10H56z" fill="#1f3c67"/><g fill="#fff" stroke="#e3d3bd"><circle cx="100" cy="20" r="19"/><circle cx="34" cy="87" r="19"/><circle cx="166" cy="87" r="19"/><circle cx="100" cy="158" r="19"/></g><path d="M93 15l7-4 7 4-7 4zM95 20v7h10v-7" style="fill:var(--card)"/><path d="M25 82h7v12h-7zm10-4h7v16h-7" style="fill:var(--card)"/><path d="M158 80h16v12h-16zm3 3v6m5-6v6" fill="none" style="stroke:var(--card)" stroke-width="2"/><g style="fill:var(--card)"><circle cx="94" cy="153" r="4"/><circle cx="106" cy="153" r="4"/><path d="M86 165c1-7 5-10 8-10s7 3 8 10zM98 165c1-7 5-10 8-10s7 3 8 10z"/></g></svg>
                </div><p>Training, documentation, office hours, and peer support enabled sustained use</p></article>
              </div>
            </section>

            <section class="io-section">
              <div class="io-heading"><span class="io-section-label">01 &middot; The challenge</span><h2>A standardized form could not eliminate execution complexity</h2><p>The insertion order followed a standard format, but campaign requirements varied across products, tactics, vendors, budgets, and execution teams. Recurring friction accumulated throughout the handoff process.</p></div>
              <div class="io-challenge-grid">
                <article class="io-pain-card">
                  <div class="io-pain-icon"><svg viewBox="0 0 32 32" fill="none"><path d="M8 5h16v22H8zM12 10h8M12 15h8M12 20h5"/><path d="M4 9v14M28 9v14"/></svg></div>
                  <small>Sales</small><h3>Process Inefficiency</h3><p>Repetitive preparation consumed time that could have been spent on revenue-generating activities.</p>
                </article>
                <article class="io-pain-card requirements">
                  <div class="io-pain-icon"><svg viewBox="0 0 32 32" fill="none"><path d="M9 5h14v22H9zM12 10h8M12 15h5"/><path d="M18 22l3-3 3 3M21 19v7"/></svg></div>
                  <small>Digital Support</small><h3>Incomplete Requirements</h3><p>Missing or ambiguous campaign details created follow-ups, assumptions, and stalled orders.</p>
                </article>
                <article class="io-pain-card variation">
                  <div class="io-pain-icon"><svg viewBox="0 0 32 32" fill="none"><path d="M6 8h8v6H6zM18 18h8v6h-8zM18 5h8v6h-8zM14 11h4M16 11v10M16 21h2"/></svg></div>
                  <small>Demand-Side Platforms (DSPs)</small><h3>Variable Execution Requirements</h3><p>Product, tactic, budget, and vendor differences made consistent interpretation difficult.</p>
                </article>
                <article class="io-pain-card risk">
                  <div class="io-pain-icon"><svg viewBox="0 0 32 32" fill="none"><path d="M5 9h17M18 5l4 4-4 4M27 23H10M14 19l-4 4 4 4"/><path d="M24 17l4 8h-8zM24 20v2"/></svg></div>
                  <small>Cross-team impact</small><h3>Handoff &amp; Execution Risk</h3><p>Clarification loops, rework, and assumptions increased turnaround time and the risk of incorrect execution.</p>
                </article>
              </div>
              <div class="io-friction-summary"><strong>Recurring consequences</strong><span>Delays</span><span>Rework</span><span>Inconsistent execution</span><span>Error risk</span><span>Lost or reduced revenue</span></div>
            </section>

            <section class="io-section io-role-section">
              <div class="io-heading"><span class="io-section-label">02 &middot; My contribution</span><h2>Turning Expertise into Automation Logic</h2><p class="io-role-lead">I collaborated as one of several peer business leads on this company-wide initiative, bringing regional market and operational expertise into solution design. I helped define campaign requirements, translate business rules into automation logic, shape the input tools, validate and refine the workflow with Dev Ops, and support rollout and adoption within my region.</p></div>
              <div class="io-contributions">
                <article class="io-contribution"><div class="io-contribution-top"><span>01</span><i><svg viewBox="0 0 32 32"><circle cx="11" cy="11" r="4"/><circle cx="23" cy="13" r="3"/><path d="M4 27v-3c0-5 3-8 7-8s7 3 7 8v3M18 20c1-2 3-3 5-3 3 0 5 2 5 6v4"/></svg></i></div><h3>Represent Business Needs</h3><p>Brought regional Sales and Digital Support perspectives into the project, including recurring workflow challenges and execution requirements.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>02</span><i><svg viewBox="0 0 32 32"><circle cx="7" cy="16" r="3"/><circle cx="16" cy="7" r="3"/><circle cx="25" cy="16" r="3"/><circle cx="16" cy="25" r="3"/><path d="M9 14l5-5M18 9l5 5M23 18l-5 5M14 23l-5-5"/></svg></i></div><h3>Map Campaign Requirements</h3><p>Mapped relationships among campaign components, product rules, targeting requirements, vendor specifications, and operational dependencies so the workflow could capture complete, executable orders.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>03</span><i><svg viewBox="0 0 32 32"><path d="M7 5h18v22H7zM11 10h10M11 15h10M11 20h6"/><path d="M21 19v6M18 22h6"/></svg></i></div><h3>Shape the Inputs</h3><p>Helped shape two input experiences: a guided Zoho path that used campaign criteria to determine appropriate selections and a streamlined Excel path for users who already knew the required configuration.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>04</span><i><svg viewBox="0 0 32 32"><path d="M6 7h8v7H6zM18 18h8v7h-8zM18 5h8v7h-8zM14 10h4M16 10v12M16 22h2"/></svg></i></div><h3>Translate Rules with Dev Ops</h3><p>Worked with Dev Ops to translate campaign relationships, eligibility criteria, dependencies, exceptions, and decision rules into logic that could validate known selections or determine appropriate ones.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>05</span><i><svg viewBox="0 0 32 32"><path d="M11 5h10M14 5v7L7 24c-1 2 0 3 2 3h14c2 0 3-1 2-3l-7-12V5"/><path d="M10 21h12M13 17l3 3 4-5"/></svg></i></div><h3>Test and Refine</h3><p>Tested sample and real orders, documented gaps and errors, and helped refine triggers, captured data, and workflow behavior.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>06</span><i><svg viewBox="0 0 32 32"><circle cx="16" cy="10" r="4"/><path d="M8 27v-4c0-5 3-8 8-8s8 3 8 8v4M5 12l-3 3 3 3M27 12l3 3-3 3"/></svg></i></div><h3>Enable Regional Adoption</h3><p>Created a two-part training video and SOP, conducted live launch training, held office hours, and provided rollout support for Sales and Digital Support teams in my region.</p></article>
              </div>
            </section>

            <section class="io-section" style="background:#f4f8fc;">
              <div class="io-heading"><span class="io-section-label">03 &middot; The solution</span><h2>Two input paths supported different user needs</h2><p>The solution accommodated users with different levels of product and platform knowledge. One path provided guided decision support, while the other allowed experienced users to enter known campaign selections directly.</p></div>
              <div class="io-paths">
                <article><span>Guided decision path</span><strong>Zoho form</strong><p>Users entered campaign criteria. When platform or product selections were unclear, the automation applied business rules and made the appropriate selections.</p></article>
                <article><span>Direct-entry path</span><strong>Excel form</strong><p>Sales and Digital Support users who understood the platform options and campaign requirements could enter their known selections directly.</p></article>
                <i>&rarr;</i>
                <article class="io-output"><span>Shared automation layer</span><strong>Workflow-populated insertion order</strong><p>Both input paths fed the automation that validated requirements and populated the insertion order.</p></article>
              </div>
            </section>

            <section class="io-section io-training">
              <div class="io-heading"><span class="io-section-label">04 &middot; Rollout and support</span><h2>Making the new process usable</h2><p>The team received one week to prepare Sales and Digital Support users for launch. My enablement materials clarified when to use the guided Zoho path for decision support and when experienced users could use the streamlined Excel path for known configurations. I also conducted live launch training and gave users multiple ways to learn and get help.</p></div>
              <div class="io-training-media"><figure class="io-training-visual"><img src="{training_visual}" alt="Laptop video tutorial displayed beside a step-by-step training guide and notes"></figure><div class="io-tags io-training-tags"><span>Two-part video walkthrough</span><span>Step-by-step SOP</span><span>Live launch training</span><span>Market office hours</span><span>Live questions and support</span></div></div>
            </section>

            <section class="io-reflection">
              <article><span>Impact</span><h3>A faster, more controlled process</h3><p>The redesigned workflow gave users clearer input paths, reduced guesswork, and stopped incomplete or invalid orders before they reached execution teams. It also created a more consistent, controlled handoff from campaign setup to execution.</p></article>
              <article><span>What I learned</span><h3>Business knowledge can become automation logic</h3><p>This was my first close look at triggers and workflow logic. It showed me that subject-matter expertise is essential when an automation must reflect real operational rules.</p></article>
              <article><span>What I would revisit</span><h3>Redesign the system, not only the workflow</h3><p>Given the opportunity, I would evaluate replacing the legacy insertion-order experience instead of building automation around it, while retaining the validation logic that made the new process useful.</p></article>
            </section>
          </main>
          <p class="io-disclosure">This was a collaborative corporate initiative. My title reflects my contribution as one of several peer business leads and my responsibility for adoption within my market; it does not imply sole ownership of the project.</p>
          <a class="io-back" href="/" target="_self">&larr; Return to portfolio</a>
        </div>
        """).replace("\n\n", "\n"),
        unsafe_allow_html=True,
    )
