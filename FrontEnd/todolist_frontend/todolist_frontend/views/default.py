from pyramid.view import view_config


@view_config(route_name='home', renderer='todolist_frontend:templates/home.jinja2')
def home(request ):
    context ={'title':'Welcome Page',}
    return context

@view_config(route_name='listitem', renderer='todolist_frontend:templates/home.jinja2')
def listitem(request):
    print("hello")
    ref = request.params['q']
    items= ["item2","item3","item4","item5",ref]
    context ={'title':'Welcome Page','items':items}
    return context
    


