import numpy as np


def calculate_graph_data(m0, F, mu, l, steps=100):
    # Вычисление времени, необходимого для того, чтобы масса уменьшилась до m_end
    t_max = (m0 - m0 * 0.8) / mu  # Время для того, чтобы масса уменьшилась до 80% от начальной

    # Временная ось
    t = np.linspace(0, t_max, steps)

    # Масса в момент времени t
    m_t = m0 - mu * t

    # Скорость в момент времени t
    v_t = (F / mu) * np.log(m0 / m_t)

    # Ускорение в момент времени t
    a_t = F / m_t

    # Позиция в момент времени t
    x_t = (F / mu) * (t - (m0 / mu) * np.log(m0 / m_t))

    return {
        "t": t.tolist(),
        "m_t": m_t.tolist(),
        "v_t": v_t.tolist(),
        "a_t": a_t.tolist(),
        "x_t": x_t.tolist()
    }
