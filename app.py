from __future__ import annotations

import html

import streamlit as st

from profile_data import (
    ABOUT,
    CONTACT,
    EXPERIENCE,
    PROFILE,
    PROJECTS,
    SKILLS,
    SOCIAL_LINKS,
)
from portfolio_navigation import render_portfolio_navigation


def safe(value: str) -> str:
    return html.escape(value)


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

        :root {
            --ink: #15243b;
            --muted: #536279;
            --paper: #ffffff;
            --surface: #ffffff;
            --accent: #5360a0;
            --accent-strong: #344681;
            --accent-soft: #edecf8;
            --blue: #27649c;
            --line: rgba(21, 36, 59, 0.13);
        }

        html { scroll-behavior: smooth; }

        .stApp {
            background:
                radial-gradient(circle at 100% 0%, rgba(111,78,154,.58) 0%, rgba(67,91,161,.37) 8rem, rgba(67,91,161,0) 25rem),
                radial-gradient(circle at 0% 100%, rgba(49,93,159,.52) 0%, rgba(104,75,151,.32) 8rem, rgba(104,75,151,0) 25rem),
                linear-gradient(135deg, #f7f9fc 0%, #ffffff 30%, #ffffff 72%, #faf8fd 100%);
            background-attachment: fixed;
            color: var(--ink);
            font-family: "DM Sans", sans-serif;
        }

        .block-container {
            max-width: 1240px;
            padding-top: 1rem;
            padding-bottom: 5rem;
        }

        h1, h2, h3 {
            color: var(--ink) !important;
            font-family: "Manrope", sans-serif !important;
            letter-spacing: -0.035em;
        }

        p, li, label { font-family: "DM Sans", sans-serif; }
        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stAppDeployButton"],
        .stAppDeployButton { display: none !important; }
        #MainMenu, footer { visibility: hidden; }

        .hero-shell {
            align-items: center;
            display: grid;
            gap: clamp(2.5rem, 5vw, 5rem);
            grid-template-columns: minmax(0, 1.45fr) minmax(290px, .55fr);
            min-height: 540px;
            padding: clamp(2rem, 3vw, 3rem) 0 clamp(3rem, 5vw, 4.5rem);
        }

        .hero-name {
            color: var(--ink);
            font-family: "Manrope", sans-serif;
            font-size: clamp(3.5rem, 6vw, 5.6rem);
            font-weight: 800;
            letter-spacing: -.065em;
            line-height: .95;
            margin-bottom: 1.5rem;
        }

        .eyebrow {
            color: var(--accent);
            font-family: "Manrope", sans-serif;
            font-size: clamp(1.15rem, 1.8vw, 1.55rem);
            font-weight: 700;
            letter-spacing: -.02em;
            line-height: 1.35;
            margin-bottom: 1.6rem;
            max-width: 850px;
        }

        .hero-title {
            font-family: "Manrope", sans-serif;
            font-size: clamp(1.65rem, 2.8vw, 2.55rem);
            font-weight: 700;
            letter-spacing: -.04em;
            line-height: 1.16;
            margin: 0 0 1.35rem;
            max-width: 820px;
        }

        .hero-title .accent {
            color: var(--accent-strong);
        }

        .hero-copy {
            color: var(--muted);
            font-size: clamp(1.1rem, 1.45vw, 1.28rem);
            line-height: 1.72;
            margin-bottom: 0;
            max-width: 780px;
        }

        .hero-actions {
            display: flex;
            flex-wrap: wrap;
            gap: .8rem;
            margin-top: 1.8rem;
        }

        .hero-cta {
            align-items: center;
            border: 1px solid var(--line);
            border-radius: 999px;
            display: inline-flex;
            font-size: .92rem;
            font-weight: 800;
            justify-content: center;
            min-height: 3.2rem;
            padding: 0 1.3rem;
            text-decoration: none !important;
            transition: transform .18s ease, box-shadow .18s ease;
        }

        .hero-cta.primary {
            background: #18365d;
            border-color: #18365d;
            color: white !important;
        }

        .hero-cta.secondary {
            background: rgba(255,255,255,.76);
            color: #18365d !important;
        }

        .hero-cta:hover {
            box-shadow: 0 9px 24px rgba(31,53,88,.14);
            transform: translateY(-2px);
        }

        .hero-proof {
            backdrop-filter: blur(12px);
            background: rgba(255,255,255,.70);
            border: 1px solid rgba(21,36,59,.10);
            border-radius: 22px;
            box-shadow: 0 20px 55px rgba(31,53,88,.08);
            padding: 1.5rem;
        }

        .hero-proof-title {
            color: var(--ink);
            font-family: "Manrope", sans-serif;
            font-size: 1rem;
            font-weight: 800;
            margin-bottom: .6rem;
        }

        .hero-stat {
            border-top: 1px solid var(--line);
            padding: 1rem 0 .85rem;
        }

        .hero-stat-value {
            color: var(--accent-strong);
            font-family: "Manrope", sans-serif;
            font-size: 1.45rem;
            font-weight: 800;
            letter-spacing: -.035em;
        }

        .hero-stat-label {
            color: var(--muted);
            font-size: .8rem;
            margin-top: .12rem;
        }

        .section {
            border-top: 1px solid var(--line);
            margin-top: 7.5rem;
            padding-top: 1.6rem;
        }

        .section-number {
            color: var(--accent);
            font-family: "Manrope", sans-serif;
            font-size: clamp(1.9rem, 3vw, 2.6rem);
            font-weight: 800;
            letter-spacing: -.04em;
            line-height: 1.05;
        }

        .section-title {
            color: var(--muted);
            font-family: "DM Sans", sans-serif;
            font-size: clamp(1.35rem, 2.2vw, 2rem);
            font-weight: 500;
            letter-spacing: -.025em;
            line-height: 1.3;
            margin: .7rem 0 2.5rem;
            max-width: 820px;
        }

        .about-copy {
            max-width: 840px;
        }

        .about-lead {
            color: var(--ink);
            font-size: 1.08rem;
            line-height: 1.78;
            margin: 0 0 1.25rem;
        }

        .about-body {
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.78;
            margin: 0 0 1.25rem;
            max-width: 800px;
        }

        .skill-group {
            background: rgba(255,255,255,.72);
            border: 1px solid var(--line);
            border-radius: 18px;
            box-sizing: border-box;
            height: 300px;
            padding: 1.45rem;
            width: 100%;
        }

        .skill-group h3 {
            font-size: 1rem;
            margin: 0 0 1.2rem;
        }

        .chip {
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 999px;
            color: var(--ink);
            display: inline-block;
            font-size: .8rem;
            margin: 0 .35rem .45rem 0;
            padding: .42rem .7rem;
        }

        .project-card {
            background: rgba(255,255,255,.78);
            border: 1px solid var(--line);
            border-radius: 22px;
            box-shadow: 0 14px 50px rgba(31,53,88,.05);
            box-sizing: border-box;
            height: 410px;
            padding: 1.7rem;
            transition: transform .2s ease, box-shadow .2s ease;
            width: 100%;
        }

        .project-card:hover {
            box-shadow: 0 18px 60px rgba(31,53,88,.11);
            transform: translateY(-4px);
        }

        .project-index {
            color: var(--accent);
            font-family: "Manrope", sans-serif;
            font-size: .78rem;
            font-weight: 800;
        }

        .project-proof {
            border-bottom: 1px solid var(--line);
            margin-top: 1.6rem;
            padding-bottom: 1.1rem;
        }

        .project-proof-value {
            color: var(--ink);
            font-family: "Manrope", sans-serif;
            font-size: 1.65rem;
            font-weight: 800;
            letter-spacing: -.045em;
            line-height: 1.1;
        }

        .project-proof-label {
            color: var(--accent);
            font-size: .68rem;
            font-weight: 800;
            letter-spacing: .08em;
            margin-top: .35rem;
            text-transform: uppercase;
        }

        .project-card h3 {
            font-size: 1.35rem;
            margin: 1.35rem 0 .7rem;
        }

        .project-card p {
            color: var(--muted);
            font-size: .92rem;
            line-height: 1.6;
        }

        .project-capabilities {
            color: var(--ink);
            font-size: .78rem;
            font-weight: 700;
            line-height: 1.55;
            margin-top: 1rem;
        }

        .project-link {
            color: var(--ink) !important;
            display: inline-block;
            font-size: .84rem;
            font-weight: 700;
            margin-top: .6rem;
            text-decoration: none;
        }

        .portfolio-directory-card {
            background: rgba(255,255,255,.78);
            border: 1px solid var(--line);
            border-radius: 20px;
            color: var(--ink) !important;
            display: block;
            box-sizing: border-box;
            height: 235px;
            padding: 1.4rem;
            text-decoration: none !important;
            transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
            width: 100%;
        }

        .portfolio-directory-card:hover {
            border-color: rgba(83,96,160,.48);
            box-shadow: 0 16px 45px rgba(31,53,88,.10);
            transform: translateY(-4px);
        }

        .portfolio-directory-card .directory-index {
            color: var(--accent);
            font-family: "Manrope", sans-serif;
            font-size: .76rem;
            font-weight: 800;
            letter-spacing: .1em;
        }

        .portfolio-directory-card h3 {
            font-size: 1.1rem;
            line-height: 1.2;
            margin: 1.35rem 0 .65rem;
        }

        .portfolio-directory-card p {
            color: var(--muted);
            font-size: .86rem;
            line-height: 1.55;
        }

        .portfolio-directory-card .directory-link {
            color: var(--ink);
            display: inline-block;
            font-size: .82rem;
            font-weight: 800;
            margin-top: .4rem;
        }

        [data-testid="stSidebar"] {
            background: #15243b;
        }

        [data-testid="stSidebar"] * {
            color: rgba(255,255,255,.86) !important;
        }

        .timeline-item {
            border-left: 2px solid rgba(83,96,160,.25);
            margin-left: .4rem;
            padding: 0 0 2.1rem 1.5rem;
            position: relative;
        }

        .timeline-item::before {
            background: var(--accent);
            border: 4px solid var(--paper);
            border-radius: 50%;
            content: "";
            height: .75rem;
            left: -.45rem;
            position: absolute;
            top: .2rem;
            width: .75rem;
        }

        .timeline-meta {
            color: var(--accent);
            font-size: .75rem;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
        }

        .timeline-item h3 {
            font-size: 1.15rem;
            margin: .4rem 0 .2rem;
        }

        .timeline-company {
            color: var(--muted);
            font-size: .88rem;
            font-weight: 600;
            margin-bottom: .65rem;
        }

        .timeline-item p {
            color: var(--muted);
            font-size: .92rem;
            line-height: 1.6;
            max-width: 740px;
        }

        .contact-panel {
            background: #18365d;
            border-radius: 26px;
            color: white;
            margin-top: 6rem;
            overflow: hidden;
            padding: clamp(2rem, 6vw, 5rem);
            position: relative;
        }

        .contact-panel::after {
            background: linear-gradient(135deg, #5360a0, #7653a0);
            border-radius: 50%;
            content: "";
            filter: blur(2px);
            height: 220px;
            opacity: .85;
            position: absolute;
            right: -70px;
            top: -85px;
            width: 220px;
        }

        .contact-panel h2 {
            color: white !important;
            font-size: clamp(2.3rem, 5vw, 4.5rem);
            line-height: 1;
            margin: 0 0 1.2rem;
            max-width: 720px;
            position: relative;
            z-index: 1;
        }

        .contact-panel p {
            color: rgba(255,255,255,.68);
            font-size: 1rem;
            line-height: 1.65;
            max-width: 580px;
            position: relative;
            z-index: 1;
        }

        .socials {
            color: var(--muted);
            font-size: .82rem;
            margin-top: 2rem;
            text-align: center;
        }

        .socials a {
            color: var(--ink) !important;
            font-weight: 700;
            margin: 0 .6rem;
            text-decoration: none;
        }

        div.stButton > button, div.stLinkButton > a {
            background: var(--accent);
            border: 0;
            border-radius: 999px;
            color: white;
            font-family: "DM Sans", sans-serif;
            font-weight: 700;
            min-height: 3.2rem;
            padding: 0 1.35rem;
            transition: transform .18s ease, box-shadow .18s ease;
        }

        div.stButton > button:hover, div.stLinkButton > a:hover {
            background: var(--accent-strong);
            box-shadow: 0 9px 24px rgba(83,96,160,.24);
            color: white;
            transform: translateY(-2px);
        }

        @media (max-width: 900px) {
            .hero-shell {
                grid-template-columns: 1fr;
                min-height: auto;
            }

            .hero-proof {
                display: grid;
                gap: 0 1.2rem;
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .hero-proof-title { grid-column: 1 / -1; }
        }

        @media (max-width: 700px) {
            .block-container { padding: 1.2rem 1rem 3rem; }
            .hero-shell { padding-top: 1.5rem; }
            .hero-name { font-size: 3.3rem; }
            .eyebrow { font-size: 1.05rem; }
            .hero-title { font-size: 1.7rem; }
            .hero-copy { font-size: 1.04rem; }
            .hero-proof { grid-template-columns: 1fr; }
            .section { margin-top: 4.5rem; }
            .section-number { font-size: 1.85rem; }
            .section-title { font-size: 1.25rem; }
            .project-card, .portfolio-directory-card, .skill-group {
                height: auto;
                min-height: 0;
                margin-bottom: .7rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_skill_group(title: str, skills: list[str]) -> None:
    chips = "".join(f'<span class="chip">{safe(skill)}</span>' for skill in skills)
    st.markdown(
        f'<div class="skill-group"><h3>{safe(title)}</h3>{chips}</div>',
        unsafe_allow_html=True,
    )


def render_project(project: dict[str, str], index: int) -> None:
    link = ""
    if project.get("url"):
        link = (
            f'<a class="project-link" href="{safe(project["url"])}" '
            'target="_blank">View project ↗</a>'
        )
    st.markdown(
        f"""
        <div class="project-card">
            <div class="project-index">0{index}</div>
            <div class="project-proof">
                <div class="project-proof-value">{safe(project["metric"])}</div>
                <div class="project-proof-label">{safe(project["metric_label"])}</div>
            </div>
            <h3>{safe(project["title"])}</h3>
            <p>{safe(project["description"])}</p>
            <div class="project-capabilities">{safe(project["tools"])}</div>
            {link}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_experience(item: dict[str, str]) -> None:
    st.markdown(
        f"""
        <div class="timeline-item">
            <div class="timeline-meta">{safe(item["period"])}</div>
            <h3>{safe(item["role"])}</h3>
            <div class="timeline-company">{safe(item["company"])}</div>
            <p>{safe(item["summary"])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_portfolio_directory_item(item: dict[str, object], index: int) -> None:
    if item.get("href"):
        destination = safe(str(item["href"]))
    else:
        project_key = safe(str(item["key"]))
        destination = f"/?project={project_key}"
    st.markdown(
        f"""
        <a class="portfolio-directory-card" href="{destination}" target="_self">
            <div class="directory-index">PROJECT {index:02d}</div>
            <h3>{safe(str(item["title"]))}</h3>
            <p>{safe(str(item["summary"]))}</p>
            <span class="directory-link">Open project page &rarr;</span>
        </a>
        """,
        unsafe_allow_html=True,
    )


inject_styles()
render_portfolio_navigation()

hero_proof = [
    ("$11.2M", "Digital portfolio led"),
    ("35% YoY", "Revenue growth"),
    ("10–12 → 3–5 days", "Reporting turnaround"),
    ("$300K → $2.75M", "Google Ads revenue"),
]
hero_proof_html = "".join(
    f'<div class="hero-stat"><div class="hero-stat-value">{safe(value)}</div>'
    f'<div class="hero-stat-label">{safe(label)}</div></div>'
    for value, label in hero_proof
)

st.markdown(
    f"""
    <section class="hero-shell" aria-label="Introduction">
        <div class="hero-main">
            <div class="hero-name">{safe(PROFILE["name"])}</div>
            <div class="eyebrow">{safe(PROFILE["eyebrow"])}</div>
            <div class="hero-title">
                {safe(PROFILE["headline_prefix"])}
                <span class="accent">{safe(PROFILE["headline_emphasis"])}</span>
            </div>
            <div class="hero-copy">{safe(PROFILE["intro"])}</div>
            <div class="hero-actions">
                <a class="hero-cta primary" href="/Case_Studies" target="_self">View case studies</a>
                <a class="hero-cta secondary" href="mailto:{safe(CONTACT['email'])}">Contact me</a>
            </div>
        </div>
        <aside class="hero-proof" aria-label="Career impact snapshot">
            <div class="hero-proof-title">Career impact</div>
            {hero_proof_html}
        </aside>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <div class="section-number">01 / SELECTED IMPACT</div>
        <div class="section-title">Strategy backed by measurable results.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

for row_start in range(0, len(PROJECTS), 2):
    row_projects = PROJECTS[row_start : row_start + 2]
    columns = st.columns(2)
    for offset, project in enumerate(row_projects):
        with columns[offset]:
            render_project(project, row_start + offset + 1)
    st.write("")

portfolio_directory_items = [
    {
        "key": "case-studies",
        "href": "/Case_Studies",
        "title": "Case Studies",
        "summary": (
            "Campaign strategies, audience decisions, channel architecture, and "
            "measurable outcomes across healthcare, B2B technology, and automotive."
        ),
    },
    {
        "key": "marketing-operations",
        "href": "/Marketing_Operations_and_Automation",
        "title": "Marketing Operations & Automation",
        "summary": (
            "Reporting, workflow, and software implementation projects that made "
            "complex marketing operations faster, clearer, and easier to maintain."
        ),
    },
    {
        "key": "tools-playbooks",
        "href": "/Tools_Playbooks_and_Frameworks",
        "title": "AI Tools & Agentic Workflows",
        "summary": (
            "AI-powered tools and structured agentic workflows that turn complex, "
            "repetitive work into guided and repeatable experiences."
        ),
    },
    {
        "key": "gtm-enablement",
        "href": "/GTM_Strategy_and_Sales_Enablement",
        "title": "GTM Strategy & Sales Enablement",
        "summary": (
            "Target-market strategy, product positioning, campaign planning, and "
            "enablement that help teams take offers to market with confidence."
        ),
    },
]

st.markdown(
    """
    <div class="section">
        <div class="section-number">02 / FEATURED WORK</div>
        <div class="section-title">Explore the work behind the outcomes.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

for row_start in range(0, len(portfolio_directory_items), 2):
    row_items = portfolio_directory_items[row_start : row_start + 2]
    columns = st.columns(2)
    for offset, item in enumerate(row_items):
        with columns[offset]:
            render_portfolio_directory_item(item, row_start + offset + 1)
    st.write("")

st.markdown(
    """
    <div class="section">
        <div class="section-number">03 / CAPABILITIES</div>
        <div class="section-title">What I bring to the table.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

skill_columns = st.columns(len(SKILLS))
for column, (group_name, group_skills) in zip(skill_columns, SKILLS.items()):
    with column:
        render_skill_group(group_name, group_skills)

st.markdown(
    """
    <div class="section">
        <div class="section-number">04 / ABOUT</div>
        <div class="section-title">The story behind the work.</div>
    </div>
    """,
    unsafe_allow_html=True,
)
about_story = (
    f'<p class="about-lead">{safe(ABOUT[0])}</p>'
    + "".join(f'<p class="about-body">{safe(paragraph)}</p>' for paragraph in ABOUT[1:])
)
st.markdown(f'<div class="about-copy">{about_story}</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section">
        <div class="section-number">05 / EXPERIENCE</div>
        <div class="section-title">A track record of transformation.</div>
    </div>
    """,
    unsafe_allow_html=True,
)
for experience in EXPERIENCE:
    render_experience(experience)

st.markdown(
    f"""
    <div class="contact-panel">
        <h2>{safe(CONTACT["heading"])}</h2>
        <p>{safe(CONTACT["message"])}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

contact_left, contact_right = st.columns([1.2, 3.8])
with contact_left:
    st.link_button("Email me", f"mailto:{CONTACT['email']}", use_container_width=True)
with contact_right:
    st.caption(CONTACT["email"])

social_links = " · ".join(
    f'<a href="{safe(url)}" target="_blank">{safe(label)}</a>'
    for label, url in SOCIAL_LINKS.items()
)
st.markdown(
    f'<div class="socials">{social_links}<br><br>Built with Streamlit · '
    f'© 2026 {safe(PROFILE["name"])}</div>',
    unsafe_allow_html=True,
)
