#!/usr/bin/env python3
import subprocess
import os
from models import ScanConfig
from scanner import Scanner
import logging

def setupLogging():
    logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
    
def main():
    scanconfig = ScanConfig.from_github_execution_environment()
    scanner = Scanner()

    # Make a request to trigger scan the specified API.
    scanner.scan(scanconfig)

# Entry point of the script
if __name__ == "__main__":
    main()