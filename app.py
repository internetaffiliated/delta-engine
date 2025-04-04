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
C = 100
F = C + 612 * np.pi
Phi = 51

# --- Derived Variables ---
I = 9 * x + 9 * R
M = E / T
S = 40  # Placeholder for strategic boost
Delta = (kappa * (M * (I + S) - F)) / Phi
G = 3 * Delta

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
    """)
    st.latex(rf"\Delta = \frac{{{kappa} \cdot ({M:.2f}({I} + {S}) - {F:.2f})}}{{{Phi}}} = {Delta:.2f}")
    st.latex(rf"G = 3 \cdot \Delta = {G:.2f}")

# --- Visualization ---
st.subheader("📊 Growth Potential")
timeline = np.linspace(0, 30, 300)
G_curve = G * np.sin(0.2 * timeline) * np.exp(-0.03 * timeline)

fig, ax = plt.subplots(figsize=(10, 3))
ax.plot(timeline, G_curve, color='cyan', label='Simulated Growth')
ax.axhline(0, linestyle='--', color='gray')
ax.set_xlabel("Time (t)")
ax.set_ylabel("Growth")
ax.set_title("Predicted Growth Simulation")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# --- Geometric Core with Animation ---
st.subheader("🔺 Geometric Core")
st.markdown("**Visualizing the internal tetrahedron state.**")

animated_svg = '''
<svg width="300" height="260" viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg">
  <polygon points="150,30 270,210 30,210" stroke="cyan" stroke-width="2" fill="none">
    <animate attributeName="stroke" values="cyan;lime;cyan" dur="3s" repeatCount="indefinite" />
  </polygon>
  <line x1="150" y1="30" x2="150" y2="210" stroke="cyan" stroke-width="2">
    <animate attributeName="stroke" values="cyan;lime;cyan" dur="3s" repeatCount="indefinite" />
  </line>
  <line x1="30" y1="210" x2="150" y2="210" stroke="cyan" stroke-width="2" />
  <line x1="270" y1="210" x2="150" y2="210" stroke="cyan" stroke-width="2" />
  <circle cx="150" cy="210" r="6" fill="lime">
    <animate attributeName="r" values="6;10;6" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>
'''

html(animated_svg, height=300, width=320)
