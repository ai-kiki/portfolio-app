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
.io-step { --card:#1769e0; --tint:#eef5ff; background:linear-gradient(180deg,#fff 0%,var(--tint) 100%); border:1px solid #dce5f0; border-radius:20px; box-shadow:0 12px 28px rgba(17,56,102,.08); display:flex; flex-direction:column; height:395px; overflow:hidden; padding:0 1.05rem 1.55rem; text-align:center; }
.io-step.guided { --card:#1769e0; --tint:#edf5ff; }
.io-step.rules { --card:#059b83; --tint:#ebf9f5; }
.io-step.order { --card:#6d55c7; --tint:#f3f0ff; }
.io-step.adoption { --card:#dd7b18; --tint:#fff5e8; }
.io-step-label { background:var(--card); border-radius:19px 19px 8px 8px; color:white; display:flex; font-size:.86rem; font-weight:850; justify-content:center; margin:-1px -1.1rem 0; min-height:45px; padding:.75rem .45rem; }
.io-step-visual { align-items:center; display:flex; flex:0 0 205px; justify-content:center; padding:.8rem 0 .25rem; }
.io-step-visual svg { filter:drop-shadow(0 8px 9px rgba(27,55,91,.1)); height:185px; max-width:100%; width:190px; }
.io-step p { color:#43546b; font-size:.92rem; line-height:1.45; margin:auto 0 .2rem; min-height:76px; }
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
.io-contributions { display:grid; gap:1rem; grid-template-columns:repeat(4,1fr); margin-top:3rem; }
.io-contribution { --accent:#4f9cff; background:linear-gradient(160deg,rgba(255,255,255,.08),rgba(255,255,255,.025)); border:1px solid rgba(255,255,255,.14); border-radius:18px; display:flex; flex-direction:column; min-height:330px; overflow:hidden; padding:1.45rem; position:relative; }
.io-contribution:nth-child(2) { --accent:#2dc6ad; }
.io-contribution:nth-child(3) { --accent:#a98cff; }
.io-contribution:nth-child(4) { --accent:#f2a64c; }
.io-contribution::before { background:var(--accent); content:""; height:5px; inset:0 0 auto; position:absolute; }
.io-contribution-top { align-items:center; display:flex; justify-content:space-between; margin-bottom:2rem; }
.io-contribution-top span { color:var(--accent); font-family:"Newsreader",Georgia,serif; font-size:2.8rem; font-weight:650; letter-spacing:-.04em; line-height:1; }
.io-contribution-top i { align-items:center; background:color-mix(in srgb,var(--accent) 18%,transparent); border:1px solid color-mix(in srgb,var(--accent) 55%,transparent); border-radius:13px; display:flex; height:50px; justify-content:center; width:50px; }
.io-contribution-top svg { fill:none; height:27px; stroke:var(--accent); stroke-linecap:round; stroke-linejoin:round; stroke-width:2; width:27px; }
.io-contribution h3 { color:white!important; font-size:1.35rem; line-height:1.2; margin:0 0 1rem; }
.io-contribution p { color:#c5d1e1; font-size:1rem; line-height:1.62; margin:0; }
.io-logic-grid { display:grid; gap:1rem; grid-template-columns:repeat(3,1fr); margin-top:2.8rem; }
.io-logic-card { background:#f7faff; border:1px solid #dce5ef; border-radius:17px; padding:1.5rem; }
.io-logic-card span { color:var(--blue); font-size:.74rem; font-weight:850; letter-spacing:.08em; text-transform:uppercase; }
.io-logic-card h3 { color:var(--ink)!important; font-size:1.2rem; margin:1.2rem 0 .7rem; }
.io-logic-card p { color:var(--muted); font-size:1.02rem; line-height:1.58; }
.io-paths { align-items:center; display:grid; gap:1rem; grid-template-columns:1fr 42px 1.1fr; grid-template-rows:1fr 1fr; margin-top:2.8rem; }
.io-paths article { background:white; border:1px solid #dce6f1; border-radius:14px; box-shadow:0 8px 18px rgba(18,54,94,.06); padding:1.45rem; }
.io-paths article:nth-child(1) { grid-column:1; grid-row:1; }
.io-paths article:nth-child(2) { grid-column:1; grid-row:2; }
.io-paths > i { color:var(--blue); font-size:1.8rem; font-style:normal; grid-column:2; grid-row:1/3; text-align:center; }
.io-paths .io-output { background:linear-gradient(150deg,#064fbf,#0872ed); border:0; color:white; grid-column:3; grid-row:1/3; padding:3.25rem 1.6rem; }
.io-paths span { color:#7a899d; display:block; font-size:.72rem; font-weight:850; letter-spacing:.1em; margin-bottom:.45rem; text-transform:uppercase; }
.io-paths .io-output span { color:#bed8ff; }
.io-paths strong { font-family:"Newsreader",Georgia,serif; font-size:1.58rem; }
.io-training { background:#f1f6fb; display:grid; gap:2.2rem; grid-template-columns:1fr 1fr; }
.io-training-panel { display:grid; gap:.8rem; grid-template-columns:1.2fr .8fr; }
.io-video, .io-guide { align-items:center; background:white; border:1px solid #cedbe9; border-radius:13px; box-shadow:0 8px 18px rgba(18,54,94,.06); display:flex; justify-content:center; min-height:150px; }
.io-video i { align-items:center; background:var(--blue); border-radius:50%; color:white; display:flex; font-style:normal; height:50px; justify-content:center; padding-left:3px; width:50px; }
.io-guide { align-content:center; display:grid; gap:.7rem; padding:1.8rem 1.1rem; }
.io-guide i { background:#cfdbea; border-radius:4px; display:block; height:7px; width:100%; }
.io-guide i:nth-child(even) { width:68%; }
.io-tags { display:flex; flex-wrap:wrap; gap:.55rem; margin-top:1.3rem; }
.io-tags span { background:#e3f4f0; border-radius:999px; color:#075082; font-size:.82rem; font-weight:750; padding:.58rem .78rem; }
.io-reflection { background:var(--navy); color:white; display:grid; gap:1px; grid-template-columns:repeat(3,1fr); padding:0; }
.io-reflection article { background:var(--navy); min-height:240px; padding:2.2rem; }
.io-reflection span { color:#70a9ff; font-size:.74rem; font-weight:850; letter-spacing:.12em; text-transform:uppercase; }
.io-reflection h3 { color:white!important; font-family:"Newsreader",Georgia,serif!important; font-size:1.7rem; margin:1.4rem 0 .8rem; }
.io-reflection p { color:#b8c6d8; font-size:1rem; line-height:1.65; }
.io-disclosure { color:#76869a; font-size:.95rem; line-height:1.55; margin:1.3rem auto .7rem; max-width:1000px; text-align:center; }
.io-back { color:var(--navy)!important; display:block; font-size:.94rem; font-weight:800; margin:1rem 0 0; text-align:center; text-decoration:none!important; }
@media(max-width:920px){.io-meta{grid-template-columns:repeat(2,1fr)}.io-workflow{grid-template-columns:repeat(4,1fr)}.io-arrow{display:none}.io-contributions,.io-challenge-grid{grid-template-columns:repeat(2,1fr)}.io-logic-grid{grid-template-columns:1fr}.io-reflection{grid-template-columns:1fr}}
@media(max-width:700px){.block-container{padding:1rem .7rem 3rem}.io-category{display:none}.io-hero{min-height:650px}.io-hero img{bottom:0;height:42%;top:auto}.io-hero::after{background:linear-gradient(180deg,#fff 0 55%,rgba(255,255,255,.1) 82%)}.io-hero-copy{padding:3rem 1.5rem 18rem;width:100%}.io-hero h1{font-size:3.55rem}.io-summary-band{padding:1.3rem 1.5rem}.io-meta{grid-template-columns:1fr 1fr}.io-section{padding:3.5rem 1.35rem}.io-workflow,.io-contributions,.io-challenge-grid,.io-training,.io-training-panel{grid-template-columns:1fr}.io-step{min-height:250px}.io-paths{grid-template-columns:1fr;grid-template-rows:auto}.io-paths article:nth-child(1),.io-paths article:nth-child(2),.io-paths>i,.io-paths .io-output{grid-column:1;grid-row:auto}.io-paths>i{transform:rotate(90deg)}}
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
            <section class="io-summary-band"><p class="io-summary">A multi-market team translated complex campaign rules into guided inputs and automated workflows, creating a faster and more controlled path to the company&rsquo;s existing insertion-order platform.</p></section>
            <section class="io-meta">
              <div><span>My role</span><strong>Automation Business Lead &amp; Market Champion</strong></div>
              <div><span>Partners</span><strong>Sales, Digital Support, Product Management, and Dev Ops</strong></div>
              <div><span>Systems</span><strong>Zoho, Excel, Zapier, web-based IO</strong></div>
              <div><span>Team model</span><strong>Peer business leads representing regional teams</strong></div>
            </section>

            <section class="io-section io-workflow-section">
              <div class="io-heading center"><span class="io-section-label">How the solution worked</span><h2>From campaign details to a cleaner insertion order</h2><p>Guided inputs and business rules reduced repetitive entry and prevented invalid combinations before the order reached execution teams.</p></div>
              <div class="io-workflow">
                <article class="io-step guided"><span class="io-step-label">Guided Inputs</span><div class="io-step-visual">
                  <svg viewBox="0 0 200 180" aria-hidden="true"><rect x="72" y="14" width="112" height="152" rx="12" fill="#fff" stroke="#bfd0e4"/><rect x="86" y="32" width="84" height="12" rx="4" fill="#dbe7f6"/><rect x="86" y="55" width="84" height="15" rx="4" fill="#eef3fa"/><rect x="86" y="79" width="84" height="15" rx="4" fill="#eef3fa"/><rect x="86" y="103" width="84" height="15" rx="4" fill="#eef3fa"/><rect x="86" y="134" width="66" height="17" rx="8" style="fill:var(--card)"/><g fill="#fff" stroke="#9eb7d3"><rect x="8" y="18" width="34" height="28" rx="7"/><rect x="8" y="55" width="34" height="28" rx="7"/><rect x="8" y="92" width="34" height="28" rx="7"/><rect x="8" y="129" width="34" height="28" rx="7"/></g><g fill="none" style="stroke:var(--card)" stroke-width="2"><path d="M42 32 C57 32 57 62 72 62"/><path d="M42 69 C57 69 58 77 72 77"/><path d="M42 106 C58 106 58 92 72 92"/><path d="M42 143 C58 143 58 107 72 107"/></g><g style="fill:var(--card)"><circle cx="25" cy="32" r="7"/><rect x="20" y="62" width="11" height="13" rx="2"/><path d="M17 103h16l-4 9h-8z"/><path d="M17 138h16v10H17z"/></g></svg>
                </div><p>Campaign details gathered for multiple channels in one structured form</p></article><span class="io-arrow">&rarr;</span>
                <article class="io-step rules"><span class="io-step-label">Business Rules</span><div class="io-step-visual">
                  <svg viewBox="0 0 200 180" aria-hidden="true"><path d="M18 53l36-16 36 16v36c0 29-18 48-36 56-18-8-36-27-36-56z" style="fill:var(--card)" opacity=".94"/><path d="M38 87l11 11 23-28" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><g><rect x="105" y="22" width="82" height="37" rx="8" fill="#fff" stroke="#c7ddd9"/><rect x="105" y="71" width="82" height="37" rx="8" fill="#fff" stroke="#c7ddd9"/><rect x="105" y="120" width="82" height="37" rx="8" fill="#fff3ef" stroke="#f0c2b6"/></g><g style="fill:var(--card)"><circle cx="170" cy="40" r="9"/><circle cx="170" cy="89" r="9"/></g><g stroke="#fff" stroke-width="2.5" fill="none"><path d="M166 40l3 3 5-7"/><path d="M166 89l3 3 5-7"/></g><circle cx="170" cy="139" r="9" fill="#e55d3e"/><path d="M166 135l8 8m0-8l-8 8" stroke="#fff" stroke-width="2.5"/><g fill="#98b3af"><rect x="116" y="35" width="37" height="7" rx="3"/><rect x="116" y="84" width="37" height="7" rx="3"/><rect x="116" y="134" width="37" height="7" rx="3"/></g><path d="M90 72h13M90 89h13M90 106h13" style="stroke:var(--card)" stroke-width="2" stroke-dasharray="3 3"/></svg>
                </div><p>Dependencies, exceptions, and campaign rules evaluated before submission</p></article><span class="io-arrow">&rarr;</span>
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
              <div class="io-heading"><span class="io-section-label">02 &middot; My contribution</span><h2>Business logic, testing, iteration, and adoption</h2><p class="io-role-lead">I collaborated as one of several equal business leads on this corporate initiative. My role combined market expertise with hands-on solution design, validation, refinement, and rollout support.</p></div>
              <div class="io-contributions">
                <article class="io-contribution"><div class="io-contribution-top"><span>01</span><i><svg viewBox="0 0 32 32"><path d="M7 5h18v22H7zM11 10h10M11 15h10M11 20h6"/><path d="M21 19v6M18 22h6"/></svg></i></div><h3>Shape the Inputs</h3><p>Helped ensure the Zoho form contained the fields required to execute campaigns and co-designed a simpler Excel option.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>02</span><i><svg viewBox="0 0 32 32"><path d="M6 7h8v7H6zM18 18h8v7h-8zM18 5h8v7h-8zM14 10h4M16 10v12M16 22h2"/></svg></i></div><h3>Translate the Rules</h3><p>Explained platform, product, tactic, geography, and optimization relationships so Dev Ops could build the workflow logic.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>03</span><i><svg viewBox="0 0 32 32"><path d="M11 5h10M14 5v7L7 24c-1 2 0 3 2 3h14c2 0 3-1 2-3l-7-12V5"/><path d="M10 21h12M13 17l3 3 4-5"/></svg></i></div><h3>Test and Refine</h3><p>Tested sample and real orders, logged errors, and helped iterate when triggers or captured data did not behave as expected.</p></article>
                <article class="io-contribution"><div class="io-contribution-top"><span>04</span><i><svg viewBox="0 0 32 32"><circle cx="16" cy="10" r="4"/><path d="M8 27v-4c0-5 3-8 8-8s8 3 8 8v4M5 12l-3 3 3 3M27 12l3 3-3 3"/></svg></i></div><h3>Enable Adoption</h3><p>Created a two-part training video, an SOP, and dedicated office hours for Sales and Digital Support teams in my region.</p></article>
              </div>
            </section>

            <section class="io-section">
              <div class="io-heading"><span class="io-section-label">03 &middot; Turning expertise into automation logic</span><h2>Translating business expertise into scalable automation logic</h2><p>My contribution was broader than defining a few validation rules. I helped the team understand how platforms, products, tactics, geography, optimization models, required fields, and exceptions worked together&mdash;then tested whether the automated workflow reflected those relationships accurately.</p></div>
              <div class="io-logic-grid">
                <article class="io-logic-card"><span>Map the operating model</span><h3>Connected the full campaign structure</h3><p>Clarified how platform, product, tactic, targeting, geography, optimization, and order fields related to one another so the workflow could capture complete campaign requirements.</p></article>
                <article class="io-logic-card"><span>Surface rules and exceptions</span><h3>Translated real-world execution requirements</h3><p>Shared conditional fields, incompatible combinations, dependencies, and edge cases the automation needed to handle. Geography and optimization constraints were two examples within a much larger rule set.</p></article>
                <article class="io-logic-card"><span>Validate and improve</span><h3>Turned testing insights into iteration</h3><p>Tested sample and real orders across different campaign scenarios, documented gaps, and worked with the project team to refine triggers, captured data, and workflow behavior.</p></article>
              </div>
            </section>

            <section class="io-section" style="background:#f4f8fc;">
              <div class="io-heading"><span class="io-section-label">04 &middot; The solution</span><h2>Two input paths supported different levels of complexity</h2><p>The underlying insertion-order platform stayed in place. The team changed how information reached it by using guided inputs to trigger Zapier workflows.</p></div>
              <div class="io-paths">
                <article><span>Complex campaigns</span><strong>Guided Zoho form</strong></article>
                <article><span>Simple campaigns</span><strong>Streamlined Excel form</strong></article>
                <i>&rarr;</i>
                <article class="io-output"><span>Shared automation layer</span><strong>Workflow-populated insertion order</strong></article>
              </div>
            </section>

            <section class="io-section io-training">
              <div><div class="io-heading"><span class="io-section-label">05 &middot; Rollout and support</span><h2>Making the new process usable</h2><p>The team received one week to prepare sales and digital support users for launch. I created my own enablement materials and gave people multiple ways to learn and get help.</p></div><div class="io-tags"><span>Two-part video walkthrough</span><span>Step-by-step SOP</span><span>Market office hours</span><span>Live questions and support</span></div></div>
              <div class="io-training-panel"><div class="io-video"><i>&#9654;</i></div><div class="io-guide"><i></i><i></i><i></i><i></i></div></div>
            </section>

            <section class="io-reflection">
              <article><span>Impact</span><h3>A faster, more controlled process</h3><p>Formal performance metrics were not captured. The redesigned process was implemented to reduce manual entry, shorten completion time, and prevent invalid parameters from reaching execution teams.</p></article>
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
