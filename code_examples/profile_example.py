from cProfile import Profile
from pstats import Stats


def profile(func, file_path):
    pr = Profile()
    pr.enable()
    func()
    pr.disable()
    s = open(file_path, 'w')
    sortby = 'cumulative'
    ps = Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
