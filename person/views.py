import json

from .models import Person

from django.http import HttpResponse


def create_person(request):
    try:
        data = json.loads(request.body)
        Person.objects.create(**data)
    except Exception as e:
        response = HttpResponse(
            status=400,
            content_type='application/json',
            content=json.dumps({
                'message': str(e)
            })
        )

    return response


def _index(request):
    reponse = HttpResponse()
    if request.method == 'GET':
        response = HttpResponse(status=501)
    elif request.method == 'POST':
        response = create_person(request)

    return response
