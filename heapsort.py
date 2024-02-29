import heapq

def minimize_cost(cables):
    heapq.heapify(cables)  # перетворюємо список на піраміду

    total_cost = 0

    while len(cables) > 1:
        # Беремо два найменших кабелі і об'єднуємо їх
        min1 = heapq.heappop(cables)
        min2 = heapq.heappop(cables)
        cost = min1 + min2
        total_cost += cost

        # Додаємо новий кабель до списку
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [8, 4, 6, 12]
min_cost = minimize_cost(cables)
print("Мінімальні загальні витрати:", min_cost)