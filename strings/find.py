text = "X-DSPAM-Confidence:    0.8475"
#extracting 0.8475 from a string
lenght = len(text)
first_index = text.find("0")
req = float(text[first_index : lenght])
print(f"{req}")