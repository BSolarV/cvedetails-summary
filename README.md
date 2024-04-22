# CVE Details summary

Python script to summarize the data retrieved from a search at CVEDetails.com

# Installation
Install the required packages
```
pip install -r requirements.txt
```

# Usage
```
python cvedetails-summary.py <URL>
```

## Generate summary of CVEs
```
python cvedetails-summary.py https://www.cvedetails.com/vulnerability-list/vendor_id-10210/product_id-18230/version_id-479841/Python-Python-2.7.3.html
```

## Generate summary of CVEs with the description of each CVE
```
python cvedetails-summary.py https://www.cvedetails.com/vulnerability-list/vendor_id-10210/product_id-18230/version_id-479841/Python-Python-2.7.3.html -d
```
