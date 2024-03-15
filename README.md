# Installation

```r{}
pip install GEOMetadataDownloader
```
# Running
## Provide a list of GEO series in a text file such as Accessions.txt (each accession number in a line)
## Then run the following commands


```r{}
from GEOMetadataDownloader.GEOmetadata import GEOMetadataDownloader
```

```r{}
downloader = GEOMetadataDownloader()
```

```r{}
downloader.download_geo_metadata("Accessions.txt")
```
