This repository houses the base class for projects that calculate progress towards meeting Sustainable Development Goals (SDGs). SDGs are measures of The 2030 Adgenda for Sustainable Development, adopted by the United Nations (UN) in 2015. There are 17 goals and 169 targets that encompass themes such as equality, climate action, and energy and infrastructure. The timely reporting of progress towards meeting SDGs by UN member states is of importance in achieving a sustainable global future: as such, this SDG base class has been created to provide a template from which calculations of individual SDG indicators can be automated.  

This base class contains common functionality required for the calculation of SDG indictors; this includes setting a root directory from which to work on a local machine, importing input data and exporting results. It is inherited as a git submodule into other repositories that calculate individual SDG indicators. 

# Set up instructions

## If re-running an existing SDG calculator with new input data:

1. Clone the repository of the calculator into your local folder.
 
2. Open git BASH and run the following two commands:


```git submodule init```

```git submodule update```





## If creating a new SDG calculator:

This can be achieved easily using the template repository to create your repo. 

See here for instructions: {link to creating from template}

See here for template repository: {link to template repo}


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

# Further Reading

## Methods offered by the base class:
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

