# Pitch Detection Algorithms (PDA)

This repository contains implementations for a few Pitch Detection Algorithms.

## Start the notebooks

Start the notebooks in order to experiment with the pitch detection algorithm.

First, make sure to setup an Anaconda environment:

```bash
conda create -y --name py37 python=3.7
conda activate py37
```

Then, install all the requirements:

```bash
conda install -y -c conda-forge --file requirements.txt
```

And finally, start the notebook server. Once the server is started, you will find the Pitch Detection Algorithm notebooks in the notebooks folder:

```bash
jupyter lab
```

## Why no Docker image?

Currently I did not create a Docker image because the code depends on your audio input and that is Operating System dependent.