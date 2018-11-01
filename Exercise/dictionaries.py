monthConversions = {
    "Jan": "January",
    "Feb":  "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions["Mar"])
print(monthConversions.get("Jun", "Not a valid Key"))
print(monthConversions.get("Luv", "Not a valid key"))