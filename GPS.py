import gps

class Locator:
    def __init__(self):
        self.session = gps.gps("localhost", "2947")
        self.session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

    def stream_data(self):
        try:
            report = self.session.next()
            if report['class'] == 'TPV': 
                if hasattr(report, 'lon') and hasattr(report, 'lat'):
                    return report.lon, report.lat
                else:
                    return None
        except KeyError:
            return None

        except StopIteration:
            self.session = None
            return None
