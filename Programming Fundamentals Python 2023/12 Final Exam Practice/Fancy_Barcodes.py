import re
def barcode_validation(list):
    pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
    for barcode in list:
        match = re.findall(pattern, barcode)

        if match:
            product_group = ''.join(re.findall(r"\d", barcode))
            if product_group == '':
                product_group ="00"
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")


number_of_barcodes = int(input())
barcode_list = []
for n in range(number_of_barcodes):
    barcode_list.append(input())

barcode_validation(barcode_list)