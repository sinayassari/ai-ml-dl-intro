# AI / ML / DL Intro

A personal learning repository for getting hands-on with the fundamentals of **Machine Learning** and **Deep Learning** using **PyTorch**. It walks through core tensor operations, then builds up to a full end-to-end PyTorch workflow — creating data, building a model, training it, evaluating it, and saving/loading it — with inline explanations and printed/plotted output at each step.

## 📁 Project Structure

```
ai-ml-dl-intro/
├── example/
│   ├── 00_pytorch__fundamentals.ipynb   # Tensor basics notebook
│   ├── 01_pytorch_workflow.ipynb        # End-to-end PyTorch workflow notebook
│   └── models/
│       └── 01_pytorch_workflow.model_0.pth   # Saved trained model weights
├── ml-intro.py          # Script walkthrough: PyTorch tensor fundamentals
├── pytorch.py           # Minimal PyTorch sanity-check script
├── requirments.txt      # Python dependencies
└── .gitignore
```

## 🧠 What's Covered

### `ml-intro.py`
A script that steps through core PyTorch tensor concepts, each with a printed example:
- **Creating tensors** — from raw Python lists, and with `torch.zeros`, `torch.ones`, `torch.rand`
- **Device check** — confirming whether a tensor is running on CPU or GPU (`tensor.device`)
- **Element-wise multiplication** — multiplying two tensors of the same shape
- **Matrix multiplication** — using the `@` operator, with shape-compatibility notes
- **`mean()`** — computing the average of a float tensor
- **`dim` reductions** — averaging across rows (`dim=0`) vs. columns (`dim=1`)
- **Indexing** — slicing specific rows/columns out of a tensor
- **`argmax()`** — finding the index of the maximum value along a dimension
- **`gather()`** — selecting specific values from a tensor by index

### `pytorch.py`
A tiny script for verifying the PyTorch install and checking CUDA (GPU) availability.

### `example/00_pytorch__fundamentals.ipynb`
A deeper dive into tensor fundamentals in notebook form:
- Scalars, vectors, matrices, and tensors — shape and `ndim`
- Random and range-based tensor creation (`torch.rand`, `torch.arange`, `zeros_like`)
- Tensor datatypes and type conversion (`float32` ↔ `float16`)
- Tensor operations: addition, subtraction, multiplication, division, matrix multiplication (`torch.matmul` / `torch.mm`)
- Aggregation: `min`, `max`, `mean`, `sum`, `argmin`, `argmax`
- Reshaping, viewing, stacking, squeezing, and unsqueezing tensors
- Multi-dimensional indexing
- Converting between NumPy arrays and PyTorch tensors

### `example/01_pytorch_workflow.ipynb`
A full, practical PyTorch modeling workflow:
- Generating synthetic linear data and splitting it into train/test sets
- Visualizing training data, test data, and predictions
- Defining a custom `LinearRegressionModel` (subclassing `nn.Module`) with learnable `weights` and `bias` parameters
- Writing a training loop with `nn.L1Loss` and `torch.optim.SGD`
- Tracking and plotting training vs. test loss curves over 200 epochs
- Saving a trained model's `state_dict()` to disk and reloading it (`example/models/01_pytorch_workflow.model_0.pth`)
- Verifying that predictions from the loaded model match the original
- Re-running the same workflow with explicit device-agnostic code (`cuda` vs `cpu`)

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip
- Jupyter Notebook / JupyterLab (to run the `.ipynb` files)

### Installation

```bash
git clone https://github.com/sinayassari/ai-ml-dl-intro.git
cd ai-ml-dl-intro
pip install -r requirments.txt
```

> **Note:** the dependency file is named `requirments.txt` (not `requirements.txt`) — use that exact filename when installing.

### Running the examples

```bash
# Scripts
python ml-intro.py
python pytorch.py

# Notebooks
jupyter notebook example/00_pytorch__fundamentals.ipynb
jupyter notebook example/01_pytorch_workflow.ipynb
```

## 📦 Dependencies

Pinned in `requirments.txt`:

| Package | Version |
|---|---|
| torch | 2.13.0 |
| torchvision | 0.28.0 |
| numpy | 2.5.2 |
| pillow | 12.3.0 |
| sympy | 1.14.0 |
| networkx | 3.6.1 |
| Jinja2 | 3.1.6 |
| MarkupSafe | 3.0.3 |
| filelock | 3.32.4 |
| fsspec | 2026.7.0 |
| mpmath | 1.3.0 |
| setuptools | 84.0.0 |
| typing_extensions | 4.16.0 |

## 🎯 Purpose

This is a personal, work-in-progress project for learning AI/ML/DL concepts from the ground up — starting with tensor mechanics in PyTorch, then progressing through a complete model training-and-evaluation workflow, before moving on to more advanced deep learning topics (CNNs, custom datasets, and beyond).

## 📄 License

No license specified yet — all rights reserved by the author unless stated otherwise.
