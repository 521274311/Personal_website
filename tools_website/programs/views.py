from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import subprocess
import re
# Create your views here.
def index(request):
    return render(request,'temp_programs/index.html')

def run_python(request):
    code = request.POST.get('code')
    ans = {}
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = BASE_DIR + '/user_data/1.py'
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(code)
    try:
        code,run_result = subprocess.getstatusoutput('python3 '+file_path)
    except Exception as e:
        code = 1
        run_result = str(e)

    run_result = run_result.replace('\n','<br />').replace('\r\n','<br />')
    pattern =  re.compile(r'File "(.*?)"')
    run_result = re.sub(pattern, 'File ""',run_result)
    print(run_result)
    ans['run_result'] = run_result
    ans['code'] = code
    return HttpResponse(json.dumps(ans))