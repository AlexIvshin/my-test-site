from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Tag, Script, Man, Link, Command
from django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm, ScriptForm, LinkForm, ManForm, CommandForm
from django.core.paginator import Paginator
from django.db.models import Q


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class ScriptDetail(ObjectDetailMixin, View):
    model = Script
    template = 'blog/script_detail.html'


class ScriptCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = ScriptForm
    template = 'blog/script_create_form.html'
    raise_exception = True


class ScriptDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Script
    template = 'blog/script_delete_form.html'
    redirect_url = 'scripts_list_url'
    raise_exception = True


class ScriptUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Script
    model_form = ScriptForm
    template = 'blog/script_update_form.html'
    raise_exception = True


class ManDetail(ObjectDetailMixin, View):
    model = Man
    template = 'blog/man_detail.html'


class ManCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = ManForm
    template = 'blog/man_create_form.html'
    raise_exception = True


class ManDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Man
    template = 'blog/man_ru_delete_form.html'
    redirect_url = 'mans_list_url'
    raise_exception = True


class ManUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Man
    model_form = ManForm
    template = 'blog/man_update_form.html'
    raise_exception = True


class CommandDetail(ObjectDetailMixin, View):
    model = Command
    template = 'blog/command_detail.html'


class CommandCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = CommandForm
    template = 'blog/command_create_form.html'
    raise_exception = True


class CommandDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Command
    template = 'blog/command_delete_form.html'
    redirect_url = 'commands_list_url'
    raise_exception = True


class CommandUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Command
    model_form = CommandForm
    template = 'blog/command_update_form.html'
    raise_exception = True


def posts_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context=context)


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def scripts_list(request):
    scripts = Script.objects.all()
    return render(request, 'blog/scripts_list.html', context={'scripts': scripts})


def links_list(request):
    links = Link.objects.all()
    return render(request, 'blog/links_list.html', context={'links': links})


def mans_list(request):
    mans = Man.objects.all()
    return render(request, 'blog/mans_list.html', context={'mans': mans})


def commands_list(request):
    commands = Command.objects.all()
    return render(request, 'blog/commands_list.html', context={'commands': commands})


def search_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        scripts = Script.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        links = Link.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        commands = Command.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        mans = Man.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        context = {
            'search_query':search_query,
            'scripts': scripts,
            'posts': posts,
            'links': links,
            'commands': commands,
            'mans': mans
        }
        return render(request, 'blog/search_list.html', context=context )
