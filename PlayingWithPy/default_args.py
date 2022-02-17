class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

"Could only change this part"
def print_from_stream(n, stream=EvenStream()):
    """Had to initialise the stream, if not then the even stream would continue on 
    from th e previous even stream"""
    stream.__init__()
    "Between these two comments"
    for _ in range(n):
        print(stream.get_next())
"The part between these two comments"

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
