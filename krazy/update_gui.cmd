call cd gui
call forfiles /M *.ui /C "cmd /c pyuic4 @file -o @fname.py"
call exit