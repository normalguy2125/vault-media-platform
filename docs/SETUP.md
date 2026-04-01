# Setup Instructions for Google Colab

This document outlines the steps to set up the Vault Media Platform project using Google Colab.

## Step 1: Open Google Colab
- Navigate to [Google Colab](https://colab.research.google.com/).

## Step 2: Create a New Notebook
- Click on 'File' in the top menu.
- Select 'New Notebook' from the dropdown.

## Step 3: Install Required Packages
In a code cell, run the following command to install the necessary packages:
```python
!pip install -r requirements.txt
```

## Step 4: Clone the Repository
To access the project files, clone the repository:
```python
!git clone https://github.com/normalguy2125/vault-media-platform.git
```

## Step 5: Navigate into the Project Directory
Change the current working directory to the cloned repository:
```python
import os
os.chdir('vault-media-platform')
```

## Step 6: Load and Run Your Scripts
You can now start running your scripts in Google Colab! 
- Make sure to adjust any file paths if necessary.

## Step 7: Save Your Work
Always save and checkpoint your work in Google Colab to prevent data loss.

For more information, refer to the official [Google Colab documentation](https://colab.research.google.com/notebooks/welcome.ipynb).