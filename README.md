# Symmetric Encryption & Cipher Modes

This project is part of a lab assignment from the ECE/CS 5560 course, focusing on symmetric-key encryption techniques and block cipher modes. It involves practical cryptography exercises using OpenSSL, Python, C, and Docker containers.

The lab covers core encryption principles, explores common vulnerabilities due to misconfiguration or misuse of cryptographic modes, and demonstrates attacks like known-plaintext and chosen-plaintext attacks.

## 🔍 Overview

Through a series of six tasks, this lab provides hands-on experience with:

- Symmetric key encryption using OpenSSL
- ECB vs CBC mode behavior and vulnerability visualization
- Custom implementation of CBC and OFB modes with AES-256
- Padding mechanisms (e.g., PKCS#5/7)
- Error propagation in different encryption modes
- Security implications of IV reuse and predictability
- Oracle-based chosen-plaintext attack (Task 6.3)

📄 A detailed report of the lab activities is included here:
- `Lab2_Symmetric_Cipher_Modes.pdf`

## 🧱 Directory Structure

```
.
├── Files/                         # Contains files used across multiple tasks (e.g., images, scripts)
├── docs/                          # Lab writeups, supporting documents
├── encryption_oracle/             # Docker-based oracle for Task 6.3
├── img/                           # Input/output images used for ECB/CBC visualization
├── task1/                         # OpenSSL encryption/decryption using various ciphers
├── task2/                         # ECB vs CBC encryption comparison on images
├── task3/                         # AES CBC & OFB implementations (Python/C)
├── task4/                         # Padding mechanism and file encryption tests
├── task5/                         # Error propagation analysis in different modes
├── task6/                         # IV analysis, common attacks, Docker setup for oracle
├── docker-compose.yml             # Docker orchestration for Task 6.3
├── LICENSE
└── symmetric_enc_report.pdf       # Full report with observations and screenshots
```

## 🧪 Lab Environment

This project uses the SEED Ubuntu 20.04 virtual machine, along with Docker containers for simulating encryption oracles. To set up the environment:

```bash
# Clone the repo and enter the directory
git clone https://github.com/your-username/symmetric-enc.git
cd symmetric-enc

# Start the encryption oracle container (only needed for Task 6.3)
docker-compose up -d
```

Use `docker ps` and `docker exec -it <container_id> bash` to access running containers if needed.

## 🔧 Tools & Technologies

- OpenSSL (`enc` command-line tool)
- Python (with PyCryptoDome or similar)
- C (AES examples)
- Docker & Docker Compose
- Hex editors (e.g., `bless`)
- Image tools (e.g., `eog` for BMP file visualization)

## ⚠️ Security Lessons

This lab helps uncover **misuse patterns** that weaken encryption:

- Why **ECB leaks patterns** in encrypted data
- Dangers of **IV reuse and predictability**
- **Padding oracle** exposure
- **Error propagation** in stream vs block modes
- Importance of random, unique IVs and authenticated encryption

## 📝 Report

Please refer to [`symmetric_enc_report.pdf`](./symmetric_enc_report.pdf) for a complete breakdown of:

- Design and implementation
- Observations and explanations
- Screenshots of encryption outputs and attacks
- Insights from common crypto pitfalls

## 📚 Credit

- Lab inspired by **SEED Labs** developed by Dr. Wenliang Du: https://seedsecuritylabs.org/
- Docker setup and lab structure based on [SEED Manual for Containers](https://github.com/seed-labs/seed-labs/blob/master/manuals/docker/SEEDManual-Container.md)
