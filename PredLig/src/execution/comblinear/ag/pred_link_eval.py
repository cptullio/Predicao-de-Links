import sframe

class Hop:
    
    
    metrics = sframe.SFrame.read_csv('/results/grafos_nowell/grqc_1994_1999/CombinationLinear/ToAG/data.csv')
    results = sframe.SFrame.read_csv('/results/grafos_nowell/grqc_1994_1999/CombinationLinear/ToAG/analysed.txt.allNodes.csv')
    metrics = metrics.join(results)
    top = 400

    def __init__(self):
        pass

    @classmethod
    def evaluate(cls, individual):
        new_metric = cls.metrics['cn'] * individual[0] + cls.metrics['aas'] * individual[1] + cls.metrics['pa'] * individual[2] \
               + cls.metrics['jc'] * individual[3] + cls.metrics['ts08'] * individual[4] + cls.metrics['ts05'] * individual[5]\
               + cls.metrics['ts02'] * individual[6]
        cls.metrics.add_column(new_metric, name='new_metric')
        top_metrics = cls.metrics.topk('new_metric', k=cls.top)
        aux = [0]
        top_metrics = top_metrics.filter_by(aux,'result')
        zero = top_metrics.num_rows()
        cls.metrics.remove_column('new_metric')
        return 1 - float(zero) / cls.top,

