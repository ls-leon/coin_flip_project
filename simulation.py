import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def run_simulation(n_flips=10000, n_trials=10000):
    """
    Simule n_trials expériences de n_flips lancers de pièce.
    """
    print(f"Simulation de {n_trials} séries de {n_flips} lancers...")
    # génère une matrice de lancers (0 ou 1) et somme chaque ligne
    # 1 = Face , 0 = Pile 
    flips = np.random.binomial(n=n_flips, p=0.5, size=n_trials)
    
    return flips

def plot_distribution(outcomes, n_flips):
    plt.figure(figsize=(10, 6))
    
    # histogramme empirique
    count, bins, ignored = plt.hist(outcomes, bins=50, density=True, 
                                    alpha=0.6, color='b', edgecolor='black', label='Distribution empirique')
    
    # courbe théorique (TCL)
    mu = n_flips * 0.5
    sigma = np.sqrt(n_flips * 0.5 * 0.5)
    
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, sigma)
    
    plt.plot(x, p, 'k', linewidth=2, label=fr'TCL: Théorie normale $\mathcal{{N}}({mu:.0f}, {sigma**2:.0f})$')
    plt.axvline(x=5200, color='r', linestyle='--', label='Seuil > 5200')
    
    plt.title("Distribution des faces sur 10 000 lancers")
    plt.xlabel("Nombre de faces")
    plt.ylabel("Densité de probabilité")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

if __name__ == "__main__":
    outcomes = run_simulation()
    plot_distribution(outcomes, 10000)