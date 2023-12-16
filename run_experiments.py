# run_experiments.pyt
#
# Author: 
# Student ID:
# Email: 
#
# Use this program to run experiments and time methods that you implement
# Commenting can be light in this file
# Based on code by Oliver Schneider


import time
import random
from dodgeball_manager import DodgeballManager
from list.array_list import ArrayList

#libraries needed to create graphs
import pandas as pd
import plotly.express as px

# experiment with DodgeballManager constructor
def exp0_dm_constructor():
    SIZE = 10001
    STEP = SIZE // 50 # 50 samples

    #df store list
    index_list = []
    store_time = []

    # make a thrower list
    thrower_list = []
    dodger_list = []
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))

    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, dodger_list)

    # test time for every 10 indices
    #print the header
    print(" Length of Thrower and Dodger list| Constructor Time (ms)")
    for i in range(1,SIZE+1, STEP):
        
        #get a different size list to ith index
        sub_thrower_list = thrower_list[:i]
        sub_dodger_list = dodger_list[:i]
        
        #start experiement
        start_time_s = time.time()
        
        dm = DodgeballManager(sub_thrower_list, sub_dodger_list)
        
        end_time_s = time.time()
        
        d_time_s = end_time_s - start_time_s
        
        d_time_ms = d_time_s * 1000
        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
        
        
    c_header = ["Constructor Time (ms)", "Length of Thrower and Dodger list"]
    c_graph_title = "Constructor Time vs. Length of Thrower and Dodger list"
        
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        

###########################
#    Sorting Function     #
###########################

# Sorting experiments
def exp1_arraylist_sort():
    SIZE = 2000
    STEP = SIZE // 10 # 10 evenly sampled sizes

    #df store list
    index_list = []
    store_time = []
    
    # print header
    print(f"n|Sort Time (ms)")
    
    # create arrays of size n
    for n in range(0, SIZE, STEP):

        # create random array list of size n
        a = ArrayList()
        for i in range(n):
            # random integer between -1000 and 1000
            a.append(random.randint(-1000,1000))

        # setup timing
        start_time_s = time.time()
        
        # sort
        a.sort()

        # end time (should be immediately following the action)
        end_time_s = time.time()
        
        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        
        #append data to each list
        index_list.append(n)
        store_time.append(d_time_ms)
        # print(f"{n}|{d_time_ms}")
        
                
    c_header = ["Sort Time (ms)", "Size of array"]
    c_graph_title = "Sort Time vs. Size of array"
        
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        
         
         
         
###########################
#    Boolean Accessors    #
###########################

# experiment with DodgeballManager "isThrower" method
# grouping "isThrower" , "isActiveDodger" and "isBenchedPlayer"
def exp2_dm_isThrower():
    SIZE = 10000
    STEP = SIZE // 100 # 100 samples

    #df store list
    index_list = []
    store_time = []
    
    # make a thrower list
    thrower_list = []
    for i in range(0,SIZE):
        thrower_list.append(str(i))

    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, ["dodger"])

    # test time for every 10 indices
    #print the header
    print("Index|isThrower Time (ms)")
    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.isThrower(str(i))
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000

        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
        
                
    c_header = ["isThrower Time (ms)", "Index"]
    c_graph_title = "isThrower Time vs. Index"
        
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        
        
        
#########################
#    Count Accessors    #
#########################

# experiment with DodgeballManager "nBenchedPlayers" method
# grouping "nBenchedPlayers" and "nActiveDodgers"
def exp3_dm_nActiveDodgers():
    SIZE = 10001
    STEP = SIZE // 100 #100 samples
    
    #df store list
    index_list = []
    store_time = []
    
    # make a dodger list
    dodger_list = []
    for i in range(0,SIZE):
        dodger_list.append(str(i))
        
    # test time for every 10 indices
    #print the header
    print("Index| nActiveDodgers Time (ms)")
    for i in range(1,SIZE+1,STEP):
        # create DodgeballManagers
        dm =  DodgeballManager(["throwers"], dodger_list[:i])
    
        # setup timing
        start_time_s = time.time()
        
        dm.nActiveDodgers()
        
        # end time (should be immediately following the action)
        end_time_s = time.time()

        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        
        #append data to each list
        # print(f"{i}|{d_time_ms}")
        store_time.append(d_time_ms)
        index_list.append(i)
        
    c_header = ["nActiveDodgers Time (ms)", "Index"]
    c_graph_title = "nActiveDodgers Time vs. Index"
        
    return _to_graph(c_header, index_list , store_time, c_graph_title)

        
        
####################
# Private Function #
####################

# experiment with DodgeballManager "_FindPlayerHelper" method
def exp4_dm_FindPlayerHelper():
    '''
    _FindPlayerHelper()
    We are testing how the change in input size affect time complexity
    Factors: length of the Arraylist affects input size therefore affect time
    '''
    SIZE = 5001
    STEP = SIZE // 20 # 20 evenly sampled sizes

    #df store list
    index_list = []
    store_time = []
    
    # make a dodger list
    dodger_list = []
    for i in range(0,SIZE):
        dodger_list.append(str(i))
        
    # test time for every 10 indices
    #print the header
    print("Index| _FindPlayerHelper Time (ms)")
    for i in range(1,SIZE+1,STEP):
        # create DodgeballManagers
        dm =  DodgeballManager(["throwers"], dodger_list[:i])
        
        # setup timing
        start_time_s = time.time()
        
        dm._FindPlayerHelper(str(i), dm._dodgerList)
        
        # end time (should be immediately following the action)
        end_time_s = time.time()

        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        # print(f"{i}|{d_time_ms}")
        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
        
                
    c_header = ["_FindPlayerHelper Time (ms)", "Index"]
    c_graph_title = "_FindPlayerHelper Time vs.Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        

# experiment with DodgeballManager "_get_index" method
def exp5_dm_get_index():
    '''
    _get_index()
    We are testing how the change in input size affect time complexity
    Factors: length of the Arraylist affects input size therefore affect time
    '''
    SIZE = 5001
    STEP = SIZE // 20 # 20 evenly sampled sizes


    #df store list
    index_list = []
    store_time = []
    
    # make a dodger list
    dodger_list = []
    for i in range(0,SIZE):
        dodger_list.append(str(i))
            
    # test time for every 10 indices
    #print the header
    print("Index| _get_index Time (ms)")
    for i in range(1,SIZE+1,STEP):
        # create DodgeballManagers, changing ArrayList size
        dm =  DodgeballManager(["throwers"], dodger_list[:i])
        
        # setup timing
        start_time_s = time.time()
        
        dm._get_index(str(i-1), dm._dodgerList)
        
        # end time (should be immediately following the action)
        end_time_s = time.time()

        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        # print(f"{i}|{d_time_ms}")
        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
        
                
    c_header = ["_get_index Time (ms)", "Index"]
    c_graph_title = "_get_index Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        


####################
#    Main Logic    #
####################

# experiment with DodgeballManager "dodge" method
def exp6_dm_dodge():
    '''
    dodge()
    We are testing how the change in input size affect time complexity
    Factors: length of thrower and dodger affects input size therefore affect time
    '''
    SIZE = 5001
    STEP = SIZE // 20 # 20 evenly sampled sizes


    #df store list
    index_list = []
    store_time = []
    
    # make a thrower and dodger list
    thrower_list = []
    dodger_list = []
    for i in range(0,SIZE):
        dodger_list.append(str(i))
        thrower_list.append(str(i))
        
    
    # test time for every 10 indices
    #print the header
    print("Index| dodge Time (ms)")
    for i in range(1,SIZE + 1,STEP):
        # create DodgeballManagers, changing ArrayList size
        dm =  DodgeballManager(thrower_list[:i],dodger_list[:i])
        
        # setup timing
        start_time_s = time.time()
        
        #taking the i element in a list
        dm.dodge(str(i-1), str(i-1))
        
        # end time (should be immediately following the action)
        end_time_s = time.time()

        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        print(f"{i}|{d_time_ms}")

        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
        
                
    c_header = ["dodge Time (ms)", "Index"]
    c_graph_title = "dodge Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)

# experiment with DodgeballManager "hit" method
def exp7_dm_hit():
    '''
    hit()
    We are testing how the change in input size affect time complexity
    Factors: length of thrower and dodger affects input size therefore affect time
    '''
    SIZE = 5000
    STEP = SIZE // 20 # 20 evenly sampled sizes


    #df store list
    index_list = []
    store_time = []
    
    # make a dodger list
    dodger_list = []
    thrower_list = []
    for i in range(0,SIZE):
        dodger_list.append(str(i))
        thrower_list.append(str(i))
        
    # test time for every 10 indices
    #print the header
    print("Index| hit Time (ms)")
    for i in range(1,SIZE+1,STEP):
        # create DodgeballManagers, changing ArrayList size
        dm =  DodgeballManager(thrower_list[:i], dodger_list[:i])
        
        #start experiement 
        start_time_s = time.time()
        
        #taking the last element in a list
        dm.hit(str(i-1),str(i-1))
        
        # end time (should be immediately following the action)
        end_time_s = time.time()

        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        # print(f"{i}|{d_time_ms}")
        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
        
    c_header = ["hit Time (ms)", "Index"]
    c_graph_title = "hit Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)

# experiment with DodgeballManager "catchBall" method
def exp8_dm_catchBall():
    '''
    catchBall()
    We are testing how the change in input size affect time complexity
    Factors: length of thrower, dodger and bench affects input size therefore affect time
    '''
    SIZE = 5001
    STEP = SIZE // 20 # 20 evenly sampled sizes


    #df store list
    index_list = []
    store_time = []
    
    # make a list
    dodger_list = []
    thrower_list = []
    for i in range(0,SIZE):
        dodger_list.append(str(i))
        thrower_list.append(str(i))
        
    # test time for every 10 indices
    #print the header
    print("Index| catchBall Time (ms)")
    for i in range(1,SIZE+1,STEP):
        # create DodgeballManagers, changing ArrayList size
        dm =  DodgeballManager(thrower_list[:i], dodger_list[:i])
        
        for k in range(0, i-1):
            dm.hit(str(k), str(k))
        
        benchList_length = dm._benchList.length()

        if benchList_length == 0:
            start_time_s = time.time()
            dm.catchBall(str(i-1), str(i-1))
            end_time_s = time.time()
            d_time_s = end_time_s - start_time_s
            d_time_ms = d_time_s * 1000
            
             #append data to each list
            index_list.append(i)
            store_time.append(d_time_ms)
        # print(f"{i}|{d_time_ms}")
            # print(f"{i}|{d_time_ms}")
        else:
            last_benched_player = dm._benchList.get(benchList_length-1)
            last_benched_player_name = last_benched_player.get_name()

            start_time_s = time.time()
            dm.catchBall(str(i-1), str(i-1), last_benched_player_name)
            end_time_s = time.time()
            d_time_s = end_time_s - start_time_s
            d_time_ms = d_time_s * 1000
    
            #append data to each list
            index_list.append(i)
            store_time.append(d_time_ms)
            # print(f"{i}|{d_time_ms}")
        
    c_header = ["catchBall Time (ms)", "Index"]
    c_graph_title = "catchBall Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)

#######################
#    Main Printing    #
#######################

# experiment with DodgeballManager "printThrowers" method
# grouping "printThrowers" , "printDodgers" and "printBench"
def exp9_dm_printThrowers():
    '''
    printThrowers()
    We are testing how the change in input size affect time complexity
    Factors: length of the list affects input size therefore affect time
    '''
    SIZE = 5001
    STEP = SIZE // 100 # 20 evenly sampled sizes

    #df store list
    index_list = []
    store_time = []
    
    # make a thrower list
    thrower_list = []
    
    # make a list to store time outputs 
    store =[]

    for i in range(0,SIZE):
        thrower_list.append(str(i))

       
    # test time for every 10 indices
    for i in range(1,SIZE+1,STEP):
        # create DodgeballManagers
        dm =  DodgeballManager(thrower_list[:i], ["dodgers"])
                
        # setup timing
        start_time_s = time.time()
        
        #taking the last element in a list
        dm.printThrowers()
        
        # end time (should be immediately following the action)
        end_time_s = time.time()

        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        store.append(f"{i}|{d_time_ms}")
        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
    
    #print the header
    print("Index| printThrowers Time (ms)")
    
    #print time
    # for t in store:
        # print(t)
        
        
    c_header = ["printThrower Time (ms)", "Index"]
    c_graph_title = "printThrower Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        


##########################
#    Complex Printing    #
##########################

# experiment with DodgeballManager "printMVP" method
def exp10_dm_printMVP():
    '''
    printMVP()
    We are testing how the change in input size affect time complexity
    Factors: length of thrower and dodger affects input size therefore affect time
    '''
    SIZE = 1001
    STEP = SIZE // 20 # 50 samples
    
    #df store list
    index_list = []
    store_time = []
    
    # make a thrower and dodger list
    thrower_list = []
    dodger_list = []
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))

    # make a list to store time outputs 
    store =[]
    
    # test time for every 50 indices
    for i in range(1,SIZE +1, STEP):
        dm = DodgeballManager(thrower_list[:i], dodger_list[:i])
        
        #hit all dodgers
        for j in range(0,i):
            dm.hit(str(j), str(j))
            
        #start experiements
        start_time_s = time.time()
        
        #taking the last element in a list
        dm.printMVP()
        
        # end time (should be immediately following the action)
        end_time_s = time.time()
        
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        store.append(f"{i}|{d_time_ms}") 
        
            #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
    
    #print header
    print("Length of Thrower and Dodger List | printMVP Time (ms")
    
    #print time
    # for t in store:
        # print(t)
        
        
    c_header = ["printMVP Time (ms)", "Index"]
    c_graph_title = "printMVP Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        

    
    # #print the times
    # for t in store:
    #     print(t)

    
# experiment with DodgeballManager "printSortedScores" method
def exp11_dm_printSortedScores():
    SIZE = 1001
    STEP = SIZE // 20 # 20 samples

    #df store list
    index_list = []
    store_time = []
    
    # make a thrower and dodger list
    thrower_list = []
    dodger_list = []
    for i in range(0,SIZE):
        thrower_list.append(str(i))
        dodger_list.append(str(i))


    # make a list to store time outputs 
    store =[]
    
    # test time for every 50 indices
    for i in range(1,SIZE +1, STEP):
        dm = DodgeballManager(thrower_list[:i], dodger_list[:i])
        
        # generate a random socre between 0 to 5000 for all throwers and dodgers
        for j in range(0,i):
            thrower = dm._throwerList.get(j)
            thrower._score = random.randint(0,500)
            
        for k in range(0,i):
            dodger = dm._dodgerList.get(k)
            dodger._score = random.randint(0,500)
            
        #start experiement
        start_time_s = time.time()
        dm.printSortedScores()
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        store.append(f"{i}|{d_time_ms}") 
        
        #append data to each list
        index_list.append(i)
        store_time.append(d_time_ms)
    
    #print header
    print("Length of Thrower and Dodger List | printSortedScore Time (ms")
    
    #print time
    # for t in store:
        # print(t)
        
        
    c_header = ["printSortedScore Time (ms)", "Index"]
    c_graph_title = "printSortedScore Time vs. Index"
    
    return _to_graph(c_header, index_list , store_time, c_graph_title)
        


    #print header
    # print("Length of Thrower and Dodger List | printSortedScores Time (ms")
    
    # #print the times
    # for t in store:
    #     print(t)
    



def _to_graph(header :list, index_length: list, time :list, graph_title :str):

    # Creating a sample DataFrame
    data = {        
    
        header[1]: index_length,
        header[0]: time
    
    }
    df = pd.DataFrame(data)
    
    # Plotting a line graph using Plotly
    fig = px.line(df, x=header[1], y=header[0], title= graph_title)

    fig.show()


if __name__ == "__main__":
    # call experiments here
    # comment out when done
    
    # exp0_dm_constructor()
    #DONE

    # exp1_arraylist_sort()
    #DONE
    
    # exp2_dm_isThrower()
    #DONE
    
    # exp3_dm_nActiveDodgers()
    #DONE
    
    # exp4_dm_FindPlayerHelper()
    #DONE

    # exp5_dm_get_index()
    #DONE
    
    # exp6_dm_dodge()
    #DONE
    
    # exp7_dm_hit()
    #DONE
    
    # exp8_dm_catchBall()
    #DONE
    
    # exp9_dm_printThrowers()
    # DONE
    
    # exp10_dm_printMVP()
    # DONE
    
    exp11_dm_printSortedScores()
    #DONE