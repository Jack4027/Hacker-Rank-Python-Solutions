regex_pattern = r"^M{0,3}(CM)?D?(CD)?(XD)?C{0,3}(XC)?L?X{0,3}(XL)?V{0,3}I{0,3}X?V?$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
