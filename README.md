# Lancers de pièce : TCL et Monte Carlo

L'objectif de ce répertoire est de résoudre un problème de probabilité classique d'abord de manière analytique (via le TCL), et ensuite de le vérifier par une simulation de Monte Carlo.

## Le problème
Si l'on lance une pièce de monnaie équilibrée 10 000 fois, quelle est la probabilité d'obtenir strictement plus de 5 200 faces ?
Ce problème permet de mettre en lumière la difficulté de capturer un événement rare et l'importance d'optimiser le code pour observer la convergence vers la LGN.

## Approche analytique
Soit $X$ le nombre de faces obtenues. $X$ suit une loi binomiale $\mathcal{B}(10000, 0.5)$.
* **Espérance** : $\mu = 5000$
* **Variance** : $\sigma^2 = 2500$ ($\sigma = 50$)

Le nombre de lancers étant grand, le **Théorème Central Limite (TCL)** nous permet d'approximer cette loi par une distribution normale : $X \sim \mathcal{N}(5000, 2500)$.

Pour trouver $P(X > 5200)$, nous calculons le Z-score, en appliquant la correction de continuité de Yates pour passer d'une loi discrète à continue :
$$Z_{corr} = \frac{5200.5 - 5000}{50} = 4.01$$

La probabilité théorique de cet événement est de l'ordre de **0.003%** (événement rare).

## Simulation
Pour prouver cette théorie, une simple simulation de 10 000 essais est insuffisante car l'événement est trop rare pour être capturé de manière fiable. 

Le script de vérification (`theorie_vs_pratique.py`) tire parti de la vectorisation de `NumPy` en C pour lancer **1 million de simulations** de 10 000 lancers en quelques secondes.

### Fichiers du projet
* `simulation.py` : Simule les lancers et trace la distribution empirique par rapport à la courbe normale théorique (via `Matplotlib`).
* `theorie_vs_pratique.py` : Compare la précision de la simulation de Monte Carlo (1M itérations) avec le résultat du Z-score exact.
* `requirements.txt` : Liste des dépendances.

## Installation & Exécution

1. Clonez ce dépôt :
```bash
git clone https://github.com/ls-leon/coin_flip_project.git
cd coin_flip_project
```
