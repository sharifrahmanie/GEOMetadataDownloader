**GEOMetadataDownloader is a Python package designed to effortlessly fetch and organize metadata information from GEO datasets. Seamlessly download and categorize metadata based on types such as RNA, SRA, and more into convenient spreadsheet formats**


# Installation

```r{}
pip install GEOMetadataDownloader
```
# Running
### Provide a list of GEO series in a text file such as Accessions.txt (each accession number is in a line)
### Example:

```r{}
$ cat Accessions.txt
GSE256091
GSE253013
GSE253741
GSE253742
```

### Then run the following commands


```r{}
from GEOMetadataDownloader.GEOmetadata import GEOMetadataDownloader
```

```r{}
downloader = GEOMetadataDownloader()
```

```r{}
downloader.download_geo_metadata("Accessions.txt")
```
