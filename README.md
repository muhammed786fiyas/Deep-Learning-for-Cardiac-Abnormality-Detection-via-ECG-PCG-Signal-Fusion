# Deep-Learning-for-Cardiac-Abnormality-Detection-via-ECG-PCG-Signal-Fusion
This project implements a deep learning framework to detect cardiac abnormalities by fusing synchronous Electrocardiogram (ECG) and Phonocardiogram (PCG) signals. The core idea is that by combining the heart's electrical activity (ECG) and its mechanical sounds (PCG), we can achieve a more robust and accurate classification than by using either signal alone.

This framework transforms the 1D time-series signals into 2D time-frequency images (scalograms) and uses Convolutional Neural Networks (CNNs) for classification. The project provides a comprehensive comparison between unimodal (ECG-only, PCG-only) and multimodal (fused) models.

**The fused GoogLeNet model achieved state-of-the-art results on the PhysioNet/CINC Challenge 2016 dataset, with 98.7% accuracy**.

---

## 📈 Project Workflow

The methodology follows a systematic pipeline:

1.  **Data Acquisition:** Uses the **PhysioNet/CINC Challenge 2016** database, which contains synchronous ECG and PCG recordings. The data is categorized as 'normal' or 'abnormal'.

2.  **Preprocessing:**
    * **Filtering:** A 4th-order Butterworth low-pass filter (20 Hz cutoff) is applied to the ECG signals, and a band-pass filter (25-400 Hz) is applied to the PCG signals to remove noise.
    * **Normalization:** All signals are normalized to zero mean and unit variance.

3.  **Data Augmentation:**
    * To expand the dataset (405 recordings), a "physiologically-aware windowing" technique is used.
    * An R-peak is located, and a **3-second segment** (6,000 samples) of the ECG is extracted, along with the synchronously aligned PCG segment.
    * This process augmented the original 405 pairs into **3,477** meaningful segments.

4.  **Scalogram Generation (Feature Extraction):**
    * The 3-second segments are transformed into 2D time-frequency representations using the **Continuous Wavelet Transform (CWT)**.
    * **ECG:** Uses the *Complex Morlet wavelet* to preserve amplitude and phase.
    * **PCG:** Uses the *Real-valued Morlet wavelet* to capture transient acoustic events.
    * The resulting scalograms are resized to `224x224` pixel images to be used as input for the CNNs.

5.  **Model Training and Fusion:**
    * Three different CNN architectures are trained and compared: **VGG16**, **GoogLeNet (Inception V3)**, and a **Custom CNN**.
    * **Unimodal:** Each model is first trained separately on *only* ECG scalograms and *only* PCG scalograms.
    * **Multimodal (Fused):** The feature vectors from the penultimate dense layers of the trained ECG and PCG models are concatenated. This fused vector is then passed to a final classification layer.

---

## 🤖 Models and Architectures

This project implements and compares three distinct architectures:

* **VGG16:** A 16-layer deep CNN known for its simple and effective architecture. Used as a feature extractor.
* **GoogLeNet (Inception V3):** A 27-layer deep network that uses "Inception modules" to perform efficient multi-scale feature extraction.
* **Custom CNN:** A custom-built 2D-CNN with four convolutional blocks, batch normalization, and max-pooling.

All models were trained with the Adam optimizer, a learning rate of 0.001, and a batch size of 64 for 100 epochs, using binary cross-entropy as the loss function.

---

## 📊 Results

The multimodal fusion models consistently and significantly outperformed the unimodal models across all metrics, proving the value of combining ECG and PCG data. The fused **GoogLeNet** model emerged as the top-performing architecture.

### Performance Comparison

| Model | Accuracy | Precision | Recall (Sensitivity) | Specificity | F1-score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| ECG-VGG16 (Unimodal) | 84.4% | 85.2% | 94.5% | 59.7% | 89.6% |
| PCG-VGG16 (Unimodal) | 71.07% | 71.79% | 100.0% | 0% | 83.09% |
| **ECG+PCG-VGG16 (Fused)** | **95.4%** | **96.03%** | **97.58%** | **90.0%** | **96.9%** |
| | | | | | |
| ECG-GoogLeNet (Unimodal) | 89.6% | 93.5% | 91.7% | 84.5% | 92.06% |
| PCG-GoogLeNet (Unimodal) | 71.07% | 71.79% | 100.0% | 0% | 83.9% |
| **ECG+PCG-GoogLeNet (Fused)** | **98.7%** | **98.4%** | **99.7%** | **96.0%** | **99.09%** |
| | | | | | |
| ECG-CNN (Unimodal) | 95.8% | 95.8% | 98.3% | 89.5% | 97.1% |
| PCG-CNN (Unimodal) | 79.1% | 88.2% | 81.6% | 73.0% | 84.8% |
| **ECG+PCG-CNN (Fused)** | **96.8%** | **97.4%** | **98.0%** | **93.5%** | **97.7%** |

### Key Takeaways

* **Fusion is Superior:** The fusion of ECG and PCG signals provides a massive boost in performance, especially in **Specificity** (correctly identifying 'normal' patients), which jumped from 0% in the PCG-only model to 96% in the fused GoogLeNet model.
* **GoogLeNet Wins:** The multi-scale Inception modules of GoogLeNet proved most effective at extracting discriminative features from the scalograms, leading to the highest overall performance.

---

## 🛠️ Technology Stack

* **Python 3.10**
* **TensorFlow 2.13**
* **Keras API**
* **Google Colab** (for GPU acceleration, NVIDIA Tesla T4)
* **CUDA 11.8**
* (Implicitly) NumPy, SciPy, Matplotlib

---
