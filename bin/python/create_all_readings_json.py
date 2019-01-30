import csv, json

# write this to json. main output of app.
main_dict = {}

# List of tuples. Each tuple has
# [0]: plan abbreviation
# [1]: plan description
# [2]: path to csv to convert to json

plans = [
        ('oyb', 'The One Year® Bible', 'input/oyb_daily_reading_texts.csv'),
        ('bp', 'The Bible Project Plan', 'input/bibleproject_daily_reading_texts.csv'),
        ('90d', 'The Bible in 90 Days', 'input/bible_in_90_days_reading_texts.csv'),
        ('chron', 'Chronological Plan', 'input/chronological_daily_reading_texts.csv'),
        ('topic', 'Topical Plan', 'input/heartlight_topical_daily_reading_texts.csv')
        ]
for plan in plans:
    main_dict[plan[0]] = {}

    # Create key for 'days'
    # e.g. 'oyb'['days'] = {'1': '', '2': ''}
    main_dict[plan[0]]['days'] = {}
    for i in range(1, 366, 1):
        main_dict[plan[0]]['days'][str(i)] = []

    # There will always be an accompanying csv with plan readings
    reader = csv.reader(open(plan[2], 'r'))
    for row in reader:
        if row[0] in main_dict[plan[0]]['days']:
            key = row[0]
            value = row[2]
            main_dict[plan[0]]['days'][key].append(value)

    # Create key for 'plan description'
    main_dict[plan[0]]['plan_description'] = plan[1]
            
with open('output/readings.json', 'w') as fp:
    json.dump(main_dict, fp)

print("Done executing program")