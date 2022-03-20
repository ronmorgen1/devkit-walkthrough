# Devkit Walk-through

## About the Devkit package
`pglearn-devkit` is a package designed to make the `pagaya_learn` package the most accessible it can possibly be. Some immediate goals of `pglearn-devkit` package are:
1. To make accessing pre-existing policies that are "in the wild" easy.
2. To enable "playing around" with those same policies.
3. In terms of exploration - Gain a more digestible insight about the jobs of each policy, and the steps of each job.

## Getting Started

### Installation

- Open a terminal window.
- Clone the repository and cd into it: `git clone https://github.com/ronmorgen1/devkit-walkthrough.git && cd devkit-walkthrough`
- Let's check that we have a valid pip.conf file: `cat ~/.config/pip/pip.conf`. The expected output is:
```
[global]

# The fixed index-url path
index-url = https://pagaya_user:*******************************************************************************@pypi.pagaya-services.com/
```
- If you don't get that, you need to create a new pip config file: `mkdir ~/.config/pip/ && mv ./pip.conf ~/.config/pip/pip.conf`. If you're getting the desired output, move to the next section.
- Create a new python environment: `python3 -m venv venv && source venv/bin/activate`
- Install the package by running: `pip install pglearn-devkit`

### Basic Usage

Follow to code-comments in the [basic example file](file:///basic-example.py) to see how to use the package.







## Resources
### Documentation
The documentation for `pglearn-devkit` is available in the [documentation center](https://verbose-carnival-77bce7c3.pages.github.io/pglearn-devkit/)
