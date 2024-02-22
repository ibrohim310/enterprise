from . import serilazers
from employees import models
from rest_framework import authentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate


#@api_view(['GET'])
#def list_products(request):
#    products = models.Product.objects.all()
#    serializer = serializers.ListProductSerializer(products, many=True)
#    return Response(serializer.data)
#
#
#@api_view(['GET'])
#@authentication_classes([authentication.TokenAuthentication])
#@permission_classes([IsAuthenticated])
#def product_detail(request, slug):
#    user = request.user
#    product = models.Product.objects.get(slug=slug)
#    image = models.ProductImage.objects.filter(product=product)
#    serializer = serializers.DetailProductSerializer(product,image)
#    return Response(serializer.data)

#category


#employee
@api_view(['POST'])
def create_staff(request):
    """ xodimlarni api qilish """
    if request.method == 'POST':
        serializer = serilazers.CreateEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_staff(request):
    """ xodimlar royhatini api qilish """
    employees = models.Employee.objects.all()
    serilazer = serilazers.ListEmployeeSerializer(employees, many=True)
    return Response(serilazer.data)
    


#attendance
@api_view(['POST'])
def create_attendance(request):
    """ xodimlarni kelgan vaqtini api qilish """
    if request.method == 'POST':
        serializer = serilazers.CreateAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def attendance_day(request):
    """ xodimlarni birkunlik davomatini api qilish"""
    serilazer = serilazers.DayAttendanceSerializer(data=request.data)


@api_view(["GET"])
def attendance_week(request):
    """ xodimlarni bir haftalik davomatini api qilish """
    serilazer = serilazers.WeekAttendanceSerializer(data=request.data)


@api_view(["GET"])
def attendance_month(request):
    """ xodimlarni bir oylik davomatini api qilish """
    serilazer = serilazers.MonthAttendanceSerializer(data=request.data)

