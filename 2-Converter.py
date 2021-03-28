import datetime
# or this , and delete first datetime.
# from datetime import datetime
data = 'Feb 12 2019 2:41PM'

converted_data = datetime.datetime.strptime(data, '%b %d %Y %I:%M%p')
print(converted_data)
# or this
print(converted_data.isoformat(sep=' '))


