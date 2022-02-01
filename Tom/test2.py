15761

import datetime
import time

StartDate = "01/01/70"

date_1 = datetime.datetime.strptime(StartDate, "%m/%d/%y")

end_date = date_1 + datetime.timedelta(days=15761)


date_2 = time.gmtime(1361804829)
print(date_2)

year = date_2[0]
month = date_2[1]
day = date_2[2]
