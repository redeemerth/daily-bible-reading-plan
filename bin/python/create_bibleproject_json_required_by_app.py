import csv, json
from collections import defaultdict

# write this to json. main output of app.
main_dict = defaultdict(lambda: defaultdict(list))

# Read from CSV, and create Dictionary
reader = csv.reader(open('input/bibleproject_lookup_by_book.csv', 'r'))
for n, row in enumerate(reader):
    if not n:
        # Skip header row (n = 0).
        continue
    # BOOK_ID,TITLE,BOOK,ORDER,VIDEO_ID        
    book_id, title, book_name, order, video_id  = row
    book_name = book_name.upper()
    main_dict['books'][book_name].append((video_id))

# Write dictioary to file (JSON)
with open('output/bibleproject_lookup_by_book.json', 'w') as fp:
    json.dump(main_dict, fp)

print("Done executing program")