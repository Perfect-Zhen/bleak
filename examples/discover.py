"""
Scan/Discovery
--------------

Example showing how to scan for BLE devices.

Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>

"""

import argparse
import asyncio
import json

from bleak import BleakScanner


async def find_by_name(args: argparse.Namespace):
    print("find_by_name: scanning for 5 seconds, please wait...")
    # print("args.device_name:", args.device_name)
    dev_name = ''.join(args.device_name)

    devices = await BleakScanner.find_device_by_name(dev_name, timeout=5)

    print("finded device: ", devices)


async def find_by_address(args: argparse.Namespace):
    print("find_by_address: scanning for 5 seconds, please wait...")
    # print("args.device_address:", args.device_address)
    dev_address = ''.join(args.device_address)

    devices = await BleakScanner.find_device_by_address(dev_address, timeout=5)
    # devices = await BleakScanner.find_device_by_name("NXP_TEMP")
    print("finded device: ", devices)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--macos-use-bdaddr",
        action="store_true",
        help="when true use Bluetooth address instead of UUID on macOS",
    )
    parser.add_argument(
        "--device_name",
        metavar="name",
        nargs="*",
        help="set device name that use for discover filter",
        type=str
    )
    parser.add_argument(
        "--device_address",
        metavar="address",
        nargs="*",
        help="set device address that use for discover filter",
        type=str
    )
    args = parser.parse_args()

    print("filter name: ", args.device_name, "; filter address: ", args.device_address)
    # print("filter address: ", args.device_address)
    asyncio.run(find_by_name(args))
    asyncio.run(find_by_address(args))
