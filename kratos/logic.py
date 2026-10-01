age_0 = 20
age_1 = 67

# ---AND---
#  1  2  OUT
#  F  F   F
#  T  F   F
#  F  T   F
#  T  T   T
if (age_0 < 20) and (age_1 < 20):
    print('both kids')
if (age_0 > 15) and (age_1 < 69):
    print('both yummy')

# ---OR---
#  1  2  OUT
#  F  F   F
#  T  F   T
#  F  T   T
#  T  T   T
if (age_0 >= 20) or (age_1 > 70):
    print('either uncs')
