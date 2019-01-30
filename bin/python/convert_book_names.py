import csv, json
'''
Use this script to replace book names with standardized book names.
Add new variants as needed.
Use Bible_Metadata_Books_of_the_Bible.csv as reference
'''

filename = 'heartlight_topical_daily_reading_texts.csv'
file = f'input/{filename}'

print(file)
reader = csv.reader(open(file, 'r'))

lookup_dict = {
    'Genesis': 'Gen',
    'Exodus': 'Exod',
    'Leviticus': 'Lev',
    'Numbers': 'Num',
    'Deuteronomy': 'Deut',
    'Joshua': 'Josh',
    'Judges': 'Judg',
    'Ruth': 'Ruth',
    'Samuel': 'Sam',
    'Kings': 'Kgs',
    'Chronicles': 'Chr',
    'Ezra': 'Ezra',
    'Nehemiah': 'Neh',
    'Esther': 'Esth',
    'Job': 'Job',
    'Psalms': 'Ps',
    'Proverbs': 'Prov',
    'Ecclesiastes': 'Eccl',
    'Song of Solomon': 'Song',
    'Isaiah': 'Isa',
    'Jeremiah': 'Jer',
    'Lamentations': 'Lam',
    'Ezekiel': 'Ezek',
    'Daniel': 'Dan',
    'Hosea': 'Hos',
    'Joel': 'Joel',
    'Amos': 'Amos',
    'Obadiah': 'Obad',
    'Jonah': 'Jonah',
    'Micah': 'Mic',
    'Nahum': 'Nah',
    'Habakkuk': 'Hab',
    'Zephaniah': 'Zeph',
    'Haggai': 'Hag',
    'Zechariah': 'Zech',
    'Malachi': 'Mal',
    'Matthew': 'Matt',
    'Mark': 'Mark',
    'Luke': 'Luke',
    'John': 'John',
    'Acts': 'Acts',
    'Romans': 'Rom',
    'Corinthians': 'Cor',
    'Galatians': 'Gal',
    'Ephesians': 'Eph',
    'Philippians': 'Phil',
    'Colossians': 'Col',
    'Thessalonians': 'Thess',
    'Timothy': 'Tim',
    'Titus': 'Titus',
    'Philemon': 'Phm',
    'Hebrews': 'Heb',
    'James': 'Jas',
    'Peter': 'Pet',
    'Jude': 'Jude',
    'Revelation': 'Rev'
}

with open(f'output/{filename}', "w", newline='') as output:
    csvwriter = csv.writer(output)
    
    for row in reader:
        book = row[2] # keep original value
        alpha_bookname = ''.join(list(filter(lambda x: x.isalpha(), book)))
        if alpha_bookname in lookup_dict:
            # Update value to equal only alpha portion of book name
            row[2] = row[2].replace(alpha_bookname, lookup_dict[alpha_bookname])
            if row[2][0].isdigit() and row[2].find(' ') < 4:
                # if book name has a digit, remove any space between it and book name.
                # use format #Bookname, e.g. 1Kgs
                row[2] = row[2].replace(' ', '', 1)
        print(row[2])
        csvwriter.writerow(row)

print("Done executing program")