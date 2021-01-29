"""Module containing scheduling algorithms.

Each scheduling algorithm receives a specific set of inputs.
They output partial mappings when requested using the query method.

Implemented scheduling methods: OpenMPStatic, LPT.
Methods with interfaces but no implementation: OpenMPDynamic, OpenMPGuided,
RecursiveBipartition.
"""


class Scheduler:
    """
    Basic scheduler class.

    Attributes
    ----------
    name : string
        Algorithm's name
    num_resources : int
        Number of identical resources
    """
    def __init__(self, num_resources, name='scheduler'):
        self.name = name
        self.num_resources = num_resources

    def __repr__(self):
        return self.name

    def query(self, resource_id):
        """
        Provides the next tasks to a given resource.

        Parameters
        ----------
        resource_id : int
            Identifier of the resource

        Returns
        -------
        empty list
        """
        return []


class OpenMPStatic(Scheduler):
    """
    Static scheduler based on the algorithm used for OpenMP.

    Notes
    -----
    This scheduler requires an additional parameters defining the chunk size.
    Its initialization method pre-computes the schedule.
    """
    def __init__(self, tasks, num_resources, chunk_size=0):
        Scheduler.__init__(self, num_resources, name='Static')
        self.chunk_size = chunk_size

        # Pre-computes the schedule
        schedule = [list() for i in range(num_resources)]
        num_tasks = len(tasks)
        # Two styles
        # if chunk size == 0, does a compact mapping
        if chunk_size == 0:
            # Size of partitions
            partition_size = num_tasks // num_resources
            # Number of resources that will have +1 tasks
            leftover = num_tasks % num_resources

            # Starting task identifier
            task = 0

            # Iterates over the resources mapping groups of tasks to them
            for resource in range(num_resources):
                # Sets the actual size of the group of tasks to map
                # to this resource based on the existence of any leftover
                if leftover > 0:
                    group_size = partition_size + 1
                    leftover -= 1
                else:  # No more resources with +1 tasks
                    group_size = partition_size

                for i in range(group_size):
                    schedule[resource].append(task)
                    task += 1  # next task to map
        else:
            # does a round-robin mapping by chunks
            resource = 0
            chunk_counter = 0
            for task in range(num_tasks):
                schedule[resource].append(task)
                chunk_counter += 1
                # if the chunk is full, starts a new one in the next resource
                if chunk_counter == chunk_size:
                    chunk_counter = 0
                    resource = (resource + 1) % num_resources

        # Stores the pre-computed schedule
        self.schedule = schedule

    def query(self, resource_id):
        """
        Provides a list of tasks to a resource once.

        Parameters
        ----------
        resource_id : int
            Identifier of the resource

        Returns
        -------
        list of int
            Pre-computed list of task identifiers, or an empty list
        """
        tasks = self.schedule[resource_id]
        if tasks:  # if they have not been scheduled before
            # empties the list
            self.schedule[resource_id] = []
        return tasks


class LPT(Scheduler):
    """
    Largest Processing Time first scheduler.

    Notes
    -----
    Its initialization creates an internal list of tasks ordered by load.
    """
    def __init__(self, tasks, num_resources):
        Scheduler.__init__(self, num_resources, name='LPT')
        num_tasks = len(tasks)
        # Orders tasks by non-increasing load
        tasks_by_priority = [(tasks[i], i) for i in range(num_tasks)]
        tasks_by_priority.sort(reverse=True)
        self.tasks = tasks_by_priority

    def query(self, resource_id):
        """
        Provides a list of one task to a resource.

        Parameters
        ----------
        resource_id : int
            Identifier of the resource

        Returns
        -------
        list of int
            List with one task identifier
        """
        if self.tasks:
            load, task_id = self.tasks.pop(0)
            return [task_id]
        else:  # nothing to return
            return []


class OpenMPDynamic(Scheduler):
    """
    Dynamic scheduler based on the algorithm used for OpenMP.

    Notes
    -----
    This scheduler requires an additional parameters defining the chunk size.
    """
    def __init__(self, tasks, num_resources, chunk_size=1):
        Scheduler.__init__(self, num_resources, name='Dynamic')
        self.chunk_size = chunk_size
        # TODO

    def query(self, resource_id):
        """
        Provides a list of tasks to a resource.

        Parameters
        ----------
        resource_id : int
            Identifier of the resource

        Returns
        -------
        list of int
            List of task identifiers based on the chunk size, or an empty list
        """
        # TODO


class OpenMPGuided(Scheduler):
    """
    Guided scheduler based on the algorithm used for OpenMP.

    Notes
    -----
    This scheduler requires an additional parameters defining the chunk size.
    The chunk size gives the minimum size of the list of tasks to return.
    The size of the list to return is based on the number of remaining
    tasks to schedule divided by the number of resources in the system.
    """
    def __init__(self, tasks, num_resources, chunk_size=1):
        Scheduler.__init__(self, num_resources, name='Guided')
        self.chunk_size = chunk_size
        # TODO

    def query(self, resource_id):
        """
        Provides a list of tasks to a resource.

        Parameters
        ----------
        resource_id : int
            Identifier of the resource

        Returns
        -------
        list of int
            List of task identifiers based on the chunk size, or an empty list
        """
        # TODO


class RecursiveBipartition(Scheduler):
    """
    Recursive bipartition scheduler for use when the number of resources
    is a power of two.

    Notes
    -----
    Its initialization method pre-computes the schedule.
    The bipartition should split a sequence of tasks in the place where
    the load is the most balanced between the two parts.
    A variation of the algorithm that works with numbers that are not power of
    two would just have to define different proportions when partitioning
    For instance, for 5 resources, the algorithm would first split the load
    at the 2/5-3/5 point and follow recursively from there.
    """
    def __init__(self, tasks, num_resources):
        Scheduler.__init__(self, num_resources, name='RB')
        # TODO

    def query(self, resource_id):
        """
        Provides a list of tasks to a resource once.

        Parameters
        ----------
        resource_id : int
            Identifier of the resource

        Returns
        -------
        list of int
            Pre-computed list of task identifiers, or an empty list
        """
        tasks = self.schedule[resource_id]
        if tasks:  # if they have not been scheduled before
            # empties the list
            self.schedule[resource_id] = []
        return tasks
