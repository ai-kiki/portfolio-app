from __future__ import annotations

import streamlit as st



st.set_page_config(
    page_title="L.C. Felton · Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


pages = [
    st.Page("app.py", title="Home", icon="🏠", url_path="", default=True),
    st.Page(
        "pages/7_Case_Studies.py",
        title="Case Studies",
        icon="📈",
        url_path="Case_Studies",
    ),
    st.Page(
        "pages/1_Marketing_Operations_and_Automation.py",
        title="Marketing Operations & Automation",
        icon="⚙️",
        url_path="Marketing_Operations_and_Automation",
    ),
    st.Page(
        "pages/2_Tools_Playbooks_and_Frameworks.py",
        title="Tools, Playbooks & Frameworks",
        icon="🧰",
        url_path="Tools_Playbooks_and_Frameworks",
    ),
    st.Page(
        "pages/3_GTM_Strategy_and_Sales_Enablement.py",
        title="GTM Strategy & Sales Enablement",
        icon="🎯",
        url_path="GTM_Strategy_and_Sales_Enablement",
    ),
    # Completed project pages stay registered so existing links remain valid,
    # but they are reached from the category hubs instead of crowding navigation.
    st.Page(
        "pages/1_Dashboard_and_Insights.py",
        title="Client-Facing Performance Dashboard",
        url_path="Dashboard_and_Insights",
    ),
    st.Page(
        "pages/2_Process_Improvement_Case_Study.py",
        title="Automated Insertion Order Workflow",
        url_path="Process_Improvement_Case_Study",
    ),
    st.Page(
        "pages/3_Teamwork_Implementation_Case_Study.py",
        title="Teamwork Project Management Rollout",
        url_path="Teamwork_Implementation_Case_Study",
    ),
]


current_page = st.navigation(pages, position="hidden")
current_page.run()
