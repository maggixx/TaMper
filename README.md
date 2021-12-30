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

If a variable referenced does not exist, it will simply return "VARIABLE[inputted variable name]"

## Exit
The exit command takes no arguments, and simply calls the python command "exit()".

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

## Speak
The speak command takes one argument (str), and it will output whatever that argument is onto the console.
If the given argument starts and ends with %, it will look for a variable with that name.

Syntax :
```
speak [output]
```

Example :
```
speak hello world
add bhsu
set bhsu hello again
speak %bhsu%
-----------------
Output :
hello world
hello again
```

# Errors
There are errors that can occur in certain places in the code
### Error 1
This error occurs when you try to run a file that does not exist.
### Error 2
This error occurs when an invalid command is read from code.
### Error 3
This error occurs when an invalid url protocol is given to the GET command.
### Error 4
This error occurs when a website/url is given to the GET command, and it is unable to connect to the given website/url.
