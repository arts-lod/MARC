from pymarc import MARCReader

# Input
filename = input("Filename: ").strip()
author_name = input("Author: ").strip()
title_content = input("Work: ").strip()

# Memory list of results
results = []

# MARC file is open
with open(filename, 'rb') as fh:
    reader = MARCReader(fh)

    # Extrction of required records
    for record in reader:
        if record and (author_name in str(record)) and (title_content in str(record)):
            result_str = 'TITLE: ' + record.title + '\n\nRECORD:\n' + str(record) + '\n\n'
            results.append(result_str)

# Visualization ten by ten of required records
index = 0
block_size = 10
total = len(results)

while index < total:
    for i in range(index, min(index + block_size, total)):
        print(results[i])

    index += block_size

    if index < total:
        user_input = input("'Enter' to continue - 'q' to quit: ").strip().lower()
        if user_input == 'q':
            print("Exit. Memory clean")
            results.clear()
            break
    else:
        print("END OF RESULTS.")

###############################################
#   TO RE-USE PLEASE CONSULT THE README FILE
###############################################
