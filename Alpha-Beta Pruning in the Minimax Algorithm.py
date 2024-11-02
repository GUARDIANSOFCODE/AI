import math

# Sample game tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': -1, 'E': 3, 'F': 5, 'G': -2
}

# Minimax with Alpha-Beta Pruning
def minimax(node, depth, is_maximizing, alpha, beta):
    if node not in tree:
        return node  # Terminal node
    
    if is_maximizing:
        max_eval = -math.inf
        for child in tree[node]:
            eval = minimax(child, depth + 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for child in tree[node]:
            eval = minimax(child, depth + 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Testing Alpha-Beta Pruning
print("Optimal value:", minimax('A', 0, True, -math.inf, math.inf))
