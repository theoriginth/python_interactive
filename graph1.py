import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🔲 Square Wave Approximation")
st.write("Square waves are constructed entirely out of **odd** harmonics.")

# Setup interactive slider controls
max_n = st.sidebar.slider("Max Harmonic Order (N)", min_value=1, max_value=99, value=1, step=2)

# Compute the Fourier mathematical arrays dynamically
x = np.linspace(-np.pi, np.pi * 3, 1000)
fourier_sum = np.zeros_like(x)

for n in range(1, max_n + 1, 2):
    fourier_sum += (4 / np.pi) * (np.sin(n * x) / n)
    
# Render the Plotly interface
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=np.sign(np.sin(x)), name="Ideal Square Wave", line=dict(color="black", dash="dash"), opacity=0.3))
fig.add_trace(go.Scatter(x=x, y=fourier_sum, name=f"Fourier Sum (N={max_n})", line=dict(color="#2A9D8F", width=2)))
fig.update_layout(xaxis_title="Time (rad)", yaxis_title="Amplitude", template="plotly_white", yaxis=dict(range=[-1.5, 1.5]), hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)