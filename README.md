
# Project: Iris Classification with DVC and Git

This project demonstrates the use of **Data Version Control (DVC)** and **Git** to manage data and model versioning in a simple machine learning workflow. The project trains a classifier on the Iris dataset to predict the species of Iris flowers.

## Table of Contents
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline](#pipeline)
- [Versioning with DVC](#versioning-with-dvc)
- [Acknowledgements](#acknowledgements)

## Project Structure

```
MLOps_DVC/
├── data/                   # Folder to store dataset
│   └── iris.csv            # Iris dataset
├── models/                 # Folder to store trained models
│   └── iris_model.pkl      # Trained model file
├── scripts/                # Folder to store scripts
│   └── train.py            # Script for training the model
├── .dvc/                   # DVC configuration and cache files
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
└── .dvcignore              # DVC ignore file
```

## Requirements

- Python 3.x
- Git
- DVC
- Scikit-learn
- Pandas
- Joblib

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DepieroAgil/MLOps_DVC
   cd repo-name
   ```
2. **Initialize DVC**:
   Make sure DVC is initialized in the project:
   ```bash
   dvc init
   ```

## Usage

### Step 1: Prepare the Dataset
- The Iris dataset (`iris.csv`) should be placed in the `data/` directory. DVC is used to track this dataset for version control.

### Step 2: Train the Model
- Run the `train.py` script located in the `scripts/` directory to train the model:
  ```bash
  python scripts/train.py
  ```
- This script will:
  - Load the Iris dataset.
  - Train a RandomForestClassifier model.
  - Save the trained model as `iris_model.pkl` in the `models/` directory.

### Step 3: Versioning with DVC
- **Track the Dataset**:
  ```bash
  dvc add data/iris.csv
  ```
- **Track the Model**:
  ```bash
  dvc add models/iris_model.pkl
  ```
- **Commit Changes to Git**:
  After adding the dataset and model to DVC, commit the DVC files to Git:
  ```bash
  git add data/iris.csv.dvc models/iris_model.pkl.dvc .gitignore
  git commit -m "Add dataset and model with DVC tracking"
  ```
  
- **Push to Remote Repository**:
  If you are using a remote repository, push the changes:
  ```bash
  git push origin main
  ```
## Pipeline

DVC enables you to create a reproducible pipeline. You can set up a pipeline with the following command:

```bash
dvc run -n train_model \
    -d data/iris.csv \
    -d scripts/train.py \
    -o models/iris_model.pkl \
    python scripts/train.py
```

This will create a pipeline that connects the dataset and training script to the resulting model, making it easier to reproduce results.

## Versioning with DVC

DVC allows version control of data and models, which is particularly useful in machine learning projects where datasets and model files tend to be large. You can track changes in your data and model, enabling you to revert to previous versions if necessary.

### Examples:
- To revert to a previous dataset or model version, you can use:
  ```bash
  dvc checkout
  ```

- To push or pull data from remote storage:
  ```bash
  dvc push      # Upload data to remote storage
  dvc pull      # Download data from remote storage
  ```

## Acknowledgements

- This project uses the [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris) from the UCI Machine Learning Repository.
- Inspired by [DVC](https://dvc.org/) documentation and examples.