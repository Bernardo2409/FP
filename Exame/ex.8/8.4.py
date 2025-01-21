import matplotlib.pyplot as plt

def desenhar_reta(x1, y1, x2, y2):
    if x1 == x2:
        # Linha vertical
        x = [x1] * 100  # Mantém o mesmo x
        y = [y1 + (y2 - y1) * i / 99 for i in range(100)]
    else:
        # Coeficiente angular (m)
        m = (y2 - y1) / (x2 - x1)
        # Gera valores de x
        x = [x1 + (x2 - x1) * i / 99 for i in range(100)]
        # Calcula os valores de y usando a equação da reta
        y = [m * (xi - x1) + y1 for xi in x]

    # Desenhar a reta
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f"Reta entre ({x1},{y1}) e ({x2},{y2})")
    plt.scatter([x1, x2], [y1, y2], color="red", label="Pontos")
    plt.axhline(0, color="black",linewidth=0.5)  # Eixo x
    plt.axvline(0, color="black",linewidth=0.5)  # Eixo y
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.title("Reta a partir de dois pontos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

# Exemplo de uso
desenhar_reta(1, 2, 4, 5)
