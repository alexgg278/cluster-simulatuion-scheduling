class Parameters:

    def __init__(self):
        # Normal distribution
        self.mean = 16
        self.std = 6

        self.jobs_types = [{'number': 2,
                            'cpu': 2,
                            'memory': 500,
                            'file_size': 10,
                            'app': 1,
                            'distr': None,
                            'distr_mem': []},
                           {'number': 2,
                            'cpu': 2,
                            'memory': 500,
                            'file_size': 10,
                            'app': 2,
                            'distr': None,
                            'distr_mem': []},
                           {'number': 2,
                            'cpu': 2,
                            'memory': 500,
                            'file_size': 10,
                            'app': 3,
                            'distr': None,
                            'distr_mem': []}]

        self.nodes_types = [{'number': 1,
                             'cpu': 20,
                             'memory': [500],
                             'region': 1},
                            {'number': 1,
                             'cpu': 20,
                             'memory': [500],
                             'region': 2},
                            {'number': 1,
                             'cpu': 20,
                             'memory': [500],
                             'region': 3},
                            {'number': 1,
                             'cpu': 20,
                             'memory': [500],
                             'region': 4},
                            {'number': 1,
                             'cpu': 20,
                             'memory': [500],
                             'region': 5},
                            {'number': 1,
                             'cpu': 20,
                             'memory': [500],
                             'region': 6}]

        self.number_jobs = self.jobs_types[0]['number'] + self.jobs_types[1]['number']

        self.iterations = 50

        self.episodes = 30

        self.jobsets = 4

        # Discount factor
        self.gamma = 1

        # Learning rate
        self.lr = 0.0005
        # Layer shapes
        self.layer_shapes = [64, 32, 16]

        self.action_space = 6
        self.state_space = 28

        # Early stopping patience
        self.patience = 50

