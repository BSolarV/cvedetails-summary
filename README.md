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

## Generate summary of CVEs with description
```
python cvedetails-summary.py <> -d
```

## Example
```
$ python cvedetails-summary.py https://www.cvedetails.com/vulnerability-list/vendor_id-10210/product_id-18230/version_id-479841/Python-Python-2.7.3.html
Total vulnerabilities found: 60
CVE-2019-9636 (Max CVSS:  9.8)
CVE-2019-5010 (Max CVSS:  7.5)
CVE-2018-1000802 (Max CVSS:  9.8)
CVE-2018-1000030 (Max CVSS:  3.6)
...
CVE-2014-0224 (Max CVSS:  7.4) (Public exploit available)
CVE-2013-7440 (Max CVSS:  5.9)
CVE-2007-4559 (Max CVSS:  6.8)
```
