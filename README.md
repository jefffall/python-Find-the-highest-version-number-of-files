# python-Find-the-highest-version-number-of-files
Given a list of files like: installerV1.2.3.dmg find the highest version numbered file


 Question 1:
----------
Given a folder of build files that might look like this:

/Build-1.dmg
/Build-2.dmg
/Build-2.1.dmg
/Build-2.1.1.dmg
/Build-3.dmg
/Build-3.2.dmg
/Build-3.19.dmg

Write a script that takes a path to the folder as an argument, and prints the highest build number (just the number, i.e. 2.1.1)
Note:  The first digit can go up to 999 and should always be present, but the second and third can only go up to 99, and might not be included.
