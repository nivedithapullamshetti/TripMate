from rest_framework import serializers


class TripSerializer(serializers.Serializer):

    source = serializers.CharField()

    destination = serializers.CharField()

    start_date = serializers.CharField()

    end_date = serializers.CharField()

    budget = serializers.IntegerField()

    transport = serializers.CharField()

    accommodation = serializers.CharField()

    activities = serializers.CharField()