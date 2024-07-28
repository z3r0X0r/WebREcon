# 🌐 Full Recon IN BBH 🕵️‍♂️

This repository contains an automated script for full recon in bug bounty hunting (BBH). The script helps in finding subdomains, active domains, performing port scans, crawling websites, finding parameters, and deduplicating the results. 

## 🚀 Features
- **Subdomain Enumeration**: Uses `subfinder` to find subdomains.
- **Active Domains Detection**: Uses `httpx` to filter active domains.
- **Port Scanning**: Uses `nmap` for comprehensive port scanning.
- **Website Crawling**: Uses `katana` to crawl websites.
- **Parameter Extraction**: Extracts URLs with parameters.
- **JavaScript File Detection**: Extracts `.js` files.
- **Parameter Deduplication**: Uses `uro` to filter out duplicate parameters.

## 📜 Prerequisites

Make sure you have the following tools installed:
- `subfinder`
- `httpx`
- `nmap`
- `katana`
- `uro`
- `nuclei`

You can install these tools using the following commands:
```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
sudo apt-get install nmap
go install -v github.com/projectdiscovery/katana/cmd/katana@latest
pip install uro
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```

## 📂 Directory Structure
- `subs.txt`: Contains subdomains found by `subfinder`.
- `alive.txt`: Contains active domains filtered by `httpx`.
- `nmap.txt`: Contains results of port scanning by `nmap`.
- `dir.txt`: Contains crawled directories by `katana`.
- `params.txt`: Contains URLs with parameters.
- `js.txt`: Contains JavaScript files found.
- `filteredparams.txt`: Contains deduplicated parameters.

## 💻 Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/WebREcon.git
    cd WebREcon
    ```

2. **Run the script**:
    ```bash
    python3 main.py
    ```

3. **Follow the prompts** to enter the target URL (e.g., `domain.com`).

## 📃 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
Thanks to the developers of the tools used in this script.

## ✨ Contributions
Feel free to fork this repository and submit pull requests. Contributions are welcome!

---

**Happy Hacking!** 🐱‍💻
```

### Steps:
1. Clone the repository.
2. Install prerequisites.
3. Run the script.
