# GenTSP

GenTSP is a Python program that solves the Traveling Salesman Problem (TSP) using a genetic algorithm approach. It optimizes the route for visiting a set of cities exactly once and returning to the starting city with the shortest possible distance.

## Features

- Genetic algorithm implementation for TSP optimization.
- Random generation of city locations within a specified range.
- Crossover and mutation operations for evolving routes.
- Output of the best route found and its total distance.

## Usage

1. Ensure you have Python installed on your system.
2. Clone the repository:

    ```bash
    git clone https://github.com/goonzchief/GenTSP.git
    cd GenTSP
    ```

3. Run the script:

    ```bash
    python gentsp.py
    ```

4. The program will print the best route found and its total distance.

## Parameters

Adjust the following parameters in the `gentsp.py` script:

- `num_cities`: Number of cities to generate.
- `population_size`: Size of the population for genetic algorithm.
- `num_generations`: Number of generations for genetic algorithm.

## Requirements

- Python 3.x
- No additional libraries required.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
