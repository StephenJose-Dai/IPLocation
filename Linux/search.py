import geoip2.database

print("请输入 ASN 文件的路径和名字,例如/root/GeoLite2-ASN.mmdb：")
asn_db_path = input()

print("请输入 Country 文件的路径和名字,例如/root/GeoLite2-Country.mmdb：")
country_db_path = input()

print("请输入 City 文件的路径和名字,例如/root/GeoLite2-City.mmdb：")
city_db_path = input()

print("请输入包含IP地址的文本文件的路径和名字,例如/root/iplist.txt：")
txt_file_path = input()

print("请输入保存结果的文件的路径和名字,例如/root/abc.json：")
output_file_path = input()

asn_reader = geoip2.database.Reader(asn_db_path)
country_reader = geoip2.database.Reader(country_db_path)
city_reader = geoip2.database.Reader(city_db_path)

with open(txt_file_path, 'r') as txt_file:
    ip_addresses = txt_file.read().splitlines()

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for ip_address in ip_addresses:
        ip_address = ip_address.strip()
        try:
            asn_response = asn_reader.asn(ip_address)
            country_response = country_reader.country(ip_address)
            city_response = city_reader.city(ip_address)

            output_file.write(f"IP地址: {ip_address}\n")
            output_file.write(f"ASN: {asn_response.autonomous_system_number} {asn_response.autonomous_system_organization}\n")
            output_file.write(f"国家: {country_response.country.name}\n")
            output_file.write(f"城市: {city_response.city.name}\n")
            output_file.write("-----------------------\n")
        except geoip2.errors.AddressNotFoundError:
            output_file.write(f"无法找到IP地址 {ip_address} 的信息,可能该地址为局域网地址。\n")

asn_reader.close()
country_reader.close()
city_reader.close()

print("结果已保存。")
