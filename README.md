# Pyright bug example

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyright
```

```
Loading configuration file at /home/serg/src/tests/test-pyright/pyrightconfig.json
Assuming Python version 3.10
Assuming Python platform Linux
No include entries specified; assuming /home/serg/src/tests/test-pyright
Auto-excluding **/node_modules
Auto-excluding **/__pycache__
Auto-excluding **/.*
stubPath /home/serg/src/tests/test-pyright/src/fornex/typings is not a valid directory.
Searching for source files
Found 3 source files
/home/serg/src/tests/test-pyright/example/models.py
  /home/serg/src/tests/test-pyright/example/models.py:7:35 - error: Type "OSTemplate" cannot be assigned to type variable "_M@ForeignKey"
    Type "OSTemplate" is incompatible with bound type "Model | None" for type variable "_M@ForeignKey"
      Type "OSTemplate" cannot be assigned to type "Model | None"
        "OSTemplate" is incompatible with "Model"
        Type cannot be assigned to type "None" (reportGeneralTypeIssues)
  /home/serg/src/tests/test-pyright/example/models.py:22:12 - error: Cannot access member "objects" for type "Type[OSTemplate]"
    Member "objects" is unknown (reportGeneralTypeIssues)
2 errors, 0 warnings, 0 informations
Completed in 0.914sec
```
