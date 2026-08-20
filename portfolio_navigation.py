from __future__ import annotations

import streamlit as st


_NAV_STYLES = """
<style>
.portfolio-nav-shell,.portfolio-nav-shell * { box-sizing:border-box; }
.portfolio-nav-shell { background:#071c3b;border-radius:0 0 18px 18px;box-shadow:0 12px 30px rgba(7,28,59,.14);font-family:"DM Sans",Arial,sans-serif;margin:-1rem auto 1.35rem;max-width:1180px;padding:.85rem 1rem; }
.portfolio-nav-links { display:grid;gap:.35rem .8rem;grid-template-columns:repeat(3,minmax(0,1fr)); }
.portfolio-nav-links a { align-items:center;border-radius:10px;color:rgba(255,255,255,.88)!important;display:flex;font-size:.86rem;font-weight:700;justify-content:flex-start;line-height:1.3;min-height:2.7rem;padding:.55rem .7rem;text-align:left;text-decoration:none!important;transition:background .18s ease,color .18s ease;white-space:normal; }
.portfolio-nav-links a:hover { background:rgba(255,255,255,.12);color:#fff!important; }
[data-testid="stSidebar"],[data-testid="collapsedControl"],[data-testid="stExpandSidebarButton"],[data-testid="stSidebarCollapseButton"] { display:none!important; }
@media (max-width:760px) { .portfolio-nav-links { grid-template-columns:repeat(2,minmax(0,1fr)); } }
@media (max-width:480px) { .portfolio-nav-shell { border-radius:0 0 14px 14px;margin-top:-.5rem; }.portfolio-nav-links { grid-template-columns:1fr; }.portfolio-nav-links a { font-size:.82rem;min-height:2.4rem;padding:.45rem .55rem; } }
</style>
"""


_NAV_MARKUP = (
    '<nav class="portfolio-nav-shell" aria-label="Portfolio navigation">'
    '<div class="portfolio-nav-links">'
    '<a href="/" target="_self">Home</a>'
    '<a href="/Case_Studies" target="_self">Case Studies</a>'
    '<a href="/Marketing_Operations_and_Automation" target="_self">Marketing Operations &amp; Automation</a>'
    '<a href="/Tools_Playbooks_and_Frameworks" target="_self">Tools, Playbooks &amp; Frameworks</a>'
    '<a href="/GTM_Strategy_and_Sales_Enablement" target="_self">GTM Strategy &amp; Sales Enablement</a>'
    "</div></nav>"
)


def render_portfolio_navigation() -> None:
    st.markdown(_NAV_STYLES, unsafe_allow_html=True)
    st.markdown(_NAV_MARKUP, unsafe_allow_html=True)
