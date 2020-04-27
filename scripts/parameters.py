class Parameters:

    def __init__(self):
        self.jobs_types = [{'probability': 0.5,
                            'cpu': 2,
                            'memory': 500,
                            'file_size': 8,
                            'transmit': 1},
                           {'probability': 0.5,
                            'cpu': 2,
                            'memory': 500,
                            'file_size': 8,
                            'transmit': 2}]

        self.nodes_types = [{'number': 1,
                             'cpu': 20,
                             'memory': 2000,
                             'bw': 1},
                            {'number': 1,
                             'cpu': 20,
                             'memory': 2000,
                             'bw': 2}]

        self.number_jobs = 20

        self.iterations = 200

        self.episodes = 30

        self.jobsets = 1

        # Discount factor
        self.gamma = 1

        # Learning rate
        self.lr = 0.001

        # Layer shapes
        self.layer_shapes = [64, 32]

        self.action_space = 8
        self.state_space = 6

