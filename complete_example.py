"""Complete example of use of the simulator.

To run, use 'python3 complete_example.py'.

This example uses the OpenMP Static scheduler to map tasks to
resource following a round-robin and a compact fashion.
The results in both cases are plotted.
"""

import simulator.schedulers as schedulers
import simulator.support as support
from simulator.simulator import simulate


print("Scenario 1: round-robin scheduler")
# Setup
num_tasks = 10
num_resources = 3
task_loads = [i+1 for i in range(num_tasks)]
round_robin = schedulers.OpenMPStatic(task_loads, num_resources, 1)
# Simulates
result = simulate(task_loads, num_resources, round_robin, True)
# Presents an analysis of the results
print(f'- Calls to the scheduler: {result[2]}')
print(f'- Changes of resources between contiguous tasks: {result[3]}')
mapping = result[0]
support.evaluate_mapping(mapping, task_loads, num_resources)
# Plots the resulting mapping and saves it to a file
support.plot_mapping(mapping, task_loads, num_resources, 'rr.png')

print("Scenario 2: compact scheduler")
compact = schedulers.OpenMPStatic(task_loads, num_resources, 0)
# Simulates
result = simulate(task_loads, num_resources, compact, True)
# Presents an analysis of the results
print(f'- Calls to the scheduler: {result[2]}')
print(f'- Changes of resources between contiguous tasks: {result[3]}')
mapping = result[0]
support.evaluate_mapping(mapping, task_loads, num_resources)
# Plots the resulting mapping and saves it to a file
support.plot_mapping(mapping, task_loads, num_resources, 'compact.png')
