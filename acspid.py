class pidcont():
    def __init__(self, P, I, D, pmax, pmin):
        self.kp = P
        self.kd = D
        self.ki = I
        self.pidmax = pmax
        self.pidmin = pmin
        self.desired = 0.0
        self.error = 0.0
        self.elast = 0.0
        self.esum = 0.0
        self.eder = 0.0

    def update(self, current):
        self.error = self.desired - current
        self.eder = self.error - self.elast
        self.elast = self.error
        self.esum = self.esum + self.error
        if self.esum > self.pidmax:
            self.esum = self.pidmax
        elif self.esum < self.pidmin:
            self.esum = self.pidmin

        self.P = self.kp * self.error
        self.D = self.kd * self.eder
        self.I = self.ki * self.esum
        pid = self.P + self.I + self.D
        return pid

    def setDesired(self, d):
        self.desired = d

    def setGains(self, P, I, D):
        self.kp = P
        self.kd = D
        self.ki = I

    def setLimits(self, pmax, pmin):
        self.pidmax = pmax
        self.pidmin = pmin
