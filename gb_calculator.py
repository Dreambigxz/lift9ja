from django.test import TestCase

# Create your tests here.
suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

def humansize(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def conv_GB_to_MB(input_megabyte):
    gigabyte = input_megabyte * 1000
    if input_megabyte == 500:
        return 500
    else:
        return gigabyte

def conv_MB_to_GB(input_megabyte):
    gigabyte = input_megabyte / 1000
    print(gigabyte)
    return gigabyte

print(conv_MB_to_GB(int('1000')))