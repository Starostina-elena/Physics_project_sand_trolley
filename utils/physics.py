import numpy as np


def calculate_graph_data(m0, F, mu, m_end):
    # Время до достижения конечной массы
    t_max = (m0 - m_end) / mu

    # Временная ось
    t = np.linspace(0, t_max, round(t_max / 0.1))
    print(t)

    # Масса в момент времени t
    m_t = m0 - mu * t

    # Скорость в момент времени t
    v_t = (F / mu) * np.log(m0 / m_t)

    # Ускорение в момент времени t
    a_t = F / m_t

    # Позиция в момент времени t
    x_t = abs((F / mu) * (t - (m0 / mu) * np.log(m0 / m_t)))

    return {
        "t": t.tolist(),
        "m_t": m_t.tolist(),
        "v_t": v_t.tolist(),
        "a_t": a_t.tolist(),
        "x_t": x_t.tolist()
    }
