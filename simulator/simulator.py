"""Module containing the scheduling simulator (engine).

The simulator takes a list of tasks and a scheduler, and
computes how the system would execute given the behavior of the scheduler.
"""

import heapq   # for heaps (it implements only min-heaps)


def simulate(tasks, num_resources, scheduler, debug=False):
    """Simulation engine.

    Parameters
    ----------
    tasks : list of int or float
        Contiguous tasks and their loads
    num_resources : int
        Number of identical resources to simulate
    scheduler : Scheduler object
        Scheduling algorithm to be used for the simulation
    debug : bool [default = False]
        True if debug messages should be printed

    Returns
    -------
    list of int, int or float, int, int
        Mapping of tasks to resources, makespan, number of calls to
        the scheduler, number of resource changes between contiguous
        tasks
    """
    print('* Starting the simulation *')
    if debug:
        print(f'- {len(tasks)} tasks running on' +
              f' {num_resources} resources using the' +
              f' {scheduler} scheduler.')

    # Setup:
    # - Creates a heap of free resources
    resources = [(0, i) for i in range(num_resources)]
    # - Creates a structure for storing where tasks are mapped
    mapping = [-1] * len(tasks)
    # - Counter of successful requests to the scheduler
    requests = 0

    # Simulation runs while there are tasks to schedule
    # Steps:
    # 1. get a free resource
    # 2. ask the scheduler for a list of tasks to schedule on the resource
    # 3. schedule the tasks in the resource, put it back in the heap
    # 4. if we get an empty list, the resource is considered to be done
    while resources:
        # Step 1
        time, res_id = heapq.heappop(resources)
        # Step 2
        new_tasks = scheduler.query(res_id)
        if new_tasks:
            # Step 3
            if debug:
                print(f'[{time}] - Resource {res_id} got tasks {new_tasks}.')
            extra_time = 0  # way to accumulate the load of the extra tasks
            requests += 1   # one more successful request
            for task_id in new_tasks:
                # Simple safety check
                if mapping[task_id] != -1:
                    print(f'- Error. Task {task_id} has already been scheduled' +
                          f' to resource {mapping[task_id]}. Stopping.')
                    return ([], -1, -1 , -1)

                # Sets the mapping of the task and adds its load to the resource
                mapping[task_id] = res_id
                extra_time += tasks[task_id]
            # puts the resource back in the heap
            heapq.heappush(resources, (time + extra_time, res_id))

        else:
            # Step 4
            if debug:
                print(f'[{time}] - Resource {res_id} is done.')

    # Computes the number of resource changes between contiguous resources
    contig_changes = 0
    for i in range(0, len(tasks)-1):
        if mapping[i] != mapping[i+1]:
            contig_changes += 1

    # No more events
    print(f'* Total execution time (makespan) = {time}\n')
    return (mapping, time, requests, contig_changes)
