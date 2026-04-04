def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input type")
        return

    if not isinstance(attendees, list):
        print("Invalid input type")
        return

    for i, attendee in enumerate(attendees, start=1):
        file_name = f"output_{i}.txt"
        with open(file_name, "w") as file:
            line = template
            if attendee["name"] is None:
                attendee["name"] = "N/A"

            if attendee["event_title"] is None:
                attendee["event_title"] = "N/A"

            if attendee["event_date"] is None:
               attendee["event_date"] = "N/A"

            if attendee["event_location"] is None:
               attendee["event_location"] = "N/A"
               
               line = line.replace("{name}", attendee["name"])
               line = line.replace("{event_title}", attendee["event_title"])
               line = line.replace("{event_date}", attendee["event_date"])
               line = line.replace("{event_location}", attendee["event_location"])
               
               file.write(line)
