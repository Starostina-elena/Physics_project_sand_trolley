import numpy as np

def calculate_graph_data(m0, F, mu, t_max, steps=100):
    t = np.linspace(0, t_max, steps)
    m_t = m0 - mu * t
    v_t = (F / mu) * np.log(m0 / m_t)
    a_t = F / m_t
    x_t = (F / mu) * (t - (m0 / mu) * np.log(m0 / m_t))
    return {"t": t.tolist(), "m_t": m_t.tolist(), "v_t": v_t.tolist(), "a_t": a_t.tolist(), "x_t": x_t.tolist()}
