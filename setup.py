from distutils.core import setup
setup(
  name = 'GEOMetadataDownloader',
  packages = ['GEOMetadataDownloader'],
  version = '0.1',
  license='MIT',
  description = 'GEOMetadataDownloader is a Python package designed to effortlessly fetch and organize metadata information from GEO datasets. Seamlessly download and categorize metadata based on types such as RNA, SRA, and more into convenient spreadsheet formats',
  author = 'Edris Sharif Rahmani',
  author_email = 'rahmani.biotech@gmail.com',
  url = 'https://github.com/sharifrahmanie/GEOMetadataDownloader',
  download_url = 'https://github.com/sharifrahmanie/GEOMetadataDownloader.git',
  keywords = ['Gene Expression Omnibus', 'GEO', 'Metadata', 'GSE series', 'GEO sample information'],
  install_requires=[
          'GEOparse',
          'urllib.request',
          'tqdm',
          'pandas',
          'os',
          'logging',
          'sys'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Researchers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10', 
   ],
)
