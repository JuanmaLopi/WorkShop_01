---

### **1. Project Overview**
`WorkShop_01` is a data analysis project focused on candidate data from a selection process. Through a comprehensive and varied dataset, the project aims to explore relevant patterns, trends, and statistics, as well as generate visualizations to facilitate a better understanding of the data.

### **2. Objectives**
- Conduct an in-depth analysis of candidate data to identify trends and patterns.
- Create clear and useful visualizations to communicate findings.
- Develop clean, modular code that allows for future analysis expansions.

### **3. Requirements and Environment Setup**
#### **3.1 Prerequisites**
- **Python 3.8+**: The programming language used for data manipulation and visualization.
- **Jupyter Notebook**: Recommended tool for interactive data exploration and analysis development.
- **Git**: For version control and collaboration.

#### **3.2 Dependency Installation**
The project includes a `requirements.txt` file with all necessary dependencies. To install these dependencies, run:
```bash
pip install -r requirements.txt
```

### **4. Project Structure**
The project is organized modularly, enabling easy navigation and understanding of the workflow.

```plaintext
WorkShop_01/
│
├── .git/               # Version control files
├── data/               # Data files used in the project
├── Graphics/           # Generated graphics and images
├── NoteBooks/          # Notebooks for interactive analysis
├── src/                # Source code for scripts and modules
├── SQL/                # SQL scripts for data manipulation
├── README.md           # Basic project documentation
└── requirements.txt    # Dependency list
```

### **5. Technical Explanation of Components**

#### **5.1 Modules and Scripts**
- **data_cleaning.py**: This script is responsible for data cleaning and preparation. It performs tasks such as handling missing values, data type conversion, and filtering relevant columns.
  
- **db_conexion.py**: A module that manages database connections. It allows for executing SQL queries to extract, insert, or manipulate data.

#### **5.2 Notebooks**
- **Data_Analysis.ipynb**: Contains the entire data analysis process, from data loading to generating charts. It focuses on interactive exploration and visualization through charts like bar charts, multiline charts, and pie charts.

#### **5.3 SQL**
- **candidates.sql**: Contains SQL queries necessary for extracting and manipulating data stored in the database.

### **6. Usage Instructions**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/JuanmaLopi/WorkShop_01.git
   cd WorkShop_01
   ```
2. **Set up the environment**:
   (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run analysis**:
   Navigate to the `src` folder and run the `data_cleaning.py` script to prepare the data.

5. **Explore visualizations**:
   Open the notebook `Data_Analysis.ipynb` to explore the data and generate visualizations.

### **7. Data Analysis and Visualization**
The analysis focuses on key columns such as:
- **Technology**: To identify the most in-demand technologies.
- **Seniority**: To assess the experience level of candidates.
- **Application Date**: To analyze temporal trends.
- **Country**: To understand geographical distribution.

The generated charts include:
- **Bar Charts**: Comparison of technologies and countries.
- **Multiline Charts**: Temporal trends.
- **Pie Charts**: Percentage distribution by category.

### **8. Testing**
The project does not include a formal test suite, but it is recommended to:
- Validate data cleaning by reviewing descriptive statistics after running `data_cleaning.py`.
- Verify the accuracy of visualizations by comparing them with expected sample values.

### **9. Maintenance and Contributions**
To contribute to the project:
1. Fork the repository.
2. Create a new branch with the feature you want to add.
3. Make your changes and commit them.
4. Open a pull request.

### **10. License and Contact**
This project is licensed under the MIT License. You can contact the author:

**Name:** Juan Manuel Lopez Rodriguez  
**Email:** [juan_m.lopez_r@uao.edu.co](mailto:juan_m.lopez_r@uao.edu.co)  
**Repository:** [https://github.com/JuanmaLopi/WorkShop_01](https://github.com/JuanmaLopi/WorkShop_01)
