from restclient import RestClient

a = RestClient("http://127.0.0.1:5000")

response = a.get("/employees")
print(response.json())

# a.put("/employees", params={	"LastName": "abc",
#                              "FirstName": "xyz",
#                              "Title": "10",
#                              "ReportsTo": "bbc",
#                              "BirthDate": "2020-09-21T17:00:34.597Z",
#                              "HireDate": "2020-09-21T17:00:34.597Z",
#                              "Address": "test",
#                              "City": "blr",
#                              "State": "kar",
#                              "Country": "Ind",
#                              "PostalCode": "5600",
#                              "Phone": "222",
#                              "Fax": "111",
#                              "Email": "12@12.com"})
