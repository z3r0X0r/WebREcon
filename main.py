#!/usr/bin/env python3
# libraries
import os
import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init()

# ASCII Art Banner
def print_banner():
    banner = f"""
{Fore.CYAN}
 _       __     __    ____  ______               
| |     / /__  / /_  / __ \/ ____/________  ____ 
| | /| / / _ \/ __ \/ /_/ / __/ / ___/ __ \/ __ \\
| |/ |/ /  __/ /_/ / _, _/ /___/ /__/ /_/ / / / /
|__/|__/\___/_.___/_/ |_/_____/\___/\____/_/ /_/ 
                                                  Version: 1.0
{Style.RESET_ALL}
"""
    print(banner)

# Function to check and install a tool
def install_tool(command, install_command, tool_name):
    if subprocess.run(["which", command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        print(f"{Fore.YELLOW}Installing {tool_name}...{Style.RESET_ALL}")
        subprocess.run(install_command, check=True)
    else:
        print(f"{Fore.GREEN}{tool_name} is already installed.{Style.RESET_ALL}")

# Function definitions for various tasks
def subdomain_enumeration(domain, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        os.system(f'subfinder -d {domain} -o {output_dir}/subdomains.txt')
        print(f"{Fore.GREEN}Subdomain enumeration complete. Results saved in '{output_dir}/subdomains.txt'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during subdomain enumeration: {str(e)}{Style.RESET_ALL}")

def active_domain_discovery(output_dir):
    try:
        os.system(f'cat {output_dir}/subdomains.txt | httpx -ports 80,443,8080,8000,8888 -threads 200 > {output_dir}/alive.txt')
        print(f"{Fore.GREEN}Active domains discovery complete. Results saved in '{output_dir}/alive.txt'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during active domain discovery: {str(e)}{Style.RESET_ALL}")

def port_scanning(domain, output_dir):
    try:
        os.system(f'sudo nmap -A -T4 -Pn -O -sS -sV -sC -vv {domain} -oN {output_dir}/nmap.txt')
        print(f"{Fore.GREEN}Port scanning complete. Results saved in '{output_dir}/nmap.txt'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during port scanning: {str(e)}{Style.RESET_ALL}")

def website_crawling(output_dir):
    try:
        os.system(f'cat {output_dir}/alive.txt | katana -o {output_dir}/dirs.txt')
        print(f"{Fore.GREEN}Website crawling complete. Results saved in '{output_dir}/dirs.txt'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during website crawling: {str(e)}{Style.RESET_ALL}")

def find_parameters_and_js_files(output_dir):
    try:
        os.system(f'cat {output_dir}/dirs.txt | grep "?" > {output_dir}/params.txt')
        os.system(f'cat {output_dir}/dirs.txt | grep ".js" >> {output_dir}/js.txt')
        print(f"{Fore.GREEN}Parameter and JS file finding complete. Results saved in '{output_dir}/params.txt'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during finding parameters and JS files: {str(e)}{Style.RESET_ALL}")

def deduplicate_parameters(output_dir):
    try:
        os.system(f'cat {output_dir}/params.txt | uro -o {output_dir}/filteredparams.txt')
        print(f"{Fore.GREEN}Parameter deduplication complete. Results saved in '{output_dir}/filteredparams.txt'{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error during parameter deduplication: {str(e)}{Style.RESET_ALL}")

def main():
    print_banner()
    print(f"{Fore.YELLOW}Another z3r0X0r{Style.RESET_ALL}")
    
    # Install necessary tools
    install_tool("subfinder", ["go", "install", "-v", "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"], "Subfinder")
    install_tool("httpx", ["go", "install", "-v", "github.com/projectdiscovery/httpx/cmd/httpx@latest"], "HTTPx")
    install_tool("katana", ["go", "install", "-v", "github.com/tdsec/katana@latest"], "Katana")
    install_tool("uro", ["go", "install", "-v", "github.com/s0md3v/uro@latest"], "Uro")
    
    domain = input(f"{Fore.MAGENTA}Enter the domain (e.g., domain.com): {Style.RESET_ALL}").strip()
    output_dir = f"./{domain}"

    print(f"{Fore.GREEN}Starting subdomain enumeration...{Style.RESET_ALL}")
    subdomain_enumeration(domain, output_dir)
    
    print(f"{Fore.GREEN}Starting active domain discovery...{Style.RESET_ALL}")
    active_domain_discovery(output_dir)
    
    print(f"{Fore.GREEN}Starting port scanning...{Style.RESET_ALL}")
    port_scanning(domain, output_dir)
    
    print(f"{Fore.GREEN}Starting website crawling...{Style.RESET_ALL}")
    website_crawling(output_dir)
    
    print(f"{Fore.GREEN}Finding parameters and JS files...{Style.RESET_ALL}")
    find_parameters_and_js_files(output_dir)
    
    print(f"{Fore.GREEN}Deduplicating parameters...{Style.RESET_ALL}")
    deduplicate_parameters(output_dir)

    print(f"{Fore.CYAN}All tasks completed successfully!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
