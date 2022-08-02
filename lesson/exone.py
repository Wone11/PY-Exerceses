from multiprocessing import Pool
def Start(tasks):
    print(f'Tasks Running : {tasks}')


#main methods called here
if __name__ == '__main__':
    tasks =['Task1','Task2','Task3']

    with Pool(len(tasks)) as pool:
        pool.map(Start,tasks)
    
    