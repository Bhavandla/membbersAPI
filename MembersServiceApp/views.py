# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from io import StringIO, BytesIO
import pandas as pd
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from MembersServiceApp.serializers import MembersSerializer
from MembersServiceApp.models import MembersModel


class ListMembers(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = MembersSerializer

    def get_queryset(self):
        query_params = self.request.query_params.dict()
        keys = ('id', 'first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id')
        filters = {k: v for k, v in query_params if k in keys}
        return MembersModel.objects.filter(**filters) if filters else MembersModel.objects.all()


class CSVUpload(generics.CreateAPIView):
    queryset = MembersModel.objects.all()
    serializer_class = MembersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.body, many=True)
        serializer.is_valid(raise_exception=False)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def post(self, request, *args, **kwargs):
        csv_file_data = request.body
        file_descriptor = BytesIO(csv_file_data) if isinstance(csv_file_data, bytes) else StringIO(csv_file_data)

        df = pd.read_csv(file_descriptor, header=0,
                         names=['first_name', 'last_name', 'phone_number', 'client_member_id', 'account_id'],
                         dtype={'first_name': 'object', 'last_name': 'object', 'phone_number': 'object',
                                'client_member_id': 'object', 'account_id': 'object'}
                         )
        df.drop_duplicates(subset=['client_member_id', 'phone_number'], keep="first", inplace=True)
        request.body = df.to_dict('records')
        return super(CSVUpload, self).post(request, *args, **kwargs)
