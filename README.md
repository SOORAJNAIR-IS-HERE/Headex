<p align="center">
  <img src="./Logo.png" alt="Headex Logo" width="600"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/Tested%20On-Windows%20%7C%20Linux-brightgreen" alt="Tested On">
  <img src="https://img.shields.io/badge/docker-build-blue" alt="Docker Build">
  <img src="https://img.shields.io/badge/automated-yes-blue" alt="Automated">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
</p>



**Headex** is a Python-based tool designed to scan and analyze HTTP headers of websites. It helps web developers and security analysts check for essential security headers and identify potential misconfigurations that could leave websites vulnerable.

## Features
- Check for critical security headers such as Content-Security-Policy, X-Frame-Options, and more.
- Provide insights and suggestions for improving header configurations.
- Supports scanning multiple URLs from a file or command line.
- Customizable user-agent and proxy support.
- Option to save output to a file.

## Installation

To run Headex, you need to have Python 3 installed. You can clone the repository and install the required dependencies.

**Clone the Repository:**

```bash
git clone https://github.com/SOORAJNAIR-IS-HERE/Headex.git
```
**Navigate to the Project Directory:**

```bash
cd Headex
```
**Install the Required Dependencies:**

```bash
pip install -r requirements.txt
```

## Usage
**To scan a single URL:**
```python
python headex.py -u http://example.com
```
**To scan a Multiple URL:**
```python
python headex.py -u http://example.com http://example2.com
```
**To scan URLs from a file:**
```python
python headex.py -f urls.txt
```
**To save output to a file:**
```python
python headex.py -u http://example.com -o output.txt
```
## License

This project is licensed under the MIT License - see the LICENSE file for details.
