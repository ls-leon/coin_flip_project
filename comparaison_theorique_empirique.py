import numpy as np
from scipy.stats import norm

def calculate_theoretical_prob(n_flips=10000, threshold=5200, use_correction=True):
    mu = n_flips * 0.5
    sigma = np.sqrt(n_flips * 0.5 * 0.5)
    
    # correction de continuité
    if use_correction:
        z_score = (threshold + 0.5 - mu) / sigma
    else:
        z_score = (threshold - mu) / sigma
        
    # P(X > 5200) = 1 - P(X <= 5200)
    prob = 1 - norm.cdf(z_score)
    return prob

def empirical_prob(n_flips=10000, n_trials=1000000, threshold=5200):
    # on utilise 1 million de simulations pour avoir une bonne estimation d'un event rare
    print(f"Lancement de {n_trials:,} simulations")
    
    # optimisation mémoire: au lieu de garder tous les lancers, on tire directement de la binomiale
    outcomes = np.random.binomial(n=n_flips, p=0.5, size=n_trials)
    
    successes = np.sum(outcomes > threshold)
    return successes / n_trials

if __name__ == "__main__":
    n_flips = 10000
    threshold = 5200
    
    # calcul Analytique
    prob_theory = calculate_theoretical_prob(n_flips, threshold, use_correction=False)
    prob_theory_corr = calculate_theoretical_prob(n_flips, threshold, use_correction=True)
    
    # simulation empirique (1 million de tests)
    prob_empirique = empirical_prob(n_flips, n_trials=1000000, threshold=threshold)
    
    print("RÉSULTATS : PROBABILITÉ D'AVOIR > 5200 FACES")
    print("-" * 40)
    print(f"Théorique (TCL, sans correction) : {prob_theory:.8f} ({prob_theory*100:.6f}%)")
    print(f"Théorique (TCL, avec correction) : {prob_theory_corr:.8f} ({prob_theory_corr*100:.6f}%)")
    print(f"Empirique (Monte carlo 1M tests)  : {prob_empirique:.8f} ({prob_empirique*100:.6f}%)")
    print("-" * 40)