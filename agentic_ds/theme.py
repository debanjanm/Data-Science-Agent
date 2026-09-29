"""Neobrutalist look: one injected stylesheet. Tune colors via the :root tokens."""

import streamlit as st

CSS = r"""
:root {
  --ink: #171717;
  --page: #F4EBC8;
  --accent: #EFB3CF;
  --support: #A9D6CB;
  --info: #B3DDEB;
  --good: #A6E3B8;
  --bad: #F09A93;
  --warn: #F5D88A;
  --white: #FFFFFF;
  --border: 3px solid var(--ink);
  --shadow: 4px 4px 0 var(--ink);
  --shadow-btn: 3px 3px 0 var(--ink);
  --shadow-panel: 7px 7px 0 var(--ink);
  --r-card: 12px;
  --r-input: 10px;
  --r-panel: 18px;
  --font-head: "Arial Black", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

/* page + main panel */
.stApp { background: var(--page); color: var(--ink); }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stMainBlockContainer"] {
  background: var(--white);
  border: 4px solid var(--ink);
  border-radius: var(--r-panel);
  box-shadow: var(--shadow-panel);
  margin: 4rem 1.75rem 2.5rem;
  padding: 2.25rem 2.5rem 3rem;
  max-width: none;
  width: calc(100% - 3.5rem);
  box-sizing: border-box;
}

/* type */
h1, h2, h3, h4, h5, h6,
[data-testid="stHeading"] h1, [data-testid="stHeading"] h2, [data-testid="stHeading"] h3 {
  font-family: var(--font-head);
  font-weight: 900;
  letter-spacing: -0.02em;
  color: var(--ink);
}
[data-testid="stHeading"] h1 {
  display: inline-block;
  background: var(--accent);
  border: var(--border);
  border-radius: var(--r-card);
  box-shadow: var(--shadow);
  padding: 0.35rem 1rem;
  margin-bottom: 0.5rem;
}
[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p, label { font-weight: 700; color: var(--ink); }
[data-testid="stCaptionContainer"] { color: var(--ink); opacity: 1; }
[data-testid="stMarkdownContainer"] a { color: var(--ink); text-decoration: underline; text-decoration-thickness: 2px; font-weight: 700; }

/* sidebar */
[data-testid="stSidebar"] { background: var(--support); border-right: 4px solid var(--ink); }
[data-testid="stSidebarNavLink"] {
  border: 3px solid transparent;
  border-radius: 999px;
  color: var(--ink);
  font-weight: 700;
}
[data-testid="stSidebarNavLink"]:hover { background: var(--info); border-color: var(--ink); }
[data-testid="stSidebarNavLink"][aria-current="page"] {
  background: var(--accent);
  border-color: var(--ink);
  box-shadow: 2px 2px 0 var(--ink);
  font-weight: 900;
}
[data-testid="stNavSectionHeader"] { font-family: var(--font-head); font-weight: 900; letter-spacing: -0.02em; color: var(--ink); }

/* cards: bordered containers, metrics, expanders, forms, chat */
[data-testid="stLayoutWrapper"] > [data-testid="stVerticalBlock"],
[data-testid="stMetric"],
[data-testid="stExpander"],
[data-testid="stForm"],
[data-testid="stChatMessage"] {
  background: var(--white);
  border: var(--border);
  border-radius: var(--r-card);
  box-shadow: var(--shadow);
}
[data-testid="stExpander"] details, [data-testid="stExpander"] summary { border: 0; border-radius: var(--r-card); background: transparent; }
[data-testid="stExpander"] summary { font-weight: 800; }
[data-testid="stMetricLabel"] { font-weight: 700; }
[data-testid="stMetricValue"] { font-family: var(--font-head); font-weight: 900; letter-spacing: -0.02em; }

/* buttons */
[data-testid="stBaseButton-secondary"],
[data-testid="stBaseButton-primary"],
[data-testid="stBaseButton-secondaryFormSubmit"],
[data-testid="stBaseButton-primaryFormSubmit"] {
  background: var(--white);
  color: var(--ink);
  border: var(--border);
  border-radius: 999px;
  box-shadow: var(--shadow-btn);
  font-weight: 800;
}
[data-testid="stBaseButton-primary"],
[data-testid="stBaseButton-primaryFormSubmit"] { background: var(--accent); }
[data-testid="stBaseButton-secondary"]:hover,
[data-testid="stBaseButton-primary"]:hover,
[data-testid="stBaseButton-secondaryFormSubmit"]:hover,
[data-testid="stBaseButton-primaryFormSubmit"]:hover {
  background: var(--info);
  color: var(--ink);
  border-color: var(--ink);
  transform: translate(-2px, -2px);
  box-shadow: 5px 5px 0 var(--ink);
}
[data-testid="stBaseButton-secondary"]:active,
[data-testid="stBaseButton-primary"]:active,
[data-testid="stBaseButton-secondaryFormSubmit"]:active,
[data-testid="stBaseButton-primaryFormSubmit"]:active {
  transform: translate(3px, 3px);
  box-shadow: 0 0 0 var(--ink);
}
button:disabled, [data-testid^="stBaseButton-"]:disabled { opacity: 0.5; }
@media (prefers-reduced-motion: no-preference) {
  [data-testid^="stBaseButton-"], [data-testid="stSidebarNavLink"] { transition: transform .08s, box-shadow .08s; }
}

/* segmented control */
[data-testid="stButtonGroup"] button[data-variant="segmented_control"] {
  background: var(--white);
  color: var(--ink);
  border: var(--border);
  font-weight: 800;
}
[data-testid="stButtonGroup"] button[data-variant="segmented_control"] * { color: var(--ink); }
[data-testid="stButtonGroup"] button[data-variant="segmented_control"][aria-checked="true"] { background: var(--accent); }
[data-testid="stButtonGroup"] button[data-variant="segmented_control"]:hover { background: var(--info); }

/* inputs (Streamlit >=1.4x uses react-aria, not BaseWeb) */
[data-testid="stSelectbox"] [role="group"],
[data-testid="stMultiSelect"] [role="group"],
[data-testid="stNumberInput"] [role="group"],
[data-testid="stTextInput"] [role="group"],
[data-testid="stTextArea"] [role="group"] {
  background: var(--white);
  border: var(--border);
  border-radius: var(--r-input);
  box-shadow: 2px 2px 0 var(--ink);
}
[data-testid="stChatInput"] { border: var(--border); border-radius: var(--r-input); box-shadow: 2px 2px 0 var(--ink); background: var(--white); }
[data-testid="stFileUploaderDropzone"] {
  background: var(--support);
  border: var(--border);
  border-radius: var(--r-card);
  box-shadow: var(--shadow);
}

/* data */
[data-testid="stDataFrame"], [data-testid="stTable"] {
  border: var(--border);
  border-radius: var(--r-card);
  box-shadow: var(--shadow);
  overflow: hidden;
}
[data-testid="stImage"] img { border: var(--border); box-shadow: var(--shadow); }

/* alerts keep semantic fills */
[data-testid="stAlert"] > div, [data-testid="stAlertContainer"] {
  border: var(--border);
  border-radius: var(--r-card);
  box-shadow: var(--shadow);
  color: var(--ink);
}
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) { background: var(--good); }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"]) { background: var(--bad); }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"]) { background: var(--warn); }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentInfo"]) { background: var(--info); }

/* status never by color alone: icon per alert kind */
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"])::before { content: "\2713"; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"])::before { content: "\2717"; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"])::before { content: "\25B2"; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentInfo"])::before { content: "\25CF"; }
[data-testid="stAlertContainer"] { display: flex; align-items: flex-start; }
[data-testid="stAlertContainer"]::before { font-weight: 900; margin-right: 0.75rem; }

/* slider, tags, tertiary buttons */
[data-testid="stSliderThumbValue"] { color: var(--ink); font-weight: 800; }
[data-tag] { background: var(--accent); border: 2px solid var(--ink); border-radius: 999px; font-weight: 700; }
[data-tag], [data-tag] * { color: var(--ink); }
[data-testid="stBaseButton-tertiary"] { color: var(--ink); font-weight: 800; }

/* visible keyboard focus */
button:focus-visible, a:focus-visible, input:focus-visible, textarea:focus-visible,
[role="radio"]:focus-visible, summary:focus-visible, [data-tag]:focus-visible,
[data-testid="stSelectbox"] [role="group"]:focus-within, [data-testid="stMultiSelect"] [role="group"]:focus-within,
[data-testid="stNumberInput"] [role="group"]:focus-within, [data-testid="stTextInput"] [role="group"]:focus-within {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

@media (max-width: 640px) {
  [data-testid="stMainBlockContainer"] {
    margin: 3.5rem 0.5rem 1.5rem;
    width: calc(100% - 1rem);
    padding: 1.25rem 1rem 2rem;
    box-shadow: 4px 4px 0 var(--ink);
  }
}
"""


def apply_theme() -> None:
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)
