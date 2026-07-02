import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🔬 Gibbs Phenomenon Close-Up")
st.write("Notice how increasing $N$ moves the spike closer to the transition wall, but the peak amplitude error stubbornly stalls around ~9%.")

max_n = st.sidebar.slider("Number of Harmonics (N)", min_value=3, max_value=299, value=11, step=4)

x_zoom = np.linspace(-0.2, 1.0, 1500)
fourier_sum = np.zeros_like(x_zoom)
for n in range(1, max_n + 1, 2):
    fourier_sum += (4 / np.pi) * (np.sin(n * x_zoom) / n)
    
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_zoom, y=np.sign(np.sin(x_zoom)), name="Ideal Transition", line=dict(color="black", dash="dash"), opacity=0.4))
fig.add_trace(go.Scatter(x=x_zoom, y=fourier_sum, name=f"Overshoot Front (N={max_n})", line=dict(color="#E63946", width=2.5)))
fig.add_hline(y=1.08949, line_dash="dot", line_color="gray", annotation_text="Theoretical Gibbs Limit (~1.09)")
fig.update_layout(xaxis_title="Time (Zoomed near Edge)", yaxis_title="Amplitude", template="plotly_white", yaxis=dict(range=[0.5, 1.25]), hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)