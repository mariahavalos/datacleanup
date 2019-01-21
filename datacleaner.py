import re
import io


with io.open("/Users/mariahavalos/Desktop/testing.csv", "r+", encoding="utf-8") as open_csv:
    content = open_csv.readlines()

    outputFile = open("/Users/mariahavalos/Desktop/testing-output.csv", "w")

    listOfNoise = {'==', '--(BUSINESS WIRE)--',
                   '(GLOBE NEWSWIRE) --', '/PRNewswire/',
                   '=====', 'Corporate News:', 'Snapshot:', 'This press release provides shareholders of', 'Notification of Sources of Distribution Under Section 19(a)',
                    '"""', 'For more information, please contact:', 'PR Newswire', 'Tel:', 'Email:', 'Telephone:', 'Phone:',
                   '+(0)', '+(1)', 'GMT -- ', "GMT - ", '"'}

    listOfFooters = {'For more information, go to', '=-'
                     'Write to', 'To learn more about ',
                     'Investors should consider the investment objectives, risks, charges and expense of the fund carefully before investing.'}

    listOfHeader = {'  --  ', '[Dow Jones]', 'Published exclusively on Dow Jones Newswires throughout the day.', 'GMT - ', 'EST - ', '.com About'}

    # Load each line of csv contents into array, return array
    for line in content:
        line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
        line = re.sub(r'^http?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
        line = re.sub(r'www\.\S+\.com', '', line)
        line = re.sub(r'\S*@\S*\s?', '', line)
        line = re.sub(r'^(?:(?:[0-9]{2}[:\/,]){2}[0-9]{2,4}|am|pm)$', '', line)
        line = re.sub(r'\b\d+(?:\.\d+)?\s+', '', line)

        for noise in listOfNoise:
            if noise in line:
                firstPartLine = line[0:line.find(noise)]
                secondPartLine = line[line.find(noise) + len(noise):len(line)]

                line = firstPartLine + secondPartLine
        for noise in listOfFooters:
            if noise in line:
                line = line[0:line.find(noise)]

        for noise in listOfHeader:
            if noise in line:
                line = line[line.find(noise) + len(noise) : len(line)]

        line = line.replace('""', '').replace("  ", '')
        line = line.encode("ascii", errors="ignore").decode()
        newLine = ''
        charPrev = ''
        for character in line:
            if character == '.' and not charPrev.isdigit() and not charPrev == 'o':
                print newLine
                newLine = ''
            else:
                newLine = newLine + character
            charPrev = character
        #outputFile.write(line)
