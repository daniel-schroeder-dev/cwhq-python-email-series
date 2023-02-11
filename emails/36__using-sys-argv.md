## Question

A young Python programmer is working on a program that will be run from the command line (a common task for Python scripts). In this program, a user can enter a folder name and the script will create a ZIP archive of all of the data in that folder and save it to a provided destination. The details of how the ZIP/save logic work aren't important for our purposes here, but how they get the folder to ZIP and the location to send the ZIP file are.

This is what they are doing so far:

```python
zip_folder = input("What folder do you want to ZIP? ")
zip_save_location = input("Where do you want the ZIP file to be saved? ")

# Run the rest of the ZIP/save logic
```

An experienced Pythonista notices that their is another way to get the users `zip_folder` and `zip_save_location` without having to prompt them while the program is running. Research how to get command-line arguments using the `sys` module and see if you can refactor the logic that gets the ZIP/save location.

## Answer

```python
import sys

zip_foder = sys.argv[1]
zip_save_location = sys.argv[2]

# Run the rest of the ZIP/save logic
```

## Explanation

The `sys.argv` property allows you to get data from the command-line. The user passes in the data when executing the Python script, like this:

```bash
python script_name.py argument1 argument2
```

In our case, if the script was called `zip_files.py` and the user wanted to zip the folder "Pictures" and send it to "ZIP-Files" they would invoke the script like this:

```bash
python zip_files.py Pictures ZIP-Files
```

## Resources

-   [The Python Docs - `sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv)
