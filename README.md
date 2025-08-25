# AIPI 503 Final Project

This project calculates the carbon emission for countries you select from the dataset. A list of user sessions for a
popular e-commerce website is the dataset we used. We group by the country and calculate the sum to determine the total
amount of bytes used for each country. Our API is a carbon emissions calculator that takes in the total amount of bytes
per country. It gives the Total CO2 emissions in grams, the percentage of websites it is cleaner than, and the energy
used per each country.

## Getting Started

### Websites

#### API
https://api.websitecarbon.com/

#### Kaggle Dataset
https://www.kaggle.com/datasets/kzmontage/e-commerce-website-logs

## Prerequisites
Python 3.11+, Git

## Installation

### Clone the repo

```
git clone https://github.com/Michaelsaju1/AIPI_503_Final_Project
cd AIPI_503_Final_Project
```

## Create and activate a virtual environment

```
python3 -m venv .venv    # Create the virtual environment
source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

## Install dependencies

```
pip install -r requirements.txt
```

## Running the App

To run the console version:

```
cd src
python3 app.py
```

To run the Streamlit version:

```
cd src
streamlit run streamlit_app.py
```

## Usage

For the console version, you will be presented

# License

This project is licensed under the MIT License. See the LICENSE file for details.
