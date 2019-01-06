import iris
import datetime

def iris_loader(cube_dir):
    cubes = iris.load(cube_dir)
    if len(cubes) == 1:
        return cubes[0]
    else:
        return cubes
    
def dt_to_integer(dt_time):
    return 1000000*dt_time.year + 10000*dt_time.month + 100*dt_time.day + dt_time.hour