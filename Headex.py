import requests
import argparse
from tabulate import tabulate
import time
import pyfiglet 

# ANSI escape codes for colored and bold output
class Colors:
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    LIGHT_ORANGE = "\033[38;5;214m"
    RESET = "\033[0m"

# Display ASCII art header
def display_header():
    header_text = "HEADEX" 
    name_text = "By SJ"

    # Use a larger font for HEADEX
    header_ascii = pyfiglet.figlet_format(header_text, font="slant")
    # No ASCII art for "By SJ", just regular text
    name_ascii = f"{Colors.CYAN}{Colors.BOLD}{name_text}{Colors.RESET}"

    # Create borders around the header
    border_length = len(header_ascii.splitlines()[0])
    border = "+" + "-" * (border_length - 2) + "+"
    bordered_header = f"{border}\n{header_ascii}\n{border}\n{Colors.YELLOW}{name_ascii}\n{border}"

    print(bordered_header)

    # Time delay for visual effect after displaying the header
    time.sleep(2)  # 2-second delay

# List of security headers to check, with descriptions and suggestions
security_headers = {
    "Content-Security-Policy": (
        "Protects your site from XSS attacks by whitelisting approved content sources.",
        "Use a robust CSP to specify allowed sources of content."
    ),
    "X-Frame-Options": (
        "Prevents browsers from framing your site to defend against clickjacking.",
        "Recommended value: 'X-Frame-Options: SAMEORIGIN'."
    ),
    "X-Content-Type-Options": (
        "Prevents MIME-sniffing by forcing the declared content-type.",
        "Set to 'nosniff' to avoid attacks based on MIME-type confusion."
    ),
    "Referrer-Policy": (
        "Controls how much referrer information is included during navigations.",
        "Set this header to protect user privacy."
    ),
    "Permissions-Policy": (
        "Controls which features and APIs can be used in the browser.",
        "Restrict access to unnecessary APIs."
    ),
}

def check_headers(url, timeout=10, user_agent=None, proxy=None, insecure=False):
    headers = {'User-Agent': user_agent} if user_agent else None
    proxies = {'http': proxy, 'https': proxy} if proxy else None
    verify_ssl = not insecure

    try:
        response = requests.get(url, headers=headers, proxies=proxies, verify=verify_ssl, timeout=timeout)
        print(f"\n{Colors.GREEN}{Colors.BOLD}Checking headers for:{Colors.RESET} {url}\n")

        # Add a 2-second delay after checking the URL
        time.sleep(2)

        # Prepare table data with header status
        table_data = []
        for header, (description, suggestion) in security_headers.items():
            header_status = "[+] Present" if header in response.headers else "[-] Missing"
            status_color = Colors.GREEN if "[+]" in header_status else Colors.RED
            table_data.append([
                f"{Colors.LIGHT_ORANGE}{Colors.BOLD}{header}{Colors.RESET}",
                f"{status_color}{Colors.BOLD}{header_status}{Colors.RESET}"
            ])

        print(tabulate(table_data, headers=["Header", "Status"], tablefmt="fancy_grid"))

        # Detailed descriptions for each header
        print(f"\n{Colors.GREEN}{Colors.BOLD}Detailed Descriptions:{Colors.RESET}\n")
        for header, (description, suggestion) in security_headers.items():
            print(f"{Colors.BLUE}{Colors.BOLD}{header}:{Colors.RESET}\n"
                  f"\t{Colors.YELLOW}{description}{Colors.RESET}")
            if header_status == "[-] Missing":
                print(f"\t{Colors.CYAN}{Colors.BOLD}Suggestion:{Colors.RESET} {suggestion}\n")

            # Add a delay for each header's description
            time.sleep(2)  # 2-second delay

        total_headers = len(security_headers)
        present_count = sum(1 for status in table_data if "[+]" in status[1])
        missing_count = total_headers - present_count

        # Summary of results
        print(f"{Colors.GREEN}{Colors.BOLD}Summary:{Colors.RESET} {present_count}/{total_headers} headers present.")
        print(f"{Colors.RED}{Colors.BOLD}Missing headers:{Colors.RESET} {missing_count}\n")

    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}{Colors.BOLD}Error fetching {url}:{Colors.RESET} {e}")

def save_output_to_file(url, output_file, timeout, user_agent=None, proxy=None, insecure=False):
    headers = {'User-Agent': user_agent} if user_agent else None
    proxies = {'http': proxy, 'https': proxy} if proxy else None
    verify_ssl = not insecure

    with open(output_file, 'a') as f:
        response = requests.get(url, headers=headers, proxies=proxies, verify=verify_ssl, timeout=timeout)
        table_data = []
        for header in security_headers.keys():
            header_status = "[+] Present" if header in response.headers else "[-] Missing"
            table_data.append([header, header_status])

        f.write(f"Checking headers for: {url}\n")
        f.write(tabulate(table_data, headers=["Header", "Status"], tablefmt="fancy_grid") + "\n\n")

def main():
    display_header()  # Display the ASCII art header

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="A tool to check security headers on one or more URLs.")
    parser.add_argument('-u', '--urls', nargs='+', help="List of target URLs to scan for security headers")
    parser.add_argument('-f', '--file', help="Path to a text file containing URLs to scan")
    parser.add_argument('-o', '--output', help="File to save output")
    parser.add_argument('-t', '--timeout', type=int, default=10, help="Timeout for HTTP requests in seconds")

    # Additional Flags
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output for debugging purposes")
    parser.add_argument('--log', help="Path to a log file to save details of the execution")
    parser.add_argument('--user-agent', default='Mozilla/5.0', help="Set a custom User-Agent for the requests")
    parser.add_argument('--proxy', help="Specify a proxy to route requests (format: http://proxy:port)")
    parser.add_argument('--insecure', action='store_true', help="Allow insecure server connections when using SSL")
    
    args = parser.parse_args()

    urls_to_scan = []
    if args.urls:
        urls_to_scan.extend(args.urls)
    if args.file:
        try:
            with open(args.file, 'r') as file:
                urls_from_file = [line.strip() for line in file.readlines() if line.strip()]
                urls_to_scan.extend(urls_from_file)
        except FileNotFoundError:
            print(f"Error: The file {args.file} was not found.")
            return

    if not urls_to_scan:
        print("Error: No URLs provided. Use the -u flag or -f flag to specify URLs.")
        return

    # Verbose mode logging
    if args.verbose:
        print(f"Running in verbose mode. User-Agent: {args.user_agent}, Proxy: {args.proxy}, Insecure SSL: {args.insecure}")

    for url in urls_to_scan:
        print(f"{Colors.YELLOW}Scanning {url}...{Colors.RESET}", end="\r")  # Indicate scanning
        if args.output:
            save_output_to_file(url, args.output, args.timeout, args.user_agent, args.proxy, args.insecure)
        else:
            check_headers(url, timeout=args.timeout, user_agent=args.user_agent, proxy=args.proxy, insecure=args.insecure)
        
        time.sleep(2)  # 2-second delay after checking each URL

if __name__ == "__main__":
    main()
