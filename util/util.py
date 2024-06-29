def parse_data(data):
    try:
        entries = data.get('entries', [])
        parsed_entries = []
        for entry in entries:
            parsed_entry = {
                'currentRank': entry['chartEntryData']['currentRank'],
                'trackName': entry['trackMetadata']['trackName'],
                'name': entry['trackMetadata']['artists'][0]['name'],
                'displayImageUri': entry['trackMetadata']['displayImageUri'],
                'value': entry['chartEntryData']['rankingMetric']['value']
            }
            parsed_entries.append(parsed_entry)
        return parsed_entries
    except KeyError as e:
        print(f'Key error: {e}')
    except Exception as e:
        print(f'Exception: {e}')