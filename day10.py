#!/usr/bin/env python3
import numpy as np
from collections import deque
from scipy.optimize import milp, LinearConstraint, Bounds

f = open("2025/ressources/day10.txt", "r") #Open File
lines = f.readlines() #Separate in lines

# Parse Input
leds = list()
buttons = list()
voltages = list()

for line in lines:
    line = line.replace("\n", "")
    parts = line.split(" ")
    
    led = parts[0]
    voltage = parts[-1]
    button = parts[1:-1]

    led = led.replace("[", "").replace("]", "").replace("#", "1").replace(".", "0")
    led = list(led)
    led = np.array(led, dtype=int)
    led = np.where(led == 1)[0]
    led = set(led)

    for i, b in enumerate(button):
        b = b.replace("(", "").replace(")", "")
        b = np.array(b.split(","), dtype=int)
        button[i] = set(b)
    
    voltage = voltage.replace("{", "").replace("}", "")
    voltage = np.array(voltage.split(","), dtype=int)

    leds.append(led)
    buttons.append(button)
    voltages.append(voltage)

# Q1
def bfs(led, buttons, desiredled):
    queue = deque()
    visited = set()
    queue.append((led, 0))
    visited.add(tuple(sorted(led)))
    
    while queue:
        current_led, depth = queue.popleft()
        if current_led == desiredled:
            return depth
        for b in buttons:
            new_led = current_led ^ b
            led_tuple = tuple(sorted(new_led))
            if led_tuple not in visited:
                visited.add(led_tuple)
                queue.append((new_led, depth + 1))
    return np.inf

total_press = 0
for led, button, voltage in zip(leds, buttons, voltages):
    presses = bfs(set(), button, led)
    total_press += presses
print("The total number of button presses is: {}".format(total_press))

# Q2
total_press = 0

def solve_integer_minimal(modified_button, voltage):
    A = modified_button.T.astype(float)
    b = voltage.astype(float)

    m, n = A.shape

    c = np.ones(n)

    constraint = LinearConstraint(A, lb=b, ub=b)

    bounds = Bounds(lb=np.zeros(n), ub=np.inf)

    integrality = np.ones(n, dtype=int)

    result = milp(c=c,
                constraints=constraint,
                bounds=bounds,
                integrality=integrality)

    if result.success:
        return np.round(result.x).astype(int)
    else:
        return None



for led, button, voltage in zip(leds, buttons, voltages):
    modified_button = np.zeros((len(button), len(voltage)), dtype=int)
    for i, b in enumerate(button):
        new_button = np.zeros_like(voltage)
        new_button[list(b)] = 1
        modified_button[i] = new_button
    sol = solve_integer_minimal(modified_button, voltage)
    presses = np.sum(sol)
    total_press += presses
    
print("The total number of button presses for the correct voltage is: {}".format(total_press))