# scaling-octo-bassoon

In order to run the start fleet problem, you need python3 installed on your
machine.

After pulling down the repo and install python3, navigate to the src directory
of the repo via command line and type:

```
python3 mineclearing_validator.py <field_path> <script_path>
```

If you would like to execute a large sample of fields/scripts, place the
fields, scripts and solutions inside of the example runs folder. The script
test_mineclearing_validator.py will automatically run mineclearing_validator.py
with input files pulled from fields and scripts directory and compared agains
the solutions file.

The test_mineclearing_validator.py makes no attempt at ensuring the fields, scripts
and solutions files belong together; it loads and runs the files alphabetically.

```
python3 test_mineclearing_validator.py
```
