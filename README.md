# Mental Health in the Tech Industry

__Contents__
- Mental_Health_Tech_Survey.ipynb

The Mental_Health_Tech_Survey.ipynb notebook explores data from a survey of mental health in the tech workplace for the years 2014, 2016, 2017, 2018, and 2019. The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry) and provided by Open Source Mental Illness (OSMI). This survey measures attitudes towards mental health-related issues in the tech workplace.

- utils<br>
  utils contains __helper_functions.py__ <br>
  The __helper_functions.py__ module includes essential functions used in the project for working with SQLite databases. These functions are responsible for connecting to the database, retrieving primary and foreign keys, executing queries, and more.<br>__generate_kaggle_credentials__ is a guide to set get the data within your workspace if you do not already have the KaggleAPI set up to work with your coding environment.<br><br>
- requirements.txt -- see this file for a complete list of requirements and versions that were used in my workspace at the time of this analysis. 

## Project Goals
- Understand the culture of the tech industry, particularly regarding mental health.
- Practice working with SQLite databases.
- Perform exploratory data analysis (EDA).
- Visualize data to gain insights.
- Enhance skills in reading data, performing queries, and filtering data using SQL and Pandas.

## Tools and Modules
- SQLite: To work with the database.
- Matplotlib: For data visualization.
- NumPy and Pandas: For data manipulation.
- Seaborn: For enhanced data visualization.
- SciPy: For statistical analysis.

Getting Started: 
1. Clone the repository 
   
2. Create a virtual environment using the requirements.txt file provided<br>
   e.g. 
```bash
python3 -m venv tech_mental_health/
# activate the venv and install all requirements provided 
source tech_mental_health/bin/activate
pip install -r requirements.txt
```

3. Open the Jupyter notebook file, Mental_Health_Tech_Survey.ipynb, in your Jupyter environment and step through to see analysis. 


### General Usage <br>
Open and run the Mental_Health_Tech_Survey.ipynb notebook.<br><br>
Ensure that mental_health.sqlite is in the notebook-created "data" directory and helper_functions.py are in the utils directory.

### License 
[MIT](https://opensource.org/license/mit/) 
