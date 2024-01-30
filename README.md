This repository houses the base class for projects that calculate Sustainable Development Goals (SDGs). SDGs are measures of The 2030 Adgenda for Sustainable DevelopmentCalculations of individual SDGs are done in other repositories that inherit this one as a git submodule. 

See below for set up details:

The expected file structure for a sdg project is as follows:
```
sdg-x-x-x
+-- .github
  +-- workflows
    +-- test.yml
+-- src
  +-- sdg_x_x_x_src
    +-- sdg_base (submodule)
    +-- __init__.py
    +-- sdg_x_x_x.py
+-- tests
  +-- __init__.py
+-- .env
+-- .gitignore
+-- .gitmodules
+-- pyproject.toml
+-- README.md
+-- user_params.py
```


to set up submodule go to the sdg_x_x_x_src folder (e.g. sdg_11_3_1_src) in git bash within the local project directory. Run the following command

```git submodule add https://github.com/ONSgeo/sdg_base.git```

this adds the submodule to the sdg project that you're developing. You can then use the features of the base class project as if they're local files from within the project.



