from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import subprocess
import re
from django.views.generic import View
from .models.languagemodels import Language


# Create your views here.
class RunLanguageView(View):

    @classmethod
    def run_python(cls, request):
        not_supported = {'open': 2, 'input': 3}
        code = request.POST.get('code')
        # print(code)
        for key in not_supported.keys():
            # print(key in code)
            if key in code:
                return HttpResponse(json.dumps(
                    {'code': not_supported[key], 'run_result': 'Sorry. Not support "' + str(key) + '" function now.'}))
        ans = {}
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = BASE_DIR + '/user_data/1.py'
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        try:
            command_run = 'python'
            if  request.POST.get('version') >= '3':
                command_run += '3 '
            else:
                command_run += '2 '
            code, run_result = subprocess.getstatusoutput(command_run + file_path)
        except Exception as e:
            code = 1
            run_result = str(e)

        run_result = run_result.replace('\n', '<br />').replace('\r\n', '<br />')
        pattern = re.compile(r'File "(.*?)"')
        run_result = re.sub(pattern, 'File ""', run_result)
        # print(run_result)
        ans['run_result'] = run_result
        ans['code'] = code

        return HttpResponse(json.dumps(ans))

    def post(self, request):
        if request.POST.get('type') == 'python':
            return RunLanguageView.run_python(request)


class PythonView(View):
    def get(self, request):
        languages = Language.objects.all()
        result = []
        for language in languages:
            result.append({'language' : language.name, 'version' : language.version, 'link' : language.link.url})

        result_group = {}
        for res in result:
            result_group.setdefault(res['language'],[]).append(res)

        return render(request,'temp_programs/index.html',{'languages' : result_group, 'current_language' : 'python', 'current_version' : '3.7'})




# def index(request):
#     return render(request,'temp_programs/index.html')
#
#
# def run_python(request):
#     not_supported = {'open' : 2,'input': 3}
#     code = request.POST.get('code')
#     # print(code)
#     for key in not_supported.keys():
#         # print(key in code)
#         if key in code:
#             return HttpResponse(json.dumps({'code' : not_supported[key],'run_result' : 'Sorry. Not support "'+str(key)+'" function now.'}))
#     ans = {}
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     file_path = BASE_DIR + '/user_data/1.py'
#     with open(file_path,'w',encoding='utf-8') as f:
#         f.write(code)
#     try:
#         code,run_result = subprocess.getstatusoutput('python3 '+file_path)
#     except Exception as e:
#         code = 1
#         run_result = str(e)
#
#     run_result = run_result.replace('\n','<br />').replace('\r\n','<br />')
#     pattern =  re.compile(r'File "(.*?)"')
#     run_result = re.sub(pattern, 'File ""',run_result)
#     # print(run_result)
#     ans['run_result'] = run_result
#     ans['code'] = code
#     return HttpResponse(json.dumps(ans))