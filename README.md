This repository houses the base class for projects that calculate progress towards meeting Sustainable Development Goals (SDGs). SDGs are measures of The 2030 Adgenda for Sustainable Development, adopted by the United Nations (UN) in 2015. There are 17 goals and 169 targets that encompass themes such as equality, climate action, and energy and infrastructure. The timely reporting of progress towards meeting SDGs by UN member states is of importance in achieving a sustainable global future: as such, this SDG base class has been created to provide a template from which calculations of individual SDG indicators can be automated.  

This base class contains common functionality required for the calculation of SDG indictors; this includes setting a root directory from which to work on a local machine, importing input data and exporting results. It is inherited as a git submodule into other repositories that calculate individual SDG indicators. 

# Set up instructions

If re-running an existing SDG calculator with new input data:

1. Clone the repository of the calculator into your local folder.
 
2. Open git BASH and run the following two commands:


```git submodule init```

```git submodule update```


If creating a new SDG calculator:

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
+-- user_params.py
```
  
1. Set up submodule go to the sdg_x_x_x_src folder in your file tree (e.g. sdg_11_3_1_src) in git bash within the local project directory. Run the following command:
 
```git submodule add https://github.com/ONSgeo/sdg_base.git```
 
this adds the submodule to the sdg project that you're developing. You can then use the features of the base class project as if they're local files from within the project.

to set up this submodule, go to the sdg_x_x_x_src folder (e.g. sdg_11_3_1_src) in git bash within the local project directory. Run the following command

```git submodule add https://github.com/ONSgeo/sdg_base.git```

this adds the submodule to the sdg project that you're developing. You can then use the features of the base class project as if they're local files from within the project.

# Further Reading

