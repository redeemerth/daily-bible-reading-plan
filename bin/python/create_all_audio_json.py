import csv, json

# write this to json. main output of app.
# contains all audio details for all plans and bible versions for that plan.
main_dict = {}

# create key for each bible reading plan
for item in ['oyb', 'bp', '90d', 'chron', 'topic']:
    main_dict[item] = {}
    
# List of tuples. Each tuple has 
# [0]: plan abbreviation
# [1]: bible translation/version abbreviation
# [2]: base url to audio
# [3]: path to csv to convert to json (if any). Use None if not.
audio = [
        ('oyb',   'nlt', 'http://audio.oneyearbibleonline.com/tomdooley/{var1}.mp3', 'input/oneyearbible_urls.csv'),
        ('oyb',   'esv', 'https://audio.esv.org/hw/hq/{var1}.mp3', None),
        ('bp',    'esv', 'https://audio.esv.org/hw/hq/{var1}.mp3', None),
        ('90d',   'esv', 'https://audio.esv.org/hw/hq/{var1}.mp3', None),
        ('chron', 'esv', 'https://audio.esv.org/hw/hq/{var1}.mp3', None),
        ('topic', 'esv', 'https://audio.esv.org/hw/hq/{var1}.mp3', None)
        ]

for a in audio:
    # Create key for plan bible version
    main_dict[a[0]][a[1]] = {}
    
    # Get URL params from csv (if needed)
    # Check if file path provided in tuple
    # Assumes any csv has header row and column one is a day number and
    # column two is a string value (one or more url params separated by spaces)
    if a[3]:
        # Create key for 'days'
        # e.g. 'oyb'['nlt']['days'] = {'1': '', '2': ''}
        main_dict[a[0]][a[1]]['days'] = {}
        for i in range(1, 366, 1):
            main_dict[a[0]][a[1]]['days'][str(i)] = ''
    
        reader = csv.reader(open(a[3], 'r'))
        for row in reader:
            if row[0] in main_dict[a[0]][a[1]]['days']:
                key = row[0]
                main_dict[a[0]][a[1]]['days'][key] = row[1]
    
    # Create key for base url
    main_dict[a[0]][a[1]]['url'] = a[2]
    
    # Create key for version abbreviation
    main_dict[a[0]][a[1]]['version'] = a[1].upper()

with open('output/audio.json', 'w') as fp:
    json.dump(main_dict, fp)

print("Done executing program")