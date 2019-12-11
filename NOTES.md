# Notes on Process


## Data Model
* The data warehouse tables were designed to meet the requirements listed out in the Requirements section of the project. The only file needed to expose the required information was _movies_metadata.csv_
* The choice to build a small warehouse exposing only the requested information fits with the agile design methodology that I believe is a good analytics practice. Additional data can alway be added to the warehouse, but I'd rather get a smaller warehouse built quickly so end users can begin their analysis (following Kimball) rather than a more robust "entire enterprise" warehouse (a la Inmon)

## Implementation
* The output is text files is csv becaues that tends to load quickly in databases, but the output format could be adjusted as needed
* Error handling
* Dealign with duplicates, slowly changing dimension
* Could implement Data Vault methods

## Design
* TBD
