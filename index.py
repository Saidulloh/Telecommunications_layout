import matplotlib.pyplot as plt
import numpy as np
import random


class CityGrid:

    _, ax = plt.subplots()
    ax.grid()
    
    def __init__(self, x_label, y_label, title) -> None:
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

    def set_obstacles(self, proc, end_number):   
        # Plot the data, set the size/размер (s), color and transparency/прозначность (alpha) of the points
        global numbers_for_x 
        global numbers_for_y 
        numbers_for_x = [random.uniform(1, end_number) for i in range((proc*end_number//100)*100)]
        numbers_for_y = [random.uniform(1, end_number) for i in range((proc*end_number//100)*100)]
        for i in range(0, len(numbers_for_x)):
            self.ax.scatter(x=numbers_for_x[i], y=numbers_for_y[i], s = 50, color = 'black', alpha = 1)

    def place_tower(self, proc, end_number):
        tower_number_x = []
        tower_number_y = []
        seventy_proc = (proc * end_number // 100) * 100
        while len(tower_number_x) < seventy_proc:
            random_number_x = random.uniform(1, end_number)
            if random_number_x not in numbers_for_x:
                if random_number_x not in tower_number_x:
                    if len(tower_number_x) <= seventy_proc:
                        tower_number_x.append(random_number_x)
            continue 

        while len(tower_number_y) < seventy_proc:
            random_number_y = random.uniform(1, end_number)
            if random_number_y not in numbers_for_y:
                if random_number_y not in tower_number_y:
                    if len(tower_number_y) <= seventy_proc:
                        tower_number_y.append(random_number_y)
            continue

        for i in range(0, len(tower_number_x)):
            self.ax.scatter(x=tower_number_x[i], y=tower_number_y[i], s = 50, color = 'red', alpha = 1)

    def end(self):
        # Label the axes and provide a title
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)

city = CityGrid('x', 'y', 'Telecommunication circuitries of New York ')
city.set_obstacles(30, 10)
city.place_tower(70, 10)
city.end()

plt.show()
