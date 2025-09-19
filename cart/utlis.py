from .constants import indian_state
import re

def validate_coupon(title,code,end_date,start_date,now_date,quantity,min_amount,discount_amount):
    # if title.isdigit():
    #     return "Title should not be numbers only"

    if title.strip() == "":
        return "Please enter Your Coupon title"

    if code.strip() == "":     
        return "Please enter your Coupon code"

    if end_date < start_date:     
        return "End date must be after start date."

    if now_date > end_date:         
        return "The end date for the coupon cannot be in the past."

    if quantity.strip() == "":       
        return "Please enter your Quantity"

    if min_amount.strip() == "":         
        return "Please enter your Minimum Amount"

    if discount_amount.strip() == "":         
        return "Please enter your Discount Amount"
    
    if float(quantity) < 1:        
        return 'Quantity should be  minimum 1'
    
    if float(min_amount) < 1:        
        return 'Not Valid Minimum amount '

    if float(discount_amount) < 1:    
        return 'Not Valid Minimum Discount amount'
    
    return None


def validate_address(name, address, house_no, city, state, country, pincode):
    if not all([name, address, house_no, city, state, country, pincode]):
        return "pls provide all field "
    if state.casefold() not in [state_name.casefold() for state_name in indian_state]:
        return "pls provide valid state"
    if not re.match(r'^[1-9][0-9]{5}$', pincode):
        return 'Invalid pincode format. Please enter a valid Indian pincode.'
    

    return None
            