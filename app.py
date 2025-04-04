import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit.components.v1 import html
import base64

st.set_page_config(page_title="Delta Tetrahedron Engine", layout="wide")

# --- Layout ---
st.title("🧪 Delta Tetrahedron Growth Simulator")
st.markdown("""
Welcome to the **Delta Engine** – a live simulation of growth shaped by mathematical structure, geometric form, and conceptual inputs.
""")

# --- Inputs ---
st.sidebar.header("🔧 Model Controls")
x = st.sidebar.slider("Effort (x)", 0, 100, 40)
R = st.sidebar.slider("Resources (R)", 0, 100, 35)
concept = st.sidebar.text_input("Concept Keyword", value="clarity")
secondary = st.sidebar.number_input("Secondary Input (Number you keep seeing?)", value=17)
timeline_unit = st.sidebar.selectbox("Timeline Unit", ["Hours", "Days", "Weeks", "Months"])
timeline_length = st.sidebar.slider("Timeline Length (Multiples of 12)", 12, 120, 36, step=12)

# --- Concept Map ---
concept_map = {
    "clarity": 1.2,
    "chaos": 0.6,
    "focus": 1.4,
    "doubt": 0.7,
    "momentum": 1.5,
    "burnout": 0.4,
    "trust": 1.3,
    "fear": 0.5,
    "intuition": 1.25,
    "distraction": 0.65
}

kappa = concept_map.get(concept.lower(), 1.0)  # default = 1.0

# --- Constants ---
E = 1.2
T = 1.0
C = 100 + (secondary % 13)  # subtly influenced by user's unique number
F = C + 612 * np.pi
Phi = 51

# --- Derived Variables ---
I = 9 * x + 9 * R
M = E / T
S = 40  # Placeholder for strategic boost
Delta = (kappa * (M * (I + S) - F)) / Phi
G = 3 * Delta

# --- Word Hint Logic ---
latin_keywords = {
    (1.2, 'clarity'): 'Lux',
    (0.6, 'chaos'): 'Confusio',
    (1.4, 'focus'): 'Intentio',
    (0.7, 'doubt'): 'Dubium',
    (1.5, 'momentum'): 'Motus',
    (0.4, 'burnout'): 'Exanimatio',
    (1.3, 'trust'): 'Fides',
    (0.5, 'fear'): 'Timor',
    (1.25, 'intuition'): 'Intuitus',
    (0.65, 'distraction'): 'Divisio'
}
latin_hint = latin_keywords.get((kappa, concept.lower()), 'Veritas')

# --- Equations ---
st.subheader("📐 Core Equation")
st.latex(r"\Delta(t) = \frac{\kappa \cdot (M(I + S) - F)}{\Phi}")

with st.expander("Show calculation breakdown"):
    st.markdown(f"""
    - **Concept Scalar (\(\kappa\))**: {kappa}
    - **Efficiency (E)**: {E}, **Time (T)**: {T} → **M** = {M:.2f}
    - **Input Potential (I = 9x + 9R)** = {I}
    - **Strategic Boost (S)** = {S}
    - **Friction Load (F)** = {F:.2f}
    - **Phi (\(\Phi\))** = {Phi}
    - **Secondary Number** = {secondary} → adjusted cost: {C}
    """)
    st.latex(rf"\Delta = \frac{{{kappa} \cdot ({M:.2f}({I} + {S}) - {F:.2f})}}{{{Phi}}} = {Delta:.2f}")
    st.latex(rf"G = 3 \cdot \Delta = {G:.2f}")
    st.markdown(f"**Latin Keyword Reference:** _{latin_hint}_")

# --- Visualization ---
st.subheader(f"📊 Growth Potential over {timeline_length} {timeline_unit}")
timeline = np.linspace(0, timeline_length, 300)
G_curve = G * np.sin(0.2 * timeline) * np.exp(-0.03 * timeline)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(timeline, G_curve, color='cyan', label='Simulated Growth')
ax.axhline(0, linestyle='--', color='gray')
ax.set_xlabel(f"Time ({timeline_unit})")
ax.set_ylabel("Growth")
ax.set_title("Predicted Growth Simulation")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# --- Geometric Core with Animation ---
st.subheader("🔺 Geometric Core")
cols = st.columns([1, 1])
with cols[0]:
    st.markdown("**Internal tetrahedron visual, responsive to growth.**")
    animated_svg = f'''
    <svg width="100%" height="260" viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg">
      <polygon points="150,30 270,210 30,210" stroke="cyan" stroke-width="2" fill="none">
        <animate attributeName="stroke" values="cyan;lime;cyan" dur="3s" repeatCount="indefinite" />
      </polygon>
      <line x1="150" y1="30" x2="150" y2="210" stroke="cyan" stroke-width="2">
        <animate attributeName="stroke" values="cyan;lime;cyan" dur="3s" repeatCount="indefinite" />
      </line>
      <line x1="30" y1="210" x2="150" y2="210" stroke="cyan" stroke-width="2" />
      <line x1="270" y1="210" x2="150" y2="210" stroke="cyan" stroke-width="2" />
      <circle cx="150" cy="210" r="{6 + abs(G) % 6}" fill="lime">
        <animate attributeName="r" values="6;10;6" dur="2s" repeatCount="indefinite" />
      </circle>
    </svg>
    '''
    html(animated_svg, height=300, width=320)

with cols[1]:
    st.markdown(f"### 🧭 Concept Translation: _{latin_hint}_")
    st.markdown("This term is derived from your keyword and current equation results, representing your system's archetypal alignment.")
    st.metric(label="G(t) Growth Value", value=f"{G:.2f}")
    st.metric(label="Δ (Delta) Value", value=f"{Delta:.2f}")
