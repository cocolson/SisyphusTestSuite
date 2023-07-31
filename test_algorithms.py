import unittest
import algorithms
import test_cases
import performance_monitor

class TestAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("")

    @classmethod
    def tearDownClass(cls):
        print("")
    
    def test_bubble_sort(self):
        print("\nTesting bubble sort algorithm...")
        test_cases_bubble_sort = test_cases.generate_bubble_sort_tests()
        for i, test_case in enumerate(test_cases_bubble_sort, 1):
            input_list, expected_output = test_case
            res, execution_time, mb_used = performance_monitor.measure_performance(algorithms.bubble_sort, input_list)
            res_status = "PASSED" if res == expected_output else "FAILED"
            print(f"Test {res_status}, Execution time: {execution_time:.6f} seconds, Memory used: {mb_used:.2f} MB, Input Size: {len(input_list)}")
            self.assertEqual(res, expected_output)
    
    def test_fibonacci(self):
        print("\nTesting fibonacci sequence algorithm...")
        test_cases_fibonacci = test_cases.generate_fibonacci_tests()
        for i, num_fibonacci in enumerate(test_cases_fibonacci, 1):
            res, execution_time, mb_used = performance_monitor.measure_performance(algorithms.fibonacci, num_fibonacci)
            res_status = "PASSED" if res == algorithms.fibonacci(num_fibonacci) else "FAILED"
            print(f"Test {res_status}, Execution time: {execution_time:.6f} seconds, Memory used: {mb_used:.2f} MB, Sequence Size: {len(res)}")
            self.assertEqual(res, algorithms.fibonacci(num_fibonacci))

    def test_prime_gen(self):
        print("\nTesting prime number generation algorithm...")
        test_cases_prime = test_cases.generate_prime_tests()
        for i, max_prime in enumerate(test_cases_prime, 1):
            res, execution_time, mb_used = performance_monitor.measure_performance(algorithms.prime_gen, max_prime)
            res_status = "PASSED" if all(algorithms.is_prime(num) for num in res) else "FAILED"
            print(f"Test {res_status}, Execution time: {execution_time:.6f} seconds, Memory used: {mb_used:.2f} MB, Max Prime: {max_prime}")
            self.assertTrue(all(algorithms.is_prime(num) for num in res), f"Test case {i} failed")