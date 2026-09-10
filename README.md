# AI / ML / DL Intro

A personal learning repository for getting hands-on with the fundamentals of **Machine Learning** and **Deep Learning** using **PyTorch**. The code here walks through core tensor operations — the building blocks behind every neural network — with inline explanations and printed output for each concept.

## 📁 Project Structure

```
ai-ml-dl-intro/
├── example/            # Supplementary example script(s)
├── ml-intro.py          # Main walkthrough: PyTorch tensor fundamentals
├── pytorch.py           # Minimal PyTorch sanity-check script
├── requirments.txt      # Python dependencies
└── .gitignore
```

## 🧠 What's Covered

`ml-intro.py` is the core file and steps through the following PyTorch tensor concepts, each with a printed example:

- **Creating tensors** — from raw Python lists, and with `torch.zeros`, `torch.ones`, `torch.rand`
- **Device check** — confirming whether a tensor is running on CPU or GPU (`tensor.device`)
- **Element-wise multiplication** — multiplying two tensors of the same shape
- **Matrix multiplication** — using the `@` operator, with shape-compatibility notes
- **`mean()`** — computing the average of a float tensor
- **`dim` reductions** — averaging across rows (`dim=0`) vs. columns (`dim=1`)
- **Indexing** — slicing specific rows/columns out of a tensor
- **`argmax()`** — finding the index of the maximum value along a dimension
- **`gather()`** — selecting specific values from a tensor by index

`pytorch.py` is a tiny script for verifying the PyTorch install and checking CUDA (GPU) availability.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/sinayassari/ai-ml-dl-intro.git
cd ai-ml-dl-intro
pip install -r requirments.txt
```

> **Note:** the dependency file is named `requirments.txt` (not `requirements.txt`) — use that exact filename when installing.

### Running the examples

```bash
python ml-intro.py
python pytorch.py
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

This is a personal, work-in-progress project for learning AI/ML/DL concepts from the ground up — starting with tensor mechanics in PyTorch before moving on to models, training loops, and more advanced deep learning topics.

## 📄 License

No license specified yet — all rights reserved by the author unless stated otherwise.
