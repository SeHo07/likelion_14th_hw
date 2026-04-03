from django.shortcuts import render

def mainpage(request):
    context = {
        "points": [
            "Django는 MTV 패턴으로 동작함",
            "기본 페이지는 HTML, View, URL 연결로 만듦",
            "템플릿 언어로 변수, 반복문, 조건문을 사용할 수 있음",
            "중복되는 코드는 template 상속으로 정리할 수 있음",
            "CSS와 이미지는 static 폴더로 분리해서 관리함",
        ],
        "cores": [
            "templates/main/mainpage.html 생성하기",
            "views.py에서 render()로 페이지 연결하기",
            "urls.py에서 URL과 view 매핑하기",
            "secondpage.html 추가해서 두 번째 페이지 만들기",
            "{% url 'name' %} 형태로 페이지 링크 연결하기",
            "{{ 변수 }}, {% for %}, {% if %} 문법 익히기",
            "base.html, block, include로 중복 코드 줄이기",
            "static/css, static/images 폴더 만들어 정적 파일 적용하기",
        ],
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    context = {
        'introduce': {
            'name': '이세호',
            'major': '컴퓨터 AI 학부',
            'num': '26학번',
            'age': '20',
            'track': '백엔드'
        },
    }
    return render(request, 'main/secondpage.html', context)