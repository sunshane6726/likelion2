Django - Model & Admin / QuerySet & Method / Detail.html / STATIC & MEDIA 
: 19. 5.21 ~ 19. 5.30의 수업내용  
==========
  
**< 5.29(Wed) - Update Release >**  
● home.html : line 30 → 글쓰기를 URL 직접 조작 필요없이 NavBar의 메뉴로 동작할수있게끔 a태그 추가.  
● detail.html : line 27 → 글쓰기를 URL 직접 조작 필요없이 NavBar의 메뉴로 동작할수있게끔 a태그 추가.  
    
    <a class="nav-item nav-link" href="{% url 'new' %}">글쓰기</a>
***    
**< 5.31(Fri) - Update Release >**  
● portfolio APP 추가
    
    python manage.py startapp portfolio        
● portfolio.html : STATIC & MEDIA 활용을 위해 새롭게 생성 및 추가.
    
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    pip install Pillow    
● 그외 settings.py / models.py / views.py / urls.py / portfolio.html-Bootstrap 수정      
