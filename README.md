# 🔐 Cryptography and Security Lab

<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=2EF723&width=435&lines=Welcome+to+Cryptography+Lab;Secure+%E2%80%A2+Fast+%E2%80%A2+Reliable;Building+Security+Solutions)](https://git.io/typing-svg)

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white&labelColor=4B8BBE)](https://www.python.org)
[![Security](https://img.shields.io/badge/Security-Cryptography-red.svg?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAAdgAAAHYBTnsmCAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADSSURBVCiRrdIxSgNBFMbx374NFnZpFEEQBCWgYGFhYWEhWHkDK0s7j+EFPICFhYVgYWFhYSGCRbAIhBAIJBvz7FLIGje7+ZqZ/zfzzcwLSZL8iqIoGGPcwzUucYJTHGAvxtgryxL/EYZhGF7wlmXZR3NGzXR3OByuiqL4rMK+74dhWN5q4HmeH8/FKshxgyecoYNLvOMDp6vxXfvYbKh0OF/L+r4/mhX0J8Kt4B7XeJRk6qRr4Q4vcI8kSU7/BNV9dizwLcRGVVV7f9W5FbgV+A3kqy+x7LiuUQAAAABJRU5ErkJggg==)](https://en.wikipedia.org/wiki/Cryptography)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/let-shyn-cook/hash?style=for-the-badge&logo=github&color=yellow)](https://github.com/yourusername/Lab_ATBMTT/stargazers)

<p align="center">
<img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg" alt="snake animation" width="100%"/>
</p>

> 🚀 A comprehensive collection of cryptography and security implementations including Caesar Cipher, Hash Functions, and Binary Analysis tools.

</div>

## 📑 Table of Contents

<details open>
<summary>Click to expand/collapse</summary>

- [✨ Features](#-features)
- [🗂 Project Structure](#-project-structure)
- [🚀 Installation](#-installation)
- [💡 Usage Examples](#-usage-examples)
- [📊 Algorithm Flowcharts](#-algorithm-flowcharts)
- [🌈 Color Reference](#-color-reference)
- [📝 License](#-license)

</details>

## ✨ Features

<div align="center">

| Feature | Description |
|---------|-------------|
| 🔄 Caesar Cipher | Advanced implementation of the classical encryption technique |
| 🔍 Hash Comparison | Secure file integrity verification tools |
| 📊 Binary Analysis | Comprehensive binary file analysis capabilities |
| 🔐 Cryptography | Implementation of fundamental security concepts |

</div>

## 🗂 Project Structure

<details>
<summary>Click to view project tree 🌳</summary>

```bash
Lab_ATBMTT/
├── 📄 binary_hash_compare.py   # Binary file hash comparison
├── 📄 caesar_cipher.py         # Caesar cipher implementation
├── 📁 collision1.bin           # Test file for hash collision
├── 📁 collision2.bin           # Test file for hash collision
├── 📄 hash_compare.py         # Hash comparison utilities
├── 📄 main.py                 # Main program entry point
├── 📄 pyproject.toml         # Project dependencies
└── 📄 sample.txt             # Sample text for testing
```

</details>

## 🚀 Installation

<details>
<summary>Click to view installation steps ⚙️</summary>

```bash
# Clone the repository
git clone https://github.com/yourusername/Lab_ATBMTT.git

# Navigate to project directory
cd Lab_ATBMTT

# Install dependencies
pip install -r requirements.txt
```

</details>

## 💡 Usage Examples

<details open>
<summary>Caesar Cipher Example 🔒</summary>

```python
from caesar_cipher import encrypt, decrypt

# Encrypt a message
encrypted = encrypt("HELLO WORLD", shift=3)
print(encrypted)  # Output: KHOOR ZRUOG

# Decrypt the message
decrypted = decrypt("KHOOR ZRUOG", shift=3)
print(decrypted)  # Output: HELLO WORLD
```

</details>

## 📊 Algorithm Flowcharts

<details open>
<summary>Caesar Cipher Process 🔄</summary>

```mermaid
%%{init: {'theme':'dark'}}%%
graph TD
    A[Start] --> B[Input Plain Text]
    B --> C[Set Shift Value]
    C --> D[For each character in text]
    D --> E{Is character a letter?}
    E -->|Yes| F[Shift character by shift value]
    E -->|No| G[Keep character as is]
    F --> H[Add to result]
    G --> H
    H --> I{More characters?}
    I -->|Yes| D
    I -->|No| J[Return encrypted/decrypted text]
    J --> K[End]

    classDef default fill:#2a2a2a,stroke:#7a7a7a,color:white;
    classDef highlight fill:#4a4a4a,stroke:#7a7a7a,color:white;
    class A,K highlight


```

</details>

<details open>
<summary>Hash Comparison Flow 🔍</summary>

```mermaid
%%{init: {'theme':'dark'}}%%
graph LR
    A[File 1] --> C[Calculate Hash]
    B[File 2] --> D[Calculate Hash]
    C --> E{Compare Hashes}
    D --> E
    E --> F[Files are identical]
    E --> G[Files are different]

    classDef default fill:#2a2a2a,stroke:#7a7a7a,color:white;
    classDef success fill:#28a745,stroke:#7a7a7a,color:white;
    classDef warning fill:#dc3545,stroke:#7a7a7a,color:white;
    class F success
    class G warning


```

## 📝 License

<details>
<summary>View License Details</summary>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

</details>

---

<div align="center">

### 🌟 Star this repository if you find it helpful!

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>

Made with ❤️ for the love of cryptography and security

![Visitors](https://api.visitorbadge.io/api/visitors?path=yourusername%2FLab_ATBMTT&label=Visitors&labelColor=%23697689&countColor=%232ccce4)

</div>