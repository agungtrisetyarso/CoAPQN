import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# ====================== Quantum Phase-Space Representations ======================
def wigner_function(alpha, decay=0.0):
    """Wigner function for a damped coherent-like state"""
    r2 = np.abs(alpha)**2 * np.exp(-decay)
    return (2 / np.pi) * np.exp(-2 * r2)

def glauber_sudarshan_p(alpha, n=2, decay=0.0):
    """Approximate Glauber-Sudarshan P-representation (highly singular for non-classical states)"""
    r2 = np.abs(alpha)**2
    # Simplified model: mixture of coherent states with decay
    p = (1 / np.pi) * np.exp(-r2) * (np.exp(-decay * r2) + 0.3 * np.sin(3 * np.angle(alpha))**2)
    return np.maximum(p, -0.5)  # can be negative (non-classical indicator)

def plot_phase_space(func, title, decay=0.0, cmap='RdBu_r'):
    x = np.linspace(-3.5, 3.5, 120)
    X, Y = np.meshgrid(x, x)
    Z = np.vectorize(lambda re, im: func(complex(re, im), decay=decay))(X, Y)
    
    plt.contourf(X, Y, Z, levels=60, cmap=cmap)
    plt.colorbar(label='Quasi-Probability')
    plt.xlabel(r'Re($\alpha$)')
    plt.ylabel(r'Im($\alpha$)')
    plt.title(title)
    plt.grid(False)

# ====================== Dramatic Visualization ======================
def generate_dramatic_phase_space():
    plt.figure(figsize=(15, 10))
    
    # Row 1: Wigner Function
    plt.subplot(2, 3, 1)
    plot_phase_space(wigner_function, "Wigner - Initial High Fidelity", decay=0.0)
    
    plt.subplot(2, 3, 2)
    plot_phase_space(wigner_function, "Wigner - After Decoherence", decay=1.2)
    
    plt.subplot(2, 3, 3)
    plot_phase_space(wigner_function, "Wigner - After PAD-ER Recovery", decay=0.15)
    
    # Row 2: Glauber-Sudarshan P-Representation
    plt.subplot(2, 3, 4)
    plot_phase_space(glauber_sudarshan_p, "Glauber-Sudarshan P\nInitial Entanglement", decay=0.0, cmap='viridis')
    
    plt.subplot(2, 3, 5)
    plot_phase_space(glauber_sudarshan_p, "Glauber-Sudarshan P\nStrong Decoherence", decay=1.5, cmap='viridis')
    
    plt.subplot(2, 3, 6)
    plot_phase_space(glauber_sudarshan_p, "Glauber-Sudarshan P\nPAD-ER Optimized", decay=0.2, cmap='viridis')
    
    plt.suptitle("Phase-Space Evolution in Perishable Entanglement Routing\n"
                 "Wigner Function vs. Glauber-Sudarshan P-Representation", fontsize=16, y=0.98)
    plt.tight_layout()
    plt.savefig('glauber_wigner_evolution.png', dpi=300, bbox_inches='tight')
    print("✅ Dramatic phase-space plots saved: glauber_wigner_evolution.png")

generate_dramatic_phase_space()
