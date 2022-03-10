# 6.1

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for address in mac:
    result.append(address.replace(":", "."))
print(result)