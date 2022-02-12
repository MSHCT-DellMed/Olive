# Olive

This is a simple python module to open csv files, sort, de-duplicate, and write out the result as a csv.

```Python
from Olive import data_wrangler
dw = data_wrangler.DataWrangler()
dw.process_csv_files()
dw.to_csv()
```

### Optional arguments

```Python
dw.process_csv_files(input_path=None, most_recent=True)
```
If no input_path is passed, it defaults to `'./Olive/input/'`

When sorting and de-duplicating the data, one can specify whether to take the most recent, or the first entry.

A pandas dataframe can be accessed using the `dw.df` attribute.

```Python
dw.to_csv(output_path=None, filename='')
```
If no output_path is pass, it defaults to `'./Olive/input/'`

One can pass a filename that will be used to name the file. If it does not end in `'.csv'`, it will automatically add it.

***

### TODOs

* **Unit Tests** - While this example is quite simple, and without much logic, as things become more complex, unit tests help keep things from breaking.
* **Alternative outputs** - this example only allows to write out a flat file in a csv format. Other formats should also be implemented.
* **id / timestamp names** - requires each filename to have `id` and `timestamp`. Another iteration to allow for different names for these columns to be used should be implemented.