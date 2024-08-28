# WorkShop_01

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Notebooks](#notebooks)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
`WorkShop_01` is a project that analyzes data on candidates, of which we can carry out an analysis and a corresponding data visualization, in order to understand the context a little more. This repository contains all the source code, data, and resources necessary to run the analyzes and visualizations.

## Project Structure
The project structure is as follows:
```
WorkShop_01/
│
├── .git/               # Git version control folder
├── .gitignore          # Files and directories ignored by Git
├── data/               # Data files used in the project
├── Graphics/           # Project graphics and images
├── NoteBooks/          # Jupyter Notebooks for analysis
├── README.md           # This Archive
├── requirements.txt    # Project dependencies
├── SQL/                # SQL scripts used
└── src/                # Project source code
```

## Installation
### Prerequisites
- **Python 3.8+** 
- Any other dependencies or software required.

### Steps
1. Clone this Repository:
   ```bash
   git clone https://github.com/JuanmaLopi/WorkShop_01.git
   ```
2. Navigate to the project directory:
   ```bash
   cd WorkShop_01
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
If you need to perform data analysis and visualization, you can refer to the data_cleaning file involved in the src folder.

What this file will allow you to do is the necessary analysis to be able to create the requested graphs, where the most important columns will be those of 'Technology', 'Seniority', 'Application Date' and 'Country'.

Likewise, you can also go to the Notebook, in which the connection to the database is explained even better and the analysis and visualization codes are embedded, with their respective explanation.

## Data
The `data/` folder contains the data sets needed for the analyses. This data has a total of 50,000 rows and 10 columns, which, since we have enough data, allows us to do a good analysis of it.

## Notebooks
Los Jupyter Notebooks en la carpeta `NoteBooks/` permiten explorar y visualizar los datos. Para ejecutar los notebooks:

```bash
jupyter notebook NoteBooks/
```

## Contributing
Contributions are welcome. Please follow the following steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Open a pull request.

## License
This project is under the MIT License - see the [LICENSE](LICENSE) file for more details.

## Contact
Name - Juan Manuel Lopez Rodriguez

email - [juan_m.lopez_r@uao.edu.co](mailto:tu-email@ejemplo.com)

Project Link: [https://github.com/JuanmaLopi/WorkShop_01](https://github.com/tu-usuario/WorkShop_01)

