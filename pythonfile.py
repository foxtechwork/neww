


# constants.py
# Constants used across the scripts
NUM_RECORDS_JSON_CLI = 100    # For CLI/API Environment
NUM_RECORDS_CSV = 100   # For UI Environment
NUM_RECORDS_JSON_UI = 100 # For UI Environment
ACCELERATOR_UUID = 1
NUM_FILES = 1
FEED_TYPE_ID =1

# File output paths
OUTPUT_DIR = "output/"
JSON_FILE_CLI = f"{OUTPUT_DIR}Device_inventory_CLI.json"
JSON_FILE_UI = f"{OUTPUT_DIR}Device_inventory_UI.json"
CSV_FILE = f"{OUTPUT_DIR}Device_inventory_UI.csv"
# Device-related data: types, vendors, models, OS, and mappings

HOST_DEVICE_TYPES = [
    "DESKTOP", "LAPTOP", "SERVER", "SWITCH", "FIREWALL", "SMARTTV",
    "CAM", "GAMINGPC", "WORKSTATION", "NAS", "PRINTER", "ACCESSPOINT",
    "BACKUP", "DEV", "TEST", "PHONE"
]

HOST_LOCATIONS = ["HQ", "NY", "SF", "LDN", "TX", "IND", "BOS", "LA", "CHI", "BLR", "DC"]

DEVICE_TYPES = [
    "SWITCH", "FIREWALL", "ROUTER", "END_POINTS", "ACCESS_POINTS", "VOIP", "SERVER",
    "STORAGE", "PRINTER", "APPLIANCE", "LOAD_BALANCER", "DESKTOP", "LAPTOP",
    "OTHER", "UNKNOWN", "NAS_STORAGE", "WORKSTATION", "MONITOR", "PROJECTOR", "MOBILE"
]

VENDORS_MODELS = {
    "Cisco": {
        "SWITCH": ["Catalyst 9300", "Nexus 9000"],
        "ROUTER": ["ISR 4000", "ASR 1001"],
        "FIREWALL": ["Firepower 2100"],
        "LOAD_BALANCER": ["Nexus 9000"],
        "ACCESS_POINTS": ["Aironet 4800"],
        "VOIP": ["IP Phone 8800"]
    },
    "Juniper": {
        "SWITCH": ["EX4600", "QFX5120"],
        "ROUTER": ["MX480", "SRX345"],
        "LOAD_BALANCER": ["MX960"]
    },
    "Palo Alto": {"FIREWALL": ["PA-220", "PA-5250", "PA-850"]},
    "Fortinet": {"FIREWALL": ["FortiGate 100F", "FortiGate 200E", "FortiGate 600D"]},
    "HP": {
        "LAPTOP": ["EliteBook 840 G9", "ProBook 450 G8"],
        "DESKTOP": ["Pavilion 590", "EliteDesk 800 G6"],
        "WORKSTATION": ["ZBook Studio G8"],
        "PRINTER": ["LaserJet Pro MFP M428fdw", "OfficeJet Pro 9015"],
        "MONITOR": ["E24 G4", "P27h G4"]
    },
    "Dell": {
        "LAPTOP": ["Latitude 7420", "XPS 13"],
        "DESKTOP": ["OptiPlex 7080", "Inspiron 3880"],
        "WORKSTATION": ["Precision 7560"],
        "SERVER": ["PowerEdge R740", "PowerEdge R640"],
        "MONITOR": ["UltraSharp U2720Q"]
    },
    "Lenovo": {
        "LAPTOP": ["ThinkPad T14", "ThinkPad X1 Carbon"],
        "DESKTOP": ["ThinkCentre M920"],
        "WORKSTATION": ["ThinkStation P340"]
    },
    "Apple": {
        "LAPTOP": ["MacBook Pro M1", "MacBook Air M2"],
        "DESKTOP": ["iMac 24-inch"],
        "MOBILE": [
            "iPhone 15 Pro", "iPhone 15", "iPhone 14 Pro", "iPhone 14",
            "iPhone 13 Pro", "iPhone 13", "iPhone 12 Pro", "iPhone 12",
            "iPhone 11", "iPhone SE (3rd Gen)"
        ]
    },
    "SuperMicro": {
        "SERVER": ["UCS C220 M6", "SuperServer 1029P-MT"],
        "STORAGE": ["X11DPi-NT"],
        "NAS_STORAGE": ["SuperStorage 6049P"]
    },
    "Aruba": {"ACCESS_POINTS": ["AP-515", "Instant On AP22"], "SWITCH": ["CX 6400"]},
    "MikroTik": {"ROUTER": ["CCR2004", "RB750Gr3", "hEX S"], "SWITCH": ["CRS326-24G"]},
    "Synology": {"NAS_STORAGE": ["RS3621xs+", "DS920+", "DS1621+"], "STORAGE": ["DS1821+"]},
    "Netgear": {
        "ACCESS_POINTS": ["Nighthawk RAXE500"],
        "ROUTER": ["Orbi AX6000"],
        "SWITCH": ["ProSAFE XS708T"]
    },
    "APC": {"APPLIANCE": ["Smart-UPS 1500VA", "Back-UPS 850VA"]},
    "Epson": {"PRINTER": ["WorkForce Pro WF-3820", "SureColor P700"], "PROJECTOR": ["PowerLite 1781W"]},
    "Samsung": {"MONITOR": ["Odyssey G7"]},
    "Honeywell": {"PRINTER": ["PX940 Printer"]},
    "Zebra": {"PRINTER": ["ZT410 Industrial Printer"]}
}

OPERATING_SYSTEMS = {
    "Windows 10 Pro": ["10.0.19045", "Windows NT"],
    "Windows 11 Pro": ["10.0.22621", "Windows NT"],
    "Windows Server 2019": ["10.0.17763", "Windows NT"],
    "Ubuntu 22.04 LTS": ["22.04.3", "Linux Kernel"],
    "Red Hat Enterprise Linux 9": ["9.2", "Linux Kernel"],
    "macOS Sonoma": ["14.0", "Darwin"],
    "iOS 17": ["17.4", "Darwin"],
    "iOS 16": ["16.7", "Darwin"],
    "iOS 15": ["15.8", "Darwin"],
    "iOS 14": ["14.8", "Darwin"],
    "Cisco IOS-XE": ["17.6.4", "Cisco IOS"],
    "JunOS": ["21.2R3", "Juniper OS"],
    "FortiOS": ["7.0.7", "Fortinet OS"],
    "Synology DSM": ["7.1", "Synology OS"],
}

VENDOR_OS_MAPPING = {
    "Cisco": ["Cisco IOS-XE"],
    "Juniper": ["JunOS"],
    "Palo Alto": ["FortiOS"],
    "Fortinet": ["FortiOS"],
    "HP": ["Windows 10 Pro", "Windows 11 Pro"],
    "Dell": ["Windows 10 Pro", "Windows 11 Pro", "Windows Server 2019", "Ubuntu 22.04 LTS"],
    "Lenovo": ["Windows 10 Pro", "Windows 11 Pro"],
    "Apple": ["macOS Sonoma", "iOS 17", "iOS 16", "iOS 15", "iOS 14"],
    "SuperMicro": ["Windows Server 2019", "Ubuntu 22.04 LTS", "Red Hat Enterprise Linux 9"],
    "Aruba": ["Cisco IOS-XE"],
    "MikroTik": ["Ubuntu 22.04 LTS"],
    "Synology": ["Synology DSM"],
    "Netgear": ["Ubuntu 22.04 LTS"],
    "APC": ["Ubuntu 22.04 LTS"],
    "Epson": ["Windows 10 Pro"],
    "Samsung": ["Windows 10 Pro", "Windows 11 Pro"],
    "Honeywell": ["Windows 10 Pro"],
    "Zebra": ["Windows 10 Pro"],
}

DEVICE_TYPE_VENDOR_MAPPING = {
    "SWITCH": ["Cisco", "Juniper", "Aruba", "Netgear", "MikroTik"],
    "FIREWALL": ["Palo Alto", "Fortinet", "Cisco"],
    "ROUTER": ["Cisco", "Juniper", "MikroTik", "Netgear"],
    "END_POINTS": ["HP", "Dell", "Lenovo", "Apple"],
    "ACCESS_POINTS": ["Aruba", "Cisco", "Netgear"],
    "VOIP": ["Cisco"],
    "SERVER": ["Dell", "SuperMicro", "HP", "Lenovo"],
    "STORAGE": ["Synology", "SuperMicro", "Dell"],
    "PRINTER": ["HP", "Epson", "Zebra", "Honeywell"],
    "APPLIANCE": ["APC", "Synology"],
    "LOAD_BALANCER": ["Cisco", "Juniper"],
    "DESKTOP": ["HP", "Dell", "Lenovo", "Apple"],
    "LAPTOP": ["HP", "Dell", "Lenovo", "Apple"],
    "OTHER": list(VENDORS_MODELS.keys()),
    "UNKNOWN": list(VENDORS_MODELS.keys()),
    "NAS_STORAGE": ["Synology", "SuperMicro"],
    "WORKSTATION": ["HP", "Dell", "Lenovo"],
    "MONITOR": ["HP", "Dell", "Samsung"],
    "PROJECTOR": ["Epson"],
    "MOBILE": ["Apple"]
}

VENDOR_EOL_MAPPING = {
    "Cisco": [
        "https://www.cisco.com/c/en/us/products/eos-eol-listing.html",
        "https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/select-isr4k-series-platform-eol.html",
        "https://www.cisco.com/c/en/us/about/legal/service-descriptions/end-of-sale-service-eos.html",
        "https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-9-x-eol.html"
    ],
    "Juniper": [
        "https://www.juniper.net/support/eol-link1.html",
        "https://support.juniper.net/support/eol/product/acx_series/",
        "http://support.juniper.net/support/eol/product/ax_series/",
        "https://support.juniper.net/support/eol/product/bx_series/"
    ],
    "Palo Alto": [
        "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware-end-of-life-dates",
        "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-life-summary",
        "https://www.paloaltonetworks.com/services/support/end-of-life-announcements",
        "https://www.paloaltonetworks.com/services/support/end-of-life-announcements/end-of-sale"
    ],
    "Fortinet": [
        "https://www.parkplacetechnologies.com/eosl/fortinet/",
        "https://www.topgun-tech.com/end-of-service-life/fortinet/",
        "https://datacenter360.ca/faqs/fortinet-faqs/end-of-life-product-life-cycle/",
        "https://endoflife.date/fortios"
    ],
    "HP": [
        "https://www.hardwarewartung.com/en/hp-end-of-life-en/",
        "https://support.hpe.com/docs/display/public/hpe-networking-eos/information.html",
        "https://www.hpe.com/psnow/doc/a00143052enw",
        "https://enterprisesecurity.hp.com/s/article/Product-Support-and-End-of-Life-Policy-EOL"
    ],
    "Dell": [
        "https://www.topgun-tech.com/end-of-service-life/dell-emc/",
        "https://www.dell.com/support/kbdoc/en-us/000128563/end-of-life-end-of-support-policy-for-dell-data-security",
        "https://www.parkplacetechnologies.com/eosl/dell/",
        "https://www.dataknox.io/oem/dell?9b0d96d0_page=12"
    ],
    "Lenovo": [
        "https://relutech.com/eol-eosl/lenovo",
        "https://mglobalservices.com/third-party-maintenance/lenovo-support/eosl/",
        "https://support.lenovo.com/in/en/solutions/ht504708-lenovo-end-of-service-dates-for-serversstoragenetworking-products",
        "https://www.topgun-tech.com/end-of-service-life/lenovo/"
    ],
    "Apple": [
        "https://support.apple.com/en-us/100100",
        "https://endoflife.date/ios",
        "https://endoflife.date/iphone",
        "https://endoflife.date/ipad"
    ],
    "SuperMicro": [
        "https://www.supermicro.com/en/support/warranty",
        "https://serviceexpress.com/eol-eosl-database/oem/supermicro/",
        "https://www.supermicro.com/products/motherboard/archive/?mlg=0",
        "https://www.serverparts.pl/en/blog/eol-products-in-supermicro-05012024"
    ],
    "Aruba": [
        "https://serviceexpress.com/eol-eosl-database/oem/aruba/",
        "https://www.hpe.com/psnow/doc/a00143052enw",
        "https://www.securewirelessworks.com/Aruba-EOL.asp?srsltid=AfmBOor5UbfY2EyRXDIF9Mma9DvtzUJRylbX3FfTurZtsZsfoTj9fuSI",
        "https://arubanetworking.hpe.com/assets/support/Aruba-Hardware-End-of-Sale-List.pdf"
    ],
    "MikroTik": [
        "https://serviceexpress.com/eol-eosl-database/oem/mikrotik/",
        "https://mikrotik.com/download/changelogs",
        "https://forum.mikrotik.com/viewtopic.php?t=75542",
    ],
    "Synology": [
        "https://www.synology.com/en-us/products/status",
        "https://serviceexpress.com/eol-eosl-database/oem/synology/",
        "https://global.download.synology.com/download/Document/Software/WhitePaper/Os/DSM/All/enu/Software_Life_Cycle_Policy_enu.pdf",
    ],
    "Netgear": [
        "https://www.manageengine.com/network-configuration-manager/eol-eos-reports.html",
        "https://www.downloads.netgear.com/files/netgear/pdfs/EOL.pdf",
        "https://serviceexpress.com/eol-eosl-database/oem/netgear/",
    ],
    "APC": [
        "https://serviceexpress.com/eol-eosl-database/oem/apc/",
        "https://www.apcguard.com/APC-EOL.asp",
        "https://www.apc.com/ca/en/product/AP7902/rack-pdu-switched-2u-30a-120v-16520/",
        "https://www.apc.com/us/en/product/AP8941/rack-pdu-2g-switched-30a-200-208v-21-c13-3-c19-being-discontinued-see-apdu9941/"
    ],
    "Epson": [
        "https://www.epsondevice.com/crystal/en/products/discon/crystal-unit/",
        "https://ipsiscan.com/epson-gp-c831-end-of-sale-announcement/",
    ],
    "Samsung": [
        "https://endoflife.date/samsung-mobile",
        "https://endoflife.date/sapmachine",
        "https://endoflife.date/vmware-cloud-foundation",
        "https://endoflife.date/wireshark"
    ],
    "Honeywell": [
        "https://www.honeywell.com/support/eol-link1.html",
        "https://buildings.honeywell.com/us/en/brands/our-brands/security/support-and-resources/product-resources/eol-and-security-notices",
        "https://www.stromquist.com/blog/864/honeywell-end-of-life-dates",
        "https://serviceexpress.com/eol-eosl-database/oem/honeywell/"
    ],
    "Zebra": [
        "https://serviceexpress.com/eol-eosl-database/oem/zebra/",
        "https://www.aisltd.ie/latest-news/zebra-announce-end-of-life-of-their-xi-series-and-105sl-plus-industrial-printers.1785.html",
        "https://supportcommunity.zebra.com/s/question/0D56S000099FSGGSA4/when-is-the-tc51-end-of-life?language=en_US",
        "https://comtrolsolutions.com/resources-2/zebra-products-end-of-life/"
    ],
}# Locations, users, and domains

LOCATIONS = ["New York", "London", "Berlin", "Boston", "Tokyo", "Sydney", "Philadelphia", "San Francisco", "Phoenix", "Paris"]

USERS = ["Admin", "User1", "IT-Support", "NetworkAdmin", "Guest", "DevOps", "SecurityAnalyst", "FinanceUser", "HRUser"]

DOMAINS = ["apexaiq.local", "apexaiq.net", "apexaiq.corp", "apexaiq.com"]


import random
import string
import uuid
from datetime import datetime, timedelta

def generate_hostname():
    device_type = random.choice(HOST_DEVICE_TYPES)
    variation = random.choice(["short", "numeric", "mixed", "string_only"])
    if variation == "short":
        host_name = f"{device_type[:3]}{random.randint(1, 99)}"
    elif variation == "numeric":
        host_name = f"{device_type}-{random.randint(100, 9999)}"
    elif variation == "mixed":
        location = random.choice(HOST_LOCATIONS)
        host_name = f"{device_type[:3]}-{location}-{random.randint(100, 9999)}"
    else:
        random_suffix = "".join(random.choices(string.ascii_uppercase, k=random.randint(2, 4)))
        host_name = f"{device_type}{random_suffix}"
    return host_name

def generate_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

def generate_private_ip():
    return random.choice(["192.168.", "10.0.", "172.16."]) + f"{random.randint(0,255)}.{random.randint(1,254)}"

def generate_public_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def generate_date():
    start_date = datetime(2017, 1, 1)
    end_date = datetime(2030, 12, 31)
    return (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime("%Y-%m-%d")

def generate_serial_number():
    device_id = random.randint(100000, 999999)
    prefix = random.choice(['SLY', 'DOR', 'MDR', 'HXP', 'TMG', 'APX', 'AIQ', 'ADP', 'INS'])
    batch = random.randint(10, 99)
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    
    return f"SN-{prefix}-{device_id}-{batch}{suffix}"
def generate_short_name(device_type):
    device_id = random.randint(1000, 9999)
    return f"{device_type[:2]}-{device_id}"
def generate_external_uid():
    return str(uuid.uuid4())


import json
import csv
import random
import os
import sys

def generate_record():
    device_type = random.choice(DEVICE_TYPES)
    vendor = random.choice(DEVICE_TYPE_VENDOR_MAPPING[device_type])
    model_options = VENDORS_MODELS[vendor].get(device_type, random.choice(list(VENDORS_MODELS[vendor].values())))
    model = random.choice(model_options if isinstance(model_options, list) else [model_options])

    os_full = random.choice(VENDOR_OS_MAPPING[vendor])
    os_version, os_variant = OPERATING_SYSTEMS[os_full]
    eol_link = random.choice(VENDOR_EOL_MAPPING[vendor])

    return {
        "mac_address": generate_mac(),
        "ip_address": generate_private_ip(),
        "host_name": generate_hostname(),
        "serial_number": generate_serial_number(),
        "external_uid": generate_external_uid(),
        "device_type": device_type,
        "vendor": vendor,
        # "model": model,
        # "short_name": generate_short_name(device_type),
        # "domain": random.choice(DOMAINS),
        # "public_ip_address": generate_public_ip(),
        "location": random.choice(LOCATIONS),
        "user": random.choice(USERS),
        "operating_system_full": os_full,
        "operating_system": os_full.split(" ")[0],
        "operating_system_version": os_version,
        "operating_system_build": os_version,
        "operating_system_patch": os_version,
        "operating_system_edition": os_version,
        "operating_system_sw_edition": os_version,
        "operating_system_target_sw": os_full.split(" ")[0],
        "operating_system_target_hw": os_full.split(" ")[0],
        "operating_system_variant": os_variant,
        "operating_system_variant_version": os_version,
        "operating_system_variant_build": os_version,
        "maintenance_end_date": generate_date(),
        "maintenance_start_date": generate_date(),
        "maintenance_source_url": eol_link
    }

def generate_json_output(num_records, filename, include_feed=True):
    inventory = [generate_record() for _ in range(num_records)]
    output_data = inventory
    if include_feed:
        output_data = {
            "accelerator_uuid": ACCELERATOR_UUID,
            "feed_type_id": FEED_TYPE_ID,
            "feed": inventory
        }
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, 'w') as file:
        json.dump(output_data, file, indent=2)
    print(f"✅ JSON file '{filename}' created with {num_records} records!")

def generate_csv_output(num_records, filename):
    inventory = [generate_record() for _ in range(num_records)]
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=inventory[0].keys())
        writer.writeheader()
        writer.writerows(inventory)
    print(f"✅ CSV file '{filename}' created with {num_records} records!")

def main():
    # Default values
    default_format = "JSON_CLI"
    default_records = 100
    default_files = 1
    default_accelerator_uuid = "default-uuid"
    default_feed_type_id = "default-feed-type"
    default_json_cli = "output_cli.json"
    default_json_ui = "output_ui.json"
    default_csv = "output.csv"

    arg_len = len(sys.argv)

    if arg_len == 1:
        file_format = default_format
        num_records = default_records
        num_files = default_files
        accelerator_uuid = default_accelerator_uuid
        feed_type_id = default_feed_type_id
        filename = None
    elif arg_len >= 4:
        file_format = sys.argv[1]
        try:
            num_records = int(sys.argv[2])
            num_files = int(sys.argv[3])
        except ValueError:
            print("Error: Number of records and files must be integers")
            return

        accelerator_uuid = sys.argv[4] if arg_len > 4 else default_accelerator_uuid
        feed_type_id = sys.argv[5] if arg_len > 5 else default_feed_type_id
        filename = sys.argv[6] if arg_len > 6 else None
    else:
        print("Error: Invalid number of arguments")
        print("Usage: python main.py [JSON_CLI|JSON_UI|CSV_FILE] [num_records] [num_files] [ACCELERATOR_UUID] [FEED_TYPE_ID] [filename]")
        return

    valid_formats = ["JSON_CLI", "JSON_UI", "CSV_FILE"]
    if file_format not in valid_formats:
        print(f"Error: Invalid format. Must be one of {valid_formats}")
        return

    global ACCELERATOR_UUID, FEED_TYPE_ID, JSON_FILE_CLI, JSON_FILE_UI, CSV_FILE
    ACCELERATOR_UUID = accelerator_uuid
    FEED_TYPE_ID = feed_type_id
    JSON_FILE_CLI = filename if filename and file_format == "JSON_CLI" else default_json_cli
    JSON_FILE_UI = filename if filename and file_format == "JSON_UI" else default_json_ui
    CSV_FILE = filename if filename and file_format == "CSV_FILE" else default_csv

    for i in range(num_files):
        if file_format == "JSON_CLI":
            generate_json_output(num_records, f"{JSON_FILE_CLI[:-5]}_{i}.json", include_feed=True)
        elif file_format == "JSON_UI":
            generate_json_output(num_records, f"{JSON_FILE_UI[:-5]}_{i}.json", include_feed=False)
        elif file_format == "CSV_FILE":
            generate_csv_output(num_records, f"{CSV_FILE[:-4]}_{i}.csv")

if __name__ == "__main__":
    main()
