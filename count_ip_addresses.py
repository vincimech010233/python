def ip_to_int(ip_address):
    # Split the IP address into octets
    octets = ip_address.split(".")
    # Convert octets to integer form
    integer_form = int(octets[0]) * 256**3 + int(octets[1]) * 256**2 + int(octets[2]) * 256 + int(octets[3])
    return integer_form

def count_ip_addresses(ip1, ip2):
    # Convert IP addresses to their integer forms
    int_ip1 = ip_to_int(ip1)
    int_ip2 = ip_to_int(ip2)
    # Find the difference between the integer forms
    return int_ip2 - int_ip1

# Examples
print(count_ip_addresses("10.0.0.0", "10.0.0.50"))  # Should return 50
print(count_ip_addresses("10.0.0.0", "10.0.1.0"))   # Should return 256
print(count_ip_addresses("20.0.0.10", "20.0.1.0"))  # Should return 246
