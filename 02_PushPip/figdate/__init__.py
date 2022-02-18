from time import gmtime, strftime

from pyfiglet import Figlet


def date(format="%Y %d %b, %A", font="graceful"):
    time = strftime(format, gmtime())
    print(Figlet(font=font).renderText(time))
