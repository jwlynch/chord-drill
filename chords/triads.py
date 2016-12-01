from chords import common

maj_roots = common.maj_roots
aug_roots = common.aug_roots

# chords for 95 - 98% of pop songs
big_four_list = common.big_four_list

# Triads

triad_list = common.triad_list

maj_triads = common.maj_roots[:]
triad_list += maj_triads[:]
big_four_list += maj_triads[:]

min_triads = []
for i in maj_roots:
    min_triads.append(i + "m")
triad_list += min_triads[:]
big_four_list += min_triads[:]

dim_triads = []
for i in maj_roots:
    dim_triads.append(i + " dim")
triad_list += dim_triads[:]

aug_triads = []
for i in aug_roots:
    aug_triads.append(i + " aug")
triad_list += aug_triads[:]

sus_triads = []
for i in maj_roots:
    sus_triads.append(i + " sus")
triad_list += sus_triads[:]
