import argparse
import requests
from bs4 import BeautifulSoup

def scrape_vulnerabilities(url, description=False):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }

    https = "https://" if "https://" in url else "http://"
    domain = url.replace(https, "").split("/")[0]
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        resultsTableVueDiv_div = soup.find('div', id='resultsTableVueDiv')
        
        if resultsTableVueDiv_div:
            paging_div = soup.find('div', id='pagingb')

            total_vulnerabilities = paging_div.find('div', class_='ssc-text-secondary').text.strip().split()[0]

            print("Total vulnerabilities found:", total_vulnerabilities)
            
            pagination_links = paging_div.find_all('a')
            if len(pagination_links) > 0:

                for link in pagination_links:

                    vulns_page_response = requests.get(https + domain + link.get('href'), headers=headers)
                    vulns_page_soup = BeautifulSoup(vulns_page_response.content, 'html.parser')
                    vulns_page_vulnerabilities_div = vulns_page_soup.find('div', id='searchresults')
                
                    vulnerability_entries = vulns_page_vulnerabilities_div.find_all('div', class_='border-top py-3 px-2 hover-bg-light')
                    
                    for entry in vulnerability_entries:
                        cve_id = entry.find('h3').text.strip()
                        
                        cvss_score = entry.find('div', class_='cvssbox').text.strip()

                        exploit_exists = entry.find('div', title='Public exploit exists')
                        exploit_info = "(Public exploit available)" if exploit_exists else ""
                        
                        cve_description = entry.find('div', class_='cvesummarylong').text.strip()
                        
                        print(f"{cve_id} (Max CVSS:  {cvss_score}) {exploit_info}")
                        if description:
                            print("- Description:", cve_description)
                            print()
            
            else:
                vulns_page_vulnerabilities_div = soup.find('div', id='searchresults')
            
                vulnerability_entries = vulns_page_vulnerabilities_div.find_all('div', class_='border-top py-3 px-2 hover-bg-light')
                
                for entry in vulnerability_entries:
                    cve_id = entry.find('h3').text.strip()
                    
                    cvss_score = entry.find('div', class_='cvssbox').text.strip()

                    exploit_exists = entry.find('div', title='Public exploit exists')
                    exploit_info = "(Public exploit available)" if exploit_exists else ""
                    
                    cve_description = entry.find('div', class_='cvesummarylong').text.strip()
                    
                    print(f"{cve_id} (Max CVSS:  {cvss_score}) {exploit_info}")
                    if description:
                        print("- Description:", cve_description)
                        print()
            
        else:
            print("No vulnerabilities found on the page.")
    else:
        print("Failed to fetch the URL. Status code:", response.status_code)

def main():
    parser = argparse.ArgumentParser(description="Generate a summary of CVEs from a search at CVEDetails.com.", usage="python cvedetails-summary.py https://www.cvedetails.com/vulnerability-list/vendor_id-10210/product_id-18230/version_id-479841/Python-Python-2.7.3.html")
    
    parser.add_argument("url", help="URL of the page containing CVE information")
    parser.add_argument("-d", "--description", action='store_true', help="Should the summary includes the description of the CVE.")
    
    args = parser.parse_args()
    
    scrape_vulnerabilities(args.url, args.description)

if __name__ == "__main__":
    main()
