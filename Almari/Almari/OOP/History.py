from user.models import CustomerHistory
from django.forms.models import model_to_dict
from decimal import Decimal
class History:
    def __init__(self,request):
        self.session = request.session
        self.request = request
        history = self.session.get('history')
        if 'history' not in self.session:
            username = request.session.get('username', None)
            if username:
                history_queryset = CustomerHistory.objects.filter(username=username)
                history_list = [self.serialize_history(model_to_dict(record)) for record in history_queryset]
                self.session['history'] = history_list
                self.history = history_list
            else:
                self.history = []
        else:
            self.history = self.session['history']    
    def serialize_history(self,history):            #method to serialize the history object to make it JSON serializable because decimal is not JSON serializable
        for key, value in history.items():
            if isinstance(value, Decimal):
                history[key] = str(value)  # or float(value) 
        return history   
    def retrieve_all_history(self):
        return self.history
    def retrieve_by_prod_history(self, prod_id):
        pass
    def retrieve_by_date_history(self, date):
        pass