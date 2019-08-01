# import time
# from random import randint
# from yaspin import yaspin

# with yaspin(text="Loading", color="blue") as spinner:
#     time.sleep(2)  # time consuming code

#     success = randint(0, 1)
#     if success:
#         spinner.ok("OK")
#     else:
#         spinner.fail("FAilure")

import time
from yaspin import yaspin

spinner = yaspin().bold.blink.yellow.bouncingBall.on_red
spinner.start()

time.sleep(3)  # time consuming tasks

spinner.stop()
