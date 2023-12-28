Handwriting Authorship Identification Project
Overview
This project involves the development of a multiclass classifier capable of distinguishing between different handwritings and determining the author. The system achieves over 96% accuracy using an innovative image-based approach and is designed to be language-independent. Leveraging TensorFlow, the model is easily scalable, making it suitable for applications such as verifying handwritten assignments in educational settings.

Key Features
High Accuracy:

Achieve authorship identification with a remarkable accuracy rate exceeding 96% using an RNN-based AI model.
Innovative Approach:

Adopt an image-based approach, departing from traditional curve analysis, to enhance flexibility and support language independence in handwriting recognition.
Efficient Training:

Utilize TensorFlow for seamless scalability, allowing the model to be trained across multiple GPUs. Particularly advantageous for handling large datasets, such as student assignments in a university setting.
Quick Training:

Significantly reduce training time to just one hour, showcasing the model's efficiency in rapidly classifying handwriting styles for up to 60 authors. This optimizes both processing speed and resource utilization.
Data Generation Capability:

Include an OpenCV script that automatically scans and generates datasets from handwriting samples. This self-generating data capability adds versatility to the model's training process.
Practical Application:

Deploy the system in educational settings to verify the authenticity of handwritten assignments, contributing to academic integrity and aiding in plagiarism detection.
Requirements
Ensure you have the following dependencies installed before running the project:

Python 3.x
TensorFlow (install with pip install tensorflow)
OpenCV (install with pip install opencv-python)
Additional dependencies specified in the requirements.txt file.
