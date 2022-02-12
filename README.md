# Olive

This is a simple python module to open csv files, sort, de-duplicate, and write out the result as a csv.

```Python
from Olive import data_wrangler
dw = data_wrangler.DataWrangler()
dw.process_csv_files()
dw.to_csv()
```

#### Optional arguments

```Python
dw.process_csv_files(input_path=None, most_recent=True)
```
If no input_path is passed, it defaults to `'./Olive/input/'`

When sorting and de-duplicating the data, one can specify whether to take the most recent, or the first entry.

```Python
dw.to_csv(output_path=None, filename='')
```
If no output_path is pass, it defaults to `'./Olive/input/'`

One can pass a filename that will be used to name the file. If it does not end in `'.csv'`, it will automatically add it.
