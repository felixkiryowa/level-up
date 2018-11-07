delivered_orders = [1,2,32,100]
pending_orders = [12,3,5,8,9,45]
def check_order_status(order_id):
    number_types = (int,float,complex)
    if isinstance(order_id, number_types):
        return order_id in delivered_orders
    raise ValueError
def check_if_order_id_does_not_exist_in_both_lists(order_id):
    return order_id not in delivered_orders and order_id not in pending_orders

def check_if_order_has_been_added_to_pending_list(order_id):
    x = len(pending_orders)
    pending_orders.append(order_id)
    orders = [] + pending_orders
    if len(orders) > x:
        return True
def check_if_order_has_been_added_to_the_delivered_list(order_id):
    if order_id in pending_orders:
        y = len(delivered_orders)
        x = len(pending_orders)
        delivered_orders.append(order_id)
        pending_orders.remove(order_id)
        current_pending_orders = [] + pending_orders
        orders = [] + pending_orders
        if len(orders) > y and len(current_pending_orders) < x:
            return True
        return False
    else:
        return False
    
    
        
        