# Changelog

## 0.2.1 - 2019-07-31

+ Bugs:

    + Fix ownership. 

+ Miscellaneous:

    + Update Isort config.


## 0.2.0 - 2019-06-28

+ Feature:

    + Replace YAPF with Black.


## 0.1.1 - 2019-05-14

+ Bugs:

    + Replace 'src' with '{{ cookiecutter.project_source_code_dir }}'.
    
    + Change .version to '0.0.0' to fix 'make-release' Invoke task.
    
    + Remove shadowing of 'compile' built-in.

+ Docs:

    + Add Invoke tasks to README skeleton.

+ Miscellaneous:

    + Change release commit message in 'make-release' Invoke task.


## 0.1.0 - 2019-05-06

+ Manage dependencies with pip-tools instead of Pipenv.
 
+ Add Invoke tasks to automate making a release.

+ Integrate Pre-commit Git Hook with CI script.

+ Refactor setup scripts.

+ Refactor utilities and add <humanize_seconds>.

+ Rename folder \<constants> to \<dirs>.

+ Add Bandit.

+ Add CHANGELOGs.

+ Update flake8 to base on double quotes.

+ Refactor cowsays! Moo!

