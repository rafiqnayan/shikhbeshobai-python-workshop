import csv

with open('user_tokens.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            user_name = row[0]
            to_email_address = row[1]
            user_token = row[2]
            line_count += 1
            print "name: %s, email: %s, token: %s" % (user_name, to_email_address, user_token)