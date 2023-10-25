"""Given an array of arguments, representing system call arguments keys and values, join it into a single, space-delimited string. You don't need to care about the application name -- your task is only about parameters.

Each element of the given array can be:

a single string,
a single string array,
an array of two strings
In the last case (array of two strings) the first string should have a "--" prefix if it is more than one character long; or a "-" prefix otherwise; e.g.:

["foo", "bar"] becomes "--foo bar"
["f", "bar"] becomes "-f bar"
You may assume that all strings are non-empty and have no spaces.

Examples
["foo", "bar"]                    #  "foo bar"
[["foo", "bar"]]                  #  "--foo bar"
[["f", "bar"]]                    #  "-f bar"
[["foo", "bar"], "baz"]           #  "--foo bar baz"
[["foo"], ["bar", "baz"], "qux"]  #  "foo --bar baz qux"
"""
def args_to_string(args):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate through the arguments in the 'args' list
    for arg in args:
        # Check if the argument is a list
        if isinstance(arg, list):
            # If the list has two elements, assume it's a prefixed argument
            if len(arg) == 2:
                # Determine the prefix "--" or "-" based on the length of the first element
                prefix = "--" if len(arg[0]) > 1 else "-"
                # Add the formatted argument to the results list
                result.append(f"{prefix}{arg[0]} {arg[1]}")
            # If the list has only one element, add it as is to the results list
            elif len(arg) == 1:
                result.append(arg[0])
        # If the argument is a string, add it as is to the results list
        elif isinstance(arg, str):
            result.append(arg)
    
    # Finally, join all the results into a string with spaces and return it
    return " ".join(result)

# Usage examples:
print(args_to_string(["foo", "bar"]))                    # Should print "foo bar"
print(args_to_string([["foo", "bar"]]))                  # Should print "--foo bar"
print(args_to_string([["f", "bar"]]))                    # Should print "-f bar"
print(args_to_string([["foo", "bar"], "baz"]))           # Should print "--foo bar baz"
print(args_to_string([["foo"], ["bar", "baz"], "qux"]))  # Should print "foo --bar baz qux"

