# Digital Twin Repository

## Overview

This repository contains the necessary components for developing and deploying a Digital Twin system for indoor air quality monitoring. The repository is structured into two main folders:

- Model_Training - Contains the entire process for training models used in Task 4.4.

- Digital_Twin - Serves as the backend for the Digital Twin application, which can be accessed at [indoor-twin.ascalia.io.](https://indoor-twin.ascalia.io/)

# Repository Structure

```
└── Digital_Twins
    ├── Model_Training/          # Model training scripts
    │   ├── preprocessing/       # Python scripts for data preprocessing
    │   ├── data/                # Input datasets for training
    │   ├── training/            # Python scripts for model training
    │   ├── main.py              # Python scripts for running the whole training process 
    │   ├── requirements.txt     # File containing the requirements for the training process
    │   ├── settings.py          # Python file containing the settings for the training process
    │   ├── utils.py             # Python file containing the utils for the training process
    │   └── README.md            # Documentation for model training
    ├── Digital_Twin/            # The digital twin application
    │   ├── models_loading/      # Python scripts for model loading
    │   ├── preprocessing/       # Python scripts for data preprocessing after user input
    │   ├── utility/             # Python scripts containing the utils for the training process
    │   ├── main.py              # Main entry point for backend services
    │   ├── requirements.txt     # Dependencies for running the application
    │   ├── Dockerfile           # Docker container definition
    │   ├── docker-compose.yaml  # Docker Compose configuration file
    │   ├── settings.py          # Python file containing the settings for the process
    │   └── README.md            # Documentation for development and usage
    └── README.md                # Main project overview and documentation
```

### 1. Model_Training

This folder contains all the scripts and resources required for training the models used in Task 4.4. The training process is fully documented in the README.md file within this folder.

### 2. Digital_Twin

This folder serves for the Digital Twin application. The Digital Twin simulates indoor air quality using trained models and computational fluid dynamics (CFD) simulations. The backend is containerized using Docker to ensure consistency across different environments. Docker  is a platform that simplifies the process of developing, packaging, and deploying applications inside containers, providing consistency across different environments. Containers encapsulate an application and its dependencies, enabling developers to create, test, and deploy applications in a predictable and isolated manner. Docker has become a cornerstone of modern application development, making it easier to build and deploy applications seamlessly across diverse computing environments.