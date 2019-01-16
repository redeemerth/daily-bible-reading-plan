import csv, json

# write this to json. main output of app.
main_dict = {}
main_dict['days'] = {}
main_dict['plans'] = {
'oyb_nlt': {
    'url': 'http://audio.oneyearbibleonline.com/tomdooley/{var1}.mp3',
    'plan_description': 'The One Year® Bible',
    'audio_description': 'NLT Audio (With Commentary)'
   }
}
for i in range(1, 366, 1):
    main_dict['days'][str(i)] = {'oyb': {'audio': {}, 'readings': []}}

# Incorporate date required to create URL
# http://audio.oneyearbibleonline.com/tomdooley/<mmdd>.mp3
# CSV will have two columns.
# Row example:  1, 0101
#               2, 0102 

reader = csv.reader(open('input/oneyearbible_urls.csv', 'r'))
for row in reader:
    if row[0] in main_dict['days']:
        key = row[0]
        value = row[1]
        main_dict['days'][key]['oyb']['audio']['nlt'] = value

reader = csv.reader(open('input/oyb_daily_reading_texts.csv', 'r'))
for row in reader:
    if row[0] in main_dict['days']:
        key = row[0]
        value = row[2]
        main_dict['days'][key]['oyb']['readings'].append(value)

with open('output/main.json', 'w') as fp:
    json.dump(main_dict, fp)

for k, v in main_dict['days'].items():
    print(f"{k}: {v}")

print("Done executing program")