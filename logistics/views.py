from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    template_name = 'logistics/index.html'

class Industries(generic.TemplateView):
    template_name = 'logistics/industries.html'


class Contact(generic.TemplateView):
    template_name = 'logistics/contact.html'



class Services(generic.TemplateView):
    template_name = 'logistics/services.html'



class Blog(generic.TemplateView):
    template_name = 'logistics/blog.html'


class BlogDetail(generic.TemplateView):
    template_name  = 'logistics/blog-single.html'


#class Blog(DetailView):
    #queryset = Post.objects.filter(status=1).order_by('-created_on')
    #def get_queryset(self):
        #return super().get_queryset()
    
    #template_name = 'blog.html'


#class BlogDetail(DetailView):
    #template_name = 'blog-details.html'


class About(generic.TemplateView):
    template_name = 'logistics/about.html'
