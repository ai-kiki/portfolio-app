from __future__ import annotations

import streamlit as st


_NAV_STYLES = """
<style>
.stApp { background:radial-gradient(circle at 100% 0%,rgba(111,78,154,.58) 0%,rgba(67,91,161,.37) 8rem,rgba(67,91,161,0) 25rem),radial-gradient(circle at 0% 100%,rgba(49,93,159,.52) 0%,rgba(104,75,151,.32) 8rem,rgba(104,75,151,0) 25rem),linear-gradient(135deg,#f7f9fc 0%,#ffffff 30%,#ffffff 72%,#faf8fd 100%)!important;background-attachment:fixed!important; }
[data-testid="stHeader"] { background:transparent!important; }
.portfolio-nav-shell,.portfolio-nav-shell * { box-sizing:border-box; }
.portfolio-nav-shell { backdrop-filter:blur(16px);background:rgba(255,255,255,.84);border:1px solid rgba(21,36,59,.09);border-radius:16px;box-shadow:0 12px 32px rgba(28,48,82,.08);font-family:"DM Sans",Arial,sans-serif;margin:0 auto 1rem;max-width:1240px;padding:.72rem .9rem; }
.portfolio-nav-links { align-items:stretch;display:grid;gap:.2rem .8rem;grid-template-columns:repeat(3,minmax(0,1fr));width:100%; }
.portfolio-nav-links a:nth-child(1) { grid-column:1;grid-row:1; }
.portfolio-nav-links a:nth-child(2) { grid-column:2;grid-row:1; }
.portfolio-nav-links a:nth-child(3) { grid-column:3;grid-row:1; }
.portfolio-nav-links a:nth-child(4) { grid-column:1;grid-row:2; }
.portfolio-nav-links a:nth-child(5) { grid-column:2;grid-row:2; }
.portfolio-nav-links a { align-items:center;border-radius:9px;color:#142b4b!important;display:flex;font-size:.82rem;font-weight:700;justify-content:flex-start;line-height:1.2;min-height:2.35rem;padding:.5rem .62rem;text-align:left;text-decoration:none!important;transition:background .18s ease,color .18s ease;white-space:normal; }
.portfolio-nav-links a:hover { background:rgba(83,96,160,.10);color:#344681!important; }
[data-testid="stSidebar"],[data-testid="collapsedControl"],[data-testid="stExpandSidebarButton"],[data-testid="stSidebarCollapseButton"] { display:none!important; }
@media (max-width:900px) {
  .portfolio-nav-links { grid-template-columns:repeat(2,minmax(0,1fr)); }
  .portfolio-nav-links a:nth-child(1) { grid-column:1;grid-row:1; }
  .portfolio-nav-links a:nth-child(2) { grid-column:2;grid-row:1; }
  .portfolio-nav-links a:nth-child(3) { grid-column:1;grid-row:2; }
  .portfolio-nav-links a:nth-child(4) { grid-column:2;grid-row:2; }
  .portfolio-nav-links a:nth-child(5) { grid-column:1/-1;grid-row:3; }
}
@media (max-width:520px) { .portfolio-nav-shell { border-radius:13px;margin-bottom:1.5rem; }.portfolio-nav-links { display:grid;grid-template-columns:repeat(2,minmax(0,1fr));width:100%; }.portfolio-nav-links a { font-size:.74rem;justify-content:flex-start;line-height:1.25;text-align:left; } }
</style>
"""


_NAV_MARKUP = (
    '<nav class="portfolio-nav-shell" aria-label="Portfolio navigation">'
    '<div class="portfolio-nav-links">'
    '<a href="/" target="_self">Home</a>'
    '<a href="/Case_Studies" target="_self">Case Studies</a>'
    '<a href="/Marketing_Operations_and_Automation" target="_self">Marketing Operations &amp; Automation</a>'
    '<a href="/Tools_Playbooks_and_Frameworks" target="_self">AI Tools &amp; Agentic Workflows</a>'
    '<a href="/GTM_Strategy_and_Sales_Enablement" target="_self">GTM Strategy &amp; Sales Enablement</a>'
    "</div></nav>"
)


def render_portfolio_navigation() -> None:
    st.markdown(_NAV_STYLES, unsafe_allow_html=True)
    st.markdown(_NAV_MARKUP, unsafe_allow_html=True)
