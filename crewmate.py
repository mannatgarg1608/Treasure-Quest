from heap import Heap


'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.id=None
        self.current_load=0
        self.treasure_queue =Heap(self.compare_priority, [])
        self.treasures_list=[]

        pass
    
    def compare_priority(self, treasure_tuple_1, treasure_tuple_2):
        first = treasure_tuple_1[0] +  treasure_tuple_1[1].arrival_time
        second = treasure_tuple_2[0] + treasure_tuple_2[1].arrival_time

        # Reverse inequality for max-heap
        if first > second:
            return 0
        elif first < second:
            return 1
        else:
            # check for edits here as smallest id is at priority
            if treasure_tuple_1[1].id < treasure_tuple_2[1].id:
                return 1
            elif treasure_tuple_1[1].id > treasure_tuple_2[1].id:
                return 0


      
    # Add more methods if required