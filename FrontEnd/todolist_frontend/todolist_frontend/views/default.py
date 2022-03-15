from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_flash_message import MessageQueue
from .. import service


ToDoListSRV = service.TodoListService()
flash_message = MessageQueue()

@view_config(route_name='home', renderer='todolist_frontend:templates/home.jinja2')
def home(request ):
    reference = request.GET.get('q')
    if reference != None:
        reference = request.GET.get('q')
        response = ToDoListSRV.get_Item(reference)
        items = [response]
    else:
        response = ToDoListSRV.get_Item(None)
        items= [response]    
    context ={'title':'Welcome Page','items':items}
    return context

    


@view_config(route_name='addItem', renderer='todolist_frontend:templates/additem.jinja2')
def addItem(request):
    if request.method == 'POST':
        i_item = request.POST.get('i_Item')
        response =ToDoListSRV.add_Item(i_item)
        
        return HTTPFound(location='/')
    else:
        context ={'title':'Welcome Page'}
        return context
