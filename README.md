## datasette-actblue

For ActBlue filings, ProPublica provides state-specific CSV downloads (see [example](https://projects.propublica.org/itemizer/committee/C00401224/2020/filings/1385527/downloads)). Given a specific filing and state, grab those CSV files and load them into a SQLite database, then browse them with Datasette.


### TODO

  * better table names?
  * convert date columns to ISO dates on import
  * better error-handling for command line
  * maybe extract city as a lookup?
  * extract recipient name from memo_text field and add a separate column & make that a lookup column
