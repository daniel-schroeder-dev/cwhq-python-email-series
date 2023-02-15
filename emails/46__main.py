def display_contact_details(contact_information):
    full_name = contact_information["full_name"]
    phone_number = contact_information["phone_number"]
    email_address = contact_information.get("email_address")
    home_address = contact_information.get("home_address")

    contact_details = f"""
        ******** PRIMARY CONTACT DETAILS ************

        Name: {full_name}
        Phone Number: {phone_number}

        *********************************************

        ******* SECONDARY CONTACT DETAILS ***********

        Email Address: {email_address}
        Home Address: {home_address}

        *********************************************
    """
    print(contact_details)



contacts = [
        {
            "full_name": "John Smith",
            "phone_number": "323-8832",
            "email_address": "jdawg@aol.com",
        },
        {
            "full_name": "Jane Doe",
            "phone_number": "341-9231",
            "email_address": "jane@hotmail.com",
            "home_address": "142 Emoji Lane",
        },
]


for contact in contacts:
    display_contact_details(contact)
