from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobDescriptionSerializer
from .main import generate_job_description

class JobDescriptionView(APIView):
    def post(self, request):
        # Validate the incoming data using the serializer
        serializer = JobDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            # Generate the job description sections
            position_description, why_work_here, job_description, requirements, perks_and_benefits, about_us, salary_range, job_info, website_link = generate_job_description(serializer.validated_data)
            
            # Prepare the response data
            response_data = {
                "position_description": position_description,
                "why_work_here": why_work_here,
                "job_description": job_description,
                "requirements": requirements,
                "perks_and_benefits": perks_and_benefits,
                "about_us": about_us,
                "salary_range": salary_range,
                "job_info": job_info,
                "website_link": website_link
            }
            
            # Return the response data as JSON
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # If the data is invalid, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
