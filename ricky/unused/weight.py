        weights_total = sum(
            map(lambda x: x["weight"], self.probabilities())
        ) + (255 * 255 * 255)
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.probabilities():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return

        weights_total = sum(
                map(lambda x: x["weight"], self.probabilities())
            )# + self.range_max - self.range_min
        if weights_total < 100:
            weights_total = 100;
        choice = random.randint(0, weights_total)
        import sys
        sys.stderr.write("choosing %s: random_int: %s, probabilities: %s\n" % (
            self.name,
            choice,
            self.probabilities()))
        position = 0
        for elem in self.probabilities():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                return


        weights_total = sum(map(lambda x: x["weight"], self.probabilities()))
        choice = random.randint(0, weights_total)
        position = 0
        for elem in self.probabilities():
            position += elem["weight"]
            if position >= choice:
                self.value = elem["value"]
                break
    def _choose_heaviest(self):
        heaviest_idx = 0
        heaviest_weight = 0
        idx = 0
        if (len(self.options())):
            for elem in self.options():
                if elem["weight"] > heaviest_weight:
                    heaviest_weight = elem["weight"]
                    heaviest_idx = idx
                idx += 1
            return self.options()[heaviest_idx]["value"]
        else:
            self.randomize()

    def heaviest(self):
        self.value = self._choose_heaviest()

    """default value is the probability with the heaviest weight"""
    self.default(self._choose_heaviest())
