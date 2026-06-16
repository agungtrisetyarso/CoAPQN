# CoAPQN: Competitive Analysis of Online Perishable Entanglement Routing in Quantum Networks

[![arXiv](https://img.shields.io/badge/arXiv-Paper-blue)](https://arxiv.org/abs/YOUR_ARXIV_ID)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the simulation code accompanying the paper:

> **Competitive Analysis of Online Perishable Entanglement Routing in Quantum Networks: A Corrected Primal-Dual Approach**

**Authors:** Agung Trisetyarso, Lenny Putri Yulianti, Kridanto Surendro

---

## Overview

This work provides a **corrected and rigorous competitive analysis** of the Perishability-Aware Primal-Dual Entanglement Routing (PAD-ER) algorithm for online entanglement routing in quantum repeater networks with decohering quantum memories.

### Key Contributions

- Establishes a fundamental **deterministic vs. randomized dichotomy**: deterministic algorithms are Θ(Λ)-competitive, while fractional/randomized primal-dual algorithms (PAD-ER) achieve Θ(log Λ)-competitiveness.
- Proves that the **perishability rate γ does not appear** in the competitive ratio (it only affects the regime where the lower bound becomes active).
- Provides a rigorous **dual-fitting proof** that explicitly tracks the decay factor \(e^{-\gamma \Delta t}\) and shows it telescopes cleanly.
- Introduces **path-correlated pricing** to eliminate bottleneck interference in multi-hop networks and restore the single-link competitive ratio.
- Extensive Monte Carlo simulations validating all theoretical results.

---

## Repository Structure
