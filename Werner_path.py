import numpy as np
import matplotlib.pyplot as plt

# ========================= PARAMETERS =========================
delta_t = np.linspace(0, 6, 300)  # Hold time in decoherence units
w_values = [1.0, 0.8, 0.6, 0.4]   # Different path Werner parameters
gamma = 1.0                       # Decoherence rate

# ========================= FIDELITY CALCULATION =========================
def fidelity(w_R, delta_t, gamma):
    return (3 * w_R * np.exp(-gamma * delta_t) + 1) / 4

# ========================= PLOT =========================
plt.figure(figsize=(9, 6))

colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']
labels = [f'$w_R = {w:.1f}$' for w in w_values]

for i, w in enumerate(w_values):
    F = fidelity(w, delta_t, gamma)
    plt.plot(delta_t, F, linewidth=2.8, color=colors[i], label=labels[i])

# Utility domain boundary (F = 0.5)
plt.axhline(y=0.5, color='red', linestyle='--', linewidth=1.8, 
            label='$F = 1/2$ (utility domain boundary)')

# Fully mixed floor
plt.axhline(y=0.25, color='gray', linestyle=':', linewidth=1.5, alpha=0.8,
            label='$F = 1/4$ (fully-mixed floor)')

plt.xlabel('Hold Time $\\Delta t$ (decoherence units)', fontsize=12)
plt.ylabel('Delivered Fidelity $F_R(\\Delta t)$', fontsize=12)
plt.title('Perishability: Fidelity Decay for Different Path Werner Parameters', fontsize=13)

plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Annotations
plt.annotate('PAD-ER prioritizes delivery\nwhile $F$ is high', 
             xy=(1.2, 0.75), xytext=(2.5, 0.85),
             arrowprops=dict(arrowstyle='->', color='blue'), fontsize=10)

plt.tight_layout()
plt.savefig('fig3_fidelity_decay.png', dpi=400, bbox_inches='tight')
plt.show()

print("Figure saved as 'fig3_fidelity_decay.png'")
