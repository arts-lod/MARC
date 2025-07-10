import os
import csv

def parse_unimarc(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        records = file.read().strip().split('\n\n')  # Assume that each record is separated by a blank line
    return records

def extract_tags(record):
    lines = record.split('\n')
    tag_001 = ""
    tag_500 = ""
    tag_215 = ""

    for line in lines:
        if line.startswith('001'):
            tag_001 = line[4:].strip()
        elif line.startswith('500'):
            tag_500 = line[4:].strip()
        elif line.startswith('215'):
            tag_215 = line[4:].strip()

    return tag_001, tag_500, tag_215

def main():
    unimarc_file = 'Export_UNIMARC_List_1751619001414.txt'
    output_csv = 'TOM.csv'
    output_csv_78 = 'TOM_78.csv'
    stats_file = 'dati.txt'

    if not os.path.exists(unimarc_file):
        print(f"File {unimarc_file} non trovato.")
        return

    records = parse_unimarc(unimarc_file)
    total_records = len(records)
    records_with_500 = 0
    records_without_500 = 0
    tag_215_with_78 = 0

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile, \
         open(output_csv_78, 'w', newline='', encoding='utf-8') as csvfile_78:
        csv_writer = csv.writer(csvfile, delimiter=';')
        csv_writer_78 = csv.writer(csvfile_78, delimiter=';')

        for idx, record in enumerate(records, 1):
            tag_001, tag_500, tag_215 = extract_tags(record)
            if tag_500:
                records_with_500 += 1
            else:
                records_without_500 += 1

            if '78' in tag_215:
                tag_215_with_78 += 1
                csv_writer_78.writerow([idx, tag_001, tag_500, tag_215, ''])  # Write to TOM_78.csv

            csv_writer.writerow([idx, tag_001, tag_500, tag_215, ''])  # Write to TOM.csv

    with open(stats_file, 'w', encoding='utf-8') as stats:
        stats.write(f"Numero totale di schede: {total_records}\n")
        stats.write(f"Numero di schede con tag 500: {records_with_500}\n")
        stats.write(f"Numero di schede senza tag 500: {records_without_500}\n")
        stats.write(f"Numero di tag 215 con '78': {tag_215_with_78}\n")

if __name__ == "__main__":
    main()
