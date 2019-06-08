#!/bin/bash
PATH_TO_PYTHON_SCRIPT=/Users/benjaminjschofield/ProgrammingLearning/random-words/random-words.py

function random_words() {
  python3 $PATH_TO_PYTHON_SCRIPT $1
}
