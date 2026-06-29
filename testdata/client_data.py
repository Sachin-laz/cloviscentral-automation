import time
import string
import random
import uuid


class ClientData:

    @staticmethod
    def valid_customer():

        unique_id = uuid.uuid4().hex[:8]

        client_code = "".join(
            random.choices(
                string.ascii_uppercase + string.digits,
                k=3
            )
        )


        return {

            "organisation": f"Automation_{unique_id}",

            "country": "India",

            "state": "Tamil Nadu",

            "client_code": client_code,

            "school_district": "Automation District",

            "district_prefix": "AD",

            "city": "Chennai",

            "address": "Chennai",

            "contact": "Sachin",

            "email": f"automation{unique_id}@test.com",

            "phone": "9876543210"
        }
    
    @staticmethod
    def updated_customer():

        timestamp = int(time.time())

        return {

            "contact": f"Updated Contact {timestamp}",

            "email": f"updated{timestamp}@test.com",

            "phone": "9123456789"
        }