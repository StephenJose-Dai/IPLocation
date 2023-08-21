import geoip2.database
import tkinter as tk
from tkinter import filedialog

# 创建一个GUI窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 弹出对话框，让用户选择ASN、国家、城市的 MMDB 文件
asn_db_path = filedialog.askopenfilename(title="选择 ASN 文件", filetypes=[("MMDB文件", "*.mmdb")])
country_db_path = filedialog.askopenfilename(title="选择 Country 文件", filetypes=[("MMDB文件", "*.mmdb")])
city_db_path = filedialog.askopenfilename(title="选择 City 文件", filetypes=[("MMDB文件", "*.mmdb")])

# 弹出对话框，让用户选择包含IP地址的文本文件
txt_file_path = filedialog.askopenfilename(title="选择IP地址文本文件", filetypes=[("文本文件", "*.txt")])

asn_reader = geoip2.database.Reader(asn_db_path)
country_reader = geoip2.database.Reader(country_db_path)
city_reader = geoip2.database.Reader(city_db_path)

with open(txt_file_path, 'r') as txt_file:
    ip_addresses = txt_file.read().splitlines()

output_file_path = filedialog.asksaveasfilename(defaultextension=".json", initialfile="results.json", title="选择保存结果的位置")  # 弹出对话框，让用户选择保存位置

with open(output_file_path, 'w',encoding='utf-8') as output_file:
    for ip_address in ip_addresses:
        # 使用 strip() 方法去除首尾空格和换行符
        ip_address = ip_address.strip()
        try:
            asn_response = asn_reader.asn(ip_address)
            country_response = country_reader.country(ip_address)
            city_response = city_reader.city(ip_address)

            print(f"IP地址: {ip_address}")
            print(f"ASN: {asn_response.autonomous_system_number} {asn_response.autonomous_system_organization}")
            print(f"国家: {country_response.country.name}")
            print(f"城市: {city_response.city.name}")
            print("-----------------------")

            output_file.write(f"IP地址: {ip_address}\n")
            output_file.write(f"ASN: {asn_response.autonomous_system_number} {asn_response.autonomous_system_organization}\n")
            output_file.write(f"国家: {country_response.country.name}\n")
            output_file.write(f"城市: {city_response.city.name}\n")
            output_file.write("-----------------------\n")
        except geoip2.errors.AddressNotFoundError:
            print(f"无法找到IP地址 {ip_address} 的信息，可能该IP是局域网IP。")
            output_file.write(f"无法找到IP地址 {ip_address} 的信息，可能该IP是局域网IP。\n")

asn_reader.close()
country_reader.close()
city_reader.close()

print("结果已保存。")
