from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    path = request.path
    print('path',path)
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        'total_visit_count':qs.count(),
        'Conversion_percentage': page_qs.count() * 100.0 / qs.count()
    }
    
    PageVisit.objects.create(path=request.path)
    return render(request, html_template,my_context)


def old_home_page_view(request, *args, **kwargs):
#     html_ = """

# <!DOCTYPE html>
# <html>
    
#     <body>
#         <div class="txt-3xl">
#             <h1>Lets get cooking!!!!!!!!</h1>

#         <p> This is my Saas app building attempt</p>

#         </div>
        
#     </body>
# </html>




# """
    # html_file_path = this_dir/"home.html"
    # html_ = html_file_path.read_text()
    return HttpResponse()
