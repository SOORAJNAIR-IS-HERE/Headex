from setuptools import setup

setup(
    name='Headex',  # Your tool's name
    version='1.0.0',  # Version of your tool
    description='A security header checking tool written in Python',  # A brief description
    author='Sooraj Nair',  # Your name
    author_email='your_email@example.com',  # Your email (optional)
    url='https://github.com/SOORAJNAIR-IS-HERE/Headex',  # Your GitHub repository URL
    py_modules=['headex'],  # The name of the Python file (without .py extension)
    install_requires=open('requirements.txt').read().splitlines(),  # Installs dependencies from requirements.txt
    entry_points={
        'console_scripts': [
            'headex=headex:main',  # This allows users to run your tool using the command 'headex'
        ],
    },
    license='MIT',  # The license of your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
