with open("/Users/mariahavalos/Desktop/testing.csv", "r") as open_csv:
    content = open_csv.readlines()

    listOfNoise = {'For more information, go to the companys website', '==', '--(BUSINESS WIRE)--',
                   '(GLOBE NEWSWIRE) --', '/PRNewswire/', 'To learn more about ',
                   'The latest Market Talks covering Equities. Published exclusively on Dow Jones Newswires throughout the day.',
                   '=====', 'Notification of Sources of Distribution Under Section 19(a)',
                   'Write to', 'Corporate News:', 'Snapshot:', 'This press release provides shareholders of'}
    # Load each line of csv contents into array, return array
    for line in content:
        for noise in listOfNoise:
            if noise in line:
                firstPartLine = line[0:line.find(noise)]
                secondPartLine = line[line.find(noise) + len(noise):len(line)]

                line = firstPartLine + secondPartLine

        print (line)


    listOfFooters = {' Investors should consider the investment objectives, risks, charges and expense of the fund carefully before investing.'}

    for line in content:
        for noise in listOfFooters:
            if noise in line:
                line = line[0:line.find(noise)]

        print (line)