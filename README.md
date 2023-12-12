# FoodClassifierAI: Food Identifier
FoodClassifierAI: A streamlined end-to-end machine learning project seamlessly classifying diverse dishes using deep learning, bringing simplicity and accuracy to food image recognition

Welcome to FoodClassifierAI, an end-to-end machine learning project designed for seamless food image recognition using deep learning techniques. This project allows you to classify a variety of dishes with simplicity and high accuracy.

## Overview

FoodClassifierAI is built on the Food 101 dataset, providing a comprehensive solution for categorizing diverse food items. The project covers the entire machine learning pipeline, from data preprocessing to model deployment, enabling efficient and effective food identification.

## Key Features

- **Dataset:** Utilizes the Food 101 dataset from Kaggle, containing a wide range of food categories.
- **Model:** Implements a deep learning model using TensorFlow for accurate and robust food classification.
- **Visualization:** Includes visualizations for data exploration, model training, and performance evaluation.
- **GitHub Collaboration:** Maintains a collaborative GitHub repository with clear documentation and version control.

## Dataset

### Food 101 Kaggle Dataset

The [Food 101 dataset](https://www.kaggle.com/dansbecker/food-101) is a comprehensive collection of food images compiled for training machine learning models in food recognition. Created for the Kaggle community, it serves as a valuable resource for developing image classification algorithms specifically tailored to food items.

#### Dataset Overview

- **Categories:** The dataset comprises images of food items from 101 different categories, covering a wide range of cuisines and dishes.
  
- **Image Samples:** Each category contains a substantial number of high-resolution images, providing diversity and richness in the dataset.

#### Features and Attributes

1. **Images:** The primary data consists of food images, each associated with a specific category label.
  
2. **Labels:** The dataset is labeled with 101 food categories, making it suitable for supervised learning tasks.

#### Dataset Usage

The Food 101 dataset is commonly used for:

- **Image Classification:** It is a popular choice for training and evaluating deep learning models for food image classification tasks.

- **Transfer Learning:** Researchers and practitioners often use this dataset for transfer learning experiments, leveraging pre-trained models on this extensive food dataset.

#### Getting the Dataset

To obtain the Food 101 dataset:

1. Visit the [Food 101 Kaggle Dataset page](https://www.kaggle.com/dansbecker/food-101).
2. Download the dataset and place it in the `data/` directory of this project.

Explore and experiment with the dataset to understand its characteristics, ensuring effective preprocessing and model training for accurate food classification.

Feel free to tailor this section to highlight specific aspects relevant to your project or audience.

#### Running on aws

##### [On ec2]

in terminal run: export DEBIAN_FRONTEND=noninteractive


git clone https://github.com/CalebMcAnuff/Cosc-aws-deploy.git
cd Cosc-aws-deploy
chmod 700 install.sh
./install.sh
[edit bashrc]
export PATH=$PATH:/home/ubuntu/.local/bin
[close bashrc]
source ~/.bashrc
aws configure
aws s3 cp s3://<s3-bucket-name>/<model_name> .
python3 main.py

## Collaborators

- [Vyom Devgan](https://github.com/vyom-devgan)
- [Rhichard Koh](https://github.com/ROCCYK)
- [Caleb McAnuff](https://github.com/CalebMcAnuff)
- [Mohsin Mohammed](https://github.com/momokamalz)
