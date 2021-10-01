# Opening Multiple File Types with Python

## Background on file types

You may come across a number of different file types for saving and exchanging information. Read through the information about different file types that are commonly used for exchanging data.

### CSV:
* https://frictionlessdata.io/docs/csv/
* https://tools.ietf.org/html/rfc4180
* https://en.wikipedia.org/wiki/Comma-separated_values

### Other delimited formats

* https://en.wikipedia.org/wiki/Tab-separated_values (Links to an external site.)
* https://en.wikipedia.org/wiki/Delimiter-separated_values (Links to an external site.)

### Fixed-width format (uncommon, used to be used more)

* http://www.softinterface.com/Convert-XLS/Features/Fixed-Width-Text-File-Definition.htm (Links to an external site.)

### FORTRAN formats for fixed-width data 

* I've used some statistical programs which used format statements like these. 
* https://eml.berkeley.edu/sst/fmttop.html

### XML:

* https://www.w3schools.com/xml/default.asp

### JSON:

* https://www.w3schools.com/js/js_json_intro.asp

With a foundation in some common text file formats used for data storage and exchange, you may as well take a look at some data exchange formats in common use in healthcare.

### HL7 (v2.x and v3)

* https://en.wikipedia.org/wiki/Health_Level_7
* https://www.youtube.com/watch?v=ZAgdYR1rmEQ

Most of the systems I work with use HL7 v2.3 and v2.5 messages. (These standards are decades old, but still in common use.)
The HL7 v3 specification exists, but it's not widely adopted. (Complexity is a barrier.)

### FHIR

* https://www.hl7.org/fhir/overview.html
* https://www.hl7.org/fhir/messaging.html
* https://www.youtube.com/watch?v=oSqISJw_nv0

### Optional

* SMART on FHIR https://www.youtube.com/watch?v=MMfe181tmwU

## Summary of steps to complete

- [ ] Fork this repository so you have your own copy to work on.
- [ ] Clone the repository on your local machine. 
- [ ] Open the repository Jupyter Notebook in VSCode or Jupyter Notebooks.
- [ ] Add the code shown in this video to your Jupyter Notebook.
- [ ] Push your updated file to your GitHub repository.
- [ ] Answer assignment questions and submit a link to this GitHub repository in Canvas.
- [ ] Remove your virtual environment from Jupyter Notebooks and from your machine.

## Fork & Clone this repository

* We did this in a previous assignment. Instructions are here: https://github.com/cmcntsh/exerGitPractice
* This can also be done directly in VSCode
  * Create a new folder on your machine where you want to put this repository if you don't already have one you want to use.
  * Copy the Clone or Download path for this repository from GitHub.
  * In VSCode from the command pallette (Ctrl-Shift-P) run Git: Clone
  * Paste the path into the path field which pops up
  * Select your new folder you created on your machine
  * A new folder for the repository with the repository files should be in the folder you selected showing in the Explorer window in VSCode on the left side.

## Open the repository Jupyter Notebook
* Open Jupyter Notebook on your machine.
* In the Files tab you should see folders that match the folders on your machine (i.e. Desktop, Documents, Downloads). Navigate to your repository folder by clicking on the folder links. Open the .ipynb file in your repository by clicking on it.
* Jupyter Notebooks can also be run in VSCode. Once you click on the file in VSCode, it takes a minute to start up. Once it starts you can create cells and run code. (The interface is a little different, though.)


## Complete the steps of the assignment

* Extract the contents of the zip folder
* Open each of the data file types and examine the contents.
    * (Excel is probably the best program for opening the .xlsx and .csv files. VSCode or Notepad++ are good for looking at the .json and .xml files.)
* How  would you go about combining the data from these different files into a single data set? 
    * If you only had the few items in this small example it would not take long to copy and paste or manually enter the data into a spreadsheet. What if you had 100 or 1000 or more individual files. Manual entry would take a long time.
* The Jupyter Notebook uses Python to open each file in the folder, add the contents to a single dataset, and save a new csv dataset with all the data.
* Open the notebook file (extension .ipynb) in Jupyter Notebooks.
* (2021 update - The notebook has been reformatted to include cells for each step of the assignment. Just complete the whole notebook.) Run each cell except the last one by clicking the Run button next to the cell or the Run button under the menu.
    * See how the dataframe at the end includes the contents of each of the individual files you looked at?
* Create a new data file for each type included in the folder. (You can use Excel to modify the content in the .xlsx and .csv files and save them under a new name in the same folder. You can use VSCode or Notepad++ to modify the content of an .xml and .json file and save those under a new name in the same folder.)
* (2021 update - You don't need to rerun the cells. The notebook has been updated to include cells for each step. Just follow the notebook as it is currently written.) Now run each cell in the Jupyter Notebook again. Notice how the contents of your new files is now included in the dataframe. Run the last cell and save the data set as a csv file. Make sure your new csv file is included in your repository.

## Push your updated file to your GitHub repository

* This can be done in VSCode.
  * In VSCode click on the Source Control button.
  * You should see the files that had changes. (Mine has the original file which shows an M next to it and a new file which says checkpoint in the name. You really only need to push the original file, but if you push both it shouldn't hurt anything.)
  * Hover over the changed file. Click the + sign to stage the change.
  * Enter a commit message in the message field and click the checkmark to commit the change.
  * Click on the 3 dots for more actions and select Sync. This will push the updated file to your GitHub repository.
  * Submit the link to your GitHub repository on Canvas.
  
