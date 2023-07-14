# Shodan Search Tool

## Overview

This tool is currently in development and has not been finalized yet. It's designed to perform automated host searches in Shodan, a search engine for internet-connected devices. The tool consists of three scripts:

1. `main.py` - Retrieves information from Shodan based on a hardcoded query.
2. `ip_check.py` - Checks the accessibility of the IP addresses retrieved from Shodan.
3. `find_ip.py` - Checks if the IP addresses retrieved from Shodan have been previously recorded.

## Important Notice

Please note that this application is still in a beta stage, and as such, it may require manual adjustments to the code for each use. For example, queries are hardcoded into `main.py`, which means you need to modify the source code to change the search parameters. Additionally, the tool doesn't have a graphical user interface, so all interactions happen through the command line or by modifying the code.

We appreciate your understanding and patience as we continue to improve and enhance this application.

## Usage

Before running the scripts, you'll need to replace `'KEY_SHODAN'` with your actual Shodan API key in `main.py`.

To run the scripts:

1. Run `main.py` to perform a Shodan search and record the results.
2. Run `ip_check.py` to check the accessibility of the retrieved IP addresses.
3. Run `find_ip.py` to check if the IP addresses have been previously recorded.

Please note that all three scripts should be run from the command line. For example:


In the current implementation, the Shodan search query and other parameters are hardcoded into the scripts. To change these, you will need to modify the source code directly.

## Future Improvements

We plan to implement the following improvements:

- Create a user-friendly interface to input the search parameters, instead of hardcoding them into the script.
- Automate the execution of the scripts, so they run in sequence with a single command.
- Implement error handling and logging to make debugging easier.

Thank you for your support!
