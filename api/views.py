from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .models import Receipt 
from .serializer import ReceiptSerializer
from .calculatePoints import calculate_points
from django.shortcuts import get_object_or_404




@api_view(['GET'])
def home_page(request):

    return Response("Fetch-Rewards-Receipt-Processor-Challenge", status=status.HTTP_200_OK)





@api_view(['GET'])
def get_points(request):
    try:
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def get_points_by_id(request, id=None):  
    if id is not None:
        receipt = get_object_or_404(Receipt, id=id)
        serializer = ReceiptSerializer(receipt)
        return Response({"points": serializer.data['totalPoints']}, status=status.HTTP_200_OK)

@api_view(['POST'])
def process_reciepts(request):
    serializer=ReceiptSerializer(data=request.data)
    if serializer.is_valid():
        total_points=calculate_points(serializer.validated_data)
        serializer.save(totalPoints=total_points)
        return Response({"id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)







