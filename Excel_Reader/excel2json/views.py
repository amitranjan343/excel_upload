from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from django.http import JsonResponse
from django.conf import settings as DSettings
from .models import Excel_DB
from pathlib import Path
from pandas import read_excel

# Create your views here.
def home(request):
    return render(request, 'home.html')

class Excel(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        try:
            if request.method == 'POST':
                #parse request
                excel_file = request.FILES.getlist('excel')[0]
                name = excel_file.name
                #create directory
                excel_dir = Path(DSettings.MEDIA_ROOT) / 'temp'
                excel_dir.mkdir(exist_ok=True)
                #write file in django
                with open(excel_dir/name, 'wb+') as f:
                    f.write(excel_file.read())
                #create json
                excel_data_df = read_excel(str(excel_dir/name))
                excel_json = excel_data_df.to_json(orient='records')
                #Database entry
                db = Excel_DB(fname=name, data=excel_json)
                db.save()
                return JsonResponse({'data' : excel_json}, safe=False)
        except Exception as e:
            raise Exception(f'Excel.post failed : {e}')