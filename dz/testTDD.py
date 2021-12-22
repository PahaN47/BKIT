from custom_filter import CurrentState
import values
from values import state
import plotter
import unittest
import os

class bot_test(unittest.TestCase):
    def test_statecheck_default(self):
        values.current_state = state.DEFAULT
        self.assertTrue(CurrentState.check(None, [state.DEFAULT]))
    def test_plot_created(self):
        plot_path = plotter.plot('x')
        self.assertTrue(os.path.exists(plot_path))
        os.remove(plot_path)

if __name__ == '__main__':
    unittest.main()
    