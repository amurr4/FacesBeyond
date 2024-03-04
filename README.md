
# FacesBeyond: PCA, GMM, and SVM for Dimensionality, Generation, and Classification

Author: Annika Murray

Portfolio Webpage: https://amm7548.wixsite.com/am-portfoliom-ds

### Overview:
Welcome to my Data Science Portfolio! This project showcases my work on utilizing the Olivetti Faces dataset to perform Principal Component Analysis (PCA), Gaussian Mixture Model (GMM) for face generation, and Support Vector Machine (SVM) for face classification.

### Description:
In this project, the goal is to explore techniques in dimensionality reduction, generative modeling, and classification using facial images. The Olivetti Faces dataset consists of grayscale images of faces from 40 different subjects, and serves as the foundation for this project.

PCA for Dimensionality Reduction:

The project begins with applying PCA to the Olivetti Faces dataset to reduce the dimensionality of the facial images. PCA will identify the principal components that capture the most variance in the dataset, allowing for a more compact representation of facial features.

GMM for Face Generation:

Gaussian Mixture Model (GMM) is employed for generating new faces. GMM will model the distribution of each subjects facial features, enabling the creation of synthetic faces. This step aims to explore the generative capabilities of GMM and create new faces that resemble those in the original dataset.

SVM for Face Classification:

To assess the effectiveness of the generated faces, Support Vector Machine (SVM) is used for classification. The generated faces will be classified to determine which original subject they look most like. SVM, a powerful classification algorithm, will be trained on the original dataset to establish a baseline for comparison.

**PCA.ipynb** : Image samples => Forward PCA => Samples in a lower-dimensional space<br>
**GMM.ipynb** : Samples in a lower-dimensional space => GMM => Random Sampling => New Samples in a lower-dimensional space<br>
**rPCA.ipynb** : New Samples in a lower-dimensional space => Inverse PCA => New Images original dimension space <br>

### Technologies Used:

VScode
Python
scikit-learn
numpy

### Data Used:
Olivetti Faces dataset:

400 images
40 subjects (10 images per subject)

### Expected Outcomes:

PCA Dimensionality Reduction:
Reduced-dimensional representation of facial images using PCA.

GMM-Generated Faces:
Faces generated using Gaussian Mixture Model.

SVM Face Classification:
Classification of generated faces using Support Vector Machine.
Identification of the original subject that the generated faces most resemble.

### Conclusion:
This project aims to explore dimensionality reduction, generative modeling, and classification in the context of facial images. The combination of PCA, GMM, and SVM provides a comprehensive understanding of these techniques' applications in the field of facial image analysis.

By leveraging advanced algorithms, this project contributes to the broader knowledge of facial image processing and opens avenues for further research in generative models and classification tasks related to facial recognition.


