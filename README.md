# EEG-Based Texture Classification
### Exploring the Impact of Texture on Brain Activity: A Study Through Electroencephalography (EEG)
A research project investigating the relationship between tactile texture and brain activity using EEG signal processing and machine learning techniques.

## Project Overview
This project explores how different surface textures affect brain activity during tactile interaction. EEG signals were collected while participants touched different materials and were analyzed to identify patterns associated with each texture.

The study focuses on classifying three types of surface textures:

- Flat – Mouse pad
- Furry – Mink fabric
- Rough – Cement slab

Two machine learning approaches, Support Vector Machine (SVM) and Artificial Neural Network (ANN), were implemented and compared for texture classification.

## Research Objectives
- Investigate the relationship between tactile textures and EEG signals.
- Analyze brain activity through EEG frequency-domain features.
- Extract frequency-band characteristics from multiple EEG channels.
- Develop machine learning models to classify different surface textures.
- Compare SVM and ANN performance using classification and unseen-data testing.

## Data Collection
EEG recordings were collected using a Cyton Biosensing Board (8 channels) with gold-cup electrodes.

The electrode positions focused on the parietal and post-central regions associated with somatosensory processing.

### EEG Channels
Eight EEG channels were used:
- Left hemisphere: P3, P5, CP3, CP5
- Right hemisphere: P4, P6, CP4, CP6

### Experimental Conditions
Three texture conditions were investigated:
- Flat
- Furry
- Rough

The experimental recording procedure included:
- Touch period: 1 minute
- Break period: 30 seconds
- Recording both left and right sides during the experiment.
- The research scope covered data collection from 20 samples during January–April 2024.

## Methodology

The project workflow consists of the following stages:

### 1. EEG Data Acquisition

EEG signals were recorded using Python scripts connected to the Cyton Biosensing Board.

Raw recordings were stored as .txt files for subsequent processing.

### 2. Signal Processing

The recorded EEG signals were prepared for frequency-domain analysis.

Fast Fourier Transform (FFT) was applied to transform signals from the time domain into the frequency domain.

### 3. Frequency Band Analysis
Five EEG frequency bands were analyzed:

- Delta
- Theta
- Alpha
- Beta
- Gamma

Frequency-band features were calculated for the eight EEG channels.

### 4. Dataset Preparation
The extracted features were organized into a structured dataset for machine learning.

Each observation contains frequency-band features from eight EEG channels and a corresponding texture label.

The classification labels are:
- flat
- furry
- rough

### 5. Machine Learning Classification
Two classification approaches were implemented:

**Support Vector Machine (SVM)** - Used to classify texture categories based on extracted EEG frequency features.

**Artificial Neural Network (ANN)** - Used to learn patterns from EEG features and predict the corresponding texture category.

### 6. Model Evaluation
Model performance was examined through classification results and additional testing using unseen data.

Confusion matrices were used to visualize classification performance.

## Experimental Results
### Classification Performance
The reported classification accuracy was:
- SVM: 100.00%
- ANN: 98.61%

The SVM model achieved perfect classification in the reported classification result, while ANN achieved 98.61%.

### Confusion Matrix
The reported confusion matrices show the classification performance across three texture categories:
- Flat
- Furry
- Rough

SVM correctly classified all 144 evaluated samples in the presented confusion matrix, while ANN misclassified two samples.

### Unseen Data Testing
Additional testing was conducted using 10 unseen examples for each texture category.

The observed results were:
| Texture | SVM | ANN |
|---|---|---|
| Flat | 10/10 | 10/10 |
| Furry | 5/10 | 10/10 |
| Rough | 0/10 | 0/10 |

The results demonstrate different classification strengths between the two approaches.
- Flat: Both models classified all 10 examples correctly.
- Furry: ANN classified all 10 examples correctly, while SVM classified 5 correctly.
- Rough: Both models struggled to correctly classify the unseen examples.

## Discussion
Although SVM achieved higher accuracy in the reported classification results, its performance did not generalize equally well across all texture categories.

ANN demonstrated better performance on unseen Furry samples.

However, both models had difficulty recognizing Rough textures during unseen-data testing.

These findings highlight the importance of evaluating machine learning models beyond their initial classification accuracy.

## Technologies and Tools
- Python
- Google Colab
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- OpenBCI / Cyton Biosensing Board
- Fast Fourier Transform (FFT)
- Support Vector Machine (SVM)
- Artificial Neural Network (ANN)

## Dataset and Privacy

The EEG dataset was personally collected during the research experiment.

Due to participant privacy and data-sharing considerations, original EEG recordings are not included in this public repository.

This repository provides:
- Dataset structure documentation
- Feature descriptions
- Synthetic sample data for demonstrating the training dataset format
- Data collection and processing workflows

Important: The synthetic sample is artificially generated and does not represent actual participant recordings. It is provided for demonstrating the data structure only and cannot reproduce the original experimental results.

## Limitations
The experimental results indicate that classification performance varies across texture categories.

In particular, both models showed limitations in recognizing Rough textures during unseen-data testing.

The reported classification accuracy should therefore be interpreted separately from the unseen-data performance.

Further investigation into feature extraction, signal characteristics, and model generalization would be valuable for improving classification performance.

**Project Type:** Academic Research / Signal Processing / Machine Learning

**Research Focus:** EEG Signal Analysis and Texture Classification
