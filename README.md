# Introduction

[The Sustainable Development Goals (SDGs)](https://sdgs.un.org/goals) are part of the UN 2030 Agenda for Sustainable Development. The Office for National Statistics (ONS) reports the UK data for the SDG indicators on the [UK SDG data webpage](https://sdgdata.gov.uk/), contributing to progress towards a sustainable global future.

In total, there are 17 Sustainable Development Goals and 169 indicators be be reported covering themes such as equality, climate action, and energy and infrastructure. This code provides a base class with methods for a [standardised template](https://github.com/ONSgeo/sdg_template) that supports the automated calculation of SDG indicators to assist in the timely reporting of progress towards sustainable development. 

## Scope

The methods of this base class provide common functionality applicable to the calulation of SDG indicators, such as inputting data and exporting results. This promotes reuse of code to avoid duplication of work.

This class is inherited into the template for SDG indicators using a git submodule found in the src folder. Scripts for the calculation of individual SDG indicators built from this template will inherit the these methods and attributes allowing for the quick development of individual SDG indicator calculations as required.

Changes made to the base class will also apply to the other SDGs. **Modifications to the base class should as such only be considered if they are also applicable to the calculation of other SDG indicators**. 

# Set up instructions

## If re-running an existing SDG calculator with new input data:

1. Clone the repository of the calculator into your local folder.
 
2. Open git BASH and run the following two commands:


```git submodule init```

```git submodule update```

## If creating a new SDG calculator:

This can be achieved easily using the template repository to create your repo. 

[See here for instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)

[See here for template repository](https://github.com/ONSgeo/sdg_template)


#### Structure of template
The expected file structure for an SDG project is as follows:
```
sdg-x-x-x
+-- .github
| +-- workflows
| | +-- test.yml
+-- src
| +-- sdg_x_x_x_src
| | +-- sdg_base (submodule)
| | +-- __init__.py
| | +-- sdg_x_x_x.py
+-- tests
| +-- __init__.py
| +-- test_sdg_x_x_x.py
+-- .env
+-- .gitignore
+-- .gitmodules
+-- pyproject.toml
+-- README.md
+-- Calculate_SDGx_x_x.ipynb
+-- user_params.py
```

#### These steps are only necessary if you haven't used the template to create your repository
1. Set up submodule go to the sdg_x_x_x_src folder in your file tree (e.g. sdg_11_3_1_src) in git bash within the local project directory. Run the following command:
 
```git submodule add https://github.com/ONSgeo/sdg_base.git```
 
this adds the submodule to the sdg project that you're developing. You can then use the features of the base class project as if they're local files from within the project.

to set up this submodule, go to the sdg_x_x_x_src folder (e.g. sdg_11_3_1_src) in git bash within the local project directory. Run the following command

```git submodule add https://github.com/ONSgeo/sdg_base.git```

this adds the submodule to the sdg project that you're developing. You can then use the features of the base class project as if they're local files from within the project.

# Methods offered by the base class:
These are accessible to all classes that inherit from it
- `set_input_data_dir()` Sets directory and creates folders from which data is input.
- `get_input_data_dir()` returns main directory in which data is stored.
- `set_output_data_dir()` sets directory and creates folders for data outputs.
- `get_output_data_dir()` Returns directory in which outputs are stored.
- `set_file_tree()` Sets file tree for input and output data.
- `create_folders()` Creates folders to store output data.
- `get_ext_files()` Retrieves input files by extension with optional file name filtering.
- `_get_read_function()` Returns the relevent read method based on the input extension.
- `load_data()` Joins and loads data as a data frame.
- `save_data()` Saves data as .csv or .shp, dependent on dataframe.
- `calculate_sdg()` Abstract method, this must be implemented in the SDG subclasses

