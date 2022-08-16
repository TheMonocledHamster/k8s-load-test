#!/usr/bin/python


from multiprocessing import Pool, cpu_count

def load_cpu() -> None:
    """
    Produces load on all available CPU cores.
    """
    processes = cpu_count()
    pool = Pool(processes)
    pool.map(cpu, range(processes))


def cpu(c) -> None:
    x = 1
    while x > 0:
        x -= (c**2) * 1e-5
