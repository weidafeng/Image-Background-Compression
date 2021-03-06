
    
import sys
import os

sys.path.append('shapeset2_1c_2s_3po.5000.test_code')

from image_config import *

d = dataset(fixed='position,orientation',shapeset=2,tag='test',free='color',seed=2,constrained='size',n_examples=5000)
d.data_directory = "."

try:
    task = sys.argv[1]
    args = sys.argv[2:]

    fn = getattr(d, task)
    
except Exception, e:
    print 'Usage: %(prog)s write_formats [format]*\n       %(prog)s view' % {'prog': sys.argv[0]}
    sys.exit()

fn(*args)

