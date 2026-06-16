import numpy as np
import matplotlib.pyplot as plt

# ========================= PARAMETERS =========================
np.random.seed(42)
Lambda = 7.0
num_hops_list = [1, 3, 5, 7, 10, 15, 20]
num_trials = 300          # Increase for smoother curves
num_requests = 60

# ========================= SIMULATION =========================
def generate_requests(num_requests, max_hops):
    requests = []
    for _ in range(num_requests):
        length = np.random.randint(1, max_hops + 1)
        # Longer paths have higher potential utility (non-linear)
        utility = np.random.uniform(5.0, 15.0) * np.sqrt(length)
        requests.append({'length': length, 'utility': utility})
    return requests

def simulate_independent(num_hops, num_requests):
    total_alg = 0.0
    total_opt = 0.0
    
    for _ in range(num_trials):
        requests = generate_requests(num_requests, num_hops)
        prices = np.zeros(num_hops)
        alg_value = 0.0
        
        for req in requests:
            L = req['length']
            path_prices = prices[:L]
            avg_price = np.mean(path_prices) if L > 0 else 0
            
            # Independent pricing suffers from bottleneck interference
            effective_cost = avg_price * (1 + 0.6 * L)
            
            if req['utility'] > effective_cost * 1.4:
                alg_value += req['utility']
                # Local update with noise (interference)
                update = req['utility'] / L * np.random.uniform(0.7, 1.3, L)
                prices[:L] += update
        
        total_alg += alg_value
        total_opt += sum(r['utility'] for r in requests)
    
    return total_alg / (total_opt + 1e-8)

def simulate_correlated(num_hops, num_requests):
    total_alg = 0.0
    total_opt = 0.0
    
    for _ in range(num_trials):
        requests = generate_requests(num_requests, num_hops)
        prices = np.zeros(num_hops)
        alg_value = 0.0
        
        for req in requests:
            L = req['length']
            avg_price = np.mean(prices[:L]) if L > 0 else 0
            
            # Path-correlated pricing
            if req['utility'] > avg_price * L * 1.15:
                alg_value += req['utility']
                # Global correlated update
                update = req['utility'] / L
                prices[:L] += update
        
        total_alg += alg_value
        total_opt += sum(r['utility'] for r in requests)
    
    return total_alg / (total_opt + 1e-8)

# ========================= RUN =========================
print("Running multi-hop simulations...\n")
ratios_ind = []
ratios_cor = []

for hops in num_hops_list:
    r_ind = simulate_independent(hops, num_requests)
    r_cor = simulate_correlated(hops, num_requests)
    ratios_ind.append(r_ind)
    ratios_cor.append(r_cor)
    print(f"Hops: {hops:2d} | Independent: {r_ind:.3f} | Correlated: {r_cor:.3f}")

# ========================= PLOT =========================
plt.figure(figsize=(8, 5.5))
plt.plot(num_hops_list, ratios_ind, 'o-', label='Independent Pricing', 
         color='red', linewidth=2.5, markersize=6)
plt.plot(num_hops_list, ratios_cor, 's-', label='Path-Correlated Pricing', 
         color='blue', linewidth=2.5, markersize=6)

plt.xlabel('Number of Hops')
plt.ylabel('Competitive Ratio')
plt.title(f'Path Competitive Ratio vs. Number of Hops ($\Lambda = {Lambda}$)')
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(num_hops_list)

plt.tight_layout()
plt.savefig('fig_interference.png', dpi=400, bbox_inches='tight')
plt.show()

print("\nFigure saved as 'fig_interference.png'")
