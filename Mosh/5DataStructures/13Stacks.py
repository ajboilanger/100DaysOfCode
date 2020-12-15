browsing_session = []  # creates empty list (new session start)
browsing_session.append(1)  # first site visited
browsing_session.append(2)  # second site visited
browsing_session.append(3)  # third site visisted
print(browsing_session)  # print list of sites visited
# create last variable and remove the last site visited from browsing_session
last = browsing_session.pop()
print(last)  # print last site visisted
print(browsing_session)  # print remaining sites in browsing_session
if not browsing_session:  # if browsing_session is empty:
    print("disabled")
else:
    # print "redirect" and whatever the last value in browsing_session is
    print("redirect", browsing_session[-1])
last = browsing_session.pop()  # remove the next site from browsing_session
print(last)  # print the new value of last
# print the remaining site in browsing_session (should be "1")
print(browsing_session)
if not browsing_session:  # if browsing_session is empty:
    print("disabled")
else:
    # print "redirect" and whatever the last value in browsing_session is
    print("redirect", browsing_session[-1])
last = browsing_session.pop()  # remove the next site from browsing_session
print(last)  # print the new value of last
print(browsing_session)  # print what should be an empty list at this point
if not browsing_session:  # if browsing_session is empty:
    print("disabled")
else:
    # print "redirect" and whatever the last value in browsing_session is
    print("redirect", browsing_session[-1])
