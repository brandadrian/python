from datetime import datetime

dateTimeObj = datetime.now()
message = 'Message from: ' + dateTimeObj.strftime("%m/%d/%Y, %H:%M:%S" + '\n')

f = open("messageFile.txt", "a")
f.write(message)
f.close()
