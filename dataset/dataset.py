import csv

print(" ==========TWITCH STREAMERS DATASET==========")
print()
print(" You will obtain a set of information on entering the name of the streamer below")
print()
with open('dataset/twitchdata.csv', 'r', encoding='utf-8') as f:
    name = input(" Enter name of streamer (write exact name): ")
    csv_r = csv.reader(f, delimiter=',')
    for rec in csv_r:
        if rec[0]==name:
            print('  Name: ', rec[0])
            print('  Watch Time in minutes: ', rec[1])
            print('  Stream Time in minutes: ', rec[2])
            print('  Language : ', rec[10])
            print('  Peak viewers: ', rec[3])
            print('  Average viewers: ', rec[4])
            print('  Followers: ', rec[5])
            print('  Followers gained in 2020: ', rec[6])
            print('  Viewers gained in 2020: ', rec[7])
            print('  Partnered (True/False): ', rec[8])
            print('  Mature (True/False): ', rec[9])
print()