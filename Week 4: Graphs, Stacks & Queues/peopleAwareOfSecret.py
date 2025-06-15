from collections import deque

def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    tracker = deque([1] + [0] * (forget - 1))

    for i in range(2, n + 1):
        tracker.rotate(1)

        learners_count = 0
        temp = deque()

        for _ in range(forget - delay):
            num = tracker.pop()
            learners_count += num

            temp.appendleft(num)

        tracker.extend(temp)
        tracker.popleft()
        tracker.appendleft(learners_count)

    return sum(tracker) % (10**9 + 7)

def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    # We will keep track of people that haven't forgotten the secret yet
    day = [0] * forget

    # First person discovers the news
    day[0] = 1

    # We need to simulate each day
    for _ in range(1, n):
        # Create new day with temp value for new learners while dropping secret holders on their last day
        new_day = [0] + day[:-1]

        # Number of learners is the sum of all remaining secret holders past the delay period
        new_day[0] = sum(new_day[delay:])
        
        day = new_day

    return sum(day) % (10**9 +7)