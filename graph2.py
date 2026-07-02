import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🔺 Triangle Wave Approximation")
st.write("Because the harmonics drop off much faster ($1/n^2$), the triangle wave converges with far fewer terms.")

max_n = st.sidebar.slider("Max Harmonic Order (N)", min_value=1, max_value=29, value=1, step=2)

x = np.linspace(-np.pi, np.pi * 3, 1000)
fourier_sum = np.zeros_like(x)

for n in range(1, max_n + 1, 2):
    term = (8 / (np.pi ** 2)) * (np.sin(n * x) / (n ** 2))
    if ((n - 1) // 2) % 2 == 1:
        fourier_sum -= term
    else:
        fourier_sum += term
        
def ideal_triangle(t):
    return (2 / np.pi) * np.arcsin(np.sin(t))
    
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=ideal_triangle(x), name="Ideal Triangle Wave", line=dict(color="black", dash="dash"), opacity=0.3))
fig.add_trace(go.Scatter(x=x, y=fourier_sum, name=f"Fourier Sum (N={max_n})", line=dict(color="#E76F51", width=2)))
fig.update_layout(xaxis_title="Time (rad)", yaxis_title="Amplitude", template="plotly_white", yaxis=dict(range=[-1.2, 1.2]), hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)