# Import seaborn
import seaborn as sns
import matplotlib

# Apply the default theme
# sns.set_theme()

# # Load an example dataset
# tips = sns.load_dataset("tips")
# print(tips)
# # Create a visualization
# sns.relplot(
#     data=tips,
#     x="total_bill", y="tip",
#     hue="smoker", style="smoker", size="size",
# )


import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class CityGrid:
    def __init__(self, rows, cols, block_density=0.3):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]  # 0 represents unblocked, 1 represents blocked
        self.block_density = block_density

        self._generate_blocks()

    def _generate_blocks(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < self.block_density:
                    self.grid[i][j] = 1

    def place_tower(self, row, col, range_radius):
        # Check if the tower can be placed at the given location
        if not (0 <= row < self.rows and 0 <= col < self.cols) or self.grid[row][col] == 1:
            print("Cannot place tower at the specified location.")
            return

        # Mark the tower coverage area
        for i in range(max(0, row - range_radius), min(self.rows, row + range_radius + 1)):
            for j in range(max(0, col - range_radius), min(self.cols, col + range_radius + 1)):
                self.grid[i][j] = 2  # 2 represents tower coverage

    def visualize_grid(self):
        fig, ax = plt.subplots()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 1:
                    rect = patches.Rectangle((j, i), 1, 1, linewidth=1, edgecolor='black', facecolor='gray')
                    ax.add_patch(rect)
                elif self.grid[i][j] == 2:
                    rect = patches.Rectangle((j, i), 1, 1, linewidth=1, edgecolor='black', facecolor='red', alpha=0.5)
                    ax.add_patch(rect)

        plt.xlim(0, self.cols)
        plt.ylim(0, self.rows)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

# Пример использования класса
city = CityGrid(rows=10, cols=10)
city.visualize_grid()

city.place_tower(3, 5, 2)
city.visualize_grid()
matplotlib.pyplot.show()