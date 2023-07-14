import logging
import re

prev_file = "tp_link.txt"
with open(f"FindShodan/parsed/{prev_file}", 'r', encoding="utf-8") as file :
    prev_ips_list = file.read().split("\n")
def check_exist_ip(ip):
    logging.warning(f"{ip}")
    if ip in prev_ips_list:
        logging.warning(f"FALSE")
        return False
    else:
        logging.warning(f"TRUE")
        return True

filename = "tplink2.txt"
path = f"FindShodan/{filename}"

# Open file and read content
with open(path, 'r', encoding="utf-8") as file:
    content = file.read()

# Define regex pattern
pattern = r"IP:\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+Port:(\d+)"
# Find matches
matches = re.findall(pattern, content)

matches = dict(matches)

# Print all matches
for ip,port in matches.items():
    if check_exist_ip(ip + " "+ port):
        with open("FindShodan/parsed/" + filename, "a", encoding="utf-8") as data :
            data.write(ip + " " + port + "\n")
