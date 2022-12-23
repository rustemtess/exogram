from django.shortcuts import render
from django.http import JsonResponse

def main():
    data = {
        name: 'bawer',
    }
    JsonResponse(data)