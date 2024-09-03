from rest_framework import serializers

class JobDescriptionSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=255)
    job_title = serializers.CharField(max_length=255)
    require_skills = serializers.CharField(max_length=1000)
    experience = serializers.CharField(max_length=1000)
    location = serializers.CharField(max_length=255)
    qualifications = serializers.CharField(max_length=1000)
    salary = serializers.CharField(max_length=255)
    job_type = serializers.CharField(max_length=255)
    benefits = serializers.CharField(max_length=1000)
