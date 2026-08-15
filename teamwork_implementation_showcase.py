from __future__ import annotations

import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st


def _hero_data_uri() -> str:
    image_path = Path(__file__).parent / "assets" / "teamwork-implementation-hero-option-b.png"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap');
[data-testid="stHeader"] { background:transparent; }
[data-testid="stAppDeployButton"],.stAppDeployButton { display:none!important; }
#MainMenu,footer { visibility:hidden; }
[data-testid="stSidebar"] { background:#071c3b; }
[data-testid="stSidebar"] * { color:rgba(255,255,255,.88)!important; }
.stApp { background:#f5f8fc; }
.block-container { max-width:1280px; padding:1.5rem 1.25rem 4rem; }
.tw-case,.tw-case * { box-sizing:border-box; }
.tw-case { --navy:#071c3b;--ink:#10233f;--muted:#5f6f84;--coral:#ec7160;--violet:#795bd6;--teal:#139b91;--blue:#2f70dc;color:var(--ink);font-family:"DM Sans",sans-serif; }
.tw-case h1,.tw-case h2,.tw-case h3,.tw-case p { margin-block-start:0; }
.tw-topbar { align-items:center;display:flex;justify-content:space-between;margin:0 auto 1.15rem;max-width:1180px; }
.tw-brand { align-items:center;color:var(--ink)!important;display:flex;font-size:.92rem;font-weight:800;gap:.65rem;letter-spacing:.08em;text-decoration:none!important;text-transform:uppercase; }
.tw-brand i { align-items:center;background:var(--navy);border-radius:50%;color:white;display:flex;font-style:normal;height:2rem;justify-content:center;width:2rem; }
.tw-category { color:var(--violet);font-size:1.08rem;font-weight:800; }
.tw-wrap { background:white;box-shadow:0 18px 55px rgba(7,28,59,.09);margin:0 auto;max-width:1180px;overflow:hidden; }
.tw-hero { min-height:545px;overflow:hidden;position:relative; }
.tw-hero img { height:100%;inset:0;object-fit:cover;position:absolute;width:100%; }
.tw-hero:after { background:linear-gradient(90deg,rgba(255,255,255,.99) 0%,rgba(255,255,255,.96) 31%,rgba(255,255,255,.72) 48%,rgba(255,255,255,.06) 74%);content:"";inset:0;position:absolute; }
.tw-hero-copy { max-width:645px;padding:5.15rem 0 4.3rem 4.3rem;position:relative;width:57%;z-index:1; }
.tw-eyebrow,.tw-section-label { color:var(--coral);font-size:.9rem;font-weight:850;letter-spacing:.13em;text-transform:uppercase; }
.tw-hero h1 { color:#07182e!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2.55rem,4vw,3.75rem);font-weight:600;letter-spacing:-.045em;line-height:.98;margin:1rem 0 1.3rem;max-width:590px; }
.tw-hero h1 em { color:var(--coral);font-style:normal; }
.tw-hero-copy p { color:#263b55;font-size:1.16rem;font-weight:550;line-height:1.55;max-width:545px; }
.tw-title-rule { background:linear-gradient(90deg,var(--coral),var(--violet));border-radius:4px;height:5px;margin-top:1.45rem;width:70px; }
.tw-meta { background:#fbfcfe;border-bottom:1px solid #dfe6ee;border-top:1px solid #dfe6ee;display:grid;grid-template-columns:1.2fr 1fr 1fr 1.25fr; }
.tw-meta div { border-right:1px solid #dfe6ee;padding:1.35rem 1.55rem; }
.tw-meta div:last-child { border-right:0; }
.tw-meta span { color:#7a899d;display:block;font-size:.7rem;font-weight:850;letter-spacing:.11em;margin-bottom:.45rem;text-transform:uppercase; }
.tw-meta strong { display:block;font-size:1.02rem;line-height:1.45; }
.tw-proof { background:var(--navy);display:grid;grid-template-columns:repeat(5,1fr); }
.tw-proof div { border-right:1px solid rgba(255,255,255,.14);min-height:148px;padding:1.55rem 1.2rem; }
.tw-proof div:last-child { border-right:0; }
.tw-proof strong { color:white;display:block;font-family:"Newsreader",Georgia,serif;font-size:2.35rem;line-height:1; }
.tw-proof span { color:#c6d2e3;display:block;font-size:.88rem;line-height:1.4;margin-top:.65rem; }
.tw-section { padding:5.1rem 4.3rem; }
.tw-heading { max-width:780px; }
.tw-heading.center { margin:0 auto 2.8rem;text-align:center; }
.tw-heading h2 { color:#0a203d!important;font-family:"Newsreader",Georgia,serif!important;font-size:clamp(2.1rem,3.4vw,3rem);font-weight:600;letter-spacing:-.04em;line-height:1.02;margin:.7rem 0 0; }
.tw-heading p { color:var(--muted);font-size:1.16rem;line-height:1.65;margin:1rem 0 0; }
.tw-section-label { font-size:1.08rem;letter-spacing:.1em; }
.tw-challenge { background:linear-gradient(180deg,#fff,#f4f7fb); }
.tw-pain-grid { display:grid;gap:1rem;grid-template-columns:repeat(4,1fr);margin-top:2.65rem; }
.tw-pain { --accent:var(--coral);--tint:#fff0ed;background:linear-gradient(180deg,#fff,var(--tint));border:1px solid #dde5ee;border-radius:18px;display:flex;flex-direction:column;min-height:325px;padding:1.45rem;position:relative;overflow:hidden; }
.tw-pain:nth-child(2){--accent:var(--violet);--tint:#f3f0ff}.tw-pain:nth-child(3){--accent:var(--teal);--tint:#eaf8f5}.tw-pain:nth-child(4){--accent:#d68a24;--tint:#fff6e9}
.tw-pain:before { background:var(--accent);content:"";height:5px;inset:0 0 auto;position:absolute; }
.tw-icon { align-items:center;background:var(--accent);border-radius:14px;color:white;display:flex;font-size:1.55rem;height:54px;justify-content:center;margin:1rem 0 1.3rem;width:54px; }
.tw-pain small { color:var(--accent);font-size:.72rem;font-weight:850;letter-spacing:.09em;text-transform:uppercase; }
.tw-pain h3 { color:var(--ink)!important;font-size:1.35rem;line-height:1.2;margin:.65rem 0 .85rem; }
.tw-pain p { color:#4b5d73;font-size:1rem;line-height:1.58;margin:0; }
.tw-observed { align-items:center;background:white;border:1px solid #dbe4ee;border-left:6px solid var(--coral);border-radius:14px;display:grid;gap:1.5rem;grid-template-columns:210px 1fr;margin-top:1.25rem;padding:1.35rem 1.55rem; }
.tw-observed strong { color:var(--navy);font-size:1.3rem; }
.tw-observed p { color:#4e6076;font-size:1rem;line-height:1.6;margin:0; }
.tw-role-section { background:var(--navy);color:white; }
.tw-role-section .tw-section-label { color:#ff9b8c; }
.tw-role-section h2 { color:white!important; }
.tw-role-section .tw-lead { color:#f1f5fa!important;font-size:1.17rem!important;line-height:1.65;max-width:890px; }
.tw-contributions { display:grid;gap:1rem;grid-template-columns:repeat(3,1fr);margin-top:3rem; }
.tw-contribution { --accent:#4f9cff;background:linear-gradient(160deg,rgba(255,255,255,.085),rgba(255,255,255,.025));border:1px solid rgba(255,255,255,.14);border-radius:18px;display:flex;flex-direction:column;min-height:335px;overflow:hidden;padding:1.5rem;position:relative; }
.tw-contribution:nth-child(2){--accent:#2dc6ad}.tw-contribution:nth-child(3){--accent:#a98cff}.tw-contribution:nth-child(4){--accent:#f2a64c}.tw-contribution:nth-child(5){--accent:#ed6f91}.tw-contribution:nth-child(6){--accent:#63c5da}
.tw-contribution:before { background:var(--accent);content:"";height:5px;inset:0 0 auto;position:absolute; }
.tw-contribution-top { align-items:center;display:flex;justify-content:space-between;margin-bottom:1.8rem; }
.tw-contribution-top span { color:var(--accent);font-family:"Newsreader",Georgia,serif;font-size:2.7rem;font-weight:650;line-height:1; }
.tw-contribution-top i { align-items:center;background:color-mix(in srgb,var(--accent) 18%,transparent);border:1px solid color-mix(in srgb,var(--accent) 55%,transparent);border-radius:13px;color:var(--accent);display:flex;font-size:1.4rem;font-style:normal;height:50px;justify-content:center;width:50px; }
.tw-contribution h3 { color:white!important;font-size:1.32rem;line-height:1.22;margin:0 0 .9rem; }
.tw-contribution p { color:#c9d5e5;font-size:1.02rem;line-height:1.62;margin:0; }
.tw-boundary { background:#102b50;border:1px solid rgba(255,255,255,.15);border-radius:14px;color:#dbe6f4;font-size:1rem;line-height:1.58;margin-top:1.2rem;padding:1.25rem 1.4rem; }
.tw-boundary strong { color:#ff9b8c; }
.tw-solution { background:#f2f5fa; }
.tw-flow { align-items:stretch;display:grid;gap:.62rem;grid-template-columns:repeat(6,1fr);margin-top:2.6rem; }
.tw-flow article { --accent:var(--blue);background:white;border:1px solid #dce5ef;border-radius:15px;box-shadow:0 9px 22px rgba(18,54,94,.07);min-height:185px;padding:1.25rem;position:relative; }
.tw-flow article:nth-child(2){--accent:var(--coral)}.tw-flow article:nth-child(3){--accent:var(--violet)}.tw-flow article:nth-child(4){--accent:var(--teal)}.tw-flow article:nth-child(5){--accent:#d68a24}.tw-flow article:nth-child(6){--accent:#3e7bd7}
.tw-flow article:before { background:var(--accent);border-radius:15px 15px 0 0;content:"";height:5px;inset:0 0 auto;position:absolute; }
.tw-flow b { color:var(--accent);display:block;font-size:.72rem;letter-spacing:.09em;margin:.45rem 0 .75rem;text-transform:uppercase; }
.tw-flow strong { color:var(--ink);display:block;font-size:1.05rem;line-height:1.3; }
.tw-flow p { color:#5c6d81;font-size:.95rem;line-height:1.52;margin:.55rem 0 0; }
.tw-mockup { background:#e8edf3;border-radius:24px;box-shadow:0 18px 36px rgba(15,45,78,.14);margin-top:2.3rem;padding:1.15rem; }
.tw-window { background:white;border-radius:16px;overflow:hidden; }
.tw-windowbar { align-items:center;background:#132d51;color:white;display:flex;justify-content:space-between;padding:1rem 1.25rem; }
.tw-windowbar strong { font-size:1.08rem; }.tw-windowbar span { color:#aebed1;font-size:.82rem; }
.tw-ui { display:grid;grid-template-columns:180px 1.7fr .92fr;min-height:470px; }
.tw-ui-nav { background:#f6f7fa;border-right:1px solid #e0e5eb;padding:1.25rem .9rem; }
.tw-ui-nav b { color:#7b8797;display:block;font-size:.69rem;letter-spacing:.1em;margin:.3rem .5rem .9rem;text-transform:uppercase; }
.tw-ui-nav span { border-radius:8px;color:#495b70;display:block;font-size:.88rem;margin:.25rem 0;padding:.62rem .65rem; }.tw-ui-nav span.active { background:#ebe6fb;color:#6446c1;font-weight:800; }
.tw-ui-main { padding:1.4rem; }.tw-ui-title { align-items:center;display:flex;justify-content:space-between;margin-bottom:1.2rem; }.tw-ui-title h3 { color:var(--ink)!important;font-size:1.35rem;margin:0; }.tw-status { background:#e9f7f3;border-radius:999px;color:#087e71;font-size:.72rem;font-weight:800;padding:.42rem .7rem; }
.tw-table-head,.tw-task { align-items:center;display:grid;gap:.5rem;grid-template-columns:1.7fr .7fr .58fr .65fr; }.tw-table-head { color:#8793a3;font-size:.64rem;font-weight:800;letter-spacing:.08em;padding:0 .6rem .5rem;text-transform:uppercase; }.tw-task { border-top:1px solid #e7ebf0;min-height:57px;padding:.65rem .6rem; }.tw-task strong { color:#30435c;font-size:.83rem; }.tw-task span { color:#64758a;font-size:.76rem; }.tw-check { align-items:center;background:#e8f6f3;border:1px solid #a9d9d2;border-radius:5px;color:#108c80;display:inline-flex!important;height:20px;justify-content:center;margin-right:.42rem;width:20px; }.tw-pill { background:#eef3fc;border-radius:999px;color:#376ab8!important;font-weight:750;padding:.28rem .42rem;text-align:center; }.tw-pill.blocked { background:#fff0ed;color:#bd5b4a!important; }
.tw-activity { background:#fbfcfe;border-left:1px solid #e3e8ee;padding:1.4rem 1.1rem; }.tw-activity h3 { color:var(--ink)!important;font-size:1.1rem;margin-bottom:1.2rem; }.tw-message { border-bottom:1px solid #e7ebf0;margin-bottom:1rem;padding-bottom:1rem; }.tw-message b { color:#283b54;display:block;font-size:.8rem; }.tw-message span { color:#8290a1;font-size:.68rem; }.tw-message p { color:#53657a;font-size:.76rem;line-height:1.45;margin:.35rem 0 0; }
.tw-mock-caption { color:#6b7a8d;font-size:.9rem;line-height:1.5;margin:1rem 0 0;text-align:center; }
.tw-rollout { background:white; }
.tw-timeline { display:grid;gap:1rem;grid-template-columns:repeat(4,1fr);margin-top:2.7rem; }
.tw-phase { --accent:var(--blue);background:#f7f9fc;border:1px solid #dbe4ee;border-radius:18px;min-height:285px;padding:1.5rem;position:relative; }.tw-phase:nth-child(2){--accent:var(--violet)}.tw-phase:nth-child(3){--accent:var(--coral)}.tw-phase:nth-child(4){--accent:var(--teal)}
.tw-phase:before { background:var(--accent);border-radius:18px 18px 0 0;content:"";height:6px;inset:0 0 auto;position:absolute; }.tw-phase small { color:var(--accent);display:block;font-size:.74rem;font-weight:850;letter-spacing:.1em;margin:.7rem 0 1rem;text-transform:uppercase; }.tw-phase h3 { color:var(--ink)!important;font-size:1.35rem;line-height:1.2;margin-bottom:.8rem; }.tw-phase p { color:#53657a;font-size:1rem;line-height:1.58;margin:0; }
.tw-results { background:linear-gradient(150deg,#071c3b,#102e55);color:white; }.tw-results .tw-section-label { color:#65d3c4; }.tw-results h2 { color:white!important; }.tw-results .tw-heading p { color:#d3ddec; }.tw-result-grid { display:grid;gap:1rem;grid-template-columns:repeat(3,1fr);margin-top:2.7rem; }.tw-result { background:white;border-radius:18px;color:var(--ink);min-height:300px;padding:1.55rem; }.tw-result:nth-child(2){background:#e5f5f1}.tw-result:nth-child(3){background:#f1edfb}.tw-result i { align-items:center;background:var(--navy);border-radius:12px;color:white;display:flex;font-size:1.35rem;font-style:normal;height:48px;justify-content:center;margin-bottom:1.3rem;width:48px; }.tw-result h3 { color:var(--ink)!important;font-size:1.38rem;line-height:1.2;margin-bottom:.8rem; }.tw-result p { color:#42556e;font-size:1.02rem;line-height:1.62;margin:0; }
.tw-reflection { display:grid;grid-template-columns:repeat(3,1fr); }.tw-reflection article { min-height:365px;padding:3rem 2.5rem; }.tw-reflection article:nth-child(1){background:#dce8f4}.tw-reflection article:nth-child(2){background:#dff3ef}.tw-reflection article:nth-child(3){background:#eeeaf7}.tw-reflection small { color:#0b315d;display:block;font-size:.9rem;font-weight:850;letter-spacing:.11em;margin-bottom:2rem;text-transform:uppercase; }.tw-reflection h3 { color:#082651!important;font-size:1.3rem;line-height:1.35;margin-bottom:.8rem;text-transform:uppercase; }.tw-reflection p { color:#173654;font-size:1.02rem;line-height:1.62;margin:0; }
.tw-disclosure { background:#f5f7fa;color:#75859a;font-size:.92rem;line-height:1.58;margin:0;padding:1.8rem 4rem;text-align:center; }.tw-back { color:var(--navy)!important;display:block;font-size:.94rem;font-weight:800;margin:1rem 0 0;text-align:center;text-decoration:none!important; }
@media(max-width:980px){.tw-proof{grid-template-columns:repeat(3,1fr)}.tw-pain-grid,.tw-timeline{grid-template-columns:repeat(2,1fr)}.tw-contributions,.tw-result-grid{grid-template-columns:repeat(2,1fr)}.tw-flow{grid-template-columns:repeat(3,1fr)}.tw-ui{grid-template-columns:150px 1fr}.tw-activity{display:none}.tw-reflection{grid-template-columns:1fr}.tw-reflection article{min-height:auto}.tw-meta{grid-template-columns:repeat(2,1fr)}}
@media(max-width:700px){.block-container{padding:1rem .7rem 3rem}.tw-category{display:none}.tw-hero{min-height:690px}.tw-hero img{bottom:0;height:43%;top:auto}.tw-hero:after{background:linear-gradient(180deg,#fff 0 55%,rgba(255,255,255,.12) 83%)}.tw-hero-copy{padding:3rem 1.5rem 19rem;width:100%}.tw-hero h1{font-size:3.2rem}.tw-meta,.tw-proof,.tw-pain-grid,.tw-contributions,.tw-flow,.tw-timeline,.tw-result-grid{grid-template-columns:1fr}.tw-section{padding:3.5rem 1.35rem}.tw-observed{grid-template-columns:1fr}.tw-ui{grid-template-columns:1fr}.tw-ui-nav{display:none}.tw-table-head,.tw-task{grid-template-columns:1.55fr .65fr .7fr}.tw-table-head span:nth-child(3),.tw-task>span:nth-child(3){display:none}.tw-disclosure{padding:1.5rem}.tw-proof div{min-height:auto}.tw-pain,.tw-contribution,.tw-phase,.tw-result{min-height:auto}}
</style>
"""


def render_teamwork_implementation_case_study() -> None:
    st.set_page_config(
        page_title="Teamwork Implementation | L.C. Felton",
        page_icon="TW",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    hero = _hero_data_uri()
    markup = dedent(
        f"""
            <div class="tw-case">
              <header class="tw-topbar"><a class="tw-brand" href="/" target="_self"><i>TW</i> Software implementation case study</a><span class="tw-category">Operational Systems</span></header>
              <main class="tw-wrap">
                <section class="tw-hero">
                  <img src="{hero}" alt="Campaign operations team collaborating around a shared project-management workspace">
                  <div class="tw-hero-copy">
                    <span class="tw-eyebrow">Software implementation &middot; Q2 2022</span>
                    <h1>Launching a Shared Campaign Operations Hub <em>in 30 Days</em></h1>
                    <p>A company-wide project management software implementation gave campaign teams one shared place to track assignments, launch status, assets, and communication.</p>
                    <div class="tw-title-rule"></div>
                  </div>
                </section>
                <section class="tw-meta">
                  <div><span>My project role</span><strong>Workflow &amp; Implementation Lead / Market Champion</strong></div>
                  <div><span>Organization</span><strong>Multi-market media organization</strong></div>
                  <div><span>Scope</span><strong>10 markets &middot; 250+ users company-wide</strong></div>
                  <div><span>Systems</span><strong>Teamwork, Zoho Forms, Zapier, Outlook</strong></div>
                </section>
                <section class="tw-section tw-challenge">
                  <div class="tw-heading"><span class="tw-section-label">01 &middot; The challenge</span><h2>Campaign work was moving, but visibility was fragmented</h2><p>Sales, Digital Support, Digital Marketing, and Ad Operations needed a shared view of campaign readiness. Instead, status, files, and decisions were distributed across individual inboxes and disconnected communication threads.</p></div>
                  <div class="tw-pain-grid">
                    <article class="tw-pain"><div class="tw-icon">✉</div><small>Communication</small><h3>Broken email chains</h3><p>Long threads were difficult to follow, easy to fragment, and rarely gave every stakeholder the same context.</p></article>
                    <article class="tw-pain"><div class="tw-icon">↻</div><small>Coordination</small><h3>Fragmented campaign requests</h3><p>Ad Operations received duplicate and piecemeal requests that sometimes arrived without complete campaign details or required assets. Teams had to reconstruct what was needed through repeated follow-up, making an already labor-intensive handoff even more belabored.</p></article>
                    <article class="tw-pain"><div class="tw-icon">✓</div><small>Readiness</small><h3>Unclear launch status</h3><p>Teams could not always tell whether every asset, approval, or fulfillment step was complete and ready for execution.</p></article>
                    <article class="tw-pain"><div class="tw-icon">⇄</div><small>Continuity</small><h3>PTO handoff risk</h3><p>Backup team members often lacked the information, documents, or context needed to keep campaigns moving.</p></article>
                  </div>
                  <div class="tw-observed"><strong>Observed business impact</strong><p>Sales reported limited visibility into campaign status, while execution teams absorbed extra follow-up, repeated questions, and avoidable launch-readiness uncertainty.</p></div>
                </section>
                <section class="tw-section tw-role-section">
                  <div class="tw-heading"><span class="tw-section-label">02 &middot; My contribution</span><h2>Configuring the system around how the market actually worked</h2><p class="tw-lead">As market champion and point of contact, I translated the local fulfillment workflow into a usable Teamwork environment, validated the end-to-end experience, and led adoption for my 22-person team.</p></div>
                  <div class="tw-contributions">
                    <article class="tw-contribution"><div class="tw-contribution-top"><span>01</span><i>⌁</i></div><h3>Map the Current State</h3><p>Documented the Digital Support workflow and refined it to address handoff gaps, launch-readiness questions, and communication needs.</p></article>
                    <article class="tw-contribution"><div class="tw-contribution-top"><span>02</span><i>⚙</i></div><h3>Configure the Environment</h3><p>Set up profiles, permissions, project templates, task owners, notifications, tags, and the local market structure. I also created a library of fill-in-the-blank communication templates to improve the completeness and accuracy of common requests.</p></article>
                    <article class="tw-contribution"><div class="tw-contribution-top"><span>03</span><i>▦</i></div><h3>Structure Repeatable Work</h3><p>Created a consistent campaign checklist and aligned task due dates to service-level expectations, with flexibility for internal deadlines.</p></article>
                    <article class="tw-contribution"><div class="tw-contribution-top"><span>04</span><i>⌕</i></div><h3>Test End to End</h3><p>Ran 12 orders from simple to complex and verified that each Teamwork project matched the details submitted through the web-based insertion order.</p></article>
                    <article class="tw-contribution"><div class="tw-contribution-top"><span>05</span><i>◇</i></div><h3>Train the Local Team</h3><p>Prepared the office for mandatory use, trained 22 Sales and support users, and explained how checklist updates replaced random status messages.</p></article>
                    <article class="tw-contribution"><div class="tw-contribution-top"><span>06</span><i>↗</i></div><h3>Support and Hand Off</h3><p>Provided six weeks of launch support, answered operational questions, and transferred primary ownership to Digital Support while continuing to use and support Teamwork as Ad Operations Manager.</p></article>
                  </div>
                  <div class="tw-boundary"><strong>Contribution boundary:</strong> The Product Team managed the Zoho fields and Dev Ops completed the supporting Zapier integration. My ownership centered on market workflow design, Teamwork configuration, testing, training, and adoption—not development of the integration itself.</div>
                </section>
                <section class="tw-section tw-solution">
                  <div class="tw-heading"><span class="tw-section-label">03 &middot; The solution</span><h2>One campaign project connected every team to the same work</h2><p>The completed workflow turned each submitted insertion order into a shared operational record with task ownership, due dates, files, status updates, and a dedicated communication thread.</p></div>
                  <div class="tw-flow">
                    <article><b>01 &middot; Intake</b><strong>Web-based IO submitted</strong><p>Campaign details entered once at the start of the process.</p></article>
                    <article><b>02 &middot; Trigger</b><strong>Project created</strong><p>The workflow generated a corresponding Teamwork project.</p></article>
                    <article><b>03 &middot; Structure</b><strong>Checklist activated</strong><p>Owners, tags, notifications, and SLA-based dates organized the work.</p></article>
                    <article><b>04 &middot; Fulfillment</b><strong>Assets centralized</strong><p>Sales and support added the materials needed for execution.</p></article>
                    <article><b>05 &middot; Handoff</b><strong>Ad Ops notified</strong><p>The project thread signaled readiness and linked the campaign materials.</p></article>
                    <article><b>06 &middot; Visibility</b><strong>Status confirmed</strong><p>Launch dates, delays, and live status remained visible to the team.</p></article>
                  </div>
                  <div class="tw-mockup">
                    <div class="tw-window">
                      <div class="tw-windowbar"><strong>Local HVAC Client | Summer AC Checkup Campaign</strong><span>Illustrative anonymized mockup</span></div>
                      <div class="tw-ui">
                        <aside class="tw-ui-nav"><b>Project</b><span>Overview</span><span class="active">Tasks</span><span>Messages</span><span>Files</span><span>Milestones</span><b style="margin-top:1.5rem">Saved views</b><span>Launch readiness</span><span>Assigned to me</span></aside>
                        <section class="tw-ui-main">
                          <div class="tw-ui-title"><h3>Campaign Fulfillment Checklist</h3><span class="tw-status">On track</span></div>
                          <div class="tw-table-head"><span>Task</span><span>Owner</span><span>Due</span><span>Status</span></div>
                          <div class="tw-task"><strong><i class="tw-check">✓</i>Confirm IO details</strong><span>A. Reed</span><span>May 09</span><span class="tw-pill">Complete</span></div>
                          <div class="tw-task"><strong><i class="tw-check">✓</i>Collect creative assets</strong><span>M. Chen</span><span>May 10</span><span class="tw-pill">Complete</span></div>
                          <div class="tw-task"><strong><i class="tw-check">✓</i>Verify landing page</strong><span>D. Patel</span><span>May 11</span><span class="tw-pill">In review</span></div>
                          <div class="tw-task"><strong><i class="tw-check">•</i>Submit to Ad Operations</strong><span>J. Moore</span><span>May 12</span><span class="tw-pill">Ready</span></div>
                          <div class="tw-task"><strong><i class="tw-check">•</i>Confirm launch date</strong><span>Ad Ops</span><span>May 13</span><span class="tw-pill blocked">Waiting</span></div>
                        </section>
                        <aside class="tw-activity"><h3>Campaign updates</h3><div class="tw-message"><b>Digital Support</b><span>9:12 AM</span><p>Final creative and landing-page details have been added. The campaign is ready for processing.</p></div><div class="tw-message"><b>Ad Operations</b><span>10:04 AM</span><p>Received. Launch is scheduled for May 15; status will be confirmed here.</p></div><div class="tw-message"><b>Sales</b><span>10:20 AM</span><p>Thank you—the status is visible on mobile and in the Outlook thread.</p></div></aside>
                      </div>
                    </div>
                  </div>
                  <p class="tw-mock-caption">This reconstruction illustrates the structure and operating model; it does not reproduce a client campaign, proprietary interface, or live company data.</p>
                </section>
                <section class="tw-section tw-rollout">
                  <div class="tw-heading"><span class="tw-section-label">04 &middot; Testing and rollout</span><h2>A 30-day implementation designed around operational continuity</h2><p>The launch moved quickly, but the work still included configuration, validation, mandatory team training, and a defined post-launch support period.</p></div>
                  <div class="tw-timeline">
                    <article class="tw-phase"><small>Phase 01</small><h3>Discover and Map</h3><p>Provided user roles, access needs, billing-profile details, and the market’s current fulfillment workflow.</p></article>
                    <article class="tw-phase"><small>Phase 02</small><h3>Configure and Validate</h3><p>Built the local operating structure and ran 12 test orders, comparing the new projects with the originating IO details.</p></article>
                    <article class="tw-phase"><small>Phase 03</small><h3>Launch Company-Wide</h3><p>The system launched across all markets at once. Use was mandatory for the teams working inside the new process.</p></article>
                    <article class="tw-phase"><small>Phase 04</small><h3>Support Adoption</h3><p>Trained 22 local users and provided six weeks of hands-on support before transferring ownership to Digital Support. I continued using Teamwork and providing support in a new capacity as Ad Operations Manager.</p></article>
                  </div>
                </section>
                <section class="tw-section tw-results">
                  <div class="tw-heading"><span class="tw-section-label">05 &middot; Results and adoption</span><h2>Qualitative feedback showed a clearer operating experience</h2><p>No formal time-savings study was completed, so the evidence is presented as stakeholder feedback and observed process improvement—not a manufactured quantitative claim.</p></div>
                  <div class="tw-result-grid">
                    <article class="tw-result"><i>✓</i><h3>Cleaner Ad Ops handoffs</h3><p>Ad Operations valued having one communication thread per campaign, fewer redundant requests, and one repository for creative assets and supporting documents.</p></article>
                    <article class="tw-result"><i>◉</i><h3>Greater Sales visibility</h3><p>Sales could see campaign status without chasing individual team members and could respond from Outlook or the mobile application while away from a desk.</p></article>
                    <article class="tw-result"><i>⇄</i><h3>Stronger continuity</h3><p>Project-level tasks, files, and discussion made it easier for backup employees to understand what was complete, what remained, and what to do next.</p></article>
                  </div>
                </section>
                <section class="tw-reflection">
                  <article><small>Impact</small><h3>A shared operational record</h3><p>The implementation replaced fragmented campaign conversations with a transparent workspace that connected status, assignments, assets, and decisions.</p></article>
                  <article><small>What I learned</small><h3>Adoption is part of system design</h3><p>Project-management software improves collaboration only when the workflow is clear and every team completes its part. Training and reinforcement were as important as configuration.</p></article>
                  <article><small>What I would revisit</small><h3>Automate visibility, not extra administration</h3><p>I would explore a low-maintenance way to automate board-level reporting and adoption measures. I intentionally avoided the manual boards feature because its upkeep added work without improving the core handoff.</p></article>
                </section>
                <p class="tw-disclosure">This was a collaborative, company-wide initiative. My title reflects market-level workflow leadership, configuration, testing, training, and adoption—not sole ownership of the enterprise implementation.</p>
              </main>
              <a class="tw-back" href="/" target="_self">&larr; Back to portfolio</a>
            </div>
        """
    )
    markup = "\n".join(line.lstrip() for line in markup.splitlines())
    st.markdown(_STYLES + markup, unsafe_allow_html=True)


if __name__ == "__main__":
    render_teamwork_implementation_case_study()
