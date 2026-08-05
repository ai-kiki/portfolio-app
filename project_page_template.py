from __future__ import annotations

import html

import streamlit as st

from profile_data import CONTACT, PROFILE


PROJECT_PAGE_CONFIGS = [
    {
        "key": "dashboard",
        "file": "pages/1_Dashboard_and_Insights.py",
        "eyebrow": "Reporting, measurement, and decision support",
        "title": "Dashboard & Insights",
        "summary": (
            "A home for dashboard strategy, reporting automation, and the executive-ready "
            "insights that turn performance data into clear decisions."
        ),
        "focus": [
            "The reporting challenge and the decisions stakeholders needed to make.",
            "The dashboard architecture, automation, and storytelling approach.",
            "The time saved, visibility gained, and business actions enabled.",
        ],
    },
    {
        "key": "process",
        "file": "pages/2_Process_Improvement_Case_Study.py",
        "eyebrow": "Operations, automation, and adoption",
        "title": "Process Improvement Case Study",
        "summary": (
            "A practical look at diagnosing operational friction, redesigning a workflow, "
            "and helping people adopt a more scalable way of working."
        ),
        "focus": [
            "The bottleneck, its root cause, and its effect on the team or customer.",
            "The redesigned process, automation choices, and implementation plan.",
            "The improvement in speed, consistency, capacity, or cost.",
        ],
    },
    {
        "key": "gtm",
        "file": "pages/3_GTM_Strategy_Project.py",
        "eyebrow": "Positioning, enablement, and market adoption",
        "title": "GTM Strategy Project",
        "summary": (
            "A go-to-market case study connecting customer need, product positioning, "
            "launch planning, sales enablement, and measurable adoption."
        ),
        "focus": [
            "The market opportunity, audience, and positioning challenge.",
            "The launch strategy, enablement plan, and cross-functional coordination.",
            "The adoption, pipeline, revenue, or customer-response signals that followed.",
        ],
    },
    {
        "key": "campaign",
        "file": "pages/4_Campaign_Optimization_Framework.py",
        "eyebrow": "Media performance and continuous improvement",
        "title": "Campaign Optimization Framework",
        "summary": (
            "A repeatable framework for turning delivery, audience, creative, and conversion "
            "signals into focused optimization decisions."
        ),
        "focus": [
            "The campaign objective, baseline performance, and constraints.",
            "The measurement cadence, decision rules, tests, and optimization workflow.",
            "The lift in performance, efficiency, retention, or client confidence.",
        ],
    },
    {
        "key": "team",
        "file": "pages/5_Team_Transformation_Project.py",
        "eyebrow": "Leadership, capability building, and change",
        "title": "Team Transformation Project",
        "summary": (
            "A leadership case study focused on clarifying roles, strengthening capability, "
            "improving accountability, and building a team ready for change."
        ),
        "focus": [
            "The team challenge, operating environment, and leadership priorities.",
            "The coaching, process, communication, and development interventions.",
            "The gains in performance, ownership, collaboration, or readiness.",
        ],
    },
    {
        "key": "materials",
        "file": "pages/6_Pitch_Decks_and_Training_Materials.py",
        "eyebrow": "Storytelling, enablement, and learning design",
        "title": "Pitch Decks & Training Materials",
        "summary": (
            "A curated space for strategic narratives, sales enablement, workshop materials, "
            "and training tools designed to make complex ideas useful."
        ),
        "focus": [
            "The audience, message, and behavior the material needed to influence.",
            "The narrative structure, visual approach, and learning experience.",
            "The use case, audience response, and business or team impact.",
        ],
    },
]


def _safe(value: object) -> str:
    return html.escape(str(value))


def _inject_page_styles() -> None:
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
            --mint: #c9f2df;
            --line: rgba(19, 35, 31, 0.12);
        }

        .stApp {
            background:
                radial-gradient(circle at 92% 4%, rgba(201, 242, 223, .70), transparent 29rem),
                linear-gradient(180deg, #fbfcf8 0%, var(--paper) 100%);
            color: var(--ink);
            font-family: "DM Sans", sans-serif;
        }

        .block-container { max-width: 1080px; padding-top: 2.2rem; padding-bottom: 5rem; }
        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stAppDeployButton"], .stAppDeployButton { display: none !important; }
        #MainMenu, footer { visibility: hidden; }
        [data-testid="stSidebar"] { background: var(--ink); }
        [data-testid="stSidebar"] * { color: rgba(255,255,255,.86) !important; }

        h1, h2, h3 {
            color: var(--ink) !important;
            font-family: "Manrope", sans-serif !important;
            letter-spacing: -.035em;
        }

        .project-topbar {
            align-items: center;
            display: flex;
            justify-content: space-between;
            margin-bottom: 4.8rem;
        }

        .project-brand {
            align-items: center;
            display: flex;
            font-family: "Manrope", sans-serif;
            font-size: .9rem;
            font-weight: 800;
            gap: .65rem;
            letter-spacing: .08em;
            text-transform: uppercase;
        }

        .project-brand-mark {
            align-items: center;
            background: var(--ink);
            border-radius: 50%;
            color: white;
            display: inline-flex;
            height: 2rem;
            justify-content: center;
            width: 2rem;
        }

        .project-status {
            background: rgba(255,255,255,.75);
            border: 1px solid var(--line);
            border-radius: 999px;
            color: var(--muted);
            font-size: .78rem;
            font-weight: 700;
            padding: .55rem .85rem;
        }

        .project-eyebrow {
            color: var(--accent);
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .13em;
            margin-top: 2.5rem;
            text-transform: uppercase;
        }

        .project-page-title {
            font-family: "Manrope", sans-serif;
            font-size: clamp(3rem, 7vw, 6.2rem);
            font-weight: 800;
            letter-spacing: -.07em;
            line-height: .94;
            margin: 1rem 0 1.5rem;
            max-width: 900px;
        }

        .project-page-summary {
            color: var(--muted);
            font-size: 1.15rem;
            line-height: 1.7;
            max-width: 740px;
        }

        .blueprint-heading {
            border-top: 1px solid var(--line);
            font-family: "Manrope", sans-serif;
            font-size: clamp(2rem, 4vw, 3.2rem);
            font-weight: 800;
            letter-spacing: -.05em;
            margin-top: 5.5rem;
            padding-top: 1.4rem;
        }

        .blueprint-card {
            background: rgba(255,255,255,.78);
            border: 1px solid var(--line);
            border-radius: 20px;
            min-height: 205px;
            padding: 1.45rem;
        }

        .blueprint-card .step {
            color: var(--accent);
            font-size: .75rem;
            font-weight: 800;
            letter-spacing: .1em;
        }

        .blueprint-card h3 { font-size: 1.05rem; margin: 1.5rem 0 .6rem; }
        .blueprint-card p { color: var(--muted); font-size: .9rem; line-height: 1.6; }

        .build-note {
            background: var(--ink);
            border-radius: 24px;
            color: white;
            margin: 4rem 0 2rem;
            padding: clamp(1.8rem, 5vw, 3.2rem);
        }

        .build-note h2 { color: white !important; font-size: 2rem; margin: 0 0 .8rem; }
        .build-note p { color: rgba(255,255,255,.7); line-height: 1.65; margin: 0; max-width: 700px; }

        div.stButton > button, div.stLinkButton > a, [data-testid="stPageLink"] a {
            border-radius: 999px;
            font-family: "DM Sans", sans-serif;
            font-weight: 700;
        }

        @media (max-width: 700px) {
            .block-container { padding: 1.2rem 1rem 3rem; }
            .project-topbar { margin-bottom: 3.2rem; }
            .project-status { display: none; }
            .project-page-title { font-size: 3.4rem; }
            .blueprint-card { min-height: 0; margin-bottom: .7rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_project_page(key: str, *, configure_page: bool = True) -> None:
    item_index = next(
        index for index, item in enumerate(PROJECT_PAGE_CONFIGS) if item["key"] == key
    )
    item = PROJECT_PAGE_CONFIGS[item_index]

    if configure_page:
        st.set_page_config(
            page_title=f"{item['title']} · {PROFILE['name']}",
            page_icon="✦",
            layout="wide",
            initial_sidebar_state="expanded",
        )
    _inject_page_styles()

    st.markdown(
        f"""
        <div class="project-topbar">
            <div class="project-brand">
                <span class="project-brand-mark">✦</span>
                {_safe(PROFILE['name'])}
            </div>
            <div class="project-status">Site framework ready</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="/" target="_self">← Back to portfolio</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="project-eyebrow">{_safe(item['eyebrow'])}</div>
        <div class="project-page-title">{_safe(item['title'])}</div>
        <div class="project-page-summary">{_safe(item['summary'])}</div>
        <div class="blueprint-heading">Case study blueprint.</div>
        """,
        unsafe_allow_html=True,
    )

    headings = ["The challenge", "My approach", "Outcomes & evidence"]
    columns = st.columns(3)
    for column, heading, detail, step in zip(columns, headings, item["focus"], range(1, 4)):
        with column:
            st.markdown(
                f"""
                <div class="blueprint-card">
                    <div class="step">0{step}</div>
                    <h3>{_safe(heading)}</h3>
                    <p>{_safe(detail)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="build-note">
            <h2>Structure first. Evidence next.</h2>
            <p>This page is intentionally prepared for the project story, supporting visuals, and measurable results. Content will be added after the overall portfolio experience is finalized.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nav_columns = st.columns(2)
    if item_index > 0:
        previous_item = PROJECT_PAGE_CONFIGS[item_index - 1]
        with nav_columns[0]:
            st.markdown(
                f'<a href="/?project={_safe(previous_item["key"])}" target="_self">'
                f'← Previous: {_safe(previous_item["title"])}</a>',
                unsafe_allow_html=True,
            )
    if item_index < len(PROJECT_PAGE_CONFIGS) - 1:
        next_item = PROJECT_PAGE_CONFIGS[item_index + 1]
        with nav_columns[1]:
            st.markdown(
                f'<a href="/?project={_safe(next_item["key"])}" target="_self">'
                f'Next: {_safe(next_item["title"])} →</a>',
                unsafe_allow_html=True,
            )

    st.caption(f"Questions or opportunities: {CONTACT['email']}")
