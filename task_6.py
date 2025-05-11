items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget=100):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_cost = 0
    selected_items = {}

    while total_cost < budget:
        for item, details in sorted_items:
            if total_cost + details['cost'] <= budget:
                selected_items[item] = 1 if item not in selected_items else selected_items[item] + 1
                total_cost += details['cost']
                break

    return selected_items, total_cost


selected_items, total_cost = greedy_algorithm(items)
print("Greedy algorithm result:")
print("Goods to buy: ", selected_items)
print("Total cost: ", total_cost)


def dynamic_programming(items, budget=100):
    items = list(items.items())
    n = len(items)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_cost = items[i - 1][1]['cost']
        item_calories = items[i - 1][1]['calories']

        for w in range(budget + 1):
            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_calories)
            else:
                dp[i][w] = dp[i - 1][w]

    result = {}
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result[items[i - 1][0]] = 1 if items[i - 1][0] not in result else result[items[i - 1][0]] + 1
            w -= items[i - 1][1]['cost']

    return result, dp[n][budget]

items_to_by, total_calories = dynamic_programming(items)
print("Dynamic algorithm result:")
print("Goods to buy: ", items_to_by)
print("Total calories: ", total_calories)
