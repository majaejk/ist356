import mymodule as mm # import and alias a module
# at the same level in the same folder as mymodule *folder*
# the mymodule folder contains __init__.py file which is run on import 
# (when cherrypicking occurs the inline in init runs but vars and fns must be selected)

print(mm.country) # print a variable defined in __init__.py
mm.say_hi("Jane")

from mymodule import say_hi # import one function from the module can also alias
say_hi("John") # call the independently imported function directly without the module prefix (global scope)
print(mm.__name__) 

# other files in module folder can have submodules that are additional files within the folder
# folder.file.function()
# from folder.file import function