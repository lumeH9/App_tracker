import unittest
from ThreadReturn import ThreadWithReturnValue
from database import save_data
from AppTracker import track_time

# simulating input for the tests
response = {'python':5, 'notepad':3}
obj_conn, obj_cursor = save_data(response)

response2 = {'WindowsTerminal': 1} # assumes that cmd is open while running some tests
seconds = 1
tracker_dict = track_time(seconds)

thread = ThreadWithReturnValue(target=track_time, args=(seconds,), daemon=True)
thread.start()
thread_response = thread.join()

print(obj_conn)
print(obj_cursor)
print('track_time result: ', tracker_dict)
print('thread response: ', thread_response)

class TestDatabaseFunction(unittest.TestCase):
    def test_connect(self):
        self.assertIn('Connection object at', str(obj_conn))
    def test_cursor(self):
        self.assertIn('Cursor object at', str(obj_cursor))

class TestAppTrackerFunction(unittest.TestCase):
    def test_return_value(self):
        self.assertDictEqual(response2, tracker_dict)

class TestThreadReturnFunction(unittest.TestCase):
    def test_return_value(self):
        self.assertDictEqual(response2, thread_response)


if __name__ == '__main__':
    unittest.main()


