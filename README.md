# TaMper

TaMper is a programming language made by XSX (maggixx) and MartyBoi (imdoingthisfortheprofile).
It is designed to be simple to read and use, but not for actual productivity.
TaMper is written in python, and uses simple commands.


## Variables
TaMper has variables, that can be referenced in some commands and can be created and set, but not deleted.
### Preset variables:
#### placeholder
Its a placeholder. What else do i have to say?
#### os
Contains the name of the current os.
## Speak
The speak command takes one argument (str), and it will output whatever that argument is onto the console.
Syntax :
```
speak [output]
```
Example :
```
speak hello world
-----------------
Output :
hello world
```

## Exit
The exit command takes no arguments, and simply calls the python command "exit()"
Syntax :
```
exit
```

## Os
The os command takes no arguments, and outputs the current os the system is running on.
Syntax :
```
os
```
Example :
```
os
-----------------
Output :
Linux-5.11.0-1023-gcp-x86_64-with-glibc2.27
(thats what repl.it uses)
```

## Lb
The lb command takes no arguments, and outputs a single line break.
Syntax :
```
lb
```
Example :
```
lb
-----------------
Output :

```

## Wait
The wait command takes one argument (int), and stops execution for the amount of seconds given.
Syntax :
```
wait [seconds]
```
Example :
```
wait 3
-----------------
Output :
(does nothing for 3 seconds)
```

## Add
The add command takes one argument (str), and adds a variable that can be called.
Syntax :
```
add [variable name]
```
Example :
```
add test
-----------------
Output :
(nothing yet)
```

## Set
The set command takes two arguments (str,str), and sets the variable with the name of argument one to argument two.
Syntax :
```
set [variable name] [value]
```
Example :
```
add test
set test Hello!
speak %test%
-----------------
Output :
Hello!
```

## Get
The get command takes two arguments (str,str) that are joined with a "://", and outputs a GET request to the given string (url expected).
Syntax :
```
get [protocol]://[url]
```
Example :
```
get https://example.com
-----------------
Output :
<html>
    ...
</html>
```

