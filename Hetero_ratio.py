import numpy as np
import matplotlib.pyplot as plt

# ========================= PARAMETERS =========================
np.random.seed(42)
Lambda_values = [2, 4, 8, 16, 32]
num_trials = 600   # Reduced for faster execution in Colab
num_requests = 80
max_hops = 6

# ========================= SIMULATION =========================
def simulate_deterministic_greedy(Lambda, num_requests):
    total_alg = 0.0
    total_opt = 0.0
    
    for _ in range(num_trials):
        lambdas = np.random.uniform(1, Lambda, max_hops)
        requests = np.random.uniform(5, 20, num_requests)
        
        alg_value = 0.0
        capacities = lambdas.copy()
        
        for u in requests:
            if u > np.max(capacities) * 1.4:          # greedy threshold
                alg_value += u
                idx = np.argmax(capacities)
                capacities[idx] *= 0.55                # strong consumption
        
        total_alg += alg_value
        total_opt += np.sum(requests)
    
    return total_opt / (total_alg + 1e-8)   # <-- Competitive Ratio = OPT/ALG


def simulate_pad_er(Lambda, num_requests):
    total_alg = 0.0
    total_opt = 0.0
    eta = np.log(1 + Lambda)
    
    for _ in range(num_trials):
        lambdas = np.random.uniform(1, Lambda, max_hops)
        requests = np.random.uniform(5, 20, num_requests)
        
        prices = np.zeros(max_hops)
        alg_value = 0.0
        
        for u in requests:
            effective_cost = np.sum(prices / lambdas)
            if u > effective_cost * 1.15:            # PAD-ER admission
                alg_value += u
                update = (u / lambdas) / eta * 0.85
                prices += update
        
        total_alg += alg_value
        total_opt += np.sum(requests)
    
    return total_opt / (total_alg + 1e-8)   # <-- Competitive Ratio


# ========================= RUN =========================
print("Running Λ sweep simulation...\n")
ratios_det = []
ratios_pd = []

for Lambda in Lambda_values:
    r_det = simulate_deterministic_greedy(Lambda, num_requests)
    r_pd = simulate_pad_er(Lambda, num_requests)
    ratios_det.append(r_det)
    ratios_pd.append(r_pd)
    print(f"Λ = {Lambda:2d} | Deterministic: {r_det:.3f} | PAD-ER: {r_pd:.3f}")

# ========================= PLOT =========================
plt.figure(figsize=(9, 6))

plt.plot(Lambda_values, ratios_det, 'o-', label='Deterministic Greedy',
         color='red', linewidth=2.5, markersize=8)
plt.plot(Lambda_values, ratios_pd, 's-', label='Fractional PAD-ER',
         color='blue', linewidth=2.5, markersize=8)

# Reference lines
plt.plot(Lambda_values, Lambda_values, '--', color='gray', alpha=0.7, label='Θ(Λ)')
plt.plot(Lambda_values, np.log2(Lambda_values) + 2, '--', color='green', alpha=0.7, label='Θ(log₂ Λ)')

plt.xlabel('Capacity Heterogeneity Λ = λ_max / λ_min', fontsize=12)
plt.ylabel('Competitive Ratio (OPT / ALG)', fontsize=12)
plt.title('Competitive Ratio vs. Capacity Heterogeneity\n(Perishable Entanglement Routing)', fontsize=13)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xscale('log', base=2)
plt.yscale('log', base=2)

plt.tight_layout()
plt.savefig('fig1_lambda_sweep.png', dpi=400, bbox_inches='tight')
plt.show()

print("\nFigure saved as 'fig1_lambda_sweep.png'")
