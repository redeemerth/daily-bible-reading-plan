import csv, json

# write this to json. main output of app.
main_dict = {}
main_dict['days'] = {}

for i in range(1, 366, 1):
    main_dict['days'][str(i)] = []

reader = csv.reader(open('input/oyb_daily_reading_texts.csv', 'r'))
for row in reader:
    if row[0] in main_dict['days']:
        key = row[0]
        value = row[2]
        main_dict['days'][key].append(value)

with open('output/oyb_readings.json', 'w') as fp:
    json.dump(main_dict, fp)

print("Done executing program")