from user.models import CustomerHistory
from django.forms.models import model_to_dict
from decimal import Decimal
class History:
    def __init__(self,request):
        self.session = request.session
        self.request = request
        history = self.session.get('history')
        username = request.session.get('username', None)
        if username:
            history_queryset = CustomerHistory.objects.filter(username=username)
            history_list = [self.serialize_history(model_to_dict(record)) for record in history_queryset]
            # Serialize the cart before storing it in the session
            self.session['history'] = history_list
            self.history = history_list
        else:
            self.history = []
    def serialize_history(self,history):            #method to serialize the history object to make it JSON serializable because decimal is not JSON serializable
        for key, value in history.items():
            if isinstance(value, Decimal):
                history[key] = str(value)  # or float(value) 
        return history   
    def retrieve_all_history(self):
        return self.history
    def retrieve_by_prod_history(self, prod):
        if prod:
            #results =  [record for record in self.history if list(eval(record['cart']).values())[0][3] == prod]
            results = []
            for record in self.history:
                #because record['cart'] is a string, we need to convert it to a dictionary using eval() 
                for key, value in eval(record['cart']).items():
                    if value[3].lower() == prod.lower():
                        results.append(record)
                        break
            if results:
                return results
            else:
                return 'No history found for the product entered.'
        else:
            return 'Please enter a product name to retrieve history.'
        
    def retrieve_by_date_history(self, date):
        if date:
            if len(date) == 8:
                results = [record for record in self.history if (record['date'])[:8] == date]
                if results:
                    return results
                else:
                    return 'No history found for the date entered.'
            else:
                return 'Invalid date format. Please enter date in DD-MM-YY format.'
        else:
            return 'Please enter a date to retrieve history.'        