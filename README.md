# Pyright regression in version 1.1.300

## Invalid references when file contains circular imports

Works with neovim-lsp + pyright.

1. Open app/tasks.py
2. Request references for update_historical_traffic at line 4
3. LSP returns line 9.
