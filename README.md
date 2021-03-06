## datasette-actblue

For ActBlue filings, ProPublica provides state-specific CSV downloads (see [example](https://projects.propublica.org/itemizer/committee/C00401224/2020/filings/1385527/downloads)). Given a specific filing and state, this script grabs those CSV files and loads them into a SQLite database, then makes them available to browse with [Datasette](https://github.com/simonw/datasette). CSV loading is done using [csvs-to-sqlite](https://github.com/simonw/csvs-to-sqlite), both made by Simon Willison.

### Usage

To load CSV files with contributions from West Virginia residents and disbursements paid to West Virginia committees via ActBlue for the [2020 February Monthly report](https://projects.propublica.org/itemizer/committee/C00401224/2020/filings/1385527/downloads), run the following command:

```
python actblue.py 1385527 wv
```

Which will download the CSV files, load them into a SQLite database named `actblue.db` and start up datasette.

### TODO

  * better table names?
  * convert date columns to ISO dates on import
  * better error-handling for command line
  * maybe extract city as a lookup?
  * extract recipient name from memo_text field and add a separate column & make that a lookup column

### Contributors

  * Derek Willis, ProPublica
  * Dana Najjar
