import re
patt = r'\d{2}-\d{2}-\d{4}'
message = "His birthday is 16-11-2016"
re.findall(patt, message)