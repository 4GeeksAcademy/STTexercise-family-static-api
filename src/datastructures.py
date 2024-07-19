
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            'id':1,
            'first_name':'John Jackson' ,
            'age': 33,
            'Lucky Numbers':[7, 13, 22]
            },
            {
            'id':2,
            'first_name':'Jane Jackson' ,
            'age': 35,
            'Lucky Numbers':[10, 14, 3]
            },
            {
            'id':3,
            'first_name':'Jimmy Jackson',
            'age': 5,
            'Lucky Numbers': [1]
            }   
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(10000, 99999)

    def add_member(self, member):
        # fill this method and update the return

        if "id" not in member:
            member["id"] = self._generateId()

        new_member = {
            "id": member["id"],
            "last_name": self.last_name,
            "first_name": member["first_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }

        self._members.append(new_member)
        return(member)

    def delete_member(self, id):
        output = {'done': False}
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                output = {'done': True}
        print(output)
        return output 

    def get_member(self, id):
        found_member = None
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return found_member  

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
    

jackson_family = FamilyStructure("Jackson")
