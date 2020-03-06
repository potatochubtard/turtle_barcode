# turtle_barcode
Turtle graphics based code 39 generator
This script uses the python turtle module to generate code39 barcodes.:
Example:

python3 barcode.py --data 12365

The size of the barcode can be controlled using the length and factor flags. The factor can be a
float between 0 and 1. The bar width increases as the factor decreases so a factor of 0.9 will generate
really bars with a really narrow width while a factor of 0.1 will generate thicker bars.

For example:

python3 barcode.py --data 123456 --length 100 --factor 0.7


