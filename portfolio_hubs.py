from __future__ import annotations

import html

import streamlit as st

from portfolio_navigation import render_portfolio_navigation


def _safe(value: object) -> str:
    return html.escape(str(value))


_HUB_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap');
[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppDeployButton"], .stAppDeployButton { display:none!important; }
#MainMenu, footer { visibility:hidden; }
.stApp { background:#f4f7fb; }
.block-container { max-width:1220px; padding:1rem 1.25rem 4.5rem; }
.portfolio-hub,.portfolio-hub * { box-sizing:border-box; }
.portfolio-hub { --navy:#071c3b;--blue:#2769d8;--coral:#ed715f;--teal:#118f86;--violet:#785dd3;--ink:#10233f;--muted:#5d6e84;color:var(--ink);font-family:"DM Sans",sans-serif; }
.hub-hero { background:linear-gradient(125deg,#071c3b 0%,#102f5d 69%,#184b75 100%);border-radius:28px;color:white;overflow:hidden;padding:clamp(2.2rem,5vw,4.5rem);position:relative; }
.hub-hero:after { background:radial-gradient(circle,rgba(255,255,255,.18) 0 2px,transparent 2.5px);background-size:22px 22px;content:"";height:240px;opacity:.45;position:absolute;right:-25px;top:-35px;width:330px; }
.hub-kicker { color:#73d8cf;font-size:.86rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase; }
.hub-hero h1 { color:white!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(3rem,6vw,5.5rem);font-weight:600;letter-spacing:-.05em;line-height:.94;margin:1rem 0 1.2rem;max-width:900px;position:relative;z-index:1; }
.hub-hero p { color:rgba(255,255,255,.82);font-size:clamp(1.08rem,1.5vw,1.28rem);line-height:1.65;margin:0;max-width:800px;position:relative;z-index:1; }
.hub-section { margin:4rem 0 1.4rem; }
.hub-section span { color:var(--coral);font-size:.82rem;font-weight:800;letter-spacing:.13em;text-transform:uppercase; }
.hub-section h2 { color:var(--navy)!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2rem,4vw,3.35rem);font-weight:600;letter-spacing:-.04em;line-height:1.05;margin:.7rem 0 .75rem; }
.hub-section p { color:var(--muted);font-size:1.08rem;line-height:1.7;margin:0;max-width:780px; }
.hub-card { background:white;border:1px solid #dce4ee;border-radius:22px;box-shadow:0 12px 30px rgba(7,28,59,.07);display:flex;flex-direction:column;height:360px;min-height:360px;overflow:hidden;padding:1.55rem;position:relative; }
.hub-card:before { background:var(--card-color);content:"";height:7px;inset:0 0 auto;position:absolute; }
.hub-card.blue { --card-color:#3b82f6; }.hub-card.teal { --card-color:#20b7aa; }.hub-card.coral { --card-color:#ef806b; }.hub-card.violet { --card-color:#8b6ee0; }
.hub-card-index { color:var(--card-color);font-family:"Newsreader",Georgia,serif;font-size:2.25rem;font-weight:600;margin:.5rem 0 1.4rem; }
.hub-card h3 { color:var(--navy)!important;font-family:"DM Sans",sans-serif!important;font-size:1.35rem;font-weight:800;letter-spacing:-.025em;line-height:1.22;margin:0 0 .9rem; }
.hub-card p { color:var(--muted);font-size:1.02rem;line-height:1.65;margin:0 0 1.4rem; }
.hub-card a { color:var(--navy)!important;font-size:.92rem;font-weight:800;margin-top:auto;text-decoration:none!important; }
.hub-card a:hover { color:var(--card-color)!important; }
.hub-tag { align-self:flex-start;background:#edf2f8;border-radius:999px;color:#496077;font-size:.76rem;font-weight:800;letter-spacing:.04em;margin-top:auto;padding:.48rem .72rem;text-transform:uppercase; }
.ai-callout { align-items:center;background:linear-gradient(115deg,#e7f7f4,#eef0ff);border:1px solid #cddddd;border-radius:24px;display:grid;gap:1.5rem;grid-template-columns:1.35fr .65fr;margin-top:3.5rem;padding:clamp(1.7rem,4vw,3rem); }
.ai-callout h2 { color:var(--navy)!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2rem,4vw,3.1rem);font-weight:600;letter-spacing:-.04em;line-height:1.05;margin:0 0 .8rem; }
.ai-callout p { color:#485f72;font-size:1.07rem;line-height:1.65;margin:0; }
.ai-callout a { background:var(--navy);border-radius:999px;color:white!important;display:inline-block;font-weight:800;padding:.9rem 1.15rem;text-align:center;text-decoration:none!important; }
.hub-note { background:#fff7f2;border-left:5px solid var(--coral);border-radius:0 18px 18px 0;color:#4c5e72;font-size:1rem;line-height:1.65;margin-top:3rem;padding:1.3rem 1.5rem; }
@media (max-width:760px) { .ai-callout { grid-template-columns:1fr; }.hub-card { height:auto;min-height:0;margin-bottom:.7rem; }.hub-hero { border-radius:20px; } }
</style>
"""


def _hero(kicker: str, title: str, description: str) -> None:
    markup = (
        '<div class="portfolio-hub"><section class="hub-hero">'
        + f'<div class="hub-kicker">{_safe(kicker)}</div>'
        + f'<h1>{_safe(title)}</h1>'
        + f'<p>{_safe(description)}</p>'
        + "</section></div>"
    )
    st.markdown(_HUB_STYLES, unsafe_allow_html=True)
    st.markdown(
        markup,
        unsafe_allow_html=True,
    )


def _section(label: str, title: str, description: str) -> None:
    st.markdown(
        f"""
        <div class="portfolio-hub"><section class="hub-section">
          <span>{_safe(label)}</span>
          <h2>{_safe(title)}</h2>
          <p>{_safe(description)}</p>
        </section></div>
        """,
        unsafe_allow_html=True,
    )


def _card(index: int, color: str, title: str, description: str, href: str | None, label: str) -> None:
    if href:
        target = "_blank" if href.startswith("http") else "_self"
        action = f'<a href="{_safe(href)}" target="{target}">{_safe(label)} &rarr;</a>'
    else:
        action = f'<span class="hub-tag">{_safe(label)}</span>'
    st.markdown(
        f"""
        <div class="portfolio-hub hub-card {color}">
          <div class="hub-card-index">{index:02d}</div>
          <h3>{_safe(title)}</h3>
          <p>{_safe(description)}</p>
          {action}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_marketing_operations_hub() -> None:
    render_portfolio_navigation()
    _hero(
        "Systems behind stronger marketing",
        "Marketing Operations & Automation",
        "Selected implementations that reduced manual work, strengthened handoffs, and turned complex marketing processes into reliable operating systems.",
    )
    _section(
        "Selected work",
        "From recurring friction to repeatable execution.",
        "Each project shows how I identified an operational problem, shaped a practical solution, and helped people adopt a better way of working.",
    )
    cards = [
        ("blue", "Client-Facing Performance Dashboard", "A Looker Studio reporting system that reduced a weekly four-to-six-hour refresh process to 15–20 minutes while giving hospital stakeholders clearer, self-service campaign visibility.", "/Dashboard_and_Insights", "View case study"),
        ("teal", "Automated Insertion Order Workflow", "A guided, rule-validated order process that replaced fragmented email handoffs, prevented incomplete requests from reaching execution, and supported multi-market adoption.", "/Process_Improvement_Case_Study", "View case study"),
        ("violet", "Teamwork Project Management Rollout", "A company-wide project management software implementation that standardized campaign intake, task ownership, communication, and status visibility for sales and support teams.", "/Teamwork_Implementation_Case_Study", "View case study"),
        ("coral", "Power BI Reporting Automation", "A reporting transformation that shortened client-ready recap turnaround from 10–12 business days to 3–5 days without adding headcount.", None, "Case study in development"),
    ]
    columns = st.columns(2)
    for index, card in enumerate(cards, start=1):
        with columns[(index - 1) % 2]:
            _card(index, *card)
            st.write("")
    st.markdown(
        '<div class="portfolio-hub"><div class="hub-note"><strong>Why these projects belong together:</strong> the technology varies, but the work is consistently about process design, adoption, measurement, and making complex operations easier to run.</div></div>',
        unsafe_allow_html=True,
    )


def render_tools_hub() -> None:
    render_portfolio_navigation()
    _hero(
        "Reusable thinking, made practical",
        "Tools, Playbooks & Frameworks",
        "Builders, decision tools, and repeatable frameworks designed to turn strategy into clear next steps—not documents that sit unused.",
    )
    st.markdown(
        """
        <div class="portfolio-hub"><section class="ai-callout">
          <div>
            <h2>See how I built this site using AI assistants.</h2>
            <p>This portfolio is also a working example of how I use structured prompts, reusable instructions, AI assistants, and iterative review to move from raw interviews to polished project stories.</p>
          </div>
          <a href="https://project-story-case-builder.ai-kiki.chatgpt.site/#top" target="_blank">Explore the builder ↗</a>
        </section></div>
        """,
        unsafe_allow_html=True,
    )
    _section(
        "Working toolkit",
        "Systems that make good decisions easier to repeat.",
        "This area will grow as additional builders, calculators, templates, and operating playbooks are completed.",
    )
    cards = [
        ("violet", "AI Case Study & Portfolio Builder", "A guided interview and drafting workflow that captures project evidence, identifies missing details, and converts raw experience into a recruiter-ready case study.", "https://project-story-case-builder.ai-kiki.chatgpt.site/#top", "Open builder"),
        ("blue", "Campaign Allocation & Optimization Playbooks", "Practical decision frameworks for translating goals, audience signals, budget constraints, and performance data into focused media actions.", None, "Portfolio sample coming soon"),
        ("teal", "AI Assistants & Agent Workflows", "Reusable instruction systems that help assistants follow a consistent process, preserve standards, and support research, drafting, quality checks, and publishing.", None, "Build story in development"),
        ("coral", "Decision Frameworks & Calculators", "Compact tools for making complex choices more transparent—from prioritization and capacity planning to campaign recommendations and resource allocation.", None, "Collection in development"),
    ]
    columns = st.columns(2)
    for index, card in enumerate(cards, start=1):
        with columns[(index - 1) % 2]:
            _card(index, *card)
            st.write("")


def render_gtm_hub() -> None:
    render_portfolio_navigation()
    _hero(
        "Turning market insight into coordinated action",
        "GTM Strategy & Sales Enablement",
        "Work that connects target markets, product positioning, campaign planning, sales readiness, and the materials teams need to take an offer to market with confidence.",
    )
    _section(
        "Portfolio direction",
        "Strategy is only useful when teams can act on it.",
        "This collection brings together the market choices, launch structure, enablement, and storytelling that help a go-to-market plan move from intent to execution.",
    )
    cards = [
        ("blue", "Product Portfolio & Target-Market Mapping", "A structured view of products, priority audiences, customer needs, and market opportunities used to guide positioning and campaign planning.", None, "Case study in development"),
        ("teal", "Sales Enablement & Rep Readiness", "Training, talk tracks, tools, and adoption support designed to help sales teams understand an offer and use it credibly in customer conversations.", None, "Portfolio sample in development"),
        ("violet", "Pitch Decks & Training Materials", "Strategic narratives and learning materials that make complex products easier to explain, sell, launch, and support.", None, "Selected samples coming soon"),
        ("coral", "Campaign Planning & Launch Strategy", "Audience, messaging, channel, timing, and measurement decisions brought together in a coordinated plan for market activation.", None, "Case study in development"),
    ]
    columns = st.columns(2)
    for index, card in enumerate(cards, start=1):
        with columns[(index - 1) % 2]:
            _card(index, *card)
            st.write("")
