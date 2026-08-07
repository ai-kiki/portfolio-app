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
from project_page_template import PROJECT_PAGE_CONFIGS, render_project_page


st.set_page_config(
    page_title=f"{PROFILE['name']} · Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

active_project = st.query_params.get("project")
project_keys = {str(item["key"]) for item in PROJECT_PAGE_CONFIGS}
if active_project in project_keys:
    render_project_page(str(active_project), configure_page=False)
    st.stop()


def safe(value: str) -> str:
    return html.escape(value)


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

        :root {
            --ink: #13231f;
            --muted: #60706b;
            --paper: #f6f8f3;
            --surface: #ffffff;
            --accent: #ff6b4a;
            --accent-soft: #ffe7df;
            --mint: #c9f2df;
            --line: rgba(19, 35, 31, 0.12);
        }

        html { scroll-behavior: smooth; }

        .stApp {
            background:
                radial-gradient(circle at 92% 4%, rgba(201, 242, 223, .70), transparent 29rem),
                linear-gradient(180deg, #fbfcf8 0%, var(--paper) 100%);
            color: var(--ink);
            font-family: "DM Sans", sans-serif;
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2.2rem;
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

        .topbar {
            align-items: center;
            display: flex;
            justify-content: space-between;
            margin-bottom: 5.5rem;
        }

        .brand {
            align-items: center;
            display: flex;
            font-family: "Manrope", sans-serif;
            font-size: .92rem;
            font-weight: 800;
            gap: .65rem;
            letter-spacing: .08em;
            text-transform: uppercase;
        }

        .brand-mark {
            align-items: center;
            background: var(--ink);
            border-radius: 50%;
            color: white;
            display: inline-flex;
            height: 2rem;
            justify-content: center;
            width: 2rem;
        }

        .status {
            align-items: center;
            background: rgba(255,255,255,.72);
            border: 1px solid var(--line);
            border-radius: 999px;
            color: var(--muted);
            display: flex;
            font-size: .82rem;
            gap: .55rem;
            padding: .55rem .85rem;
        }

        .status-dot {
            background: #26b778;
            border-radius: 50%;
            box-shadow: 0 0 0 4px rgba(38,183,120,.14);
            height: .5rem;
            width: .5rem;
        }

        .eyebrow {
            color: var(--accent);
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .14em;
            margin-bottom: 1rem;
            text-transform: uppercase;
        }

        .hero-title {
            font-family: "Manrope", sans-serif;
            font-size: clamp(3.2rem, 7.8vw, 7rem);
            font-weight: 800;
            letter-spacing: -.075em;
            line-height: .92;
            margin: 0 0 1.6rem;
            max-width: 920px;
        }

        .hero-title .accent {
            color: var(--accent);
            font-style: italic;
        }

        .hero-copy {
            color: var(--muted);
            font-size: 1.15rem;
            line-height: 1.7;
            margin-bottom: 1rem;
            max-width: 680px;
        }

        .location-line {
            color: var(--ink);
            font-size: .9rem;
            font-weight: 600;
            margin: 1.1rem 0 2rem;
        }

        .section {
            border-top: 1px solid var(--line);
            margin-top: 6rem;
            padding-top: 1.4rem;
        }

        .section-number {
            color: var(--accent);
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .12em;
        }

        .section-title {
            font-family: "Manrope", sans-serif;
            font-size: clamp(2.1rem, 4vw, 3.7rem);
            font-weight: 800;
            letter-spacing: -.055em;
            line-height: 1;
            margin: .7rem 0 2rem;
        }

        .about-copy {
            max-width: 920px;
        }

        .about-lead {
            color: var(--ink);
            font-family: "Manrope", sans-serif;
            font-size: clamp(1.45rem, 2.8vw, 2.25rem);
            font-weight: 600;
            letter-spacing: -.035em;
            line-height: 1.35;
            margin: 0 0 2rem;
        }

        .about-body {
            color: var(--muted);
            font-size: 1.06rem;
            line-height: 1.78;
            margin: 0 0 1.25rem;
            max-width: 800px;
        }

        .skill-group {
            background: rgba(255,255,255,.72);
            border: 1px solid var(--line);
            border-radius: 18px;
            min-height: 190px;
            padding: 1.45rem;
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
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 22px;
            box-shadow: 0 14px 50px rgba(19,35,31,.05);
            height: 100%;
            min-height: 420px;
            padding: 1.7rem;
            transition: transform .2s ease, box-shadow .2s ease;
        }

        .project-card:hover {
            box-shadow: 0 18px 60px rgba(19,35,31,.10);
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
            font-size: 1.45rem;
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
            min-height: 205px;
            padding: 1.4rem;
            text-decoration: none !important;
            transition: transform .2s ease, box-shadow .2s ease, border-color .2s ease;
        }

        .portfolio-directory-card:hover {
            border-color: rgba(255,107,74,.55);
            box-shadow: 0 16px 45px rgba(19,35,31,.09);
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
            background: #13231f;
        }

        [data-testid="stSidebar"] * {
            color: rgba(255,255,255,.86) !important;
        }

        .timeline-item {
            border-left: 2px solid var(--mint);
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
            background: var(--ink);
            border-radius: 26px;
            color: white;
            margin-top: 6rem;
            overflow: hidden;
            padding: clamp(2rem, 6vw, 5rem);
            position: relative;
        }

        .contact-panel::after {
            background: var(--accent);
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
            background: #f15e3e;
            box-shadow: 0 9px 24px rgba(255,107,74,.24);
            color: white;
            transform: translateY(-2px);
        }

        @media (max-width: 700px) {
            .block-container { padding: 1.2rem 1rem 3rem; }
            .topbar { margin-bottom: 4rem; }
            .status { display: none; }
            .hero-title { font-size: 3.6rem; }
            .section { margin-top: 4.5rem; }
            .project-card { min-height: 240px; margin-bottom: .7rem; }
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

st.markdown(
    f"""
    <div class="topbar">
        <div class="brand">
            <span class="brand-mark">✦</span>
            {safe(PROFILE["name"])}
        </div>
        <div class="status">
            <span class="status-dot"></span>
            {safe(PROFILE["availability"])}
        </div>
    </div>

    <div class="eyebrow">{safe(PROFILE["eyebrow"])}</div>
    <div class="hero-title">
        {safe(PROFILE["headline_prefix"])}
        <span class="accent">{safe(PROFILE["headline_emphasis"])}</span>
    </div>
    <div class="hero-copy">{safe(PROFILE["intro"])}</div>
    <div class="location-line">⌁ {safe(PROFILE["location"])}</div>
    """,
    unsafe_allow_html=True,
)

hero_left, _ = st.columns([1.25, 3.75])
with hero_left:
    st.link_button("Start a conversation", f"mailto:{CONTACT['email']}", use_container_width=True)

st.markdown(
    """
    <div class="section">
        <div class="section-number">01 / ABOUT</div>
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
        <div class="section-number">02 / CAPABILITIES</div>
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
        <div class="section-number">03 / SELECTED IMPACT</div>
        <div class="section-title">Where strategy became measurable results.</div>
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

st.markdown(
    """
    <div class="section">
        <div class="section-number">04 / PROJECT PORTFOLIO</div>
        <div class="section-title">Explore the work behind the outcomes.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

portfolio_directory_items = [
    *PROJECT_PAGE_CONFIGS,
    {
        "key": "case-studies",
        "href": "/Case_Studies",
        "title": "Campaign Case Studies",
        "summary": (
            "A visual library of campaign strategies, audience decisions, channel "
            "architecture, and measurable outcomes across multiple industries."
        ),
    },
]

for row_start in range(0, len(portfolio_directory_items), 3):
    row_items = portfolio_directory_items[row_start : row_start + 3]
    columns = st.columns(3)
    for offset, item in enumerate(row_items):
        with columns[offset]:
            render_portfolio_directory_item(item, row_start + offset + 1)
    st.write("")

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
