import requests
import json

class TodoListService:

    def add_Item(self,new_item):
        try:    
            if new_item: 
                # API call to add value to back end 
                if len(new_item) > 10 and len(new_item) < 100:
                    url = 'http://localhost:5000/addToDoItem'
                    data = {"item": new_item} 
                    j_response = requests.post(url, json=data)
                    response = j_response.json()  
                    if j_response.status_code == 200:
                        data_pass = True
                        message = response['message']
                    else: 
                        data_pass = False
                        message = "Item Added"
                else:
                    data_pass = False
                    message = "Note Length not acceptable !!"
            else: 
                message = "No item Provided"
        except:
            message = "Item Not Added"
        return {'data_pass': data_pass,'message':message}



    def get_Item(self,i_reference):
        url = 'http://localhost:5000/search'            
        j_body = {'reference': i_reference}
        json_return = requests.get(url, params=j_body)
        response = json_return.json()    
        return response