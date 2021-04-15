class TopVotedCandidate:
    def __init__(self, persons, times):
        self.persons = persons
        self.times = times
        self.time_length = len(times)
        self.election_at_time = {}
        self.leads = []
        lead = -1
        for t, p in zip(times, persons):
            if p not in self.election_at_time:
                self.election_at_time[p] = 0
            self.election_at_time[p] += 1
            if self.election_at_time.get(lead, 0) <= self.election_at_time[p]:
                lead = p
            self.leads.append(lead)


    def q(self, t):
        t = t[0]

        left, right = 0, self.time_length - 1
        while left <= right:
            middle = (right + left) // 2
            if t == self.times[middle]:
                return self.leads[middle]
            elif t < self.times[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return self.leads[left - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

if __name__=="__main__":
    obj = TopVotedCandidate([0,1,1,0,0,1,0], [0,5,10,15,20,25,30])
    temp = []
    for query in [[3],[12],[25],[15],[24],[8]]:
        temp.append(obj.q(query))
    print(temp)
