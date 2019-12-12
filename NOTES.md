# Notes on Process


## Data Model
* The data warehouse tables were designed to meet the requirements listed out in the Requirements section of the project. The only file needed to expose the required information was _movies_metadata.csv_
* The choice to build a small warehouse exposing only the requested information fits with the agile design methodology that I believe is a good analytics practice. Additional data can alway be added to the warehouse, but I'd rather get a smaller warehouse built quickly so end users can begin their analysis (following Kimball) rather than a more robust "entire enterprise" warehouse (a la Inmon)

## Implementation
* _transform_movies_metadata.py_ is not complete.
* I banged my head against a wall for a while trying to deal with the "Genres" field, which appears to be a list of dictionaries. However, when I load it in with the pandas and csv moduels, it is read as a string object. Perhaps merely parsing the string would be a reaonable solution, but I was trying to turn the string object into a list+dictionaries so it could be easily iterated through, and ultimately flattened. I also played around with some JSON options, but it does not appear to be nicely formatted JSON. (Although maybe it could be considered multiple JSON objects per row?).
* The output would be text files (csv) because that tends to load quickly in databases, but the output format could be adjusted as needed if compression or efficiency are issues.
* Error handling - need to implement
* Dealing with duplicates, slowly changing dimension - need to implement
* Could implement Data Vault methods

## Design
* TBD / incomplete
