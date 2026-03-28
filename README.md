# 😷 Face Mask Detection using CNN

## 📌 Overview

This project implements a **Convolutional Neural Network (CNN)** to detect whether a person is wearing a face mask or not.
It is a **binary image classification** problem with two classes: **With Mask 😷** and **Without Mask ❌**.

The model is optimized for **fast training (2–3 minutes)** and achieves good accuracy, making it suitable for **academic projects and demonstrations**.

---

## 🚀 Features

* ✅ Fast training (optimized for Google Colab)
* 🧠 Lightweight CNN model
* 📊 Accuracy visualization
* 💾 Model saving and reuse
* 🔍 Predict on custom images

---

## 🗂️ Dataset

Dataset used: **Face Mask Dataset** from Kaggle

It contains two categories:

* `with_mask`
* `without_mask`

Dataset is automatically downloaded using `kagglehub`.

---

## ⚙️ Tech Stack

* **Python**
* **TensorFlow / Keras**
* **NumPy**
* **Matplotlib**
* **KaggleHub**

---

## 📂 Project Structure

```
Face-Mask-Detection/
│
├── model/
│   └── face_mask_model.h5
│
├── dataset/
│   ├── with_mask/
│   └── without_mask/
│
├── notebook.ipynb
├── README.md
└── test.jpg
```

---

## 🔄 Workflow

1. Download dataset using KaggleHub
2. Preprocess images (rescaling + resizing)
3. Train CNN model
4. Validate performance
5. Save trained model
6. Test on new images

---

## 🧠 Model Architecture

* Conv2D (16 filters) + MaxPooling
* Conv2D (32 filters) + MaxPooling
* Flatten
* Dense (64 neurons)
* Output layer (Sigmoid)

---

## 🏋️ Training Details

* Image Size: **64 × 64**
* Batch Size: **16**
* Epochs: **3 (fast training)**
* Loss Function: **Binary Crossentropy**
* Optimizer: **Adam**

---

## 📊 Results

* Training Accuracy: ~85–90%
* Validation Accuracy: ~80–88%
* Training Time: ~2–3 minutes (Colab CPU)

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install kagglehub tensorflow matplotlib
```

### 2️⃣ Run Notebook

Open the notebook in **Google Colab** and execute all cells.

---

## 🔍 Prediction Example

```python
if prediction[0][0] > 0.5:
    print("No Mask ❌")
else:
    print("Mask ✅")
```

---

## ⚠️ Common Issues

* ❌ Wrong dataset path
  👉 Ensure correct folder structure

* ❌ flow_from_directory error
  👉 Check subfolder inside dataset

---

## 💡 Future Improvements

* 🚀 Use **MobileNetV2** for higher accuracy
* 📷 Real-time detection using OpenCV
* 🌐 Deploy as web app

---

## 👨‍💻 Author

**Sidhant Kumar**

---

## ⭐ Acknowledgements

* Kaggle for dataset
* TensorFlow/Keras for deep learning framework

---

## 📌 License

This project is for **educational purposes only**.
