import numbers 
import itertools
from datetime import timedelta

class TimeZone:
    def __init__(self,name,offset_hours,offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError("Timezone cannot be empty")

        self._name = str(name).strip()

        if not isinstance(offset_hours,numbers.Integral):
            raise ValueError('Hour offset must be an integer')
        
        if not isinstance(offset_minutes,numbers.Integral):
            raise ValueError("Minute offset must be an integer")
        
        if offset_hours > 59 or offset_minutes < -59:
            raise ValueError("Minutes offset must be between -59 and 59 inclusive.")
        

        offset = timedelta(hours=offset_hours,minutes = offset_minutes)
        if offset < timedelta(hours = -12,minutes=0) or offset > timedelta(hours=14,minutes=0):
            raise ValueError("Offset must be between -12:00 and +14:00.")
        
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes

        self._offset = offset 

    @property
    def offset(self):
        return self._offset 
    

    @property
    def name(self):
        return self._name 
    

    def __eq__(self, other):
        
        return (isinstance(other,TimeZone) and 
         self.name == other.name and 
         self._offset_hours == other._offset_hours and 
         self._offset_minutes == other._offset_minutes)
    
    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")
    
tz1 = TimeZone('ABC',-2,-15)

from datetime import datetime





class TransactionID:
    def __init__(self,start_id):
        self._start_id  = start_id 

    def next(self):
        self._start_id += 1
        return self._start_id



class Account:
    transaction_counter = itertools.count(100)

    def __init__(self, account_number, first_name, last_name):
        self.__account_number = account_number
        self.first_name = first_name  # This will trigger the setter
        self.last_name = last_name    # This will trigger the setter

    def make_transaction(self):
        new_trans_id = next(Account.transaction_counter)
        return new_trans_id

    @property
    def account_number(self):
        return self.__account_number

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        self.__first_name = Account.validate_name(value, 'First Name')

    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, value):
        self.__last_name = Account.validate_name(value, 'Last Name')

    @staticmethod
    def validate_name(value, field_title):
        if len(str(value).strip()) == 0:
            raise ValueError(f"{field_title} cannot be empty.")
        
        return str(value).strip()


try:
    a = Account('5342', "Mahika", "None")
    print(a.first_name) 
except ValueError as ex:
    print(ex)

