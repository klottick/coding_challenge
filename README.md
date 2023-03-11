# Checkpoint Coding Challange

This is a set of basic challenge questions to ensure canidates for Checkpoint Software Engineering
actually know the basics of programming and for us to evaluate their comprehension of the Python Langugage
as well as their coding style

## Submitting your challenge

## Prerequisites

You will need to have the following installed

* Python 3.8 or newer
* [Python Poetry](https://python-poetry.org/docs/#installation)

## Setup your environment

* Clone this repo
* run `poetry install .`
* make a new branch `git checkout -b submission/$USER`
  * Where $USER is your surname (family name)
* Update the code inside `coding_challenge/questions.py` to solve the presented problems

## Things you should and should not do

* You should not use any third-party libraries to solve the questions
  * However, you can use any third party library you whish to add "Flare" to your submission
  * Use `poetry add $LIBRARY` to add a dependency

* You should ensure your code is your code
  * If you borrow something from stack overflow or other places you should credit the author and link to the answer or post you used
  * If you do borrow code, explain why you did and needed to and explain why their peice of code is valid and efficient

* You should ensure your code is clean, efficient, easy to read and follow, and most importantly, correct

* You should run the test cases locally using:
  * `poetry run pytest`

* If you wish use a newer version of Python then 3.8, because you want to highlight a new language feature that makes your code better
  * Upgdate the version used in the following files to reflect the Python version you wish to use:
    * `.github/workflows/run_tests.yaml`
    * `pyproject.toml`

* Feel free to do anything in your PR that you think improves the challenge and helps to highlight other skills your want to show off
  * All the follow is completely optional but anything that helps to show off your skills is helpful
  * Examples
    * Make a Web UI using React or similar framework to run and show the tests results
    * Add parrellel test execution
    * Make a Restful API to run the tests cases
      * Use a db or other tool to add caching for previsouly retrieved questions based in the given input

## Using an alternative language

If you wish to use another language, you may absolutely do so, but you must do the following:

* Update the Github action to run the tests in your selected language
  * This link covers most popular lanagues:
    * [Github CI](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
* Convert the unit tests to work for your lanage of choice
