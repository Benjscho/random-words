# random-words

This is a quick function that pulls an optional number of random words from a text file and prints them to the console. The words included in this project were taken from https://github.com/dwyl/english-words.

To run this from the command line generating x number of words:
```sh
python3 random-words.py x
```

If run without a value for x, the default value is 1.

##Shell command usage

Added Shell command. To use:
- Update the path in .my_commands.sh to the absolute path of your download directory.
- Update the same path in random-words.py.
- Navigate to the random-words directory and run the below in the terminal:
```sh
source .my_commands.sh
```

You can then run this in any directory to generate any number of random words, as below:

```sh
random_words x
```
