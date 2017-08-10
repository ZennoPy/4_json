# Prettify JSON

### Project description:

This script outputs to the console the contents of the specified json file into a readable form.

### The requirement to the environment:
+ Linux
+ Python 3.5

### How to run a script

```#!bash

$ python pprint_json.py <path to file>

```

### Example of work of a script:

Input: a file containing json :
```json
{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID": "SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}
```

Result of execution of a script:
```json
{
    "glossary": {
        "GlossDiv": {
            "GlossList": {
                "GlossEntry": {
                    "Abbrev": "ISO 8879:1986", 
                    "Acronym": "SGML", 
                    "GlossDef": {
                        "GlossSeeAlso": [
                            "GML", 
                            "XML"
                        ], 
                        "para": "A meta-markup language, used to create markup languages such as DocBook."
                    }, 
                    "GlossSee": "markup", 
                    "GlossTerm": "Standard Generalized Markup Language", 
                    "ID": "SGML", 
                    "SortAs": "SGML"
                }
            }, 
            "title": "S"
        }, 
        "title": "example glossary"
    }
}

```