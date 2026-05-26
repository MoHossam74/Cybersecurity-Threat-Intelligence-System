"""
Cyber Shield Dashboard
A professional AI-powered cybersecurity analytics platform.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Cyber Shield · Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Global Styles
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@300;400;500;600&display=swap');

/* ── Root palette ── */
:root {
    --bg-base:     #05080f;
    --bg-surface:  #0b1120;
    --bg-elevated: #111c30;
    --border:      #1e3050;
    --border-glow: #2a4a7f;
    --accent-1:    #38bdf8;
    --accent-2:    #818cf8;
    --accent-3:    #34d399;
    --danger:      #f87171;
    --warning:     #fbbf24;
    --text-primary:#f1f5f9;
    --text-muted:  #64748b;
    --text-dim:    #94a3b8;
}

/* ── Base ── */
.stApp {
    background: var(--bg-base);
    background-image:
        radial-gradient(ellipse 80% 60% at 50% -10%, rgba(56,189,248,.08) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 90% 10%,  rgba(129,140,248,.06) 0%, transparent 50%);
    font-family: 'Inter', sans-serif;
    color: var(--text-primary);
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--bg-surface);
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

/* ── Layout ── */
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
    max-width: 1600px;
}

/* ── Page header ── */
.page-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 6px;
}
.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 42px;
    font-weight: 800;
    letter-spacing: -1px;
    background: linear-gradient(135deg, #f1f5f9 30%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin: 0;
}
.page-subtitle {
    color: var(--text-muted);
    font-size: 14px;
    font-weight: 400;
    letter-spacing: 0.02em;
    margin-bottom: 28px;
}
.live-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(52, 211, 153, .12);
    border: 1px solid rgba(52, 211, 153, .35);
    color: #34d399;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    padding: 4px 10px;
    border-radius: 100px;
    letter-spacing: .04em;
}
.live-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #34d399;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: .3; }
}

/* ── KPI Cards ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 14px;
    margin-bottom: 24px;
}
.kpi-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
    transition: border-color .2s;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
    opacity: 0;
    transition: opacity .2s;
}
.kpi-card:hover { border-color: var(--border-glow); }
.kpi-card:hover::before { opacity: 1; }
.kpi-icon {
    font-size: 18px;
    margin-bottom: 12px;
    display: block;
}
.kpi-label {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: var(--text-muted);
    margin-bottom: 8px;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1;
}
.kpi-value.accent  { color: var(--accent-1); }
.kpi-value.success { color: var(--accent-3); }
.kpi-value.danger  { color: var(--danger);   }
.kpi-value.warning { color: var(--warning);  }
.kpi-sub {
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 6px;
    font-family: 'IBM Plex Mono', monospace;
}

/* ── Section Cards ── */
.section-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: var(--bg-elevated);
    border-radius: 12px;
    padding: 4px;
    border: 1px solid var(--border);
    margin-bottom: 24px;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 13px;
    color: var(--text-muted);
    border-radius: 8px;
    padding: 8px 18px;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: var(--bg-surface) !important;
    color: var(--accent-1) !important;
    border: 1px solid var(--border) !important;
}

/* ── Sidebar branding ── */
.sidebar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 0 20px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 16px;
}
.sidebar-brand-name {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 800;
    color: var(--text-primary);
    letter-spacing: -0.5px;
}
.sidebar-brand-tag {
    font-size: 10px;
    color: var(--text-muted);
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: .06em;
}

/* ── Filter section label ── */
.filter-label {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: var(--text-muted);
    margin: 16px 0 8px;
}

/* ── Upload area ── */
[data-testid="stFileUploader"] {
    background: var(--bg-elevated);
    border: 1px dashed var(--border-glow);
    border-radius: 14px;
    padding: 8px;
}

/* ── DataFrame ── */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    border: 1px solid var(--border);
    overflow: hidden;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: var(--bg-elevated);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
}
[data-testid="stMetricLabel"] { color: var(--text-muted) !important; font-size: 12px; }
[data-testid="stMetricValue"] { color: var(--accent-1) !important; font-family: 'Syne', sans-serif; }

/* ── Divider ── */
hr { border-color: var(--border); margin: 20px 0; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--bg-base); }
::-webkit-scrollbar-thumb { background: var(--border-glow); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────
ACCENT_SEQUENCE = ["#38bdf8", "#818cf8", "#34d399", "#fbbf24", "#f87171",
                   "#c084fc", "#fb923c", "#2dd4bf"]

PLOTLY_BASE = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter, sans-serif", color="#94a3b8", size=12),
    title_font=dict(family="Syne, sans-serif", size=17, color="#f1f5f9"),
    margin=dict(l=12, r=12, t=52, b=16),
    legend=dict(bgcolor="rgba(0,0,0,0)", bordercolor="#1e3050", borderwidth=1),
)


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────
def styled_fig(fig, height: int = 380) -> go.Figure:
    """Apply consistent dark theme to a Plotly figure."""
    fig.update_layout(**PLOTLY_BASE, height=height)
    fig.update_xaxes(gridcolor="#1e3050", linecolor="#1e3050", tickfont_color="#64748b")
    fig.update_yaxes(gridcolor="#1e3050", linecolor="#1e3050", tickfont_color="#64748b")
    return fig


def kpi_card(icon: str, label: str, value: str, sub: str = "", color: str = "accent") -> None:
    """Render a single KPI card."""
    st.markdown(f"""
    <div class="kpi-card">
        <span class="kpi-icon">{icon}</span>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value {color}">{value}</div>
        {"<div class='kpi-sub'>" + sub + "</div>" if sub else ""}
    </div>
    """, unsafe_allow_html=True)


def section_header(title: str, subtitle: str = "") -> None:
    """Render a consistent section header inside a tab."""
    st.markdown(f"""
    <div style="margin-bottom:20px">
        <div style="font-family:'Syne',sans-serif;font-size:20px;font-weight:700;
                    color:#f1f5f9;letter-spacing:-.3px">{title}</div>
        {"<div style='font-size:13px;color:#64748b;margin-top:4px'>" + subtitle + "</div>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


def has_col(df: pd.DataFrame, *cols: str) -> bool:
    """Return True if all given columns exist in the dataframe."""
    return all(c in df.columns for c in cols)


def safe_pct(series, value: str) -> float:
    """Percentage of rows where series equals value (case-insensitive)."""
    return series.astype(str).str.lower().eq(value.lower()).mean() * 100


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div>
            <div class="sidebar-brand-name">🛡️ CyberShield</div>
            <div class="sidebar-brand-tag">AI ANALYTICS PLATFORM · v2.0</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload dataset (.xlsx)",
        type=["xlsx"],
        help="Upload your cybersecurity Excel dataset to begin analysis.",
        label_visibility="visible",
    )

    if uploaded_file:
        st.markdown('<div class="filter-label">Filters</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# No File State
# ─────────────────────────────────────────────
if not uploaded_file:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:6px">
        <div class="page-title">Cyber Shield Dashboard</div>
        <div class="live-badge">
            <div class="live-dot"></div>AWAITING DATA
        </div>
    </div>
    <div class="page-subtitle">
        AI-powered cybersecurity analytics · Threat intelligence · ML anomaly detection
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card" style="text-align:center;padding:60px 40px">
        <div style="font-size:52px;margin-bottom:16px">📂</div>
        <div style="font-family:'Syne',sans-serif;font-size:22px;font-weight:700;
                    color:#f1f5f9;margin-bottom:8px">Upload your dataset to begin</div>
        <div style="color:#64748b;font-size:14px;max-width:400px;margin:0 auto">
            Upload an <strong style="color:#94a3b8">.xlsx</strong> file via the sidebar.
            Expected columns: Year, Country, Attack Type, Target Industry,
            Financial Loss, and ML prediction fields.
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# ─────────────────────────────────────────────
# Load Data
# ─────────────────────────────────────────────
@st.cache_data(show_spinner="Loading dataset…")
def load_data(file) -> pd.DataFrame:
    return pd.read_excel(file)

df = load_data(uploaded_file)

# ─────────────────────────────────────────────
# Sidebar Filters (after file load)
# ─────────────────────────────────────────────
with st.sidebar:
    filtered_df = df.copy()

    filter_cols = {
        "Year": "Year",
        "Country": "Country",
        "Attack Type": "Attack Type",
        "Target Industry": "Industry",
        "Risk_Tier": "Risk Tier",
    }

    for col, label in filter_cols.items():
        if col in df.columns:
            options = sorted(df[col].dropna().astype(str).unique())
            selected = st.selectbox(label, ["All"] + list(options))
            if selected != "All":
                filtered_df = filtered_df[filtered_df[col].astype(str) == selected]

    st.markdown("---")
    st.caption(f"**{len(filtered_df):,}** of **{len(df):,}** records")

# ─────────────────────────────────────────────
# Page Header
# ─────────────────────────────────────────────
st.markdown(f"""
<div style="display:flex;align-items:center;gap:14px;margin-bottom:6px">
    <div class="page-title">Cyber Shield Dashboard</div>
    <div class="live-badge">
        <div class="live-dot"></div>LIVE
    </div>
</div>
<div class="page-subtitle">
    {len(filtered_df):,} incidents analysed &nbsp;·&nbsp;
    Uploaded: <strong style="color:#94a3b8">{uploaded_file.name}</strong>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# KPI Row
# ─────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    kpi_card("🗂️", "Total Incidents", f"{len(filtered_df):,}", "filtered dataset")

with c2:
    if has_col(filtered_df, "Traffic_Label"):
        rate = safe_pct(filtered_df["Traffic_Label"], "anomaly")
        kpi_card("⚠️", "Anomaly Rate", f"{rate:.1f}%",
                 "high" if rate > 50 else "normal",
                 color="danger" if rate > 50 else "warning")
    else:
        kpi_card("⚠️", "Anomaly Rate", "N/A", color="accent")

with c3:
    if has_col(filtered_df, "Financial Loss (in Million $)"):
        avg_loss = filtered_df["Financial Loss (in Million $)"].mean()
        kpi_card("💸", "Avg Financial Loss", f"${avg_loss:.1f}M",
                 "per incident", color="warning")
    else:
        kpi_card("💸", "Avg Financial Loss", "N/A", color="accent")

with c4:
    if has_col(filtered_df, "Number of Affected Users"):
        users = filtered_df["Number of Affected Users"].sum()
        kpi_card("👥", "Affected Users", f"{users:,.0f}", "cumulative total", color="accent")
    else:
        kpi_card("👥", "Affected Users", "N/A", color="accent")

with c5:
    if has_col(filtered_df, "Risk_Tier"):
        high_risk = (filtered_df["Risk_Tier"].astype(str) == "High Risk").sum()
        pct = high_risk / max(len(filtered_df), 1) * 100
        kpi_card("🔴", "High Risk", f"{high_risk:,}", f"{pct:.1f}% of incidents",
                 color="danger" if pct > 30 else "warning")
    else:
        kpi_card("🔴", "High Risk", "N/A", color="accent")

# ─────────────────────────────────────────────
# Tabs
# ─────────────────────────────────────────────
tab_overview, tab_threat, tab_distribution, tab_ml, tab_data = st.tabs([
    "📊  Overview",
    "🔍  Threat Analysis",
    "🌍  Attack Distribution",
    "🤖  ML Results",
    "📋  Data Preview",
])

# ══════════════════════════════════════════════
# Tab 0 · Overview
# ══════════════════════════════════════════════
with tab_overview:
    section_header("Overview", "High-level summary of the filtered dataset")

    col1, col2 = st.columns(2)

    with col1:
        if has_col(filtered_df, "Attack Type"):
            counts = filtered_df["Attack Type"].value_counts().reset_index()
            counts.columns = ["Attack Type", "Count"]
            fig = px.bar(
                counts, x="Attack Type", y="Count",
                title="Attack Type Distribution",
                color="Count",
                color_continuous_scale=[[0, "#1e3050"], [0.5, "#38bdf8"], [1, "#818cf8"]],
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    with col2:
        if has_col(filtered_df, "Risk_Tier"):
            risk = filtered_df["Risk_Tier"].value_counts().reset_index()
            risk.columns = ["Risk Tier", "Count"]
            fig = px.pie(
                risk, names="Risk Tier", values="Count",
                title="Risk Tier Breakdown",
                hole=0.55,
                color_discrete_sequence=["#f87171", "#fbbf24", "#34d399"],
            )
            fig.update_traces(textinfo="label+percent", textfont_size=12)
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    # ── Severity heatmap (Attack Type × Industry) ──
    if has_col(filtered_df, "Attack Type", "Target Industry"):
        pivot = (
            filtered_df.groupby(["Attack Type", "Target Industry"])
            .size()
            .reset_index(name="Count")
        )
        heatmap_data = pivot.pivot(index="Target Industry", columns="Attack Type", values="Count").fillna(0)
        fig = go.Figure(go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns.tolist(),
            y=heatmap_data.index.tolist(),
            colorscale=[[0, "#0b1120"], [0.4, "#1e4a7f"], [1, "#38bdf8"]],
            hovertemplate="%{y} × %{x}: <b>%{z:.0f}</b><extra></extra>",
        ))
        fig.update_layout(title="Incident Heatmap · Attack Type vs Industry")
        st.plotly_chart(styled_fig(fig, height=420), use_container_width=True)


# ══════════════════════════════════════════════
# Tab 1 · Threat Analysis
# ══════════════════════════════════════════════
with tab_threat:
    section_header("Threat Analysis", "Temporal trends, source intelligence, and financial impact")

    col1, col2 = st.columns(2)

    with col1:
        if has_col(filtered_df, "Year"):
            yearly = filtered_df.groupby("Year").size().reset_index(name="Incidents")
            fig = px.area(
                yearly, x="Year", y="Incidents",
                title="Incident Trend by Year",
                markers=True,
                line_shape="spline",
            )
            fig.update_traces(
                line_color="#38bdf8",
                fillcolor="rgba(56,189,248,.12)",
                marker=dict(color="#38bdf8", size=7, line=dict(color="#0b1120", width=2)),
            )
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    with col2:
        if has_col(filtered_df, "Attack Type"):
            counts = filtered_df["Attack Type"].value_counts().reset_index()
            counts.columns = ["Attack Type", "Count"]
            fig = px.pie(
                counts, names="Attack Type", values="Count",
                title="Attack Type Share",
                hole=0.5,
                color_discrete_sequence=ACCENT_SEQUENCE,
            )
            fig.update_traces(textinfo="label+percent")
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        if has_col(filtered_df, "Source_IP"):
            top_ips = filtered_df["Source_IP"].value_counts().head(10).reset_index()
            top_ips.columns = ["Source IP", "Count"]
            fig = px.bar(
                top_ips, x="Count", y="Source IP",
                orientation="h",
                title="Top 10 Source IPs",
                color="Count",
                color_continuous_scale=[[0, "#1e3050"], [1, "#38bdf8"]],
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    with col4:
        if has_col(filtered_df, "Financial Loss (in Million $)", "Attack Type"):
            loss = (
                filtered_df.groupby("Attack Type")["Financial Loss (in Million $)"]
                .mean()
                .reset_index()
                .sort_values("Financial Loss (in Million $)", ascending=False)
            )
            fig = px.bar(
                loss, x="Attack Type", y="Financial Loss (in Million $)",
                title="Average Financial Loss by Attack Type",
                color="Financial Loss (in Million $)",
                color_continuous_scale=[[0, "#1e3050"], [0.5, "#fbbf24"], [1, "#f87171"]],
                text_auto=".1f",
            )
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(styled_fig(fig), use_container_width=True)


# ══════════════════════════════════════════════
# Tab 2 · Attack Distribution
# ══════════════════════════════════════════════
with tab_distribution:
    section_header("Attack Distribution", "Geographic, industry, port, and protocol breakdowns")

    col1, col2 = st.columns(2)

    with col1:
        if has_col(filtered_df, "Country"):
            cc = filtered_df["Country"].value_counts().head(15).reset_index()
            cc.columns = ["Country", "Count"]
            fig = px.bar(
                cc, x="Count", y="Country",
                orientation="h",
                title="Top 15 Affected Countries",
                color="Count",
                color_continuous_scale=[[0, "#1e3050"], [1, "#818cf8"]],
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            fig.update_coloraxes(showscale=False)
            fig.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(styled_fig(fig, 440), use_container_width=True)

    with col2:
        if has_col(filtered_df, "Target Industry"):
            ic = filtered_df["Target Industry"].value_counts().reset_index()
            ic.columns = ["Industry", "Count"]
            fig = px.bar(
                ic, x="Industry", y="Count",
                title="Targeted Industries",
                color="Count",
                color_continuous_scale=[[0, "#1e3050"], [1, "#34d399"]],
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(styled_fig(fig, 440), use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        if has_col(filtered_df, "Destination_Port"):
            ports = filtered_df["Destination_Port"].value_counts().head(10).reset_index()
            ports.columns = ["Port", "Count"]
            ports["Port"] = ports["Port"].astype(str)
            fig = px.bar(
                ports, x="Port", y="Count",
                title="Top 10 Targeted Ports",
                color="Count",
                color_continuous_scale=[[0, "#1e3050"], [1, "#38bdf8"]],
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            fig.update_coloraxes(showscale=False)
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    with col4:
        if has_col(filtered_df, "Protocol"):
            proto = filtered_df["Protocol"].value_counts().reset_index()
            proto.columns = ["Protocol", "Count"]
            fig = px.pie(
                proto, names="Protocol", values="Count",
                title="Protocol Distribution",
                hole=0.5,
                color_discrete_sequence=ACCENT_SEQUENCE,
            )
            fig.update_traces(textinfo="label+percent")
            st.plotly_chart(styled_fig(fig), use_container_width=True)


# ══════════════════════════════════════════════
# Tab 3 · ML Results
# ══════════════════════════════════════════════
with tab_ml:
    section_header("Machine Learning Results", "Model performance, anomaly detection, and risk classification")

    # ── Accuracy row ──
    m1, m2, m3, m4, m5 = st.columns(5)

    if has_col(filtered_df, "ML_Traffic_Pred", "Traffic_Label"):
        acc = (
            filtered_df["ML_Traffic_Pred"].astype(str).str.lower()
            == filtered_df["Traffic_Label"].astype(str).str.lower()
        ).mean() * 100
        m1.metric("Model Accuracy", f"{acc:.2f}%")
    else:
        m1.metric("Model Accuracy", "N/A")

    m2.metric("CV F1 Score",  "74.00%")
    m3.metric("AUC-ROC",      "77.20%")

    if has_col(filtered_df, "Risk_Tier"):
        hr_count = (filtered_df["Risk_Tier"].astype(str) == "High Risk").sum()
        hr_pct   = hr_count / max(len(filtered_df), 1) * 100
        m4.metric("High Risk Incidents", f"{hr_count:,}", f"{hr_pct:.1f}%")
    else:
        m4.metric("High Risk Incidents", "N/A")

    if has_col(filtered_df, "ML_Anomaly_Prob"):
        avg_prob = filtered_df["ML_Anomaly_Prob"].mean() * 100
        m5.metric("Avg Anomaly Prob", f"{avg_prob:.2f}%")
    else:
        m5.metric("Avg Anomaly Prob", "N/A")

    st.markdown("---")

    # ── Gauge + Risk bar ──
    col_g, col_r = st.columns(2)

    with col_g:
        if has_col(filtered_df, "ML_Anomaly_Prob"):
            avg_prob = filtered_df["ML_Anomaly_Prob"].mean()
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=avg_prob * 100,
                title={"text": "Average Anomaly Probability", "font": {"size": 17, "color": "#f1f5f9", "family": "Syne"}},
                number={"suffix": "%", "font": {"size": 40, "color": "#38bdf8", "family": "Syne"}},
                delta={"reference": 50, "relative": False,
                       "increasing": {"color": "#f87171"}, "decreasing": {"color": "#34d399"}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#64748b", "tickfont": {"color": "#64748b"}},
                    "bar":  {"color": "#38bdf8", "thickness": 0.25},
                    "bgcolor": "rgba(0,0,0,0)",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0,  40], "color": "rgba(52,211,153,.15)"},
                        {"range": [40, 70], "color": "rgba(251,191,36,.15)"},
                        {"range": [70,100], "color": "rgba(248,113,113,.15)"},
                    ],
                    "threshold": {"line": {"color": "#f87171", "width": 3},
                                  "thickness": 0.85, "value": 65},
                }
            ))
            fig.update_layout(
                **{k: v for k, v in PLOTLY_BASE.items() if k not in ("margin",)},
                height=340,
                margin=dict(l=30, r=30, t=60, b=20),
            )
            st.plotly_chart(fig, use_container_width=True)

    with col_r:
        if has_col(filtered_df, "Risk_Tier"):
            rc = filtered_df["Risk_Tier"].value_counts().reset_index()
            rc.columns = ["Risk Tier", "Count"]
            color_map = {"High Risk": "#f87171", "Medium Risk": "#fbbf24", "Low Risk": "#34d399"}
            fig = px.bar(
                rc, x="Risk Tier", y="Count",
                title="Incidents per Risk Tier",
                color="Risk Tier",
                color_discrete_map=color_map,
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    # ── Anomaly classification + XGB severity ──
    col_a, col_x = st.columns(2)

    with col_a:
        if has_col(filtered_df, "ML_High_Confidence_Anomaly"):
            ac = filtered_df["ML_High_Confidence_Anomaly"].value_counts().reset_index()
            ac.columns = ["Status", "Count"]
            fig = px.bar(
                ac, x="Status", y="Count",
                title="ML Anomaly Classification",
                color="Status",
                color_discrete_sequence=["#38bdf8", "#818cf8"],
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            st.plotly_chart(styled_fig(fig), use_container_width=True)

    with col_x:
        if has_col(filtered_df, "XGB_Severity_Pred"):
            sc = filtered_df["XGB_Severity_Pred"].value_counts().reset_index()
            sc.columns = ["Severity", "Count"]
            fig = px.bar(
                sc, x="Severity", y="Count",
                title="XGBoost Severity Prediction",
                color="Severity",
                color_discrete_sequence=ACCENT_SEQUENCE,
                text="Count",
            )
            fig.update_traces(textposition="outside", textfont_color="#94a3b8")
            st.plotly_chart(styled_fig(fig), use_container_width=True)


# ══════════════════════════════════════════════
# Tab 4 · Data Preview
# ══════════════════════════════════════════════
with tab_data:
    section_header("Dataset Preview", f"{len(filtered_df):,} rows after filtering")

    # ── Quick stats row ──
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Total Rows",    f"{len(df):,}")
    s2.metric("Filtered Rows", f"{len(filtered_df):,}")
    s3.metric("Columns",       f"{len(df.columns):,}")
    s4.metric("Missing Values", f"{filtered_df.isnull().sum().sum():,}")

    st.markdown("---")

    # ── Column filter ──
    all_cols = list(filtered_df.columns)
    selected_cols = st.multiselect(
        "Select columns to display",
        options=all_cols,
        default=all_cols[:min(10, len(all_cols))],
    )

    display_df = filtered_df[selected_cols] if selected_cols else filtered_df
    st.dataframe(
        display_df,
        use_container_width=True,
        height=500,
    )

    # ── Download ──
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️  Download filtered dataset as CSV",
        data=csv,
        file_name="cybershield_filtered.csv",
        mime="text/csv",
    )
