if page_data is None:  # Token expired or error
#     with :
#         print("GENERATING A NEW TOKEN: ")
#         access_token = get_access_token()
#         if access_token is None:
#             print("Failed to create a new access token")
#             print("Data extracted up to page:", page_number - 1)
#             break  # Exit the loop if no more data or error after refreshing token
#         else:
#             headers["Authorization"] = f"Bearer {access_token}"
# else:
#     all_data.extend(page_data)

