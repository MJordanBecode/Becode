from lxml import etree
# I define my source document
tree = etree.parse("../data/data.xml")
# I look at my document and identify the tag path to get to the "user" information
# Indeed, the information is in a name tag itself present in a user tag
# it even presents itself in a users tag. This last tag is located at the root of the directory
# so in tree.xpath("/users/user/name") there are the tags associated with our search
for user in tree.xpath("/users/user/nom"):
    # I want to display only the content (.text) of these tags /users/user/name
    print(user.text)