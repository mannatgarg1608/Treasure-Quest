'''
    This file contains the class definition for the StrawHat class.
'''



from  crewmate import CrewMate
from heap import Heap 
from treasure import Treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        #declaring the main heap which contains the crewmates and each crewmate has a list of treasures in it
        self.m=m
        self.crewmates=Heap(self.comparator_function,[])

    def comparator_function(self,crew1,crew2):
        #this is my comparator function which compares the load and then the id which i have asssigned
        if crew1.current_load <crew2.current_load:
            return 1
        elif crew1.current_load >crew2.current_load:
            return 0
        else:
            if crew1.id <crew2.id:
                return 1
            elif crew1.id >crew2.id:
                return 0
            else:
                return -1
        
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        #adds the heap it the legth of heap is not full
        if  self.crewmates.size() < self.m:
             crew=CrewMate()
             crew.id=self.crewmates.size()
             self.crewmates.insert(crew)
        #get the top update the load and then reinsert it in heap
        topt=self.crewmates.extract()
        if topt.current_load < treasure.arrival_time  :
            topt.current_load= treasure.size +treasure.arrival_time
        else :
            topt.current_load += treasure.size
     
        remaining_size=treasure.size
        topt.treasures_list.append([remaining_size,treasure])
       
        self.crewmates.insert(topt)
       
        # Write your code here
      
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        #this lists stores all of my processed treasures
        treasures = []

        # Process each crewmate
        for i in range(self.crewmates.size()):
            crewmate = self.crewmates.heap[i]
            #if a crewmate has no treasure it break and continues
            if not crewmate.treasures_list:
                continue

            # Start the current time from the arrival of the first treasure
            current_time = crewmate.treasures_list[0][1].arrival_time
            traverse = 0
            l = len(crewmate.treasures_list)

            # Process each treasure in the list
            while traverse < l:
                to_add = crewmate.treasures_list[traverse]

                if crewmate.treasure_queue.is_empty():
                    crewmate.treasure_queue.insert(to_add)
                else:
                    top = crewmate.treasure_queue.extract()
                   
                    time_gap = to_add[1].arrival_time - current_time

                    # Case 1: when the treasure is completetly processed and then just after next treasure comes
                    if time_gap == top[0]:
                        current_time =current_time+top[0]
                        top[1].completion_time = current_time
                        top[0] = 0 
                        treasures.append(top[1])
                        crewmate.treasure_queue.insert(to_add)
                        
                    # Case 2: Partial processing (time_gap < top[0]) the crewmates is freed for some time since it has processed before next arrives
                    elif time_gap < top[0]:
                        current_time =current_time+time_gap
                        top[0] -= time_gap  
                        crewmate.treasure_queue.insert(top) 
                        crewmate.treasure_queue.insert(to_add)  

                    # Case 3: Process multiple treasures during the time gap 
                    else:
                        while top and time_gap >= top[0]:
                            current_time += top[0]
                            top[1].completion_time = current_time
                            treasures.append(top[1])
                            time_gap -= top[0] 
                            top[0]=0
                            top = crewmate.treasure_queue.extract()

                            if top is None:
                                break
# if while processing a number of treasures has been completely processed and a last one is processed to some extenct
                        if top is not None:
                            current_time+=time_gap
                            top[0] -= time_gap
                            crewmate.treasure_queue.insert(top)
                        
                        crewmate.treasure_queue.insert(to_add)
                        current_time=to_add[1].arrival_time

                traverse =traverse+1

            # Process remaining treasures in the queue since adding is done but now we want to process the added treasure from the left state
            
            while not crewmate.treasure_queue.is_empty():
                top2 = crewmate.treasure_queue.extract()
                if top2 is None:
                    break
                remaining=top2[0]
                top2[1].completion_time = current_time + remaining
                current_time = current_time + remaining
                
                top2[0]=0
                treasures.append(top2[1])
                

            for i in range(len(crewmate.treasures_list)):
                crewmate.treasures_list[i][0]=crewmate.treasures_list[i][1].size



       #sorting the treasures by id
        treasures.sort(key=lambda t: t.id)

        return treasures

