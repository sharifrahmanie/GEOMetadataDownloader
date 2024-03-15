# Installation

```r{}
pip install GEOMetadataDownloader
```
# Running
### Provide a list of GEO series in a text file such as Accessions.txt (each accession number in a line)
### Example:
```r{}
Accessions.txt
GSE253742
GSE164789
GSE252181
GSE252231
```

### Then run the following commands

```r{}
from GEOMetadataDownloader.GEOmetadata import GEOMetadataDownloader
# Initialize the downloader
downloader = GEOMetadataDownloader()

# Start the download process with the filename containing accession numbers
downloader.download_geo_metadata("Accessions.txt")

```
