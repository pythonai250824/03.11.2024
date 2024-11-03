
import hw_sol_my_func
from hw_sol_my_func import print_stars

for _ in range(5):
    hw_sol_my_func.print_stars()
print()
for _ in range(5):
    print_stars()
print()

print('module, whats your name?', __name__)

#help(my_func)
help(hw_sol_my_func.print_stars)