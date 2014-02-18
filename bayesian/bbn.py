
class Node(object):

    def __init__(self, name, parents=[], children=[]):       
        self.name = name
        self.parents = parents[:]
        self.children = children[:]
	
		
class BBNNode(Node):

    def __init__(self, factor):
        super(BBNNode, self).__init__(factor.__name__)
        self.func = factor
        self.argspec = get_args(factor)
         
            

def build_bbn(*args, **kwds):
    '''Builds a BBN Graph from
    a list of functions and domains'''
    variables = set()
    domains = kwds.get('domains', {})
    name = kwds.get('name')
    variable_nodes = dict()
    factor_nodes = dict()
	
    for factor in args:
        factor_args = get_args(factor)
        variables.update(factor_args)
        bbn_node = BBNNode(factor)
        factor_nodes[factor.__name__] = bbn_node
	
	
	



