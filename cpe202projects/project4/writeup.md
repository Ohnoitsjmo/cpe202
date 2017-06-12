#Project 4
 
 
# Team Members:
 
- Jacky An
- Makena Kong
- Justin Mo
- Anthony Vuong
 
 
# Expected Data Structures
 
The purpose of a coverage tester is to record which lines of code are not utilized and to return the percentage of tested code. A simple implementation could use arraylists to represent the files used and the coverage of each file. When other files, like a file of functions, are imported into the current file, those files will also be tested for coverage. Each file is represented by an array list containing the number of statements, lines missed, and coverage percentage. To find the lines missed, another array can be used where each index represents the line number and Booleans indicating if the line is used. This array is altered while running each line of code.
 
 
# Initial Code Examination
 
The README briefly summarizes how coverage.py works. It lists the compatible versions of Python and the updates from previous versions of the project. There are 34 source files in the coverage subdirectory and many test files in the tests subdirectory - all source code. The amount of code is innumerable, but it seems almost half of the content is commentary.
 
In the tests subdirectory, test_collector.py tests specific aspects of the collection process by tracing an imported file during execution, ensuring it does not retrace the same file, and checking that each file was checked. The second file, test_concurrency.py, tests the available concurrency libraries after deciding which lines in the file are eligible code.
 
The files examined in the coverage directory are performed for coverage.py. The first file, collector.py, collects raw data in a Collector object.The second file, config.py, is a configuration file. The third file, control.py, controls the access, configuration and debugging. The fourth file, data.py, manages the collected coverage data. The last file, debug.py, controls the debugging process and what information gets displayed for an error.
 
 
 
# Detailed Code Examination

The initial speculation was that arraylists would be used to implement coverage.py. However, the actual data structures used are dictionaries, stacks, sets, and built-in lists. In the coverage directory, data.py organizes the collected data into a class of lists and dictionaries that will eventually be stored in a JSON format file.
 
The data is distributed into a CoverageData class with the four attributes: lines, arcs, file_tracer and runs. Inside the class are methods that father and organize the data into lists and methods that generate the structures for each attribute. Lines is a dictionary that maps file names to lists of the line numbers executed. If the data has arcs, arcs is a dictionary that maps file names to lists of the line number pairs. File_tracers is a dictionary that maps file names to plugin names. And lastly, runs is a list of dictionaries of run information for coverage.py.
 
Once the data is stored in a file, the object is erased.The files are then handled in the CoverageDataFiles class, which contains a warning reference that indicates when a file cannot be read, a debug reference for creating debug messages, and a basename reference to use for storing data passed into the class. This class also contains several functions that will erase, read, write, and format the data. Additional functions include one that combines several files of data together, another to change the JSON file into canonical form, and another to make the data look presentable to the reader. All these functions are then executed by the main function after receiving a command line argument. Most of the data in these files are stored in lists, which is an appropriate data structure since the data needs to be accessed quickly. 
 
# Summary
 
The comments are significantly helpful when reading each chunk of source code. The ‘’’ comments describe what a function or class does, whereas the # comments explain steps or clarify the processes. Maintaining this code would be straightforward because the source code is well-organized by the comments.
 
 Regarding our own code, our comments do not explain functions in-depth. The comments in the coverage source files do not follow our template for a function; they lack the signature and purpose statements. Instead, detailed descriptions are added strategically, such as comments inside functions that describe how the function operates, thus anyone can grasp how the source file works.
 
Overall, coverage.py is orderly and easy to understand. Although the code can be hard to follow, the comments simplify and clarify so that any user can comprehend the contents of the files.

