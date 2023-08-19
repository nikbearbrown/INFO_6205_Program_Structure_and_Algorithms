---
Author: Dhanush Kumar Shankar
NUID: 002932182
Date: 08/18/2023
Topics covered: Local search, Gradient descent, Metropolis, Simulated Annealing, Hopfield Nets
---



## Text Book Definition
A Local Search Algorithm is a type of **optimization technique** used in computer science and artificial intelligence to solve optimization problems. It is a heuristic search method that iteratively explores the solution space by making incremental changes to a current solution and evaluating the quality of these changes. The goal of a local search algorithm is to find a solution that is locally optimal within a specific neighborhood of the solution space.

>🤔 You probably might have a hard time understanding what the above definition means...

## In ElI5 Terms
Imagine you're in a huge maze, and you want to find the best way out. The maze is so big that it would take forever to check every single path. So, instead, you decide to use a special trick called a Local Search Algorithm.

Here's how it works: You start at a spot in the maze, and you look around at the paths nearby. You pick one path that looks promising, and you take a step in that direction. You keep doing this, taking small steps and always choosing the path that seems better than where you are right now.

The trick is that you're not trying to find the absolute best way out of the entire maze – that would take too long. Instead, you're just trying to find the best way out of the area you're in at the moment. It's like you're finding the best "local" solution in the part of the maze you're exploring.

This method helps you find a pretty good way out of the maze much faster than if you tried every path. However, there's a catch: sometimes, you might get stuck in a part of the maze that seems good, but it's not the very best way out of the whole maze. That's the trade-off for being quicker.

So, a Local Search Algorithm is like a smart way to solve tough puzzles when you can't check everything. It's like taking small steps and always going in the direction that looks better, even if you might not end up finding the very best answer.

![Maze](Maze.png)

> 🔁 Now try reading the text book definition again and see if you are able to understand it now.

## Need for Local Search
 - Local search is needed when dealing with complex optimization problems where finding a [global optimum](https://en.wikipedia.org/wiki/Global_optimization) is computationally infeasible or extremely time-consuming.
 - In such cases, local search aims to find a reasonably good solution within a reasonable amount of time, even if it might not be the absolute best solution.

## Working of a Local Search Algorithm
1. **Initialization**: The algorithm starts with an initial solution to the problem. This solution can be generated randomly or using a heuristic.
2. **Evaluation**: The quality of the initial solution is evaluated using an objective function. The objective function measures how good the solution is, based on the problem constraints and requirements.
3. **Neighborhood search**: The algorithm generates neighboring solutions by making small modifications to the current solution. These modifications can be random or guided by heuristics.
4. **Selection**: The neighboring solutions are evaluated using the objective function, and the best solution is selected as the new current solution.
5. **Termination**: The algorithm terminates when a stopping criterion is met. This criterion can be a maximum number of iterations, a threshold value for the objective function, or a time limit.
6. **Solution**: The final solution is the best solution found during the search process.

![Local Search](<Local search.png>) 

### Pseudocode for Local Search

```
function LocalSearch(initialSolution):
    currentSolution = initialSolution
    bestSolution = initialSolution

    while termination condition is not met:
        neighbors = generateNeighbors(currentSolution)
        
        for neighbor in neighbors:
            if evaluation(neighbor) > evaluation(currentSolution):
                currentSolution = neighbor
                
                if evaluation(neighbor) > evaluation(bestSolution):
                    bestSolution = neighbor
                break
        
        if no improving neighbor is found:
            return bestSolution
    
    return bestSolution
```

Explanation of the pseudocode steps:

1. **Initialization:** Start with an initial solution as the current and best solution.
2. **Termination Condition:** Continue the loop until a certain stopping condition is met, such as a maximum number of iterations or a predefined convergence criterion.
3. **Generate Neighbors:** Generate a set of neighboring solutions based on the current solution. Neighbors are solutions that are slightly different from the current one.
4. **Iterate Through Neighbors:** Iterate through the generated neighbors.
5. **Evaluation:** For each neighbor, evaluate its quality using an evaluation function that measures how good the solution is (e.g., a fitness function). If the neighbor's evaluation is better than the current solution's evaluation, move to the neighbor.
6. **Update Best Solution:** If the neighbor's evaluation is better than the best solution's evaluation so far, update the best solution to the neighbor.
7. **Break if Improvement:** If an improving neighbor is found, break the loop and start the next iteration.
8. **No Improving Neighbor:** If no improving neighbor is found, return the best solution found so far.
9. **Return Solution:** After the termination condition is met, return the best solution found during the search.

## Local Search and Its Connection to Optimization Problems
Local search is a powerful tool in the realm of optimization problems. It offers a practical approach to navigating the vast solution space that optimization problems often present. While exhaustively exploring every possible solution is often impractical or computationally infeasible, local search algorithms tackle this challenge by focusing on improving solutions within localized regions. Let's delve deeper into how local search connects with optimization problems:

1. **Navigating Complex Solution Spaces:** In many optimization problems, the number of possible solutions is enormous. Think of it like finding the highest point on a mountain range covered in fog – you can't see the entire landscape, but you can explore the terrain around you. Local search allows you to take small steps in the solution space, continuously adjusting your path to ascend towards better solutions.
2. **Local vs. Global Optima:** Optimization problems typically seek the best possible solution, either by maximizing or minimizing an objective function. A global optimum is the best solution across the entire solution space, while a local optimum is the best within a specific region. Local search algorithms focus on identifying these local optima – the highest peaks within the fog – which may not be the highest peaks globally.
3. **Trade-offs for Efficiency:** Local search algorithms make a trade-off between efficiency and optimality. While they may not always lead to the absolute best solution, they can quickly guide you to good solutions without exhaustively evaluating every possibility. This efficiency is especially valuable when dealing with complex problems, such as routing optimization, machine learning model training, or game strategy planning.

## Types of Local Search Algorithms
### Gradient Descent
---
- Gradient Descent is an optimization technique used to find the minimum (or maximum) of a function. It's like finding the lowest point in a hilly terrain while wearing a blindfold. You start at a random point and iteratively take steps in the direction of the steepest decrease (negative gradient) of the function to reach the bottom of the hill.
- In optimization problems, the "hill" represents the objective function you want to minimize, and the "steps" correspond to adjusting the parameters of the function's input. Gradient Descent is a local search because it focuses on finding the lowest point within a small region of the function's landscape.

![Gradient_descent](<Gradient descent.png>)

**Connection to Local Search:**
<br>
Gradient Descent is a classic example of a local search algorithm. Instead of trying every possible input value (which might be infeasible for complex functions), it progressively approaches a locally optimal solution. However, it can get trapped in local minima, which are the lowest points in a specific neighborhood, without finding the global minimum.

**Python Implementation**

```python
def gradient_descent(initial_value, learning_rate, num_iterations):
    current_value = initial_value
    
    for _ in range(num_iterations):
        gradient = compute_gradient(current_value)
        current_value = current_value - learning_rate * gradient
    
    return current_value

def compute_gradient(x):
    # Replace with the derivative of your objective function with respect to x (This is given for x^2 )
    gradient = 2 * x
    
    return gradient

# Set initial values
initial_value = 5.0
learning_rate = 0.1
num_iterations = 100

final_value = gradient_descent(initial_value, learning_rate, num_iterations)

print("Optimal value:", final_value)

```

**Explanation:**
<br>
1. The `gradient_descent` function takes three parameters: `initial_value`, `learning_rate`, and `num_iterations`.
2. Inside the function, `current_value` is initialized with the `initial_value`. This value will be updated iteratively using the Gradient Descent algorithm.
3. The loop runs for `num_iterations` times. In each iteration, it calculates the gradient of the objective function at the `current_value` using the `compute_gradient` function.
4. The gradient indicates the direction and magnitude of the steepest increase of the objective function. By subtracting the product of `learning_rate` and `gradient`, we move in the opposite direction (toward the steepest decrease) to update `current_value`.
5. After all iterations, the final `current_value` is returned, which represents the locally optimal solution found by Gradient Descent.
6. The `compute_gradient` function calculates the gradient of a simple quadratic function `2x`. In practice, this function should be replaced with the derivative of the actual objective function you want to optimize.
7. The initial values are set: `initial_value` is 5.0, `learning_rate` is 0.1, and `num_iterations` is 100.
8. The `gradient_descent` function is called with the initial values, and the result (final value after Gradient Descent) is stored in `final_value`.
9. Finally, the optimal value found by the Gradient Descent algorithm is printed.


### Metropolis Algorithm
---
- The Metropolis Algorithm is a probabilistic optimization technique often used in simulated annealing. It's like a traveler exploring a city – they occasionally take detours even if they're on the right path to avoid getting stuck. In optimization, the algorithm explores the solution space by accepting "bad" moves early on and gradually becoming more selective.
- Metropolis is connected to local search because it's a way to avoid getting trapped in local optima. It introduces randomness to explore globally instead of being confined to a single region.

**Connection to Local Search:**
<br>
The Metropolis Algorithm exemplifies local search with an important twist – it doesn't always accept improvements. Instead, it sometimes accepts worse solutions with a certain probability, allowing the algorithm to escape local optima and continue searching for a better solution.


**Python Implementation**
```Python
import random
import math

def metropolis_algorithm(initial_solution, num_iterations, temperature):
    current_solution = initial_solution
    best_solution = initial_solution
    
    for _ in range(num_iterations):
        new_solution = generate_neighbor(current_solution)
        delta_energy = evaluate(new_solution) - evaluate(current_solution)
        
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_solution = new_solution
            
            if evaluate(new_solution) < evaluate(best_solution):
                best_solution = new_solution
    
    return best_solution

def generate_neighbor(solution):
	perturbation = random.uniform(-0.1, 0.1) # Adjust the range as needed
	new_solution = solution + perturbation
	return new_solution

def evaluate(solution):
    # Replace with your objective function (Objective function can be anything that you need to optimize like x^2)
    return solution ** 2

# Set initial values
initial_solution = 2.0
num_iterations = 1000
temperature = 1.0

final_solution = metropolis_algorithm(initial_solution, num_iterations, temperature)

print("Optimal solution:", final_solution)

```

**Explanation:**
<br>
1. The `metropolis_algorithm` function takes three parameters: `initial_solution`, `num_iterations`, and `temperature`.
2. Inside the loop, a new solution is generated using the `generate_neighbor` function. The energy change (`delta_energy`) is calculated by evaluating the new solution's energy (objective function value) minus the current solution's energy.
3. The algorithm either accepts the new solution if the energy is reduced (`delta_energy < 0`) or accepts it with a certain probability (`random.random() < math.exp(-delta_energy / temperature)`). This probability is influenced by the temperature parameter.
4. If the new solution is accepted, it becomes the current solution. If the new solution's energy is lower than the best solution's energy so far, it becomes the new best solution.
5. After all iterations, the best solution found by the Metropolis Algorithm is returned.
6. The `generate_neighbor` function generates a neighboring solution by adding a small random value to the current solution. This is a simplified example; in practice, neighbor generation can be more complex.
7. The `evaluate` function calculates the energy (objective function value) of a solution. In this case, it's a simple quadratic function.
8. Initial values are set: `initial_solution` is 2.0, `num_iterations` is 1000, and `temperature` is 1.0.
9. The `metropolis_algorithm` function is called, and the final solution found is printed.

#### Metropolis + Simulated Annealing
---
- The Metropolis Algorithm and Simulated Annealing work hand in hand to optimize complex problems.
- Simulated Annealing is like a metal being cooled down slowly to reduce defects, while the Metropolis Algorithm guides the search within this cooling process. It's like a hiker exploring a mountain range while occasionally accepting uphill paths to avoid getting trapped.

![Sim_gif](<Simmulated annealing.gif>)

**Python Implementation**

```Python
import random
import math

def metropolis_with_annealing(initial_solution, num_iterations, initial_temperature):
    current_solution = initial_solution
    best_solution = initial_solution
    temperature = initial_temperature
    
    for _ in range(num_iterations):
        new_solution = generate_neighbor(current_solution)
        delta_energy = evaluate(new_solution) - evaluate(current_solution)
        
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            current_solution = new_solution
            
            if evaluate(new_solution) < evaluate(best_solution):
                best_solution = new_solution
        
        # Reduce temperature (annealing)
        temperature *= 0.95  # Adjust cooling rate as needed
    
    return best_solution

def generate_neighbor(solution):
	perturbation = random.uniform(-0.1, 0.1) # Adjust the range as needed
	new_solution = solution + perturbation
	return new_solution

def evaluate(solution):
    # Replace with your objective function (Objective function can be anything that you need to optimize like x^2)
    return solution ** 2

# Set initial values
initial_solution = 2.0
num_iterations = 1000
initial_temperature = 10.0

final_solution = metropolis_with_annealing(initial_solution, num_iterations, initial_temperature)

print("Optimal solution:", final_solution)

```

- In this example, the code incorporates an annealing process by gradually reducing the temperature in each iteration. The temperature influences the probability of accepting uphill moves – as the temperature decreases, the algorithm becomes more selective and explores the solution space more carefully.
- This combined approach of the Metropolis Algorithm with Simulated Annealing allows for a balanced exploration-exploitation trade-off, enabling the algorithm to escape local optima and find better solutions.

### Hopfield Networks (Hopfield Nets)
---
Hopfield Networks, also known as Hopfield Nets, are a type of recurrent neural network (RNN) that was introduced by John Hopfield in 1982. They are primarily designed for content-addressable memory and optimization tasks. Unlike typical feedforward neural networks that process information in a one-way direction, Hopfield Networks have recurrent connections that allow information to loop back within the network.

**Content-Addressable Memory:** <br>
One of the key features of Hopfield Networks is their ability to store and retrieve patterns in a content-addressable manner. This means that given a corrupted or incomplete version of a stored pattern, the network can recover and restore the complete pattern. This property is particularly useful for tasks like pattern recognition and completion.

**Energy Landscape and Stable States:** <br>
Hopfield Networks operate based on an energy function. Each pattern stored in the network corresponds to a stable state or local minimum in the energy landscape. The network iteratively updates its neuron states in an attempt to minimize the overall energy. When the network converges to a stable state, it corresponds to one of the stored patterns.

**Dynamics of Update:** <br>
The update process in a Hopfield Network is often referred to as "asynchronous" or "sequential" update. In each iteration, a neuron is selected, and its state is updated based on the states of its connected neurons and the synaptic weights between them. This process is repeated for each neuron in a random or predetermined order. The network continues updating until it reaches a stable state or energy minimum.

**Applications:** <br>
Hopfield Networks have found applications in various areas, including:
**Pattern Recognition:** They can recognize and complete distorted or noisy patterns, making them suitable for image and speech recognition tasks.
**Content-Addressable Memory:** They can store and retrieve associative memories, which is useful for storing relationships between different pieces of information.
**Optimization:** They can be used to solve optimization problems by finding energy-minimizing states that correspond to optimal solutions.

**Limitations:**
While Hopfield Networks have some attractive properties, they also have limitations. For example, they can sometimes converge to undesired or spurious states that are not valid patterns. Additionally, they may have limited capacity for storing patterns and can suffer from slow convergence for large networks.




**Connection to Local Search:**
<br>
Hopfield Networks epitomize local search by finding stable states (local optima) in an energy landscape. They iteratively update neuron states until they reach an energy-minimizing configuration. These networks excel in solving constraint satisfaction problems and pattern recognition tasks.

![Hopfield_Nets](<Hopfield Nets.png>)

**Python Implementation**

```Python
import numpy as np

def hopfield_network(input_patterns):
    num_patterns, pattern_size = input_patterns.shape
    weights = np.zeros((pattern_size, pattern_size))
    
    for pattern in input_patterns:
        weights += np.outer(pattern, pattern)
    
    return weights

def update_neuron(neuron_state, weights):
    energy_change = np.dot(weights, neuron_state)
    neuron_state = np.sign(energy_change)
    return neuron_state

# Set input patterns
input_patterns = np.array([
    [-1, 1, -1, 1],
    [1, -1, 1, -1]
])

# Train Hopfield network
weights = hopfield_network(input_patterns)

# Set initial neuron state
initial_neuron_state = np.array([-1, 1, -1, 1])

# Update neuron state iteratively
for _ in range(10):
    updated_neuron_state = update_neuron(initial_neuron_state, weights)
    initial_neuron_state = updated_neuron_state

print("Final neuron state:", updated_neuron_state)

```

**Explanation:**
<br>
1. The `hopfield_network` function takes a matrix of input patterns as input. It calculates and returns the weights matrix based on the outer product of the input patterns.
2. The `update_neuron` function takes the current neuron state and the weights matrix as inputs. It calculates the energy change caused by the weights and updates the neuron state based on the energy change.
3. The input patterns are defined as binary values (-1 and 1) in the `input_patterns` array.
4. The Hopfield network is trained by calculating the weights using the `hopfield_network` function.
5. The initial neuron state is set using the `initial_neuron_state` array.
6. The neuron state is updated iteratively using the `update_neuron` function. The process converges towards a stable state.
7. The final neuron state after iterations is printed.

**Example:**
<br>
In this example, the input patterns are binary sequences represented by -1 and 1. The Hopfield network is trained using these patterns, and the algorithm updates the neuron state iteratively. The final neuron state represents a stable state that corresponds to one of the input patterns, demonstrating the content-addressable memory property of Hopfield Networks.

## Applications of Local Search in Real Life
- Local search algorithms find practical use in a wide array of real-life scenarios. These algorithms are not confined to theoretical or abstract domains; they are integral to solving complex problems across various fields. Here are some noteworthy applications:

### 1. **Traveling Salesman Problem:**
The classic Traveling Salesman Problem (TSP) challenges us to find the shortest route that visits a set of cities and returns to the starting point. Local search algorithms help navigate the vast number of possible routes to find efficient solutions for delivery routes, urban planning, and logistics optimization.
### 2. **Job Scheduling:**
Optimal job scheduling is essential in industries like manufacturing, transportation, and healthcare. Local search algorithms optimize task assignment, minimizing completion time, resource usage, or other objectives. These algorithms enhance production efficiency and ensure optimal utilization of resources.
### 3. **Vehicle Routing:**
In fleet management, determining the most efficient routes for multiple vehicles is crucial. Local search algorithms help solve vehicle routing problems by allocating tasks and optimizing routes, saving time, fuel, and costs.
### 4. **Game Strategies:**
Local search plays a pivotal role in developing game strategies, where players make sequential decisions to maximize their chances of winning. Game-playing algorithms, including those used in chess, Go, and poker, rely on local search to explore possible moves and identify strong plays.
### 5. **Network Design and Optimization:**
Designing efficient communication networks is a complex challenge. Local search algorithms help optimize network layouts, maximizing data transmission speed, minimizing latency, and ensuring effective resource allocation.



## 💡 Are you ready to test your knowledge?


1. What is the main goal of a Local Search Algorithm? <br>
	a) To find the absolute best solution globally  
	b) To find a solution that is locally optimal within a specific neighborhood  
	c) To find solutions by exploring the entire solution space  
	d) To find the worst possible solution
	
<details> <summary>Click to reveal answer</summary> b) To find a solution that is locally optimal within a specific neighborhood </details>

2. In the context of a maze, how does a Local Search Algorithm work? <br>
	a) It explores the entire maze exhaustively  
	b) It takes big leaps to quickly reach the destination  
	c) It takes small steps and improves the current solution  
	d) It only considers the starting point
	
<details> <summary>Click to reveal answer</summary> c) It takes small steps and improves the current solution </details>

3. What does the Metropolis Algorithm add to the standard local search approach? <br>
	a) It always accepts better solutions  
	b) It explores the entire solution space  
	c) It occasionally accepts worse solutions with a certain probability  
	d) It improves the evaluation function
	
<details> <summary>Click to reveal answer</summary> c) It occasionally accepts worse solutions with a certain probability </details>

4. How does Simulated Annealing enhance the Metropolis Algorithm? <br>
	a) By using a fixed temperature throughout the search  
	b) By cooling down the algorithm gradually  
	c) By always accepting worse solutions  
	d) By increasing the acceptance probability
	
<details> <summary>Click to reveal answer</summary> b) By cooling down the algorithm gradually </details>

5. Which statement best describes the behavior of Gradient Descent? <br>
	a) It takes large steps in the direction of steepest increase  
	b) It always chooses the random path for exploration  
	c) It takes small steps in the direction of steepest decrease  
	d) It avoids moving in any direction
	
<details> <summary>Click to reveal answer</summary> c) It takes small steps in the direction of steepest decrease </details>

6. How does the Metropolis Algorithm handle exploring solutions? <br>
	a) It explores all possible solutions systematically  
	b) It only explores solutions in the vicinity of the starting point  
	c) It randomly explores solutions without considering quality  
	d) It explores solutions by selecting the best one at each step
	
<details> <summary>Click to reveal answer</summary> c) It randomly explores solutions without considering quality </details>

7. In the context of the Hopfield Network, what does a stable state represent? <br>
	a) A global optimum  
	b) A random solution  
	c) A locally optimal solution  
	d) An unreachable solution
	
<details> <summary>Click to reveal answer</summary> a) A global optimum </details>

## References
1. Local search (optimization). (2023, May 20). In _Wikipedia_. https://en.wikipedia.org/wiki/Local_search_(optimization)
2. Gradient descent. (2023, August 12). In _Wikipedia_. https://en.wikipedia.org/wiki/Gradient_descent
3. Simulated annealing. (2023, August 9). In _Wikipedia_. https://en.wikipedia.org/wiki/Simulated_annealing
4. Hopfield network. (2023, August 7). In _Wikipedia_. https://en.wikipedia.org/wiki/Hopfield_network
5. https://www.scaler.com/topics/local-search-algorithm-in-artificial-intelligence/
6. https://towardsdatascience.com/an-introduction-to-a-powerful-optimization-technique-simulated-annealing-87fd1e3676dd
7. https://www.geeksforgeeks.org/hopfield-neural-network/
