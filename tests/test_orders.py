import unittest
from order_verify import  check_order_status
from order_verify import check_if_order_id_does_not_exist_in_both_lists
from order_verify import check_if_order_has_been_added_to_pending_list
from order_verify import check_if_order_has_been_added_to_the_delivered_list

class TestOrder(unittest.TestCase):
    def test_order_status(self):
        order_id = 2
        self.assertEqual(check_order_status(order_id),True)
    # test if the input is an integer
    def test_if_input_is_integer(self):
        self.assertRaises(ValueError, check_order_status, 'two')

    # test for an order id that does not exist in both lists
    def test_if_order_id_doesnot_exist_in_both_lists(self):
        self.assertTrue(check_if_order_id_does_not_exist_in_both_lists(300))

    # test for adding of a new order
    def test_if_new_order_is_added_to_pending_list(self):
        self.assertTrue(check_if_order_has_been_added_to_pending_list(67))

    # test for marking an order delivered
    def test_if_new_order_is_added_to_delivered_list(self):
        self.assertTrue(check_if_order_has_been_added_to_the_delivered_list(3))


   