from datetime import timedelta
import search
import gc

import queue
from threading import Thread

result = list()
      
def delta_flight(delta, travel_airports, back_airports, travel_date, back_date):
    dates_list = []
    price_list = []
    link_list = []
    for start in range(-delta, delta+1):
        t_date = travel_date + timedelta(days=start)
        for end in range(-delta, delta+1):
            b_date = back_date + timedelta(days=end)
            try:
                price, link = search.fsearch_lowprice(travel_airports, back_airports, t_date, b_date)
                price_list.append(price)
                link_list.append(link)
                dates_list.append((t_date, b_date))
            except IndexError:
                print("Oops! Error on dates: " + str(t_date) + " and " + str(b_date))
            finally:
                gc.collect()
            print(price)
            print(link)
            print((t_date, b_date))
    
    return(price_list, link_list, dates_list)
    
    
def delta_flight_thread(delta, travel_airports, back_airports, travel_date, back_date):
    dates_list = []
    price_list = []
    link_list = []
    
    q = queue.Queue(maxsize=0) #Initialize queue
    num_threads = 2
    
    # Initialize threads
    for i in range(num_threads):
        worker = Thread(target=worker_task, args=(q,))
        worker.setDaemon(True)
        worker.start()
    
    # Populate queue
    for start in range(-delta, delta+1):
        t_date = travel_date + timedelta(days=start)
        for end in range(-delta, delta+1):
            b_date = back_date + timedelta(days=end)
            q.put((travel_airports,back_airports,t_date,b_date))
            
    print("Queue size: " + str(q.qsize()))

    q.join() # Blocks until all items in the queue have been gotten and processed
    
    # Separate results
    for i in result:
       price_list.append(i[0])
       link_list.append(i[1])
       dates_list.append((i[2],i[3]))
       
       
    return(price_list, link_list, dates_list)
    
    
def worker_task(q):
    while True:
        item = q.get() # Get item from queue

        price, link = search.fsearch_lowprice(item[0], item[1], item[2], item[3])

        result.append((price, link, item[2], item[3])) # Appends item result to result list
        print((price, link, item[2], item[3]))
        
        gc.collect()
        
        q.task_done() # Indicates that a task is complete
    