Assignment 3
============


.. questionnaire:: questionnaire_text_demo 10
  :title: Questionnaire full of freetext questions
  :submissions: 3
  :reveal-model-at-max-submissions: false

  This is about using the terminal in bayes to analyse some files.  

  .. freetext:: 5
    :length: 5
    :required:

    The folder `names` contains hundreds of files, each with a few names in them. Which is the most common first name? The idea is to use `cat`, `sed`/`awk`, `uniq -c`, `sort -nr`, and `head -1`

    test
    !test § Hint: follow the instructions.

  .. freetext:: 5
    :length: 5
    :required:

    The folder `tar` some files. The largest of them uses the name from the previous question as a password. Extract it, and remove all files containing a number. Re-zip the file, and get the checksum of the tarball. 
    Not as good a question for piping, but is good practise for navigating the filesystem and working with files.
    
    test
    !test § Hint: follow the instructions.