"""
Console help prompt.
Shown when executing `mastertables` from the terminal.
"""

def help():
    print("This package is not intended to be used from the console.")
    print("Usage in scripts:")
    print("")
    print("    from mastertables import mastertables")
    print("    mt = mastertables.MasterTablesClient(\"<api_key>\")")
    print("    mt.get_vocabulary(\"<vocabulary_id>\", [, category=\"<category>\"])")
    print("    mt.get_vocabulary_reverse(\"<vocabulary_id>\", [, category=\"<category>\"])")
    print("    mt.get_values(\"<vocabulary_id>\")")
    print("")
    print("For more help, visit: https://github.com/athento/mastertables")
