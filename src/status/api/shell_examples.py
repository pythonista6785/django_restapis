from django.utils.six import BytesIO
from rest_framework.renders import JSONRenderer
from rest_framework.parsers import JSONParser


from status.api.serializers import StatusSerializers
from status.models import Status

'''
Serialize single obect
'''
obj = Status.objects.first()
serializer = StatusSerializers(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)


'''
Serailize a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializers(obj, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)


stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


''''
Create Objects
'''
data = {'user': 1}
serializer = StatusSerializers(data=data)
serializer.is_valid()
serializer.save()

# if serializer.is_valid():
# 	serializer.save()


'''
Update Object

'''
obj = Status.objects.first()
data = {'content': 'Something here', 'user': 1}
update_serializer = StatusSerializers(obj, data=data)
update_serializer.is_valid()
update_serializer.save()


'''
Delete Object
'''
data = {'user': 1, 'content': 'please delete me'}
create_obj_serializer = StatusSerializers(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save() # it returns instance of the object 
print(create_obj)

#data = {'id': 9}
obj = Status.objects.last()
get_data_serializer = StatusSerializers(obj)
# update_serializer.is_valid()
# update_serializer.save()
print(get_data_serializer.data)
#print(obj.delete())

from rest_framework import serializers

class CustomSerializer(serializers.Serializer):
	content = serializers.CharField()
	email = serializers.EmailField()


data = {'email': 'hello@gmail.com', 'content': 'please add me'}
create_obj_serializer = CustomSerializer(data=data)
if create_obj_serializer.is_valid():
	valid_data = create_obj_serializer.data
	print(valid_data)