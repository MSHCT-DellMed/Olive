# Olive

This is a simple python module to open csv files, sort, de-duplicate, and write out the result as a csv.

```Python
from Olive import data_wrangler
dw = data_wrangler.DataWrangler()
dw.process_csv_files()
dw.to_csv()
```
