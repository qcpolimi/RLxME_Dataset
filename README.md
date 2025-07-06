# Minor Embedding for Quantum Annealing with Reinforcement Learning

This repository contains the randomly generated graphs used in the work *Minor Embedding for Quantum Annealing with Reinforcement Learning* by Riccardo Nembrini, Maurizio Ferrari Dacrema and Paolo Cremonesi.

## Randomly Generated Graphs Dataset

The dataset includes training and testing sets of randomly generated graphs, stored in `.zip` files located in the `dataset` directory. These files contain NetworkX graphs saved in the `edgelist` format.

To extract and prepare the data for use, run the following command:

```
python extract_data.py
```

Make sure to run this command from the root directory of the repository. The command will extract the data into two directories, `training` and `testing`, within the `dataset` folder.

## Analyzing and Visualizing Graphs

We also provide a Jupyter Notebook, `load_data.ipynb`, which demonstrates how to load and analyze the two graph sets, as well as how to visualize the graphs.

The notebook includes key information about the graphs. If you wish to run it locally, you will need to install the necessary libraries, which are listed in the `requirements.txt` file.

To set up your environment, you can create a new Python environment using `virtualenv`, `conda`, or other tools. Then, install the required libraries using `pip` or your preferred package manager:

```
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Once the environment is set up, you can open and run the notebook to explore the data and graphs.
