# AI / ML / DL Intro

A personal learning repo for getting hands-on with the fundamentals of AI, Machine Learning, and Deep Learning — starting with PyTorch tensor basics.

## About

This repository is a sandbox for working through core PyTorch and deep learning concepts, one script at a time. It's meant as a personal reference and practice space rather than a packaged library.

## Contents

| File | Description |
|---|---|
| `ml-intro.py` | Walkthrough of core PyTorch tensor operations: creating tensors, `zeros`/`ones`/`rand`, checking device (CPU/GPU), element-wise multiplication, matrix multiplication, `mean()`, reducing along a `dim`, indexing, `argmax()`, and `gather()`. |
| `pytorch.py` | Minimal script for creating a tensor and checking CUDA (GPU) availability. |
| `example/` | Additional example code. |
| `requirments.txt` | Python dependencies for the project. |

## Tech Stack

- Python
- [PyTorch](https://pytorch.org/) / TorchVision
- NumPy

## Prerequisites

- Python 3.9+
- pip

## Installation

```bash
# Clone the repo
git clone https://github.com/sinayassari/ai-ml-dl-intro.git
cd ai-ml-dl-intro

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirments.txt
```

## Usage

Run any of the scripts directly to see the tensor operations in action:

```bash
python ml-intro.py
python pytorch.py
```

## Topics Covered

- Tensor creation (`torch.tensor`, `torch.zeros`, `torch.ones`, `torch.rand`)
- CPU vs. GPU (CUDA) device checks
- Element-wise multiplication
- Matrix multiplication
- Reductions (`mean()`, `dim`)
- Indexing and slicing
- `argmax()`
- `gather()`

## Notes

This is a work-in-progress learning project — code and structure may change as new concepts are added.

## License

No license specified yet. All rights reserved by default unless a license is added.
