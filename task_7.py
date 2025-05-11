import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls=100_000):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    probabilities = {total: (count / num_rolls) for total, count in sum_counts.items()}
    print(probabilities)
    return sum_counts, probabilities


def print_probability_table(sum_counts, probabilities):
    print("Sum | Count     | Probability")
    print("-----------------------------")
    for total in range(2, 13):
        count = sum_counts[total]
        prob = probabilities[total]
        print(f"{total:>3} | {count:>9} | {prob:.3%}")


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(sums, probs, color='#1296F0', edgecolor='black')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Monte Carlo Simulation: Dice Roll Sums')
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.001, f'{yval:.3%}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


sum_counts, probabilities = simulate_dice_rolls(100_000)
print_probability_table(sum_counts, probabilities)
plot_probabilities(probabilities)
