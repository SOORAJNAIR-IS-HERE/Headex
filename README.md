![Headex Logo](./Logo.png)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tested On](https://img.shields.io/badge/Tested%20On-Linux%20%7C%20OSX%20%7C%20Windows%20%7C%20)
![Docker Build](https://img.shields.io/badge/docker-build-blue)
![Automated](https://img.shields.io/badge/automated-yes-blue)
![License](https://img.shields.io/badge/License-MIT-blue)



**Headex** is a Python-based tool designed to scan and analyze HTTP headers of websites. It helps web developers and security analysts check for essential security headers and identify potential misconfigurations that could leave websites vulnerable.

## Features
- Check for critical security headers such as Content-Security-Policy, X-Frame-Options, and more.
- Provide insights and suggestions for improving header configurations.
- Supports scanning multiple URLs from a file or command line.
- Customizable user-agent and proxy support.
- Option to save output to a file.

## Installation

To run Headex, you need to have Python 3 installed. You can clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/Headex.git
cd Headex
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
