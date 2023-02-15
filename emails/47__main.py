def get_password(site_name):
    for site_data in password_manager:
        if site_name in site_data.values():
            print(f"The password for {site_name} is: {site_data['password']}")
            break
    else:
        print(f"No password found for {site_name}!")


password_manager = [
    {
        "site_name": "AOL Email",
        "password": "cds_in_the_mail",
    },
    {
        "site_name": "Instakilo",
        "password": "s0c!i@lm3d1@",
    },
    {
        "site_name": "CodeWizardsHQ",
        "password": "!lIk3<odin",
    },
]


get_password("CodeWizardsHQ")  # The password for CodeWizardsHQ is: !lIk3<odin
get_password("Gmail")  # No password found for Gmail!



