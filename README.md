# Flask Page Tester

This project offers a quick and simple flask webserver that takes a page
 as an argument. Another optional argument is a file that contains a
 dictionary with the variables the page should render.

The project only requires Flask to be present on the system, and assumes
 a certain folder structure:

    |-static        -> the js/css/img etc files
    |-templates     -> the location of the templates to render
    |   |-subpages  -> (optional) includes for flask
    |   |-layouts   -> (optional) masterpage templates
    |-varfile.py    -> (optional) Variables to pass on to the page

# The varfile

The varfile should contain the `page_vars` variable, which should be a 
 dictionary containing the variable names(keys) and content (values).
An example is provided (`hello_world.py`)
