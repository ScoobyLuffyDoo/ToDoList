from pyramid.view import view_config


@view_config(route_name='home', renderer='todolist_frontend:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'ToDoList_FrontEnd'}



@view_config(route_name='hello', renderer='todolist_frontend:templates/hello.jinja2')
def hello(request):
    return {'hello': 'Hello World'}

