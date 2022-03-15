import requests

class TodoListService:

    def add_Item(self,i_reference):
        try:    
            if i_reference: 
                # API call to add value to back end 
                response = "Item Added"
            else: 
                response = "No item Provided"
        except:
            response = "Item Not Added"
        return response



    def get_Item(self,i_reference):
        if i_reference:
            # API call to Backend to get single Items
            response ="single"
        else:
            # APi Call to backend to get all the values that
            response ="all"
        
        return response