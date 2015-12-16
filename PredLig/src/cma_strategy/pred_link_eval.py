import sframe


class SFrame:
    metrics = sframe.SFrame.read_csv('data.csv')
    results = sframe.SFrame.read_csv('results.csv')
    top = 20

    def __init__(self):
        pass

    @classmethod
    def evaluate(cls, individual):
        new_metric = cls.metrics['aas'] * individual[0] + cls.metrics['cn'] * individual[1] + cls.metrics['DJC'] * individual[2] \
               + cls.metrics['DTS'] * individual[3] + cls.metrics['DTSv2'] * individual[4] + cls.metrics['jc'] * individual[5]\
               + cls.metrics['pa'] * individual[6] + cls.metrics['ts'] * individual[7]
        copy_metrics = cls.metrics.copy()
        copy_metrics.add_column(new_metric, name='new_metric')
        copy_metrics = copy_metrics.topk('new_metric', k=cls.top)
        copy_results = cls.results.copy()
        copy_metrics = copy_metrics.join(copy_results)
        copy_metrics = copy_metrics.sort('new_metric', ascending=False)
        aux = [0]
        copy_metrics = copy_metrics.filter_by(aux,'result')
        zero = copy_metrics.num_rows()
        del copy_metrics
        del copy_results
        return float(zero) / cls.top,
