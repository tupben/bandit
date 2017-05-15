# The Multi-Armed Bandit Problem
#
# Quick Summary:
# https://en.wikipedia.org/wiki/Multi-armed_bandit

import numpy as np

class Machine():
	def __init__(self, name):
		self.name = name
		self.payout = 0
		self.plays = 0

X = Machine('_')
Y = Machine('.')
Z = Machine('^')

global casino
casino = [X,Y,Z]

# pprint prints the attributes of every machine
#
def pprint():
	print
	for machine in casino:
		print 'name : ',machine.name,'    plays : ', machine.plays,'     payout :  ', machine.payout
	print

# UCB1 evaluates the appeal of machines balancing
# exploitation and exploration.
#
def ucb1(m):
	all_turns = 0
	for machine in casino:
		all_turns += machine.plays
	if m.plays == 0:
		return 'visit me'
	return m.payout/m.plays + 3*((np.log(all_turns)/m.plays)**.5)

# Select chooses the machine with the highest ucb1 score.
# (note: 'str'> float)
#
def select():
	best_score=None
	for machine in casino[:]:
		score = ucb1(machine)
		if score > 'a':
			return machine
		if score > best_score:
			best_score = score
			best_machine = machine
	return best_machine

# Simulate gives the payout for a given machine. Here X>Y>Z
#
def simulate(machine):
	if machine == X:
		return np.round(np.random.rand())
	if machine == Y:
		return np.round(np.random.rand()**2)
	if machine == Z:
		return float(0)

# Back_prop updates the stats of the chosen machine.
#
def back_prop(machine,win):
	machine.payout += win
	machine.plays += 1

# Run_bandit runs all steps. 
# Note: The Monte Carlo problem would include an 'expand' step.
#
def run_bandit():
	a = select()
	# Expand
	b = simulate(a)
	back_prop(a,b)
	return a.name

# Runs the program many times, shows the first and last 1000 choices
# You can see that the algorithm has learned to favor machine 1 (name: '-')
# but it still tries other machines occasionally.
#
history = ''
for a in range(20000):
	pick = run_bandit()
	history += pick
print 'FIRST 1000 EPOCHS:'
print history[:1000]
print '\nLAST 1000 EPOCHS:'
print history[-1000:]
pprint()


# The theoretical limit of earnings in this situation is
# the number of iterations played * the maximum payout (1).
# But the best machine only pays out it's max an average of
# 50% of the time, so over large sample size,
# the perfect player who chooses this machine each time, will
# likely end up with (0.5*plays) dollars/units/bitcoins/wtvr.
#
# Tinkering with the UCB1 constant (2) gives more exploration or
# less. 2 appears better than extremely large constants or
# extremely small constants. Running the whole program 1000x
# with differently weighted machines and different UCB1
# constants would help determine the best constant.
# (For more, see 'regret' as a definition of success/failure)
# 
potential_earnings  = 20000/2
actual_earnings = sum(machine.payout for machine in casino)
print 'Actual Earnings    :', actual_earnings
print 'Potential Earnings :', potential_earnings
print 'Percent            :', 100 * actual_earnings/potential_earnings

# Concern: using global variables seems inelegant.
# Change to pass variables as arguments.
#
# Next: Monte Carlo Tree Search. But how do I treat nodes
# in a tree when I don't know how many there will be?
# I can't use objects the way I do here.
