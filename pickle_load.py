from transaction_id import get_transaction_id
import pickle
file_name = 'coupons/coupon_codes'

def dump_file(file, file_name):
    outfile = open(file_name, 'wb')
    pickle.dump(file, outfile)
    outfile.close()

def load_file(file_name):
    infile = open(file_name, 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    return new_dict
#
# g_c_c('5kc')
# g_c_c('10kc')
# g_c_c('15kc')
# g_c_c('20kc')

# dump_file([], file_name)
# dump_file(g_c_c('5kc', 5), file_name)
# load_file(file_name)