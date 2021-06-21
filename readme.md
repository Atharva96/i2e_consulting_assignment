-> Flow of Application
The main page consists of a textarea and container for avaliable files and also along with them there are 
options to perform required operations like 

1. Create a file
2. Read a file 
3. Update a file
4. Delete a file

==>> All in one page


Files are stored in database and also on FileSysystem as well inside 'textfiles' folder.

1. Create file router creates a new file and deletes the previous files if given name already exists and create a new
file with updated content

2. Read a file router reads the content of file using a specific id linked with file record inside database.

3. Update a file router update the content of file using a specific id linked with file record inside database.

4. Delete a file router deletes the file using a specific id linked with file record inside database.

5. index.html is the main page of the Django application.

6. base.html is a kind of parent page from which other pages are inherited and fetch the upper class functionalities

7. navbar.html is used for navigation pannel which contains dummy buttons for menu

8. sqlite3 database is used as it is inbuilt supported database for Django