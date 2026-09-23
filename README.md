# 🧠 AI / ML / DL Intro

A hands-on learning repository for understanding the fundamentals of **Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL)** with **Python and PyTorch**.

This project starts with the fundamentals of PyTorch tensors and gradually moves toward a complete machine learning workflow — from creating and preparing data to building, training, evaluating, saving, and loading a neural network model.

> 🚧 **Status:** Work in progress — new AI/ML/DL concepts and practical examples will be added over time.

---

## 🎯 Goals

The main goal of this repository is to build a strong practical foundation in AI, Machine Learning, and Deep Learning by combining:

* 📚 Fundamental concepts
* 💻 Python implementations
* 🔥 PyTorch
* 📓 Jupyter Notebooks
* 📊 Data visualization
* 🧪 Model training and evaluation
* 💾 Model saving and loading
* ⚡ CPU/GPU workflows

The repository is designed to progress from **basic tensor operations** toward more advanced deep-learning topics.

---

## 📚 Topics Covered

### PyTorch Fundamentals

The project introduces the fundamental building blocks of PyTorch, including:

* Scalars, vectors, matrices, and tensors
* Tensor shapes and dimensions
* Tensor creation
* Random tensors
* Tensor data types
* CPU and GPU devices
* Element-wise operations
* Matrix multiplication
* Indexing and slicing
* Aggregation operations
* `mean()`, `sum()`, `min()`, and `max()`
* `argmin()` and `argmax()`
* `gather()`
* Reshaping and viewing tensors
* Stacking and squeezing tensors
* NumPy ↔ PyTorch conversion

### Machine Learning Workflow

The repository also demonstrates a complete machine learning workflow:

1. Generate data
2. Prepare and split datasets
3. Visualize the data
4. Define a model
5. Define a loss function
6. Select an optimizer
7. Train the model
8. Evaluate predictions
9. Visualize training results
10. Save the trained model
11. Load the model
12. Verify predictions

### Deep Learning

The project will gradually expand toward more advanced topics, including:

* Neural networks
* Custom datasets
* Computer vision
* Convolutional Neural Networks (CNNs)
* Model evaluation
* GPU acceleration
* Advanced PyTorch workflows

---

## 📁 Project Structure

```text
ai-ml-dl-intro/
│
├── example/
│   ├── 00_pytorch__fundamentals.ipynb
│   ├── 01_pytorch_workflow.ipynb
│   │
│   └── models/
│       └── 01_pytorch_workflow.model_0.pth
│
├── ml-intro.py
├── pytorch.py
├── requirments.txt
├── .gitignore
└── README.md
```

---

## 🔎 Repository Contents

### `ml-intro.py`

A practical introduction to PyTorch tensor operations.

It demonstrates:

* Creating tensors from Python lists
* Creating tensors with `torch.zeros()`
* Creating tensors with `torch.ones()`
* Creating random tensors with `torch.rand()`
* Checking tensor devices
* Element-wise multiplication
* Matrix multiplication
* Calculating means
* Dimension-based reductions
* Tensor indexing
* `argmax()`
* `gather()`

---

### `pytorch.py`

A minimal PyTorch environment test.

It can be used to verify:

* PyTorch installation
* PyTorch version
* CUDA availability
* GPU support

---

### `00_pytorch__fundamentals.ipynb`

A notebook-based introduction to PyTorch tensor fundamentals.

Topics include:

* Scalars
* Vectors
* Matrices
* Tensors
* Tensor dimensions
* Tensor shapes
* Random tensor generation
* `torch.arange()`
* `torch.zeros()`
* `zeros_like()`
* Data types
* `float32`
* `float16`
* Tensor arithmetic
* Matrix multiplication
* Aggregation
* Reshaping
* Viewing tensors
* Stacking
* Squeezing and unsqueezing
* Multi-dimensional indexing
* NumPy integration

---

### `01_pytorch_workflow.ipynb`

A complete machine-learning workflow implemented with PyTorch.

The notebook covers:

* Generating synthetic linear data
* Creating training and testing datasets
* Visualizing data
* Building a custom model with `nn.Module`
* Creating learnable weights and bias
* Defining a loss function
* Training with gradient descent
* Using `torch.optim.SGD`
* Using `nn.L1Loss`
* Tracking training and test loss
* Plotting loss curves
* Saving model weights
* Loading a trained model
* Comparing predictions
* CPU/GPU device-agnostic implementation

The model weights are stored in:

```text
example/models/01_pytorch_workflow.model_0.pth
```

---

## 🚀 Getting Started

### Prerequisites

Before starting, make sure you have:

* Python 3.9+
* pip
* Jupyter Notebook or JupyterLab
* Basic Python knowledge

A CUDA-compatible NVIDIA GPU is optional but useful for experimenting with GPU acceleration.

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/sinayassari/ai-ml-dl-intro.git
```

Navigate into the project:

```bash
cd ai-ml-dl-intro
```

Install the dependencies:

```bash
pip install -r requirments.txt
```

> **Note:** The dependency file is currently named `requirments.txt` rather than the conventional `requirements.txt`.

---

## ▶️ Running the Examples

### Run the PyTorch fundamentals script

```bash
python ml-intro.py
```

### Check your PyTorch installation

```bash
python pytorch.py
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open:

```text
example/00_pytorch__fundamentals.ipynb
```

or:

```text
example/01_pytorch_workflow.ipynb
```

You can also launch a notebook directly:

```bash
jupyter notebook example/00_pytorch__fundamentals.ipynb
```

---

## 📦 Main Dependencies

The project currently uses PyTorch and related Python packages.

| Package         | Purpose                            |
| --------------- | ---------------------------------- |
| **PyTorch**     | Machine learning and deep learning |
| **TorchVision** | Computer vision utilities          |
| **NumPy**       | Numerical computing                |
| **Pillow**      | Image processing                   |
| **SymPy**       | Symbolic mathematics               |
| **NetworkX**    | Graph/network utilities            |
| **Jinja2**      | Template support                   |

The complete dependency list is available in:

```text
requirments.txt
```

---

## 🧩 Learning Path

The repository follows a gradual learning path:

```text
Python
  │
  ▼
PyTorch Fundamentals
  │
  ├── Tensors
  ├── Shapes & Dimensions
  ├── Operations
  └── Device Management
  │
  ▼
Machine Learning Fundamentals
  │
  ├── Data
  ├── Models
  ├── Loss Functions
  ├── Optimizers
  └── Training
  │
  ▼
Model Evaluation
  │
  ├── Predictions
  ├── Training Loss
  └── Test Loss
  │
  ▼
Model Persistence
  │
  ├── Save
  └── Load
  │
  ▼
Deep Learning
  │
  ├── Neural Networks
  ├── CNNs
  ├── Custom Datasets
  └── Computer Vision
```

---

## 🧪 Example Workflow

A typical PyTorch workflow in this repository looks like:

```python
# 1. Create data
X = ...
y = ...

# 2. Define a model
model = ...

# 3. Define loss function
loss_fn = ...

# 4. Define optimizer
optimizer = ...

# 5. Train
for epoch in range(epochs):
    # Forward pass
    predictions = model(X)

    # Calculate loss
    loss = loss_fn(predictions, y)

    # Zero gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update parameters
    optimizer.step()

# 6. Save the model
torch.save(model.state_dict(), "model.pth")

# 7. Load the model
model.load_state_dict(torch.load("model.pth"))
```

---

## ⚡ CPU & GPU Support

The examples demonstrate device-agnostic PyTorch code so that models can run on either CPU or CUDA-enabled GPUs.

A typical device configuration is:

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

You can check CUDA availability with:

```python
import torch

print(torch.cuda.is_available())
```

If CUDA is available, PyTorch can use the GPU for supported operations.

---

## 💡 Future Roadmap

Planned topics include:

* [ ] Neural Network fundamentals
* [ ] Classification
* [ ] Regression
* [ ] Custom datasets
* [ ] Data preprocessing
* [ ] Convolutional Neural Networks
* [ ] Computer Vision
* [ ] Transfer Learning
* [ ] Model evaluation
* [ ] Hyperparameter tuning
* [ ] Data augmentation
* [ ] Natural Language Processing
* [ ] Transformers
* [ ] Generative AI
* [ ] Practical AI projects

---

## 🤝 Contributing

This is primarily a personal learning repository, but suggestions, improvements, and educational contributions are welcome.

If you find an issue or have an idea for improving the examples, feel free to open an issue or submit a pull request.

---

## 📄 License

No license has been specified for this repository yet.

Unless a license is added, the repository's contents should be considered **all rights reserved**.

---

## 👨‍💻 Author

**Sina Yassari**

GitHub:

[github.com/sinayassari](https://github.com/sinayassari?utm_source=chatgpt.com)

---

## ⭐ About This Project

This repository is part of a hands-on journey into:

**Artificial Intelligence → Machine Learning → Deep Learning → Practical AI**

The focus is on learning by **understanding the concepts, writing the code, experimenting with models, and building practical projects**.

If you find the repository useful, consider giving it a ⭐ on GitHub.
