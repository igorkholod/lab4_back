from braces.views import CsrfExemptMixin

from pharmacy.models import Drug, Pharmacy
from django.contrib.auth.models import User
from .serializers import DrugSerializer, PharmacySerializer, DrugSearchSerializer, DrugPharmacySearchSerializer,\
    DrugPharmacy
from rest_framework.response import Response
from rest_framework.views import APIView


class DrugView(APIView):
    @staticmethod
    def get(request, id):
        try:
            drug = Drug.objects.get(id=id)
        except Drug.DoesNotExist:
            return Response({'Error': 'NOT_FOUND'})

        serializer = DrugSerializer(drug)
        return Response(serializer.data)


class PharmacyView(APIView):
    @staticmethod
    def get(request, id):
        try:
            pharmacy = Pharmacy.objects.get(id=id)
        except Pharmacy.DoesNotExist:
            return Response({'Error': 'NOT_FOUND'})

        serializer = PharmacySerializer(pharmacy)
        return Response(serializer.data)


class DrugSearchView(APIView):
    @staticmethod
    def get(request, search):
        drugs = Drug.objects.filter(name__icontains=search)
        if drugs:
            serializer = DrugSearchSerializer(drugs, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'NOT_FOUND'})


class PharmacySearchView(APIView):
    @staticmethod
    def get(request, id):
        pharmacies = DrugPharmacy.objects.filter(drug=id)
        if pharmacies:
            serializer = DrugPharmacySearchSerializer(pharmacies, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error': 'NOT_FOUND'})


class RegisterView(CsrfExemptMixin, APIView):
    @staticmethod
    def post(request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            return Response({'response': 'EMAIL_TAKEN'})
        if User.objects.filter(username=username).exists():
            return Response({'response': 'USERNAME_TAKEN'})

        User.objects.create_user(username=username, password=password, email=email).save()
        return Response({'response': 'OK'})
