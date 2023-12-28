
# Handwriting Authorship Identification Project

## Overview

This project is dedicated to the development of a robust multiclass classifier designed to distinguish between different handwriting styles and accurately determine the author. The system achieves exceptional accuracy, exceeding 96%, through the implementation of an innovative image-based approach. This language-independent model is scalable using TensorFlow, making it highly suitable for applications such as verifying handwritten assignments in educational settings.

## Key Features

### 1. High Accuracy

-   Achieve precise authorship identification with a remarkable accuracy rate exceeding 96% using an RNN-based AI model.

### 2. Innovative Approach

-   Adopt an image-based approach, moving away from traditional curve analysis, to enhance flexibility and support language independence in handwriting recognition.

### 3. Efficient Training

-   Utilize TensorFlow for seamless scalability, enabling the model to be trained across multiple GPUs. This is particularly advantageous for handling large datasets, such as student assignments in a university setting.

### 4. Quick Training

-   Significantly reduce training time to just one hour, showcasing the model's efficiency in rapidly classifying handwriting styles for up to 60 authors. This optimization enhances both processing speed and resource utilization.

### 5. Data Generation Capability

-   Include an OpenCV script that automatically scans and generates datasets from handwriting samples. This self-generating data capability adds versatility to the model's training process.

### 6. Practical Application

-   Deploy the system in educational settings to verify the authenticity of handwritten assignments, contributing to academic integrity and aiding in plagiarism detection.
## Requirements

Ensure you have the following dependencies installed before running the project:

-   Python 3.x
-   TensorFlow (install with `pip install tensorflow`)
-   OpenCV (install with `pip install opencv-python`)
