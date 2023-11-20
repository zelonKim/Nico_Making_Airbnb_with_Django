from django.utils import timezone
from rest_framework import serializers
from .models import Booking

class CreateRoomBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = ("check_in", "check_out", "guests")

    def validate_check_in(self, value):  # def validate_필드명(self, 파라미터): 필드명에 해당하는 값을 파라미터로 받음. 
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can`t book in the past")
        print(value)  # 2023-12-25
        return value
    
    def validate_check_out(self, value):  
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Can`t book in the past")
        print(value)  # 2023-12-29
        return value    


    def validate(self, data):  # def validate(self, 파라미터): 모든 필드에 해당하는 값을 파라미터로 받음.
        room = self.context.get('room')
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("Check-in date must precede Check-out date")
        if Booking.objects.filter(room=room, check_in__lte=data["check_out"], check_out__gte=data['check_in']).exists():
            raise serializers.ValidationError("Those dates are already taken")
        print(data) # [('check_in', datetime.date(2023, 12, 25)), ('check_out', datetime.date(2023, 12, 29)), ('guests', 2)]
        return data
       
      


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("pk", "check_in", "check_out", "experience_time", "guests")