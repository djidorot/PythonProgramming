import math
import pandas as pd
from math import pi, sin
from math import *

# 1. Import Entire Module - Imports everything and requires using the module name as a prefix.
print(math.sqrt(16))  # Output: 4.0

# 2. Import with an Alias - Renames the module to a shorter name for cleaner code.
df = pd.DataFrame()

# 3. Import Specific Attributes - Imports specific items directly into your script so you do not need a prefix.
print(pi)  # Output: 3.141592653589793

# 4. Import Everything (*)- Imports all components of a module directly into your workspace. Note: Avoid this method as it can cause naming conflicts with your own variables.
print(floor(4.7))  # Output: 4