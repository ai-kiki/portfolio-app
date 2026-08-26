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
