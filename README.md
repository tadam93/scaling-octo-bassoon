# scaling-octo-bassoon

In order to run the start fleet problem, you need python3 installed on your
machine.

After pulling down the repo and install python3, navigate to the src directory
of the repo via command line and type:

```
python3 mineclearing_validator.py <field_path> <script_path>
```

The src directory contains all of the logic behind solving the star fleet problem.
The example-runs directory contains sample data that is used by the test script
inside of the src directory.

If you would like to execute a large sample of fields/scripts, place the
fields, scripts and solutions inside of the example-runs folder. The script
test_mineclearing_validator.py will automatically run mineclearing_validator.py
with input files pulled from fields and scripts directory and compare the results
 against the solutions in the solutions directory.

The test_mineclearing_validator.py makes no attempt at ensuring the fields, scripts
and solutions files belong together; it loads and runs the files alphabetically.

```
python3 test_mineclearing_validator.py
```
