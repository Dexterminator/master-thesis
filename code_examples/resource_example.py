import resource


def get_resource_usage(func):
    func()
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print usage.ru_maxrss  # maximum memory usage
    print usage.ru_utime  # time in user mode
    print usage.ru_stime  # time in system mode
