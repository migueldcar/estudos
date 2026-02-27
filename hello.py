def pressao_hidrostatica(altura_m: float) -> float:
    """
    Retorna pressão hidrostática aproximada em bar (gauge),
    considerando água e g ≈ 9,81 m/s².
    """
    rho = 1000  # kg/m³
    g = 9.81    # m/s²
    p_pa = rho * g * altura_m
    p_bar = p_pa / 1e5
    return p_bar

if __name__ == "__main__":
    h = 3.0
    print(f"Para h={h} m, pressão ≈ {pressao_hidrostatica(h):.3f} bar")