from __future__ import annotations

import html
from textwrap import dedent

import streamlit as st


def _safe(value: object) -> str:
    return html.escape(str(value))


_ICON_PATHS = {
    "alert": '<path d="M21.7 18 13.9 4.5a2.2 2.2 0 0 0-3.8 0L2.3 18A2 2 0 0 0 4 21h16a2 2 0 0 0 1.7-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "briefcase": '<rect width="18" height="14" x="3" y="7" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M12 12v.01"/>',
    "calendar": '<path d="M8 2v4"/><path d="M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    "car": '<path d="m5 17-1 2"/><path d="m19 17 1 2"/><path d="M5 9l2-4h10l2 4"/><path d="M3 12a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v5H3v-5Z"/><path d="M7 13h.01"/><path d="M17 13h.01"/>',
    "chart": '<path d="M3 3v18h18"/><path d="m7 16 4-5 4 3 5-7"/>',
    "check": '<path d="M22 11.1V12a10 10 0 1 1-5.9-9.1"/><path d="m9 11 3 3L22 4"/>',
    "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5"/><path d="M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20"/><path d="M12 2a15 15 0 0 0 0 20"/>',
    "growth": '<path d="M3 3v18h18"/><path d="m7 14 4-4 4 4 6-7"/><path d="M15 7h6v6"/>',
    "lightbulb": '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M8.5 14.5A6 6 0 1 1 15.5 14.5C14.6 15.3 14 16.4 14 18h-4c0-1.6-.6-2.7-1.5-3.5Z"/>',
    "map": '<path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
    "megaphone": '<path d="m3 11 18-5v12L3 14v-3Z"/><path d="M11.6 16.9 13 22H7l-1.3-7"/>',
    "money": '<circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 18V6"/>',
    "monitor": '<rect width="20" height="14" x="2" y="3" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/>',
    "mouse": '<rect width="14" height="20" x="5" y="2" rx="7"/><path d="M12 6v4"/>',
    "network": '<circle cx="12" cy="5" r="3"/><circle cx="5" cy="19" r="3"/><circle cx="19" cy="19" r="3"/><path d="m10.5 7.5-4 8"/><path d="m13.5 7.5 4 8"/><path d="M8 19h8"/>',
    "pause": '<circle cx="12" cy="12" r="10"/><path d="M9 9v6"/><path d="M15 9v6"/>',
    "pie": '<path d="M21.2 15.9A10 10 0 1 1 8.1 2.8"/><path d="M12 2v10h10A10 10 0 0 0 12 2Z"/>',
    "play": '<circle cx="12" cy="12" r="10"/><path d="m10 8 6 4-6 4Z"/>',
    "plus": '<path d="M5 12h14"/><path d="M12 5v14"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-8 9-4.5-1.5-8-4-8-9V5l8-3 8 3v8Z"/><path d="m9 12 2 2 4-4"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9"/><path d="M16 3.1a4 4 0 0 1 0 7.8"/>',
}


def _icon(name: str, *, class_name: str = "") -> str:
    return (
        f'<svg class="{_safe(class_name)}" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.9" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{_ICON_PATHS[name]}</svg>'
    )


_BASE_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@500;600;700;800&display=swap');
[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppDeployButton"], .stAppDeployButton { display: none !important; }
#MainMenu, footer { visibility: hidden; }
[data-testid="stSidebar"] { background: #13231f; }
[data-testid="stSidebar"] * { color: rgba(255,255,255,.88) !important; }
.block-container { max-width: 1280px; padding: 1.6rem 1.25rem 4rem; }
.cs-shell, .cs-shell * { box-sizing: border-box; }
.cs-shell { color: var(--ink); font-family: "DM Sans", sans-serif; }
.cs-shell h1, .cs-shell h2, .cs-shell h3, .cs-shell p { margin-block-start: 0; }
.cs-shell h1, .cs-shell h2, .cs-shell h3 { color: inherit !important; font-family: "Manrope", sans-serif !important; }
.cs-sitebar { align-items: center; display: flex; justify-content: space-between; margin: 0 auto 1.25rem; max-width: 1180px; }
.cs-sitebrand { align-items: center; color: var(--ink) !important; display: flex; font-size: .85rem; font-weight: 800; gap: .65rem; letter-spacing: .08em; text-decoration: none !important; text-transform: uppercase; }
.cs-sitebrand i { align-items: center; background: var(--deep); border-radius: 50%; color: #fff; display: inline-flex; font-style: normal; height: 2.1rem; justify-content: center; width: 2.1rem; }
.cs-category { color: var(--accent); font-family: "Manrope", sans-serif; font-size: clamp(1.25rem,2.4vw,1.8rem); font-weight: 700; }
.cs-flight-row { align-items: center; color: var(--muted); display: flex; font-size: .7rem; font-weight: 850; gap: .55rem; justify-content: flex-end; letter-spacing: .07em; margin: .7rem .15rem 0; text-transform: uppercase; }
.cs-flight-row strong { background: var(--soft); border: 1px solid var(--line); border-radius: 999px; color: var(--ink); padding: .38rem .62rem; }
.cs-wrap { margin: 0 auto; max-width: 1180px; }
.cs-hero { background: var(--deep); border-radius: var(--hero-radius); color: #fff; display: grid; gap: 2rem; grid-template-columns: 1.25fr .75fr; overflow: hidden; padding: clamp(2rem,5vw,4rem); position: relative; }
.cs-hero::after { background: var(--glow); border-radius: 50%; content: ""; height: 320px; opacity: .13; position: absolute; right: -110px; top: -145px; width: 320px; }
.cs-kicker, .cs-label { color: var(--highlight); font-size: clamp(.86rem,1.5vw,1.08rem); font-weight: 800; letter-spacing: .065em; text-transform: uppercase; }
.cs-hero h1 { font-size: clamp(2.9rem,6vw,5.2rem); font-weight: 700; letter-spacing: -.065em; line-height: .98; margin: .9rem 0 1.2rem; }
.cs-hero h1 em { color: var(--highlight); font-style: normal; }
.cs-hero-copy > p { color: var(--hero-copy); font-size: clamp(1.05rem,2vw,1.28rem); line-height: 1.55; margin: 0; max-width: 760px; }
.cs-hero-metric { align-items: center; display: flex; flex-direction: column; justify-content: center; position: relative; text-align: center; z-index: 1; }
.cs-hero-metric strong { color: var(--highlight); font-family: "Manrope", sans-serif; font-size: clamp(4.4rem,10vw,8rem); font-weight: 700; letter-spacing: -.085em; line-height: .85; }
.cs-hero-metric span { font-size: 1.2rem; font-weight: 700; margin-top: 1.05rem; }
.cs-hero-metric small { color: var(--hero-muted); font-size: .92rem; margin-top: .55rem; }
.cs-ring { align-items: center; background: conic-gradient(var(--highlight) 0 var(--ring), rgba(255,255,255,.13) var(--ring)); border-radius: 50%; display: flex; height: 210px; justify-content: center; position: relative; width: 210px; }
.cs-ring::after { background: var(--deep); border-radius: 50%; content: ""; height: 148px; position: absolute; width: 148px; }
.cs-ring > div { position: relative; z-index: 1; }
.cs-ring strong { display: block; font-size: 3.4rem; }
.cs-kpis { display: grid; gap: .8rem; grid-template-columns: repeat(var(--kpi-count),1fr); margin: .8rem 0; }
.cs-kpis article, .cs-card { background: var(--surface); border: 1px solid var(--line); box-shadow: 0 12px 30px var(--shadow); }
.cs-kpis article { align-items: center; border-radius: var(--card-radius); display: flex; gap: 1rem; min-height: 142px; padding: 1.3rem; }
.cs-icon-bubble { align-items: center; background: var(--soft); border-radius: var(--icon-radius); color: var(--accent); display: flex; flex: 0 0 auto; height: 58px; justify-content: center; width: 58px; }
.cs-icon-bubble svg { height: 29px; width: 29px; }
.cs-kpis strong { display: block; font-family: "Manrope",sans-serif; font-size: clamp(1.55rem,2.5vw,2rem); line-height: 1; }
.cs-kpis p { color: var(--ink); font-size: .99rem; font-weight: 700; line-height: 1.35; margin: .45rem 0 0; }
.cs-kpis small { color: var(--muted); display: block; font-size: .86rem; line-height: 1.35; margin-top: .3rem; }
.cs-grid-2 { display: grid; gap: .8rem; grid-template-columns: .92fr 1.08fr; }
.cs-card { border-radius: var(--card-radius); padding: clamp(1.4rem,3vw,2rem); }
.cs-card-heading { align-items: center; display: flex; gap: .85rem; margin-bottom: 1.35rem; }
.cs-card-heading > span { align-items: center; background: var(--accent-gradient); border-radius: var(--icon-radius); color: #fff; display: flex; flex: 0 0 auto; height: 58px; justify-content: center; width: 58px; }
.cs-card-heading svg { height: 29px; width: 29px; }
.cs-card-heading small, .cs-section-heading small, .cs-contribution small, .cs-takeaway small { color: var(--accent); display: block; font-size: 1rem; font-weight: 800; letter-spacing: .055em; text-transform: uppercase; }
.cs-card-heading h2, .cs-section-heading h2, .cs-contribution h2 { font-size: clamp(1.55rem,3vw,2.2rem); font-weight: 650; letter-spacing: -.04em; line-height: 1.1; margin: .25rem 0 0; }
.cs-list { display: grid; gap: .6rem; }
.cs-list > div { align-items: center; background: var(--bg); border-radius: 12px; display: grid; gap: .85rem; grid-template-columns: 44px 1fr; padding: .9rem; }
.cs-list svg { color: var(--accent); height: 27px; justify-self: center; width: 27px; }
.cs-list p { margin: 0; }
.cs-list strong, .cs-list span { display: block; }
.cs-list strong { font-size: 1.08rem; }
.cs-list span { color: var(--muted); font-size: .98rem; line-height: 1.45; margin-top: .25rem; }
.cs-steps { display: grid; gap: .6rem; grid-template-columns: repeat(3,1fr); }
.cs-steps > div { border-left: 3px solid var(--accent); min-height: 225px; padding: .35rem .8rem 1rem 1rem; }
.cs-steps > div:nth-child(2) { border-color: var(--deep); }
.cs-steps > div:nth-child(3) { border-color: var(--highlight); }
.cs-steps .cs-icon-bubble { margin-bottom: .9rem; }
.cs-steps strong { font-size: 1.08rem; }
.cs-steps p { color: var(--muted); font-size: .98rem; line-height: 1.5; margin: .45rem 0 0; }
.cs-full { margin-top: .8rem; }
.cs-audience-layout { align-items: center; display: grid; gap: 2rem; grid-template-columns: 200px 1fr; }
.cs-donut { align-items: center; background: conic-gradient(var(--accent) 0 50%, var(--line) 50%); border-radius: 50%; display: flex; height: 156px; justify-content: center; margin: auto; position: relative; width: 156px; }
.cs-donut::after { background: var(--surface); border-radius: 50%; content: ""; height: 100px; position: absolute; width: 100px; }
.cs-donut div { position: relative; text-align: center; z-index: 1; }
.cs-donut strong { display: block; font-family: "Manrope",sans-serif; font-size: 2.15rem; }
.cs-donut span { color: var(--muted); }
.cs-donut-note { color: var(--muted); font-size: .95rem; line-height: 1.45; margin-top: .8rem; text-align: center; }
.cs-chip-grid { display: grid; gap: .6rem; grid-template-columns: repeat(3,1fr); }
.cs-chip { align-items: center; background: var(--bg); border-radius: 11px; display: flex; gap: .75rem; min-height: 72px; padding: .8rem; }
.cs-chip svg { color: var(--deep); flex: 0 0 auto; height: 27px; width: 27px; }
.cs-chip strong, .cs-chip small { display: block; }
.cs-chip strong { font-size: .98rem; }
.cs-chip small { color: var(--muted); font-size: .86rem; line-height: 1.35; margin-top: .2rem; }
.cs-chip.wide { background: var(--soft); grid-column: 1/-1; }
.cs-dark { background: var(--deep); border-radius: var(--section-radius); color: #fff; margin-top: .8rem; padding: clamp(1.6rem,4vw,2.5rem); }
.cs-dark .cs-section-heading small { color: var(--highlight); }
.cs-dark .cs-section-heading h2 { color: #fff !important; margin: .35rem 0 1.4rem; }
.cs-channel-grid { align-items: stretch; display: grid; gap: .7rem; grid-template-columns: repeat(var(--channel-count),1fr); }
.cs-channel-grid article { background: rgba(255,255,255,.075); border: 1px solid rgba(255,255,255,.15); border-radius: 13px; min-height: 190px; padding: 1.25rem; }
.cs-channel-grid svg { color: var(--highlight); height: 31px; width: 31px; }
.cs-channel-grid strong { display: block; font-size: 1.16rem; margin: .75rem 0 .4rem; }
.cs-channel-grid p { color: var(--hero-copy); font-size: .96rem; line-height: 1.5; margin: 0; }
.cs-measurement { display: grid; gap: .6rem; grid-template-columns: repeat(3,1fr); margin-top: .9rem; }
.cs-measurement span { align-items: center; background: rgba(255,255,255,.08); border-radius: 10px; display: flex; gap: .55rem; justify-content: center; min-height: 52px; }
.cs-measurement svg { color: var(--highlight); height: 22px; width: 22px; }
.cs-bars { display: grid; gap: .85rem; }
.cs-bars > div { align-items: center; display: grid; gap: .7rem; grid-template-columns: 150px 1fr 70px; }
.cs-bars span { font-size: .92rem; font-weight: 700; }
.cs-bars i { background: var(--soft); border-radius: 999px; display: block; height: 14px; overflow: hidden; }
.cs-bars b { background: var(--bar-gradient); border-radius: inherit; display: block; height: 100%; }
.cs-bars strong { color: var(--accent); font-size: .76rem; text-align: right; text-transform: uppercase; }
.cs-note { background: var(--soft); border-left: 4px solid var(--accent); border-radius: 6px; color: var(--muted); font-size: .92rem; line-height: 1.5; margin: 1rem 0 0; padding: .8rem 1rem; }
.cs-flow { align-items: stretch; display: grid; gap: .75rem; grid-template-columns: 1fr 36px 1fr 36px 1fr; }
.cs-flow article { background: var(--bg); border: 1px solid var(--line); border-radius: 13px; min-height: 165px; padding: 1.25rem; }
.cs-flow > svg { align-self: center; color: var(--accent); height: 27px; width: 27px; }
.cs-flow article > div { align-items: center; color: var(--accent); display: flex; gap: .6rem; min-height: 48px; }
.cs-flow article > div strong { font-family: "Manrope",sans-serif; font-size: 2.6rem; }
.cs-flow article > div svg { height: 35px; width: 35px; }
.cs-flow article > div span { font-size: 1.05rem; font-weight: 800; }
.cs-flow article p { color: var(--muted); font-size: .94rem; line-height: 1.48; margin: .7rem 0 0; }
.auto-diagnostic-flow { align-items: stretch; display: grid; gap: .75rem; grid-template-columns: 1fr 36px 1fr; }
.auto-diagnostic-flow > article { background: var(--bg); border: 1px solid var(--line); border-radius: 13px; min-height: 185px; padding: 1.2rem; }
.auto-diagnostic-flow > svg { align-self: center; color: var(--accent); height: 27px; width: 27px; }
.auto-diagnostic-flow article > div { align-items: center; color: var(--accent); display: flex; gap: .65rem; }
.auto-diagnostic-flow article > div svg { height: 31px; width: 31px; }
.auto-diagnostic-flow article > div strong { font-size: 1.08rem; }
.auto-diagnostic-flow article p { color: var(--muted); font-size: .94rem; line-height: 1.48; margin: .9rem 0; }
.auto-diagnostic-flow article > span { color: var(--accent); font-size: .82rem; font-weight: 800; }
.auto-performance-row { align-items: stretch; display: grid; gap: .8rem; grid-template-columns: 1.3fr .7fr; }
.auto-vdp-compare { align-items: center; background: rgba(255,255,255,.075); border: 1px solid rgba(255,255,255,.15); border-radius: 13px; display: grid; gap: 1rem; grid-template-columns: 1fr 34px 1fr; padding: 1.25rem; }
.auto-vdp-compare > svg { color: var(--highlight); height: 27px; width: 27px; }
.auto-vdp-compare span, .auto-vdp-compare small { display: block; }
.auto-vdp-compare span { color: var(--highlight); font-size: .82rem; font-weight: 800; text-transform: uppercase; }
.auto-vdp-compare strong { display: block; font-family: "Manrope",sans-serif; font-size: 3rem; margin: .3rem 0; }
.auto-vdp-compare small { color: var(--hero-copy); font-size: .85rem; }
.auto-vdp-compare i { background: rgba(255,255,255,.14); border-radius: 999px; display: block; height: 11px; margin-top: .8rem; overflow: hidden; }
.auto-vdp-compare b { background: linear-gradient(90deg,var(--accent),var(--highlight)); border-radius: inherit; display: block; height: 100%; }
.auto-lift { align-items: center; background: var(--accent); border-radius: 13px; display: flex; flex-direction: column; justify-content: center; min-height: 210px; padding: 1.2rem; text-align: center; }
.auto-lift svg { height: 34px; width: 34px; }
.auto-lift strong { font-family: "Manrope",sans-serif; font-size: 3.2rem; line-height: 1; margin-top: .45rem; }
.auto-lift span { font-size: 1rem; font-weight: 800; }
.auto-lift small { color: rgba(255,255,255,.84); margin-top: .45rem; }
.auto-timeline-row { align-items: stretch; display: grid; gap: .55rem; grid-template-columns: 1fr 25px 1fr 25px 1fr 25px 1fr; }
.auto-timeline-row > article { background: var(--bg); border-radius: 12px; min-height: 145px; padding: 1rem; }
.auto-timeline-row > svg { align-self: center; color: var(--accent); height: 23px; width: 23px; }
.auto-timeline-row article span { color: var(--accent); display: block; font-size: .75rem; font-weight: 850; text-transform: uppercase; }
.auto-timeline-row article strong { display: block; font-family: "Manrope",sans-serif; font-size: 1.5rem; margin-top: .7rem; }
.auto-timeline-row article p { color: var(--muted); font-size: .86rem; line-height: 1.4; margin: .35rem 0 0; }
.auto-timeline-row article:last-child { background: var(--accent); color: white; }
.auto-timeline-row article:last-child span, .auto-timeline-row article:last-child p { color: white; }
.cs-market { align-items: center; display: grid; gap: 1.2rem; grid-template-columns: .75fr 48px 1.25fr; }
.cs-market > svg { color: var(--accent); height: 34px; justify-self: center; width: 34px; }
.cs-market-origin { align-items: center; background: var(--accent-gradient); border-radius: var(--card-radius); color: #fff; display: flex; flex-direction: column; justify-content: center; min-height: 145px; padding: 1.25rem; text-align: center; }
.cs-market-origin svg { height: 32px; width: 32px; }
.cs-market-origin strong { font-size: 1.5rem; margin-top: .5rem; }
.cs-market-origin span { color: rgba(255,255,255,.78); font-size: .9rem; margin-top: .3rem; }
.cs-market-destinations { display: grid; gap: .65rem; grid-template-columns: repeat(2,1fr); }
.cs-market-destinations article { align-items: center; background: var(--soft); border-radius: 13px; display: flex; gap: .8rem; min-height: 110px; padding: 1rem; }
.cs-market-destinations svg { color: var(--accent); height: 28px; width: 28px; }
.cs-market-destinations strong, .cs-market-destinations span { display: block; }
.cs-market-destinations span { color: var(--muted); font-size: .9rem; margin-top: .25rem; }
.cs-bottom { display: grid; gap: .8rem; grid-template-columns: 1.25fr .75fr; margin-top: .8rem; }
.cs-contribution, .cs-takeaway { border-radius: var(--card-radius); padding: 1.7rem; }
.cs-contribution { align-items: center; background: var(--surface); border: 1px solid var(--line); display: grid; gap: 1.5rem; grid-template-columns: .75fr 1.25fr; }
.cs-contribution h2 { font-size: clamp(1.35rem,2.4vw,1.85rem); margin: .4rem 0 0; }
.cs-capabilities { display: grid; gap: .5rem; grid-template-columns: repeat(2,1fr); }
.cs-capabilities span { align-items: center; background: var(--soft); border-radius: 10px; color: var(--deep); display: flex; font-size: .9rem; justify-content: center; min-height: 46px; padding: .55rem; text-align: center; }
.cs-takeaway { align-items: center; background: var(--highlight); color: var(--deep); display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cs-takeaway > svg { height: 40px; margin-bottom: .7rem; width: 40px; }
.cs-takeaway small { color: var(--deep); }
.cs-takeaway > p { font-family: "Manrope",sans-serif; font-size: clamp(1.18rem,2.3vw,1.55rem); line-height: 1.4; margin: .85rem 0 0; }
.cs-next { border-top: 1px solid rgba(20,45,50,.25); margin-top: 1.1rem; padding-top: 1rem; }
.cs-next strong { font-size: .82rem; letter-spacing: .05em; text-transform: uppercase; }
.cs-next p { font-size: .92rem; line-height: 1.5; margin: .45rem 0 0; }
.cs-disclosure { color: var(--muted); font-size: .82rem; line-height: 1.55; margin: 1.25rem auto .8rem; max-width: 1000px; text-align: center; }
.cs-back { color: var(--deep) !important; display: block; font-weight: 800; margin-top: 1.2rem; text-align: center; text-decoration: none !important; }
@media (max-width: 900px) {
  .cs-hero, .cs-grid-2, .cs-bottom { grid-template-columns: 1fr; }
  .cs-hero-metric { align-items: flex-start; text-align: left; }
  .cs-kpis { grid-template-columns: repeat(2,1fr); }
  .cs-channel-grid { grid-template-columns: repeat(2,1fr); }
  .cs-contribution { grid-template-columns: 1fr; }
}
@media (max-width: 680px) {
  .block-container { padding: 1rem .7rem 3rem; }
  .cs-category { display: none; }
  .cs-hero h1 { font-size: 2.9rem; }
  .cs-kpis, .cs-steps, .cs-chip-grid, .cs-channel-grid, .cs-measurement, .cs-market-destinations, .cs-capabilities { grid-template-columns: 1fr; }
  .cs-audience-layout, .cs-flow, .cs-market { grid-template-columns: 1fr; }
  .cs-flow > svg, .cs-market > svg, .auto-diagnostic-flow > svg, .auto-timeline-row > svg { justify-self: center; transform: rotate(90deg); }
  .auto-diagnostic-flow, .auto-performance-row, .auto-vdp-compare, .auto-timeline-row { grid-template-columns: 1fr; }
  .auto-vdp-compare > svg { justify-self: center; transform: rotate(90deg); }
  .cs-steps > div { min-height: 0; }
  .cs-bars > div { grid-template-columns: 112px 1fr; }
  .cs-bars strong { display: none; }
}
</style>
"""


_GALLERY_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@600;700;800&display=swap');
[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppDeployButton"], .stAppDeployButton { display: none !important; }
#MainMenu, footer { visibility: hidden; }
[data-testid="stSidebar"] { background: #13231f; }
[data-testid="stSidebar"] * { color: rgba(255,255,255,.88) !important; }
.stApp { background: radial-gradient(circle at 94% 6%, rgba(201,242,223,.72),transparent 28rem),linear-gradient(180deg,#fbfcf8,#f6f8f3); }
.block-container { max-width: 1160px; padding-top: 2rem; padding-bottom: 5rem; }
.gallery, .gallery * { box-sizing: border-box; }
.gallery { color: #13231f; font-family: "DM Sans",sans-serif; }
.gallery-top { align-items: center; display: flex; justify-content: space-between; margin-bottom: 4.8rem; }
.gallery-brand { align-items: center; display: flex; font-size: .9rem; font-weight: 800; gap: .65rem; letter-spacing: .08em; text-transform: uppercase; }
.gallery-brand i { align-items: center; background:#13231f; border-radius:50%; color:white; display:flex; font-style:normal; height:2rem; justify-content:center; width:2rem; }
.gallery-status { background:rgba(255,255,255,.75); border:1px solid rgba(19,35,31,.12); border-radius:999px; color:#60706b; font-size:.8rem; font-weight:700; padding:.55rem .85rem; }
.gallery-eyebrow { color:#ff6b4a; font-size:.78rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase; }
.gallery h1 { color:#13231f !important; font-family:"Manrope",sans-serif !important; font-size:clamp(3rem,7vw,6rem); font-weight:800; letter-spacing:-.07em; line-height:.94; margin:1rem 0 1.35rem; }
.gallery-intro { color:#60706b; font-size:1.14rem; line-height:1.7; max-width:760px; }
.gallery-grid { display:grid; gap:1rem; grid-template-columns:repeat(3,1fr); margin-top:3rem; }
.gallery-card { background:white; border:1px solid rgba(19,35,31,.12); border-radius:26px; box-shadow:0 16px 50px rgba(19,35,31,.07); color:inherit !important; display:block; min-height:480px; overflow:hidden; padding:2rem; position:relative; text-decoration:none !important; transition:transform .2s ease,box-shadow .2s ease; }
.gallery-card:hover { box-shadow:0 22px 65px rgba(19,35,31,.13); transform:translateY(-5px); }
.gallery-card.health { --c:#2d7691; --d:#123e4b; --s:#dcebed; }
.gallery-card.tech { --c:#6d39db; --d:#0b1f3a; --s:#e9f0ff; }
.gallery-card.auto { --c:#f07832; --d:#1b262b; --s:#e3e9eb; }
.gallery-card::before { background:var(--d); content:""; height:11px; inset:0 0 auto; position:absolute; }
.gallery-card-head { align-items:center; display:flex; justify-content:space-between; margin-top:.4rem; }
.gallery-category { color:var(--c); font-size:.78rem; font-weight:800; letter-spacing:.1em; text-transform:uppercase; }
.gallery-icon { align-items:center; background:var(--s); border-radius:16px; color:var(--d); display:flex; height:58px; justify-content:center; width:58px; }
.gallery-icon svg { height:29px; width:29px; }
.gallery-metric { color:var(--d); font-family:"Manrope",sans-serif; font-size:clamp(3rem,5vw,4.6rem); font-weight:800; letter-spacing:-.07em; line-height:.92; margin:2.3rem 0 .7rem; }
.gallery-card h2 { color:#13231f !important; font-family:"Manrope",sans-serif !important; font-size:1.55rem; letter-spacing:-.035em; line-height:1.15; margin:0 0 1rem; }
.gallery-card p { color:#60706b; font-size:.98rem; line-height:1.65; }
.gallery-tags { display:flex; flex-wrap:wrap; gap:.45rem; margin-top:1.35rem; }
.gallery-tags span { background:var(--s); border-radius:999px; color:var(--d); font-size:.77rem; font-weight:700; padding:.43rem .68rem; }
.gallery-open { bottom:1.8rem; color:var(--d); font-size:.88rem; font-weight:800; position:absolute; }
.gallery-note { border-top:1px solid rgba(19,35,31,.12); color:#60706b; font-size:.9rem; line-height:1.6; margin-top:3.5rem; padding-top:1.2rem; }
@media(max-width:980px){.gallery-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.block-container{padding:1.2rem 1rem 3rem}.gallery-top{margin-bottom:3.5rem}.gallery-status{display:none}.gallery-grid{grid-template-columns:1fr}.gallery-card{min-height:450px}}
</style>
"""


def _render_gallery() -> None:
    health_icon = _icon("target")
    tech_icon = _icon("network")
    auto_icon = _icon("car")
    st.markdown(
        _GALLERY_STYLES
        + dedent(f"""
        <div class="gallery">
          <div class="gallery-top">
            <div class="gallery-brand"><i>&#10022;</i> L.C. Felton</div>
            <div class="gallery-status">Campaign strategy portfolio</div>
          </div>
          <div class="gallery-eyebrow">Selected campaign work</div>
          <h1>Case studies built around the decisions that drove results.</h1>
          <p class="gallery-intro">Explore how I translated business objectives into audience, channel, budget, measurement, and optimization strategies across different industries and constraints.</p>
          <section class="gallery-grid">
            <a class="gallery-card health" href="/Case_Studies?case=ent-physician" target="_self">
              <div class="gallery-card-head"><span class="gallery-category">Healthcare</span><span class="gallery-icon">{health_icon}</span></div>
              <div class="gallery-metric">1,139</div>
              <h2>Appointments for an ENT physician campaign</h2>
              <p>A cross-channel strategy helped a regional healthcare system reverse declining appointment volume despite restrictions on health-related targeting.</p>
              <div class="gallery-tags"><span>Audience strategy</span><span>Meta Ads</span><span>Programmatic</span><span>Measurement</span></div>
              <span class="gallery-open">Open case study &rarr;</span>
            </a>
            <a class="gallery-card tech" href="/Case_Studies?case=cloud-services-cybersecurity" target="_self">
              <div class="gallery-card-head"><span class="gallery-category">B2B Technology</span><span class="gallery-icon">{tech_icon}</span></div>
              <div class="gallery-metric">23%</div>
              <h2>Increase in booked appointments</h2>
              <p>A seven-month regional campaign used current intent signals and disciplined geographic allocation to grow cloud-services and cybersecurity demand.</p>
              <div class="gallery-tags"><span>Market strategy</span><span>DV360</span><span>YouTube</span><span>Streaming / CTV</span></div>
              <span class="gallery-open">Open case study &rarr;</span>
            </a>
            <a class="gallery-card auto" href="/Case_Studies?case=used-car-sales" target="_self">
              <div class="gallery-card-head"><span class="gallery-category">Automotive</span><span class="gallery-icon">{auto_icon}</span></div>
              <div class="gallery-metric">88%</div>
              <h2>Of available inventory sold in 62 days</h2>
              <p>A focused VIN Marketing strategy combined vehicle-level analysis, stronger VDPs, and disciplined budget acceleration to move aging inventory.</p>
              <div class="gallery-tags"><span>VIN strategy</span><span>VDP optimization</span><span>Budget pacing</span><span>Client counsel</span></div>
              <span class="gallery-open">Open case study &rarr;</span>
            </a>
          </section>
          <p class="gallery-note">Client identities and selected identifying details are intentionally withheld. Results and attribution notes are disclosed within each case study.</p>
        </div>
        """),
        unsafe_allow_html=True,
    )


def _render_ent() -> None:
    def bubble(name: str) -> str:
        return f'<span class="cs-icon-bubble">{_icon(name)}</span>'

    st.markdown(
        _BASE_STYLES
        + dedent(f"""
        <div class="cs-shell" style="--bg:#f3f0e8;--surface:#fffefa;--soft:#dcebed;--ink:#172f38;--muted:#5b6e73;--line:#cbd9da;--deep:#123e4b;--accent:#2d7691;--highlight:#9fd3c7;--glow:#9fd3c7;--hero-copy:#d5e5e7;--hero-muted:#b7cdd1;--shadow:rgba(18,62,75,.08);--accent-gradient:#2d7691;--bar-gradient:linear-gradient(90deg,#2d7691,#9fd3c7);--hero-radius:28px 8px 28px 8px;--card-radius:19px 6px 19px 6px;--section-radius:20px 6px 20px 6px;--icon-radius:50%;--kpi-count:3;--channel-count:3;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/Case_Studies" target="_self"><i>CS</i> Portfolio case study</a><span class="cs-category">Healthcare</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">Client-reported campaign outcome</span><h1><em>1,139 appointments</em></h1><p>A cross-channel campaign for an Ear, Nose &amp; Throat physician helped a regional healthcare system reverse declining appointment volume despite restrictions on health-related audience targeting.</p></div>
              <div class="cs-hero-metric"><strong>10&times;<sup>+</sup></strong><span>typical appointment volume</span><small>Reported by the client</small></div>
            </section>
            <section class="cs-kpis">
              <article>{bubble('calendar')}<div><strong>45 days</strong><p>Into a planned three-month test</p></div></article>
              <article>{bubble('pause')}<div><strong>Paused early</strong><p>Demand exceeded physician capacity</p></div></article>
              <article>{bubble('map')}<div><strong>25-mile radius</strong><p>Centered on the physician's office</p></div></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The challenge</small><h2>A constrained path to growth</h2></div></div><div class="cs-list">
                <div>{_icon('growth')}<p><strong>Declining volume</strong><span>Appointments were down quarter over quarter.</span></p></div>
                <div>{_icon('map')}<p><strong>Location competition</strong><span>A second ENT location in the system was performing better.</span></p></div>
                <div>{_icon('shield')}<p><strong>Targeting limits</strong><span>Health-condition audiences were unavailable in Meta Ads.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('lightbulb')}</span><div><small>The strategy</small><h2>Research became the targeting advantage</h2></div></div><div class="cs-steps">
                <div>{bubble('search')}<strong>Research</strong><p>Mapped patient needs through life stage, lifestyle, profession, and caregiving.</p></div>
                <div>{bubble('network')}<strong>Architecture</strong><p>Combined Meta Ads and programmatic capabilities instead of relying on one platform.</p></div>
                <div>{bubble('chart')}<strong>Measurement</strong><p>Required conversion tracking, testing, and performance monitoring from launch.</p></div>
              </div></article>
            </section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('users')}</span><div><small>Audience architecture</small><h2>Multiple paths to one patient journey</h2></div></div><div class="cs-audience-layout">
              <div><div class="cs-donut"><div><strong>45</strong><span>days</span></div></div><div class="cs-donut-note">About halfway through<br>the planned test window</div></div>
              <div class="cs-chip-grid">
                <div class="cs-chip">{_icon('users')}<strong>Parents</strong></div><div class="cs-chip">{_icon('users')}<strong>Caregivers</strong></div><div class="cs-chip">{_icon('users')}<strong>Older adults</strong></div>
                <div class="cs-chip">{_icon('target')}<strong>Active lifestyles</strong></div><div class="cs-chip">{_icon('target')}<strong>Voice professionals</strong></div><div class="cs-chip">{_icon('search')}<strong>Lookalikes + retargeting</strong></div>
                <div class="cs-chip wide">{_icon('database')}<div><strong>Vetted third-party health data</strong><small>HIPAA-compliant medical-condition and health-related audience segments</small></div></div>
              </div>
            </div></section>
            <section class="cs-dark"><div class="cs-section-heading"><small>Channel architecture</small><h2>Different jobs. One patient journey.</h2></div><div class="cs-channel-grid">
              <article>{_icon('megaphone')}<strong>Meta Ads</strong><p>Facebook and Instagram paid placements for awareness, audience testing, and retargeting</p></article>
              <article>{_icon('monitor')}<strong>Programmatic</strong><p>Vetted third-party health-data segments, lookalikes, and retargeting</p></article>
              <article>{_icon('mouse')}<strong>Measurement</strong><p>Website inquiries, appointment activity, and channel evaluation</p></article>
            </div></section>
            <section class="cs-bottom">
              <article class="cs-contribution"><div><small>My strategic contribution</small><h2>From business objective to measurable media plan.</h2></div><div class="cs-capabilities"><span>Overall strategy</span><span>Audience research</span><span>Campaign architecture</span><span>Media selection</span><span>Budget allocation</span><span>Measurement planning</span><span>Reporting &amp; analytics</span><span>Client communication</span><span>Performance oversight</span></div></article>
              <article class="cs-takeaway"><small>Strategic takeaway</small><p>When direct targeting narrows, research and channel architecture become the targeting strategy.</p><div class="cs-next"><strong>My recommendation</strong><p>I would have recommended maintaining the balanced channel and audience strategy, monitoring the older-adult segment's slight performance advantage, and coordinating additional scaling with the physician's appointment capacity.</p></div></article>
            </section>
            <p class="cs-disclosure">Client identity and selected details have been modified. Performance figures are client-reported totals during the campaign period and are not presented as appointments directly attributed to advertising.</p>
            <a class="cs-back" href="/Case_Studies" target="_self">&larr; Return to all case studies</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )


def _render_tech() -> None:
    def bubble(name: str) -> str:
        return f'<span class="cs-icon-bubble">{_icon(name)}</span>'

    contributions = [
        "Overall strategy", "Market analysis", "Budget allocation", "Audience research",
        "Channel architecture", "Intent-signal strategy", "Measurement planning",
        "Performance optimization", "Cross-market enablement",
    ]
    contribution_html = "".join(f"<span>{_safe(item)}</span>" for item in contributions)
    st.markdown(
        _BASE_STYLES
        + dedent(f"""
        <div class="cs-shell" style="--bg:#f2f5fa;--surface:#ffffff;--soft:#e9f0ff;--ink:#14243a;--muted:#5e6b7d;--line:#d5deea;--deep:#0b1f3a;--accent:#6d39db;--highlight:#59ddd3;--glow:#59ddd3;--hero-copy:#cbd7e8;--hero-muted:#cfdaea;--shadow:rgba(11,31,58,.07);--accent-gradient:linear-gradient(145deg,#2563eb,#7c3aed);--bar-gradient:linear-gradient(90deg,#2563eb,#59ddd3);--hero-radius:10px 30px 10px 30px;--card-radius:8px 22px 8px 22px;--section-radius:9px 24px 9px 24px;--icon-radius:14px;--kpi-count:4;--channel-count:4;--ring:23%;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/Case_Studies" target="_self"><i>CS</i> Portfolio case study</a><span class="cs-category">B2B Technology</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">Client-attributed regional outcome</span><h1><em>23%</em> increase in booked appointments</h1><p>A seven-month, $125,000 campaign increased combined online and phone-booked appointments across Virginia and Washington, D.C.&mdash;while the regional market generated nearly one-third of the company's national website traffic.</p></div>
              <div class="cs-hero-metric"><div class="cs-ring"><div><strong>23%</strong><span>more appointments</span></div></div><small>Compared with first-half 2022</small></div>
            </section>
            <section class="cs-kpis">
              <article>{bubble('globe')}<div><strong>31%</strong><p>Of national website traffic</p><small>Generated by the VA/DC market</small></div></article>
              <article>{bubble('growth')}<div><strong>49%</strong><p>Increase in website visits</p><small>Compared with first-half 2022</small></div></article>
              <article>{bubble('users')}<div><strong>7%</strong><p>Increase in webinar registrations</p><small>VA/DC market</small></div></article>
              <article>{bubble('money')}<div><strong>$125K</strong><p>Total campaign budget</p><small>June&ndash;December 2022</small></div></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The challenge</small><h2>Build a fresher path to B2B growth</h2></div></div><div class="cs-list">
                <div>{_icon('database')}<p><strong>No first-party lists</strong><span>Legal and data-use alignment prevented list activation.</span></p></div>
                <div>{_icon('mouse')}<p><strong>Limited conversion tracking</strong><span>A Meta pixel could not be installed.</span></p></div>
                <div>{_icon('globe')}<p><strong>Statewide scale</strong><span>A fixed budget had to cover Virginia and Washington, D.C.</span></p></div>
                <div>{_icon('briefcase')}<p><strong>Incumbent comparison</strong><span>The plan would be evaluated alongside a long-standing agency.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('pie')}</span><div><small>Geographic budget strategy</small><h2>Coverage first. Population second.</h2></div></div><p style="color:var(--muted);font-size:1rem;line-height:1.55;">I divided Virginia into regions, removed areas outside the service footprint, and weighted investment toward stronger population opportunities.</p><div class="cs-bars">
                <div><span>High-opportunity regions</span><i><b style="width:100%"></b></i><strong>Highest</strong></div><div><span>Growth regions</span><i><b style="width:72%"></b></i><strong>Scaled</strong></div><div><span>Rural regions</span><i><b style="width:38%"></b></i><strong>Reduced</strong></div><div><span>Unserved areas</span><i><b style="width:4%"></b></i><strong>Excluded</strong></div>
              </div><p class="cs-disclosure" style="margin-bottom:0;text-align:right;">Illustrates allocation logic&mdash;not actual spend percentages.</p></article>
            </section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('search')}</span><div><small>Intent architecture</small><h2>Current signals replaced an unavailable first-party advantage</h2></div></div><div class="cs-flow">
              <article><div><strong>~200</strong><span>starting signals</span></div><p>Cloud, storage, servers, networking, telecom, software, and business technology</p></article>{_icon('arrow')}<article><div>{_icon('target')}<span>Performance filter</span></div><p>Conversions, CTR of at least 0.18%, and stronger impression delivery</p></article>{_icon('arrow')}<article><div>{_icon('check')}<span>Focused list</span></div><p>Custom-intent signals demonstrating meaningful activity remained in market</p></article>
            </div><p class="cs-note"><strong>Important distinction:</strong> These were custom-intent signals in DV360 and YouTube&mdash;not paid Google Search Ads.</p></section>
            <section class="cs-dark"><div class="cs-section-heading"><small>Channel architecture</small><h2>Four channels. Four defined jobs.</h2></div><div class="cs-channel-grid">
              <article>{_icon('megaphone')}<strong>Meta Ads</strong><p>Job-title, interest, and behavior targeting using testimonial video, static, and carousel ads</p></article><article>{_icon('network')}<strong>DV360</strong><p>Custom intent, contextual business and technology placements, and site retargeting</p></article><article>{_icon('play')}<strong>YouTube</strong><p>Intent-driven video reach around business and technology information consumption</p></article><article>{_icon('monitor')}<strong>Streaming / CTV</strong><p>Top-of-funnel testimonial visibility with more deliberate frequency</p></article>
            </div><div class="cs-measurement"><span>{_icon('chart')}<strong>Client analytics</strong></span><span>{_icon('users')}<strong>Webinar reporting</strong></span><span>{_icon('monitor')}<strong>Call-center feedback</strong></span></div></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('network')}</span><div><small>Organizational impact</small><h2>A regional strategy became a repeatable playbook</h2></div></div><div class="cs-market"><article class="cs-market-origin">{_icon('map')}<strong>Virginia + D.C.</strong><span>Built and optimized</span></article>{_icon('arrow')}<div class="cs-market-destinations"><article>{_icon('briefcase')}<p><strong>Rhode Island</strong><span>Strategy walkthrough delivered</span></p></article><article>{_icon('briefcase')}<p><strong>Oklahoma</strong><span>Campaign plan shared</span></p></article></div></div><p style="color:var(--muted);font-size:.98rem;line-height:1.55;margin:1rem 0 0;text-align:center;">The campaign approach was shared with other Cox Media teams, demonstrating that the strategy was useful beyond a single market.</p></section>
            <section class="cs-bottom"><article class="cs-contribution"><div><small>My strategic contribution</small><h2>From service footprint to scalable market playbook.</h2></div><div class="cs-capabilities">{contribution_html}</div></article><article class="cs-takeaway">{_icon('shield')}<small>Strategic takeaway</small><p>Clear channel roles, current intent signals, and disciplined geographic allocation can overcome major data and tracking limitations.</p></article></section>
            <p class="cs-disclosure">Client identity and selected identifying details have been modified. Performance figures are client-attributed market-level outcomes reported through the client's analytics, webinar, appointment, and internal reporting systems. The approximate Meta Ads CTR is intentionally omitted from headline results because the retained format-level definition is unavailable.</p>
            <a class="cs-back" href="/Case_Studies" target="_self">&larr; Return to all case studies</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )


def _render_auto() -> None:
    def bubble(name: str) -> str:
        return f'<span class="cs-icon-bubble">{_icon(name)}</span>'

    contributions = [
        "Overall strategy", "Inventory analysis", "Channel prioritization",
        "VDP conversion strategy", "Pricing counsel", "Budget acceleration",
        "Reporting & analytics", "Client communication",
    ]
    contribution_html = "".join(f"<span>{_safe(item)}</span>" for item in contributions)
    st.markdown(
        _BASE_STYLES
        + dedent(f"""
        <div class="cs-shell" style="--bg:#f2f0eb;--surface:#fffdfa;--soft:#e3e9eb;--ink:#20292d;--muted:#657075;--line:#cfd7d9;--deep:#1b262b;--accent:#f07832;--highlight:#ffb44a;--glow:#f07832;--hero-copy:#d2dde0;--hero-muted:#c7d3d6;--shadow:rgba(31,42,46,.07);--accent-gradient:#f07832;--bar-gradient:linear-gradient(90deg,#f07832,#ffb44a);--hero-radius:26px 8px 26px 8px;--card-radius:18px 6px 18px 6px;--section-radius:22px 7px 22px 7px;--icon-radius:50%;--kpi-count:4;--channel-count:3;--ring:88%;">
          <header class="cs-sitebar"><a class="cs-sitebrand" href="/Case_Studies" target="_self"><i>CS</i> Portfolio case study</a><span class="cs-category">Automotive</span></header>
          <section class="cs-wrap">
            <section class="cs-hero">
              <div class="cs-hero-copy"><span class="cs-kicker">Platform-verified inventory outcome</span><h1><em>88%</em> of available inventory sold in 62 days</h1><p>A focused VIN Marketing strategy combined vehicle-level signals, VDP improvements, and budget acceleration to move aging used-car inventory despite intense competition and a limited budget.</p></div>
              <div class="cs-hero-metric"><div class="cs-ring"><div><strong>88%</strong><span>sell-through</span></div></div></div>
            </section>
            <div class="cs-flight-row"><span>Campaign flight</span><strong>2019</strong></div>
            <section class="cs-kpis">
              <article>{bubble('target')}<div><strong>46%</strong><p>Sold within 30 days</p><small>Early inventory momentum</small></div></article>
              <article>{bubble('growth')}<div><strong>543%</strong><p>Increase in daily VDP views</p><small>Equal 10-day periods</small></div></article>
              <article>{bubble('chart')}<div><strong>6.4&times;</strong><p>Previous VDP average</p><small>0.44 before &rarr; 2.83 after</small></div></article>
              <article>{bubble('calendar')}<div><strong>75 &rarr; 62</strong><p>Planned vs. actual days</p><small>Budget accelerated near close</small></div></article>
            </section>
            <section class="cs-grid-2">
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('alert')}</span><div><small>The business pressure</small><h2>Move aging inventory before margin eroded</h2></div></div><div class="cs-list">
                <div>{_icon('calendar')}<p><strong>Aging vehicles</strong><span>Inventory had remained unsold for more than 30 days.</span></p></div>
                <div>{_icon('map')}<p><strong>17 nearby competitors</strong><span>Independent, new, certified-preowned, and used dealerships crowded the area.</span></p></div>
                <div>{_icon('money')}<p><strong>Extremely limited budget</strong><span>The original multichannel idea narrowed to one focused tactic.</span></p></div>
                <div>{_icon('growth')}<p><strong>Profit pressure</strong><span>Carrying and operating costs continued while inventory sat.</span></p></div>
              </div></article>
              <article class="cs-card"><div class="cs-card-heading"><span>{_icon('search')}</span><div><small>The diagnostic strategy</small><h2>Different signals required different answers</h2></div></div><div class="auto-diagnostic-flow">
                <article><div>{_icon('mouse')}<strong>Low VDP activity</strong></div><p>The vehicle likely had a visibility or discoverability problem.</p><span>Increase qualified exposure</span></article>{_icon('arrow')}<article><div>{_icon('target')}<strong>Views without a sale</strong></div><p>The offer, pricing, urgency, or presentation needed closer review.</p><span>Strengthen the VDP and offer</span></article>
              </div><p class="cs-note"><strong>Strategic counsel:</strong> I paired the media analysis with candid conversations about pricing, competition, and what the available budget could realistically achieve.</p></article>
            </section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('mouse')}</span><div><small>VDP conversion refresh</small><h2>Minor page improvements created stronger reasons to act</h2></div></div><div class="cs-chip-grid">
              <div class="cs-chip">{_icon('play')}<strong>Walkaround video</strong></div><div class="cs-chip">{_icon('mouse')}<strong>Stronger CTA</strong></div><div class="cs-chip">{_icon('target')}<strong>Manager Special</strong></div><div class="cs-chip">{_icon('money')}<strong>Price Drop</strong></div><div class="cs-chip">{_icon('car')}<strong>Updated presentation</strong></div><div class="cs-chip">{_icon('check')}<strong>Changes implemented</strong></div>
            </div></section>
            <section class="cs-dark"><div class="cs-section-heading"><small>Engagement lift</small><h2>Vehicle pages gained measurable momentum</h2></div><div class="auto-performance-row">
              <article class="auto-vdp-compare"><div><span>Before launch</span><strong>0.44</strong><small>average daily VDP views</small><i><b style="width:16%"></b></i></div>{_icon('arrow')}<div><span>After launch</span><strong>2.83</strong><small>average daily VDP views</small><i><b style="width:100%"></b></i></div></article>
              <article class="auto-lift">{_icon('chart')}<strong>543%</strong><span>increase</span><small>6.4&times; the previous average</small></article>
            </div><p style="color:var(--hero-copy);font-size:.86rem;margin:1rem 0 0;text-align:center;">Measured across comparable 10-day periods before and after launch.</p></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('chart')}</span><div><small>Campaign pacing</small><h2>Optimization followed the shrinking inventory</h2></div></div><div class="auto-timeline-row">
              <article><span>Plan</span><strong>75 days</strong><p>Focused VIN Marketing launch</p></article>{_icon('arrow')}<article><span>Day 30</span><strong>46% sold</strong><p>Early sell-through momentum</p></article>{_icon('arrow')}<article><span>Final stretch</span><strong>3 remained</strong><p>Budget accelerated</p></article>{_icon('arrow')}<article><span>Day 62</span><strong>88% sold</strong><p>Campaign concluded early</p></article>
            </div></section>
            <section class="cs-card cs-full"><div class="cs-card-heading"><span>{_icon('shield')}</span><div><small>Measurement system</small><h2>Site activity and live inventory stayed connected</h2></div></div><div class="cs-flow">
              <article><div>{_icon('mouse')}<span>Website pixel</span></div><p>Measured VDP and site activity</p></article>{_icon('arrow')}<article><div>{_icon('car')}<span>Live inventory</span></div><p>Reflected vehicle availability</p></article>{_icon('arrow')}<article><div>{_icon('check')}<span>Sold VINs</span></div><p>Verified sell-through results</p></article>
            </div></section>
            <section class="cs-bottom"><article class="cs-contribution"><div><small>My strategic contribution</small><h2>From aging inventory to focused sales momentum.</h2></div><div class="cs-capabilities">{contribution_html}</div></article><article class="cs-takeaway">{_icon('car')}<small>Strategic takeaway</small><p>With a constrained budget, focus matters more than channel count.</p><div class="cs-next"><p>The right inventory signals, stronger product pages, and disciplined optimization can turn aging inventory into measurable sales momentum.</p></div></article></section>
            <p class="cs-disclosure">Client identity and selected identifying details have been modified. Sell-through, VDP activity, and inventory-status changes were measured through the VIN Marketing platform, website pixel, and live dealership inventory updates. The 543% increase and 6.4&times; multiplier are calculated from verified 0.44 and 2.83 averages across comparable 10-day periods.</p>
            <a class="cs-back" href="/Case_Studies" target="_self">&larr; Return to all case studies</a>
          </section>
        </div>
        """),
        unsafe_allow_html=True,
    )


def render_case_studies() -> None:
    st.set_page_config(
        page_title="Campaign Case Studies | L.C. Felton",
        page_icon="CS",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    selected = str(st.query_params.get("case", "")).strip()
    if selected == "ent-physician":
        _render_ent()
    elif selected == "cloud-services-cybersecurity":
        _render_tech()
    elif selected == "used-car-sales":
        _render_auto()
    else:
        _render_gallery()
