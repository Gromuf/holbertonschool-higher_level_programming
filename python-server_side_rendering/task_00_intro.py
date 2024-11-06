#!/usr/bin/env python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if (
        not isinstance(attendees, list)
        or not all(isinstance(attendee, dict)
                   for attendee in attendees)
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A") or "N/A"
        event_location = attendee.get("event_location", "N/A")

        invitation_content = template.format(
            name=name,
            event_title=event_title,
            event_date=event_date,
            event_location=event_location
        )

        output_filename = "output_{}.txt".format(index)
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation_content)
            print("Generated file: {}".format(output_filename))
        except Exception as err:
            print(
                "Error: Failed to write {}. Reason: {}"
                .format(output_filename, err)
                )
