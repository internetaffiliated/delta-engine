import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit.components.v1 import html

st.set_page_config(page_title="Delta Tetrahedron", layout="wide")

# Sidebar Controls
with st.sidebar:
    st.title("Controls")
    x = st.slider("Effort (x)", 0, 100, 40)
    R = st.slider("Resources (R)", 0, 100, 35)
    concept = st.text_input("Concept Keyword", value="clarity")
    user_input_scalar = st.number_input("Input Scalar (Numeric)", value=1.0)
    timeline_unit = st.selectbox("Timeline Unit", ["Hours", "Days", "Weeks", "Months"])
    timeline_length = st.slider("Timeline Length", 12, 120, 36, step=12)

# Concept-to-scalar mapping
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
kappa = concept_map.get(concept.lower(), user_input_scalar)

# Constants and Computation
E = 1.2
T = 1.0
C = 100
F = C + 612 * np.pi
Phi = 51
I = 9 * x + 9 * R
M = E / T
S = 40
Delta = (kappa * (M * (I + S) - F)) / Phi
G = 3 * Delta

# Latin Term Mapping
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

# Layout Columns
col1, col2 = st.columns([2, 1])

# Left Column: Graph & Equation
with col1:
    st.markdown("## Δ and G Simulation")
    st.latex(r"\Delta(t) = \frac{\kappa \cdot (M(I + S) - F)}{\Phi}")

    timeline = np.linspace(0, timeline_length, 300)
    G_curve = G * np.sin(0.2 * timeline) * np.exp(-0.03 * timeline)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(timeline, G_curve, color='cyan', label='Simulated Growth')
    ax.axhline(0, linestyle='--', color='gray')
    ax.set_xlabel(f"Time ({timeline_unit})")
    ax.set_ylabel("Growth")
    ax.set_title("Growth Projection")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    with st.expander("🔬 Full Equation Breakdown"):
        st.markdown(f"""
        - **κ (Concept Scalar)**: {kappa}
        - **M (Efficiency/Time)**: {M:.2f}
        - **Input Potential (I)**: {I}
        - **Strategic Boost (S)**: {S}
        - **Friction Load (F)**: {F:.2f}
        - **Φ (Normalization)**: {Phi}
        """)
        st.latex(rf"\Delta = \frac{{{kappa} \cdot ({M:.2f}({I} + {S}) - {F:.2f})}}{{{Phi}}} = {Delta:.2f}")
        st.latex(rf"G = 3 \cdot \Delta = {G:.2f}")

# Right Column: Geometry and Metrics
with col2:
    st.markdown("## 🔺 Tetrahedron State")
    animated_svg = f'''
    <svg width="100%" height="240" viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg">
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
    html(animated_svg, height=260)
    st.metric(label="Δ (Delta)", value=f"{Delta:.2f}")
    st.metric(label="G(t)", value=f"{G:.2f}")
    st.caption(f"Latin Mapping: _{latin_hint}_")
